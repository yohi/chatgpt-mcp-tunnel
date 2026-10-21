#!/usr/bin/env bash
# Interactive starter: Docker aws login --remote (default) -> STS -> AWS MCP.
# No source AWS login cache is mounted in the MCP container.
set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")/.."

if [[ ! -t 0 || ! -t 1 ]]; then
  echo 'ERROR: Run from an interactive terminal to complete aws login --remote.' >&2
  exit 2
fi
if [[ ! -f .env.aws || ! -f compose.aws.quick-sts.yaml ]]; then
  echo 'ERROR: Required .env.aws or compose.aws.quick-sts.yaml is missing.' >&2
  exit 2
fi
base=(docker compose --env-file .env.aws -f compose.aws.yaml)
quick=(docker compose --env-file .env.aws -f compose.aws.yaml -f compose.aws.quick-sts.yaml)

# Never print compose config: it contains the OpenAI runtime API key.
# Explicitly activate the issuer profile for config inspection. Compose
# otherwise omits profiled services and the isolation check gets KeyError.
# Docker Compose 2.24.4+ is required for !override of the source cache mount.
"${quick[@]}" --profile aws-quick-sts-issue config --format json | python3 -c '
import json,sys
cfg=json.load(sys.stdin)
mcp=cfg["services"]["aws-tunnel"]
volumes=mcp["volumes"]
assert len(volumes)==1, "Unexpected MCP mounts"
v=volumes[0]
assert v["target"]=="/run/aws-mcp-quick-sts" and v["read_only"], "Role volume must be read-only"
assert "/home/awsuser/.aws" not in json.dumps(mcp), "Source login cache leaked into MCP"
issuer=cfg["services"]["aws-quick-sts-issue"]
assert issuer["environment"]["AWS_PROFILE"]=="default", "Issuer must use Docker default"
assert issuer["environment"]["AWS_MCP_STS_ROLE_ARN"]=="arn:aws:iam::456720798575:role/aws-security-audit-readonly", "Unexpected target role ARN"
print("PASS: role-only MCP volume and target role")
'

# Build only on first start / missing quick-STS helper. Subsequent starts reuse images.
if ! docker image inspect chatgpt-mcp-tunnel:local >/dev/null 2>&1; then
  echo 'First use: building base Tunnel image...'
  docker compose build tunnel
fi
# Rebuild when the local issuer script changed, even if an old image exists.
expected_sha=$(sha256sum scripts/aws-mcp-sts-quick.py | cut -d' ' -f1)
image_sha=''
if docker image inspect chatgpt-aws-mcp-tunnel:local >/dev/null 2>&1; then
  image_sha=$(docker run --rm --entrypoint sha256sum chatgpt-aws-mcp-tunnel:local \
    /usr/local/bin/aws-mcp-sts-quick.py 2>/dev/null | cut -d' ' -f1) || image_sha=''
fi
if [[ "$image_sha" != "$expected_sha" ]]; then
  echo 'Building AWS MCP image with the matching default-profile issuer...'
  "${base[@]}" build aws-tunnel
fi

# The first Docker login may have a root-owned AWS cache directory. Repair
# ownership only if the configured aws-auth UID cannot write to it. The
# legacy initializer changes only the volume root; it does not delete cache.
if ! "${base[@]}" run --rm --no-deps --entrypoint /bin/sh aws-auth \
  -c 'test -d /home/awsuser/.aws && test -w /home/awsuser/.aws' >/dev/null 2>&1; then
  echo 'Initializing Docker AWS login cache ownership...'
  "${base[@]}" run --rm --no-deps aws-sso-init
  "${base[@]}" run --rm --no-deps --entrypoint /bin/sh aws-auth \
    -c 'test -d /home/awsuser/.aws && test -w /home/awsuser/.aws'
fi

# Stop old direct-login MCP before modifying its mounts/profile. Clear STS cache.
"${base[@]}" stop aws-tunnel
"${quick[@]}" run --rm --no-deps aws-quick-sts-init
"${quick[@]}" run --rm --no-deps aws-quick-sts-clear

# This command must remain interactive; browser sign-in + auth code are mandatory.
# Host default and Docker default use separate login caches.
echo 'Sign in using the Docker AWS CLI URL and enter the returned code in this terminal.'
"${base[@]}" run --rm --no-deps aws-auth login --remote --profile default

account=$("${base[@]}" run --rm --no-deps aws-auth sts get-caller-identity \
  --profile default --query Account --output text | tail -n 1 | tr -d '\r')
if [[ "$account" != '456720798575' ]]; then
  echo 'ERROR: Wrong AWS account; STS issuance aborted.' >&2
  exit 1
fi
printf 'PASS: Docker login account %s\n' "$account"

# Only the one-shot issuer can read both source login and role credential volumes.
"${quick[@]}" run --rm --no-deps aws-quick-sts-issue
"${quick[@]}" up -d --no-deps --force-recreate aws-tunnel

# Confirm the effective role in the MCP container without displaying any credentials.
"${quick[@]}" exec -T aws-tunnel python -c '
import boto3
from pathlib import Path
assert not Path("/home/awsuser/.aws/config").exists(), "Source cache mounted in MCP"
s=boto3.Session(profile_name="aws-mcp-sts-quick")
assert s.get_credentials().method=="custom-process", "Unexpected credential provider"
actual=s.client("sts").get_caller_identity()["Arn"]
expected="arn:aws:sts::456720798575:assumed-role/aws-security-audit-readonly/aws-mcp-quick-readonly"
assert actual==expected, "Wrong role session identity"
print("PASS: MCP uses dedicated temporary STS role")
'
echo 'AWS MCP started with 1-hour STS credentials.'
echo 'Run this command again before STS expiry to renew (interactive login each run).'
