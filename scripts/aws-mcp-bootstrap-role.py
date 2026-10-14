#!/usr/bin/env python3
"""Temporary AWS MCP IAM role lifecycle. Opt-in create and post-shutdown cleanup.

IAM role names follow the *literal* requested YYYYYMMDDHHMMSS format:
five-digit, zero-padded year + Tokyo-local month/day/hour/minute/second.
Neither the role nor the saved state is shared with the MCP container.

--apply: explicitly create a NEW temporary role once, ReadOnlyAccess only.
--cleanup --confirm-stopped: verify exact previously created role and delete it,
only after the caller has stopped both MCP tunnel and STS broker processes.
No IAM changes occur during default preview; never edit unrelated roles.
"""
import argparse
import datetime as dt
import json
import os
from pathlib import Path
import re
import stat
import sys
import tempfile
import time
from zoneinfo import ZoneInfo

import boto3
from botocore.exceptions import ClientError

PROFILE = "aws-mcp-readonly"
ROLE_PREFIX = "ReadOnlyIAMRole_"
ROLE_NAME_RE = re.compile(r"^ReadOnlyIAMRole_[0-9]{15}$")
STATE = Path("/home/awsuser/.aws/chatgpt-mcp-iam-role.json")
ROLE_CREDS = Path("/run/aws-mcp-credentials/credentials.json")
READ_ONLY_POLICY = "arn:aws:iam::aws:policy/ReadOnlyAccess"
TAG_OWNER = "chatgpt-mcp-tunnel-temporary"
USER_RE = re.compile(r"^arn:(aws|aws-us-gov|aws-cn):iam::([0-9]{12}):user/(.+)$")


def role_name_at(now=None):
    now = now or dt.datetime.now(ZoneInfo("Asia/Tokyo"))
    return f"{ROLE_PREFIX}{now.year:05d}{now:%m%d%H%M%S}"


def describe_target(identity, role_name):
    user_arn = identity["Arn"]
    match = USER_RE.fullmatch(user_arn)
    if not match or identity.get("Account") != match.group(2):
        raise ValueError("source must be the original IAM user, never root/assumed role")
    if not ROLE_NAME_RE.fullmatch(role_name):
        raise ValueError("unexpected temporary role name")
    role_arn = f"arn:{match.group(1)}:iam::{match.group(2)}:role/{role_name}"
    trust = {
        "Version": "2012-10-17",
        "Statement": [{
            "Sid": "OnlySourceConsoleUserCanAssume",
            "Effect": "Allow",
            "Principal": {"AWS": user_arn},
            "Action": "sts:AssumeRole",
        }],
    }
    tags = [
        {"Key": "ManagedBy", "Value": TAG_OWNER},
        {"Key": "SourcePrincipal", "Value": user_arn},
    ]
    return user_arn, role_arn, trust, tags


def check_private_parent(path):
    folder = path.parent
    info = folder.lstat()
    if not stat.S_ISDIR(info.st_mode) or info.st_uid != os.geteuid() or info.st_mode & 0o077:
        raise ValueError("IAM lifecycle state directory has unsafe permissions")


def read_state(path=STATE):
    check_private_parent(path)
    try:
        info = path.lstat()
    except FileNotFoundError:
        return None
    if not stat.S_ISREG(info.st_mode) or info.st_uid != os.geteuid() or info.st_mode & 0o077:
        raise ValueError("IAM lifecycle state file has unsafe permissions")
    with path.open(encoding="utf-8") as handle:
        record = json.load(handle)
    if not isinstance(record, dict) or set(record) != {
        "version", "role_name", "role_arn", "role_id", "source_arn",
    }:
        raise ValueError("invalid IAM role state document")
    if record["version"] != 1 or not ROLE_NAME_RE.fullmatch(record["role_name"]):
        raise ValueError("invalid IAM role state/version")
    if not all(isinstance(record[key], str) and record[key] for key in (
        "role_arn", "role_id", "source_arn"
    )):
        raise ValueError("invalid IAM role state fields")
    return record


