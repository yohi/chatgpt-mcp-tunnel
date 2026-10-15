#!/usr/bin/env python3
"""Independent IAM role credential issuer for the AWS MCP Tunnel.

Only this process can see the source AWS CLI console-login cache. It uses
STS AssumeRole with a ReadOnlyAccess *session policy*, additionally limiting
permissions granted by the dedicated read-only role. It publishes only the
short-lived assumed-role credential_process JSON to a separate Docker volume.

The MCP runtime mounts *only* the target volume read-only.
"""
import datetime as dt
import json
import os
from pathlib import Path
import re
import stat
import sys
import tempfile
import time

import boto3
from botocore.exceptions import BotoCoreError, ClientError

STORE = Path("/run/aws-mcp-credentials")
SOURCE_PROFILE = "aws-mcp-readonly"
SESSION_NAME = "chatgpt-mcp-readonly"
SESSION_POLICY_ARN = "arn:aws:iam::aws:policy/ReadOnlyAccess"
DURATION_SECONDS = 3600
REFRESH_SECONDS = 1200
RETRY_SECONDS = 60
ROLE_ARN_PATTERN = re.compile(r"^arn:(aws|aws-us-gov|aws-cn):iam::[0-9]{12}:role/[A-Za-z0-9+=,.@_/-]+$")

ROLE_STATE = Path("/home/awsuser/.aws/chatgpt-mcp-iam-role.json")
TEMP_ROLE_NAME_RE = re.compile(r"^ReadOnlyIAMRole_[0-9]{15}$")
SOURCE_USER_PATTERN = re.compile(
    r"^arn:(aws|aws-us-gov|aws-cn):iam::([0-9]{12}):user/.+$"
)


def derive_role_arn():
    """Read only the explicitly recorded bootstrap role for this source user."""
    directory = ROLE_STATE.parent.lstat()
    record_info = ROLE_STATE.lstat()
    if (not stat.S_ISDIR(directory.st_mode) or directory.st_uid != os.geteuid()
            or directory.st_mode & 0o077
            or not stat.S_ISREG(record_info.st_mode)
            or record_info.st_uid != os.geteuid()
            or record_info.st_mode & 0o077):
        raise ValueError("IAM role lifecycle state has unsafe permissions")
    with ROLE_STATE.open(encoding="utf-8") as source:
        state = json.load(source)
    if (not isinstance(state, dict) or state.get("version") != 1
            or not isinstance(state.get("role_name"), str)
            or not TEMP_ROLE_NAME_RE.fullmatch(state["role_name"])
            or not isinstance(state.get("role_id"), str)
            or not state["role_id"]):
        raise ValueError("missing or invalid temporary role ownership state")
    identity = boto3.Session(profile_name=SOURCE_PROFILE).client("sts").get_caller_identity()
    match = SOURCE_USER_PATTERN.fullmatch(identity.get("Arn", ""))
    if (not match or match.group(2) != identity.get("Account")
            or state.get("source_arn") != identity.get("Arn")):
        raise ValueError("role owner does not match source login IAM user")
    role_arn = f"arn:{match.group(1)}:iam::{match.group(2)}:role/{state['role_name']}"
    if state.get("role_arn") != role_arn:
        raise ValueError("temporary IAM role ARN mismatch")
    return role_arn


def check_destination(directory):
    info = directory.lstat()
    if (not stat.S_ISDIR(info.st_mode) or info.st_uid != os.geteuid()
            or info.st_mode & 0o077):
        raise ValueError("role credential volume must be private and owned by UID 10001")


def make_role_document(response, expected_arn):
    credentials = response["Credentials"]
    assumed = response["AssumedRoleUser"]["Arn"]
    # The identity came from STS response, not user-controlled profile labels.
    if ":assumed-role/" not in assumed:
        raise ValueError("AssumeRole did not return an assumed-role identity")
    # A role's path (if any) is stripped from an assumed-role session ARN.
    role_name = expected_arn.rsplit("/", 1)[-1]
    account = expected_arn.split(":")[4]
    partition = expected_arn.split(":")[1]
    prefix = f"arn:{partition}:sts::{account}:assumed-role/{role_name}/"
    if not assumed.startswith(prefix):
        raise ValueError("unexpected assumed-role identity")
    expiration = credentials["Expiration"]
    if not isinstance(expiration, dt.datetime) or expiration.tzinfo is None:
        raise ValueError("STS returned no timezone-aware expiration")
    if (expiration - dt.datetime.now(dt.timezone.utc)).total_seconds() < 1800:
        raise ValueError("STS returned insufficient credential lifetime")
    return {
        "Version": 1,
        "AccessKeyId": credentials["AccessKeyId"],
        "SecretAccessKey": credentials["SecretAccessKey"],
        "SessionToken": credentials["SessionToken"],
        "Expiration": expiration.astimezone(dt.timezone.utc).isoformat().replace("+00:00", "Z"),
    }


def atomic_publish(document, directory=STORE):
    directory = Path(directory)
    check_destination(directory)
    path = None
    try:
        handle, name = tempfile.mkstemp(prefix=".role-", dir=directory)
        path = Path(name)
        with os.fdopen(handle, "w", encoding="utf-8") as output:
            os.fchmod(output.fileno(), 0o600)
            json.dump(document, output, separators=(",", ":"))
            output.write("\n")
            output.flush()
            os.fsync(output.fileno())
        os.replace(path, directory / "credentials.json")
        path = None
        dir_handle = os.open(directory, os.O_RDONLY | os.O_DIRECTORY)
        try:
            os.fsync(dir_handle)
        finally:
            os.close(dir_handle)
    finally:
        if path is not None:
            path.unlink(missing_ok=True)


def acquire(role_arn):
    source = boto3.Session(profile_name=SOURCE_PROFILE)
    sts = source.client("sts")
    response = sts.assume_role(
        RoleArn=role_arn,
        RoleSessionName=SESSION_NAME,
        DurationSeconds=DURATION_SECONDS,
        PolicyArns=[{"arn": SESSION_POLICY_ARN}],
    )
    document = make_role_document(response, role_arn)
    # Verify the actual temporary session *before* exposing it to MCP.
    temporary_session = boto3.Session(
        aws_access_key_id=document["AccessKeyId"],
        aws_secret_access_key=document["SecretAccessKey"],
        aws_session_token=document["SessionToken"],
    )
    expected_identity = response["AssumedRoleUser"]["Arn"]
    actual_identity = temporary_session.client("sts").get_caller_identity()["Arn"]
    if actual_identity != expected_identity:
        raise ValueError("STS temporary credential identity mismatch")
    return document


def main():

    try:
        check_destination(STORE)
    except (OSError, ValueError):
        print("AWS MCP broker: run aws-role-init for the private credential volume", file=sys.stderr)
        return 2

    while True:
        try:
            role_arn = derive_role_arn()
            document = acquire(role_arn)
            atomic_publish(document)
            print("AWS MCP broker: STS read-only session renewed", flush=True)
            delay = REFRESH_SECONDS
        except (BotoCoreError, ClientError, ValueError, OSError, KeyError):
            # Fail closed. Keep prior (soon-expiring) STS credentials, never
            # replace with source admin session or log access key/token.
            print("AWS MCP broker: role refresh failed; investigate login/STS/trust", file=sys.stderr, flush=True)
            delay = RETRY_SECONDS
        time.sleep(delay)


if __name__ == "__main__":
    sys.exit(main())
