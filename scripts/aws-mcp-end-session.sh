#!/usr/bin/env bash
# End the temporary IAM-role AWS MCP session and remove the project-owned
# timestamped role, leaving administrator login and Atlassian untouched.
# This is an *explicit* operator action; an ordinary container restart or
# Docker daemon failure MUST NOT delete an in-use IAM role.
set -euo pipefail

cd "$(dirname "$0")/.."
common=(docker compose --env-file .env.aws -f compose.aws.yaml)
isolated=(${common[@]} -f compose.aws.api-tools.example.yaml)

# First stop all potential issuers/users of the role. A failure here
# aborts before any IAM role deletion attempt.
"${isolated[@]}" stop aws-tunnel aws-credential-broker

remaining=$("${isolated[@]}" ps -q --status running aws-tunnel aws-credential-broker)
if [[ -n "${remaining}" ]]; then
  echo "Refusing IAM role deletion: AWS MCP Tunnel or broker still running" >&2
  exit 1
fi

# Cleanup re-verifies the exact IAM RoleId, ARN, trust principal,
# ownership tags, policies and absence of instance profiles.
# It purges only the role-only STS credential document, detaches our
# managed ReadOnlyAccess policy and deletes only the recorded role.
"${common[@]}" run --rm --no-deps aws-role-bootstrap --cleanup --confirm-stopped
