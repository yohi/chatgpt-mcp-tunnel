#!/usr/bin/env python3
"""One-time, explicit IAM bootstrap for the isolated AWS MCP STS broker.

Default: read-only preview. With --apply, create exactly one dedicated IAM
role (if absent), trust only the current AWS console-login IAM user, and attach
only ReadOnlyAccess. Never edit an existing role; refuse unexpected policies.
No secret credentials or tokens are printed.
"""
import argparse
import json
import re
import sys

import boto3
from botocore.exceptions import ClientError

PROFILE = "aws-mcp-readonly"
ROLE_NAME = "ChatGPTMcpReadOnlyRole"
READ_ONLY_POLICY = "arn:aws:iam::aws:policy/ReadOnlyAccess"
USER_RE = re.compile(r"^arn:(aws|aws-us-gov|aws-cn):iam::([0-9]{12}):user/(.+)$")


def describe_target(identity):
    user_arn = identity["Arn"]
    matched = USER_RE.fullmatch(user_arn)
    if not matched or identity.get("Account") != matched.group(2):
        raise ValueError("AWS login must be a direct IAM user, not root or an assumed role")
    partition, account = matched.group(1), matched.group(2)
    return (
        user_arn,
        f"arn:{partition}:iam::{account}:role/{ROLE_NAME}",
        {
            "Version": "2012-10-17",
            "Statement": [{
                "Sid": "OnlySourceConsoleUserCanAssume",
                "Effect": "Allow",
                "Principal": {"AWS": user_arn},
                "Action": "sts:AssumeRole",
            }],
        },
    )


def is_missing_role(error):
    return isinstance(error, ClientError) and error.response["Error"]["Code"] == "NoSuchEntity"


def validate_existing_role(iam, role_name, expected_trust):
    role = iam.get_role(RoleName=role_name)["Role"]
    if role.get("Path") != "/" or role.get("PermissionsBoundary"):
        raise ValueError("existing role has nonstandard path or permissions boundary; inspect manually")
    trust = role.get("AssumeRolePolicyDocument")
    if isinstance(trust, str):
        raise ValueError("existing role trust policy must be independently inspected")
    if trust != expected_trust:
        raise ValueError("existing role trust policy differs from dedicated user-only trust")
    attached = iam.list_attached_role_policies(RoleName=role_name)["AttachedPolicies"]
    if sorted(x["PolicyArn"] for x in attached) != [READ_ONLY_POLICY]:
        raise ValueError("existing role must have exactly ReadOnlyAccess attached")
    inline = iam.list_role_policies(RoleName=role_name)["PolicyNames"]
    if inline:
        raise ValueError("existing role has unexpected inline policies")
    return role


def bootstrap(session, apply=False):
    sts = session.client("sts")
    iam = session.client("iam")
    identity = sts.get_caller_identity()
    user_arn, role_arn, trust = describe_target(identity)
    print(f"Source identity: {user_arn}")
    print(f"Target role: {role_arn}")
    print(f"Attached policy: {READ_ONLY_POLICY}")
    print("Trust: exact source IAM user only")
    try:
        validate_existing_role(iam, ROLE_NAME, trust)
    except ClientError as exc:
        if not is_missing_role(exc):
            raise
    else:
        print("Role exists and policy/trust exactly match; no changes made")
        return role_arn

    if not apply:
        print("DRY RUN ONLY: no IAM changes. Re-run with --apply to create the role.")
        return role_arn

    # The user must explicitly request --apply. No broadening of any existing
    # IAM principal's permissions. CreateRole precedes policy attachment;
    # without the attachment, the new role has no identity-based grants.
    iam.create_role(
        RoleName=ROLE_NAME,
        Path="/",
        AssumeRolePolicyDocument=json.dumps(trust, separators=(",", ":")),
        Description="Dedicated read-only session role for ChatGPT AWS MCP Tunnel",
        MaxSessionDuration=3600,
    )
    try:
        iam.attach_role_policy(RoleName=ROLE_NAME, PolicyArn=READ_ONLY_POLICY)
    except ClientError:
        print("ATTENTION: role was created but policy attachment failed; investigate before using", file=sys.stderr)
        raise
    validate_existing_role(iam, ROLE_NAME, trust)
    print("Role CREATED with only ReadOnlyAccess; external IAM review still required")
    return role_arn


def main():
    parser = argparse.ArgumentParser(description="Bootstrap isolated AWS MCP read-only role")
    parser.add_argument("--apply", action="store_true", help="Explicitly create missing IAM role")
    args = parser.parse_args()
    try:
        bootstrap(boto3.Session(profile_name=PROFILE), apply=args.apply)
    except (ClientError, ValueError, KeyError) as error:
        # Errors could contain AWS account IDs and principal names, but never
        # intentionally include raw credentials or session token data.
        print(f"Bootstrap refused/failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