def save_state(record, path=STATE):
    check_private_parent(path)
    if path.exists() or path.is_symlink():
        raise ValueError("role state already exists; refusing overwrite")
    handle, name = tempfile.mkstemp(dir=path.parent, prefix=".role-state-")
    tmp = Path(name)
    try:
        with os.fdopen(handle, "w", encoding="utf-8") as out:
            os.fchmod(out.fileno(), 0o600)
            json.dump(record, out, separators=(",", ":"))
            out.write("\n")
            out.flush()
            os.fsync(out.fileno())
        os.replace(tmp, path)
    finally:
        tmp.unlink(missing_ok=True)


def is_missing_role(exc):
    return (isinstance(exc, ClientError) and
            exc.response["Error"]["Code"] == "NoSuchEntity")


def role_policies(iam, role_name):
    attached = [p["PolicyArn"] for page in iam.get_paginator(
        "list_attached_role_policies"
    ).paginate(RoleName=role_name) for p in page["AttachedPolicies"]]
    inline = [n for page in iam.get_paginator(
        "list_role_policies"
    ).paginate(RoleName=role_name) for n in page["PolicyNames"]]
    profiles = [p for page in iam.get_paginator(
        "list_instance_profiles_for_role"
    ).paginate(RoleName=role_name) for p in page["InstanceProfiles"]]
    return attached, inline, profiles


def validate_owned_role(iam, state, trust, tags, cleanup=False):
    role_name = state["role_name"]
    role = iam.get_role(RoleName=role_name)["Role"]
    if (role["Arn"] != state["role_arn"] or role["RoleId"] != state["role_id"]
            or role.get("Path") != "/" or role.get("PermissionsBoundary")
            or role.get("AssumeRolePolicyDocument") != trust):
        raise ValueError("role identity/trust/path changed; refusing modification")
    actual_tags = [
        tag for page in iam.get_paginator("list_role_tags").paginate(RoleName=role_name)
        for tag in page["Tags"]
    ]
    if sorted(actual_tags, key=lambda x: x["Key"]) != sorted(tags, key=lambda x: x["Key"]):
        raise ValueError("role ownership tags changed; refusing modification")
    attached, inline, profiles = role_policies(iam, role_name)
    if inline or profiles:
        raise ValueError("role has inline policies or instance profiles; refusing modification")
    expected = [READ_ONLY_POLICY] if not cleanup else [[], [READ_ONLY_POLICY]]
    if (sorted(attached) != sorted(expected) if not cleanup
            else sorted(attached) not in expected):
        raise ValueError("role managed policy set changed; refusing modification")
    return attached


def clear_cached_credentials():
    # Only delete the project-owned role credential JSON; never purge the
    # admin console login cache or another user's credentials.
    if not ROLE_CREDS.parent.exists():
        return
    info = ROLE_CREDS.parent.lstat()
    if not stat.S_ISDIR(info.st_mode) or info.st_uid != os.geteuid() or info.st_mode & 0o077:
        raise ValueError("role credential directory is unsafe; refusing cleanup")
    try:
        item = ROLE_CREDS.lstat()
    except FileNotFoundError:
        return
    if not stat.S_ISREG(item.st_mode) or item.st_uid != os.geteuid() or item.st_mode & 0o077:
        raise ValueError("role credential file is unsafe; refusing cleanup")
    ROLE_CREDS.unlink()


