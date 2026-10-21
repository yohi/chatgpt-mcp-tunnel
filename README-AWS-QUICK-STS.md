# Temporary AWS MCP ReadOnly via manual STS AssumeRole

> **Docker login / one-command startup:** use `bash scripts/aws-mcp-quick-start.sh`
> and the steps in [README-AWS-QUICK-DOCKER-LOGIN.md](README-AWS-QUICK-DOCKER-LOGIN.md).
> The manual commands below describe the older `aws-mcp-readonly` path and
> are not needed for the Docker `default` login startup.


> **Opt-in, lower-assurance workaround.** This does **not** replace the STS-001 / G1 governance, role review, threat model, or production AWS MCP Broker. It does not assert `STS-001 VERIFIED`. No IAM mutations or live AWS tests are performed by repository code or CI.

The current `master` AWS MCP proxy reads the browser login session directly and uses `--read-only`, which may hide AWS's generic `run_script` tool. **Never simply remove `--read-only` from the direct-login profile if the source identity has administrator privileges.** This quick path exposes the generic tool only after a distinct, explicitly designated IAM role is assumed. The MCP container **cannot mount the original browser login cache**.

## Prerequisites

1. Docker Compose 2.24.4+ supporting `!override` (without it stop; do not remove the tag).
2. Existing `aws login --remote --profile aws-mcp-readonly` completed in the project's `aws-auth` container.
3. A **pre-existing**, manually provisioned same-account IAM role, trusted by the logged-in IAM identity, with `arn:aws:iam::aws:policy/ReadOnlyAccess` attached. The caller must be allowed to call `sts:AssumeRole`. Do not use an admin role or root. **This implementation does not create, update, or delete roles.** Its temporary session additionally passes `ReadOnlyAccess` as a managed session policy. These controls do not establish a universal write-deny for resource-based policies granting directly to session principals; review those separately.
4. A dedicated AWS Secure MCP Tunnel configured as in `README-AWS.md`. Keep Atlassian's Tunnel and `.env` unchanged.

Append the approved **role ARN** (not an access key) to local `.env.aws`:

```dotenv
AWS_MCP_STS_ROLE_ARN=arn:aws:iam::123456789012:role/YourPreExistingMcpReadOnlyRole
```

Never commit `.env.aws`. Replace the example ARN with the exact role established by your AWS administrator.

## Build, issue, then start

Execute in the repository root on the quick-STS branch:

```bash
# Stop any already-running direct-login AWS MCP container before changing profiles.
docker compose --env-file .env.aws -f compose.aws.yaml stop aws-tunnel

# Build tunnel-client first; then build the image with quick STS helper.
docker compose build tunnel
docker compose --env-file .env.aws -f compose.aws.yaml build aws-tunnel

# Inspect effective Compose; aws-tunnel must have ONLY /run/aws-mcp-quick-sts:ro.
docker compose --env-file .env.aws -f compose.aws.yaml \
  -f compose.aws.quick-sts.yaml config --format json > /tmp/aws-quick-effective.json
python3 - <<'PY'
import json
x=json.load(open('/tmp/aws-quick-effective.json',encoding='utf-8'))
vol=x['services']['aws-tunnel']['volumes']
assert len(vol)==1 and vol[0]['target']=='/run/aws-mcp-quick-sts' and vol[0]['read_only']
assert '/home/awsuser/.aws' not in json.dumps(x['services']['aws-tunnel'])
print('Verified role-only mount; source login cache absent from MCP.')
PY

# Initialize separate private role volume (no IAM change).
docker compose --env-file .env.aws -f compose.aws.yaml \
  -f compose.aws.quick-sts.yaml run --rm --no-deps aws-quick-sts-init

# Issue ONE one-hour session. Requires IAM role trust and sts:AssumeRole.
docker compose --env-file .env.aws -f compose.aws.yaml \
  -f compose.aws.quick-sts.yaml run --rm --no-deps aws-quick-sts-issue

# Important: recreate existing aws-tunnel, otherwise it may still have source cache mounted.
docker compose --env-file .env.aws -f compose.aws.yaml \
  -f compose.aws.quick-sts.yaml up -d --no-deps --force-recreate aws-tunnel
```

The one-shot issuer checks the source account, STS assumed-role ARN, and actual identity using the returned temporary credentials. It publishes only temporary role credentials in a separate private volume, mode `0600`, using atomic replace. This is **not an effective-permissions audit**.

## Verify the actual runtime credentials

```bash
docker compose --env-file .env.aws -f compose.aws.yaml \
  -f compose.aws.quick-sts.yaml exec -T aws-tunnel python - <<'PY'
import boto3
from pathlib import Path
assert not Path('/home/awsuser/.aws/config').exists()
s=boto3.Session(profile_name='aws-mcp-sts-quick')
assert s.get_credentials().method == 'custom-process'
arn=s.client('sts').get_caller_identity()['Arn']
assert ':assumed-role/' in arn and '/aws-mcp-quick-readonly' in arn
print('Role-only STS identity OK (no credentials printed)')
PY
```

`sts:GetCallerIdentity` confirms the role identity, **not** a comprehensive read-only enforcement proof. Use only explicitly nonmutating MCP reads (e.g. EC2 Describe) for smoke testing; do not attempt writes to test denial against a real resource.

## Manual renewal and stop

This implementation intentionally has **no background renewal**. Repeat `aws-quick-sts-issue` every 45-50 minutes while in use, then recreate `aws-tunnel` to flush the proxy's in-memory credential state if needed. The browser login may need to be renewed after up to 12 hours:

```bash
docker compose --env-file .env.aws -f compose.aws.yaml \
  run --rm aws-auth login --remote --profile aws-mcp-readonly
```

For an end-of-use stop, retain unrelated Atlassian services:

```bash
docker compose --env-file .env.aws -f compose.aws.yaml \
  -f compose.aws.quick-sts.yaml stop aws-tunnel
```

Then clear the role-only credential file (without accessing or deleting the browser login cache):

```bash
docker compose --env-file .env.aws -f compose.aws.yaml \
  -f compose.aws.quick-sts.yaml run --rm --no-deps aws-quick-sts-clear
```

Temporary STS credentials expire automatically after an hour, but can otherwise remain in the Docker volume. Protect Docker host access and backups. Never use `docker compose down -v` or `--remove-orphans`; those may destroy unrelated credentials and containers.

**Known limitations:** broad read permission can expose private data; `run_script` is write-capable in principle and relies on effective AWS IAM evaluation; direct role-session resource policies can escape session-policy limits; no automatic renewal, explicit deny guarantee, continuous checks, user-scoped isolation, formal security authorization, or production-grade audit. Do not present this as formal STS-001 closure or G1 adoption.