def lifecycle(session, apply=False, cleanup=False, confirmed_stopped=False):
    sts = session.client("sts")
    iam = session.client("iam")
    identity = sts.get_caller_identity()
    stored = read_state()

    if cleanup:
        if not confirmed_stopped:
            raise ValueError("cleanup requires --confirm-stopped after stopping both services")
        if stored is None:
            print("No project-owned temporary IAM role recorded; nothing to delete")
            return None
        if stored["source_arn"] != identity["Arn"]:
            raise ValueError("source IAM user differs from role creator; refusing delete")
        _, _, trust, tags = describe_target(identity, stored["role_name"])
        print(f"Cleanup requested: {stored['role_arn']}")
        try:
            attached = validate_owned_role(iam, stored, trust, tags, cleanup=True)
        except ClientError as exc:
            if not is_missing_role(exc):
                raise
            clear_cached_credentials()
            STATE.unlink()
            print("Role already absent; local role state cleaned")
            return None
        # Remove the local cache even if IAM deletion fails, to avoid
        # continuing to use a potentially stale STS session.
        clear_cached_credentials()
        if attached:
            iam.detach_role_policy(RoleName=stored["role_name"], PolicyArn=READ_ONLY_POLICY)
        iam.delete_role(RoleName=stored["role_name"])
        STATE.unlink()
        print("Temporary IAM role deleted; admin console-login cache retained")
        return None

    name = stored["role_name"] if stored else role_name_at()
    source, arn, trust, tags = describe_target(identity, name)
    print(f"Logged-in IAM principal: {source}")
    print(f"Temporary role: {arn}")
    print(f"Role permissions: {READ_ONLY_POLICY}")
    if stored:
        if stored["source_arn"] != source or stored["role_arn"] != arn:
            raise ValueError("saved role belongs to a different IAM principal/account")
        validate_owned_role(iam, stored, trust, tags)
        print("Existing project-owned role verified; no changes made")
        return arn
    if not apply:
        print("PREVIEW ONLY: no role created; name will be generated at apply-time")
        return arn
    # A preexisting timestamp-name role, even if similar, is not adopted.
    try:
        iam.get_role(RoleName=name)
    except ClientError as exc:
        if not is_missing_role(exc):
            raise
    else:
        raise ValueError("temporary role name collision; refusing adoption")

    created = iam.create_role(
        RoleName=name,
        Path="/",
        AssumeRolePolicyDocument=json.dumps(trust, separators=(",", ":")),
        Description="Temporary least-privilege role for ChatGPT AWS MCP, cleanup required",
        MaxSessionDuration=3600,
        Tags=tags,
    )["Role"]
    record = {
        "version": 1,
        "role_name": name,
        "role_arn": arn,
        "role_id": created["RoleId"],
        "source_arn": source,
    }
    # Write the durable ownership record before policy attachment. If this
    # crashes, the next bootstrap run can still identify the created role.
    save_state(record)
    try:
        iam.attach_role_policy(RoleName=name, PolicyArn=READ_ONLY_POLICY)
        for attempt in range(5):
            try:
                validate_owned_role(iam, record, trust, tags)
                break
            except (ClientError, ValueError):
                if attempt == 4:
                    raise
                time.sleep(1)
    except (ClientError, ValueError):
        print("ATTENTION: role was created but validation/attachment failed. "
              "Do NOT start the broker; inspect role and run explicit cleanup.",
              file=sys.stderr)
        raise
    print("Temporary role created; run explicit stop-and-cleanup at end of use")
    return arn


def main():
    parser = argparse.ArgumentParser(description="Lifecycle of temporary AWS MCP IAM role")
    exclusive = parser.add_mutually_exclusive_group()
    exclusive.add_argument("--apply", action="store_true", help="Create the temporary role")
    exclusive.add_argument("--cleanup", action="store_true", help="Delete after MCP shutdown")
    parser.add_argument("--confirm-stopped", action="store_true",
                        help="Confirm AWS Tunnel and broker have been stopped")
    args = parser.parse_args()
    try:
        lifecycle(boto3.Session(profile_name=PROFILE),
                  apply=args.apply, cleanup=args.cleanup,
                  confirmed_stopped=args.confirm_stopped)
    except (ClientError, ValueError, KeyError, OSError, json.JSONDecodeError) as exc:
        print(f"Lifecycle refused/failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
