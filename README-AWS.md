# AWS MCP (read-only by default) via Secure MCP Tunnel

**No ChatGPT plugin/app/connector to AWS is used by this design.** ChatGPT connects only to the explicitly configured **OpenAI Secure MCP Tunnel**. The AWS CLI and SigV4 proxy run in Docker; no host AWS CLI, Python, uv, Node.js, or npm installation is required.

## Architecture

```text
ChatGPT (custom MCP > Tunnel > AWS-specific Tunnel ID)
  ↕ OpenAI Secure MCP Tunnel
Docker: aws-tunnel = tunnel-client → stdio mcp-proxy-for-aws-cli (SigV4)
  ↕ HTTPS signed with AWS CLI console-login temporary credentials
AWS managed MCP Server (Tokyo by default)
  ↕ IAM evaluation on downstream AWS APIs
AWS account, dedicated read-only IAM console identity / federated role

One-time / periodic interactive login:
Host browser ↔ AWS Sign-In (console login, cross-device code)
Docker: aws-auth (official AWS CLI v2 image)
  ↕ shared AWS-only named volume aws-sso-data
Docker: aws-tunnel
```

The existing Atlassian MCP uses `compose.yaml` and the `oauth-data` volume. **AWS uses an independent Tunnel ID, key, image, Compose file, credential cache volume, and internal health listener (127.0.0.1:18081)**. The preexisting volume and initializer retain their `aws-sso-*` names for backward compatibility; **IAM Identity Center is not required**. AWS containers use Docker bridge networking, not host networking. **No AWS health port is published to the host.** The OpenAI runtime's detailed `/health/*` API is explicitly *loopback-only* and denies requests forwarded through Docker's published ports with HTTP **403**; an address of `127.0.0.1` on the host does not make the request a container-internal loopback peer. Use `docker compose exec` for component-level diagnostics. See [upstream health documentation](https://github.com/openai/tunnel-client/blob/master/docs/health.md).

## Security decision: read-only is enforced by IAM

This starter uses two independent layers:

1. **Dedicated IAM console identity or federated role with effective read-only access.** For a proof of connectivity, `ReadOnlyAccess` is a broad starting point, not a production least-privilege policy; scope services and resources further before production. Never authenticate the MCP using AWS root or an administrator. `ReadOnlyAccess` can read sensitive S3 data, DynamoDB records and service configurations.
2. **Login privilege separate from resource access.** AWS CLI `aws login` requires `SignInLocalDevelopmentAccess` on the console principal. This grants console-to-CLI sign-in capability, **not** downstream AWS resource write permissions. Scope both login privileges and AWS resource permissions to the dedicated principal.
3. **`mcp-proxy-for-aws-cli --read-only`** filters tools using MCP `readOnlyHint` annotations. These annotations **are not a security boundary**. An AWS MCP tool that can execute API calls/scripts might be filtered out even when you want resource inventory. Do not remove `--read-only` just to bypass this without explicitly reviewing the IAM policy and tool risks.

Use `AWS_PROFILE=aws-mcp-readonly` only. The proxy is given exactly **one** AWS profile and the login cache is not shared with Atlassian. No IAM access key is created or stored by this project. The Boto3 `login_session` provider requires `boto3[crt]` (Boto3 >=1.41.0); the runtime image installs that extra explicitly.

**Explicit operational rules:** No AWS mutation, IAM changes or live service operations are performed automatically. Do not grant write permissions to this role as a convenient workaround. A future write-capable route needs independent review and a separate role, Tunnel and approval path. At-rest access to the Docker volume permits use of its cached console-login credentials; protect Docker administrative access and backups.

## Fast path: one command to provision the IAM role (no console clicks)

If you already have a valid `aws login --remote --profile aws-mcp-readonly`
session, **you do not have to create or configure the IAM role manually**.
The repo includes an explicitly invoked, one-shot bootstrap that:
- Identifies the *current* IAM user using STS `GetCallerIdentity`.
- Creates the fixed role `ChatGPTMcpReadOnlyRole`, trusting **only that IAM user**.
- Attaches **only** the AWS-managed `ReadOnlyAccess` policy to the new role.
- Refuses to overwrite an existing role with a different trust relationship,
  attached policies, or unexpected inline policy.
- Never prints session access keys or modifies the existing IAM user.
- Does not grant write privileges to the role and does not start the MCP.

**Before the first run:** pull the PR #10 branch and build the AWS image.
Do not merge this draft or start the AWS Tunnel while it is using the
administrator's original credentials.

```bash
git fetch origin
git switch feat/aws-broad-iam-read-api-tools
git pull --ff-only origin feat/aws-broad-iam-read-api-tools
docker compose --env-file .env.aws -f compose.aws.yaml build aws-tunnel

# Read-only preview of current identity and target role.
docker compose --env-file .env.aws -f compose.aws.yaml \
  run --rm --no-deps aws-role-bootstrap

# Only the following invocation creates an IAM role if it is absent.
docker compose --env-file .env.aws -f compose.aws.yaml \
  run --rm --no-deps aws-role-bootstrap --apply
```

The tool is **not run automatically** during Compose startup, builds,
or installation. The `--apply` command is an explicit
IAM **CreateRole / AttachRolePolicy** operation, so review the preview
before running it. Administrator authorization is required on the original
IAM login account. If a same-named role already exists, the script
validates and **does not modify** it.

After that, the STS Broker automatically derives the approved default role
ARN from the authenticated account. **No manual account ID, role ARN, or
additional `.env.aws` setting is required.** The optional
`AWS_MCP_READ_ROLE_ARN` environment setting is for an independently
reviewed *non-default* role; never point it at an admin role.

Proceed to the [STS broker activation steps](#activate-on-an-authorized-read-only-iam-role).
IAM role creation is an AWS account mutation, which has not been executed
by the repository or its CI. The human operator must review IAM trust,
permission boundaries, resource policies, organization SCPs and sensitive
read-data exposure independently before enabling `run_script`.

## All-service AWS API reads via isolated STS credentials (opt-in)

The baseline `compose.aws.yaml` deliberately leaves
`mcp-proxy-for-aws-cli --read-only` enabled. Because AWS's generic
`run_script` can invoke **both** read and write APIs, its MCP tool
annotation hides it completely; this prevents ChatGPT from using even
EC2 `DescribeInstances` through that tool. This is a **tool visibility
filter**, not granular service-level authorization.

For an AWS-wide read API inventory (EC2, ECS, S3, Lambda, RDS, IAM,
CloudWatch, etc.), `compose.aws.api-tools.example.yaml` exposes
`run_script` **only with a separate STS AssumeRole credential boundary**.
This is a replacement for the earlier unsafe override that used the
administrator's login credentials directly.

```text
aws-auth                   (console login as existing IAM user)
    └── aws-sso-data             ← admin login cache
              │
              ▼
aws-credential-broker     (boto3 login → sts:AssumeRole)
    ├── AWS-managed ReadOnlyAccess SESSION POLICY (intersection)
    └── aws-mcp-role-credentials  ← atomic STS role credentials (0600)
              │                         (separate named Docker volume)
              ▼                         (read-only mount)
aws-tunnel                (credential_process + SigV4)
    ├── NO aws-sso-data mount
    ├── NO AWS login source profile
    └── MCP run_script → AWS API (IAM role/session policy enforcement)
```

**Trust and authorization prerequisites (operator / IAM owner)**

1. Provision an independently reviewed IAM role such as
   `ChatGPTMcpReadOnlyRole`. Its **trust policy** must permit precisely the
   intended human IAM principal to call `sts:AssumeRole`. Its **permissions**
   policy should grant `arn:aws:iam::aws:policy/ReadOnlyAccess` or a
   narrower, reviewed set of read actions; don't attach administrator
   permissions. The source login user's existing grants are **not
   inherited** by the assumed role.
2. The broker also passes AWS-managed `ReadOnlyAccess` as an **STS managed
   session policy**, so the role session grants only the **intersection**
   of the role policy and that policy. The credential is valid for one hour
   and is reissued every 20 minutes, while source `aws login` is valid.
   Do not assume this is a universal deny guarantee against resource-based
   policies granting directly to session principals, cross-account trust,
   or data-plane query semantics. Review the role trust, policies, resource
   policies, boundaries and Organizations SCPs separately.
3. Restrict the OpenAI AWS Tunnel to trusted users, enable audit logging and
   review access to sensitive data. IAM `ReadOnlyAccess` is broad and not
   guaranteed to include every conceivable read API. A reader may still
   fetch customer data, secret metadata and some data-plane records.
4. **Never** rely solely on the words "read-only" in a profile, natural
   language prompts, or an MCP annotation. Do not mutate IAM/STS/roles as
   part of the Docker setup; provisioning/approval is external to this PR.

**Requirements**: Docker Compose **2.24.4+**, the existing Docker AWS image,
a working `aws login --remote --profile aws-mcp-readonly` cache, and an
existing independently reviewed IAM role (which the optional one-time
bootstrap above can create). The Compose `!override` YAML tag is a mandatory security
invariant: it **replaces**, rather than merges, the original admin
credential mount. If Compose does not support it, **stop**; do not remove
the tag to work around parsing.

### Activate on an authorized read-only IAM role

When using the **one-command default role bootstrap** above,
**no `.env.aws` change is necessary**: the broker derives the role ARN from
the same authenticated AWS account. For an independently provisioned and
approved custom role only, optionally set
`AWS_MCP_READ_ROLE_ARN=arn:aws:iam::<ACCOUNT_ID>:role/<APPROVED_ROLE>`
in the local ignored `.env.aws`.

Confirm the role and trust policy were independently reviewed before
applying the runtime override. From the repository root:

```bash
docker compose version

# Validate the effective config and inspect it BEFORE touching containers.
docker compose --env-file .env.aws \
  -f compose.aws.yaml -f compose.aws.api-tools.example.yaml \
  config --quiet

# One-time ownership initialization for the *role-only* credential volume.
# It never alters the original AWS login cache.
docker compose --env-file .env.aws \
  -f compose.aws.yaml -f compose.aws.api-tools.example.yaml \
  run --rm --no-deps aws-role-init

# Start the independent STS role credential broker.
docker compose --env-file .env.aws \
  -f compose.aws.yaml -f compose.aws.api-tools.example.yaml \
  up -d --no-deps aws-credential-broker

# See only role credential health, not access keys or tokens.
docker compose --env-file .env.aws \
  -f compose.aws.yaml -f compose.aws.api-tools.example.yaml \
  ps

# Start AWS Tunnel with role-only credentials and broad API tool discovery.
docker compose --env-file .env.aws \
  -f compose.aws.yaml -f compose.aws.api-tools.example.yaml \
  up -d --force-recreate aws-tunnel
```

Then verify isolation without printing any credential values:

```bash
docker compose --env-file .env.aws \
  -f compose.aws.yaml -f compose.aws.api-tools.example.yaml \
  exec -T aws-tunnel python - <<'PY'
import boto3
import os
from pathlib import Path
session = boto3.Session(profile_name="aws-mcp-sts-readonly")
creds = session.get_credentials()
assert creds is not None and creds.method == "custom-process", "role credential_process not in use"
print("Profile:", session.profile_name)
print("Provider:", creds.method)
print("Admin cache mounted:", Path("/home/awsuser/.aws/config").exists())
identity = session.client("sts").get_caller_identity()
assert ":assumed-role/" in identity["Arn"], "Expected STS role session"
assert "/ChatGPTMcpReadOnlyRole/" in identity["Arn"], "Unexpected role identity"
print("STS role identity: OK")
print("No credentials printed")
PY
```

**Review the role name above** when using a different role (change the
assertion to your approved IAM role's name). The expected provider name
in botocore is normally `custom-process`; `sts:GetCallerIdentity`
verifies session identity, not the total effective permissions.
Check the actual tool list after reconnecting ChatGPT (`run_script`,
possibly prefixed `aws___`), then exercise non-mutating API calls.

### Renewal, fail-closed operation, and rollback

The broker alone can access the admin login cache. Its STS session is
refreshed every 20 minutes; the MCP child uses AWS SDK
`credential_process` with the **Expiration** field, which causes
credentials to be re-read before expiry. The broker writes an atomic,
owner-only 0600 file on a private volume. If source `aws login` expires
(up to 12h), re-run:

```bash
docker compose --env-file .env.aws -f compose.aws.yaml \
  run --rm aws-auth login --remote --profile aws-mcp-readonly
```

Broker refresh retries after 60 seconds. If requests are already failing,
verify the broker with `ps` and `logs --tail=100 aws-credential-broker`
before retrying the custom MCP connection. The MCP will reject absent,
malformed or nearly expired STS credentials, rather than use the admin
source profile. Restart only the AWS Tunnel if the Python MCP proxy
continues using an expired in-memory credential set. Neither routine
renewal nor startup requires deleting a cached-login or role-credential
volume. A broker crash cannot issue new sessions.

**Rollback**: recreate AWS Tunnel from the baseline Compose (this hides
`run_script` and restores the original SDK login source, which is
ADMINISTRATIVE in the current account). For maximum safety, **stop** it
instead of running baseline MCP under an administrator identity:

```bash
docker compose --env-file .env.aws -f compose.aws.yaml stop aws-tunnel
docker compose --env-file .env.aws \
  -f compose.aws.yaml -f compose.aws.api-tools.example.yaml \
  stop aws-credential-broker
```

Do **not** use `--remove-orphans`, `down -v` or Docker volume removal.
The original AWS login credentials remain available to `aws-auth` and
`aws-credential-broker`, so protect the Docker host and never treat
compromise of the broker or host as an isolated read-only event.
The dedicated role must not trust arbitrary principals, allow privilege
escalation, or expose write paths.

References: [AWS STS AssumeRole session policies](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html),
[AWS Boto3 credential_process](https://docs.aws.amazon.com/boto3/latest/guide/credentials.html),
[Docker Compose !override](https://docs.docker.com/reference/compose-file/merge/),
[AWS managed ReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/ReadOnlyAccess.html).

## One-time AWS and OpenAI preparation (human administrator)

1. **No IAM Identity Center setup is necessary.** Have an AWS administrator arrange a dedicated IAM console identity or suitable IAM-federated role with only the required AWS read permissions, plus `SignInLocalDevelopmentAccess` to enable `aws login`. Confirm the role is not able to mutate resources or escalate its own privileges. Do not use root or an existing admin console identity as a shortcut.
2. Create a **second** OpenAI Tunnel dedicated to AWS, separate from the existing Atlassian Tunnel. Ensure the runtime key and ChatGPT operator have Tunnels Read+Use privileges for the correct workspace. Do not use a Platform admin API key for the daemon.
3. Copy the AWS environment template locally and edit only the new AWS Tunnel credentials. Keep the existing Atlassian `.env` unchanged:

```bash
cp .env.aws.example .env.aws
chmod 600 .env.aws
${EDITOR:-vi} .env.aws
```

Do not commit this file, account IDs, login session cache, one-time device codes, authorization links, runtime API keys or credentials.

## First-time Docker build and browser console login

These commands run in the repository root. The existing published-tunnel-binary verification in `Dockerfile` is **reused**, so build it first:

```bash
docker compose build tunnel
docker compose --env-file .env.aws -f compose.aws.yaml build aws-tunnel
```

Prepare the AWS-only credential-cache volume for **non-root UID 10001**. This step also
repairs the volume's top-level mount directory created by an earlier failed
image pull, **without deleting or recursively changing existing cached credentials**:

```bash
docker compose --env-file .env.aws -f compose.aws.yaml \
  run --rm aws-sso-init

# Confirm UID 10001 can write to the mounted AWS cache:
docker compose --env-file .env.aws -f compose.aws.yaml \
  run --rm --no-deps --entrypoint sh aws-tunnel \
  -c 'test -d /home/awsuser/.aws && test -w /home/awsuser/.aws'
```

`aws-sso-init` is an **opt-in one-shot** root helper with only `CAP_CHOWN`
and only the AWS named volume mounted; it does not contact AWS or touch the
Atlassian volume. The helper changes **only the mount directory's ownership**,
not any nested files. This is deliberate: recursive `chown -R` cannot traverse
a private mode-0700 directory with only `CAP_CHOWN`, and changing descendants
could unexpectedly modify previously stored authentication state.
If a preexisting nested AWS cache is owned by another UID, stop and inspect
its ownership before attempting any separate migration. The helper does not
run with the long-lived tunnel. Do not run it unnecessarily after SSO has
been configured.

**Stop using `aws configure sso`: IAM Identity Center is not enabled or required.**
Use the official AWS CLI v2 `aws login --remote` on the helper container,
with the exact profile name `aws-mcp-readonly`. The command prints a
cross-device login URL and code. Complete the sign-in from the Linux host's
browser **as the dedicated read-only AWS identity**, not root or admin.

```bash
docker compose --env-file .env.aws -f compose.aws.yaml \
  run --rm aws-auth login --remote --profile aws-mcp-readonly
```

If prompted for a default Region, choose the AWS MCP endpoint Region
(default `ap-northeast-1`), or your required AWS resource Region. You are
**not** prompted for an Identity Center start URL or SSO Region.
Do not paste authorization URLs, codes, login-cache contents, or AWS
account IDs into public issues/chats. If login is denied, have an AWS
administrator verify `SignInLocalDevelopmentAccess` is assigned to
the exact effective console identity; do not switch to root.

This also supports later reauthentication using the same command.
Credentials are refreshed automatically during an active login session,
with maximum session validity of 12 hours.

Verify which principal was selected (read-only API, but account/role information should not be posted publicly):

```bash
docker compose --env-file .env.aws -f compose.aws.yaml \
  run --rm aws-auth sts get-caller-identity --profile aws-mcp-readonly
```

Console-login caches are persistent, but the credentials refresh automatically within an active session; interactive **re-login is needed at the session boundary** (up to 12 hours). This design does not bypass MFA. The Python proxy resolves temporary credentials through Boto3 + CRT. See the credential-refresh caveat below.

## Start, inspect and connect to ChatGPT

```bash
docker compose --env-file .env.aws -f compose.aws.yaml up -d aws-tunnel
docker compose --env-file .env.aws -f compose.aws.yaml ps
docker compose --env-file .env.aws -f compose.aws.yaml logs --tail=100 aws-tunnel

# Detailed health APIs are restricted to internal loopback. Host curl to
# 127.0.0.1:18081 returned 403 with the old published-port configuration.
docker compose --env-file .env.aws -f compose.aws.yaml exec -T aws-tunnel \
  python -c '
import json
from urllib.request import urlopen
for path in ("/health/control-plane", "/health/mcp"):
    with urlopen("http://127.0.0.1:18081" + path, timeout=5) as response:
        data = json.load(response)
    print(path)
    print(json.dumps(data, indent=2))
'
```

A `control-plane.status: ok` with `last_success` proves a successful OpenAI poll, **not** AWS authorization. The stdio MCP health may say `not_observed` until actual ChatGPT traffic flows. If the login has expired, repeat `aws login --remote` using the `aws-auth` helper; if the proxy continues to report stale credentials after re-login, restart only `aws-tunnel`.

In ChatGPT, add a **custom MCP with connection type Tunnel** using the newly created AWS Tunnel ID. The ChatGPT-to-local-Tunnel hop uses *No authentication*, while the Docker proxy signs AWS requests with SigV4; these are different authentication boundaries. Restrict Tunnel access to the intended users, as the cached AWS console identity is shared by callers of this Tunnel.

**First read-only test:** "Use the AWS Tunnel to list the available AWS Regions and search AWS documentation. Do not modify anything." Then inspect `/health/mcp`. To verify actual AWS account access, test an IAM-permitted, non-mutating resource-listing tool if that tool is available under `--read-only`. If no such tool is exposed, mark **AWS-resource-read acceptance unproven** and review the filtered tool list and IAM policy rather than turning off controls.

## Troubleshooting and local trust

- HTTP `403 Forbidden` from `curl http://127.0.0.1:18081/health/control-plane`: this is the tunnel-client's **local-only diagnostics access policy**, not AWS IAM or failed OpenAI polling. Old Compose versions published the AWS health port through Docker bridge, changing the apparent client address. The current Compose removes that publication; read `/health/control-plane` and `/health/mcp` with the documented `docker compose exec -T aws-tunnel python` command.
- OpenAI poll in `backoff` or `network_error`: inspect `/health/control-plane` and TLS errors. `/readyz` alone is not proof of a successful poll.
- No changes to the AWS SigV4 endpoint, IAM principal, profile, or cached login credentials are needed when correcting a health-only 403. Recreate **only** the AWS tunnel container (`docker compose --env-file .env.aws -f compose.aws.yaml up -d --no-deps --force-recreate aws-tunnel`) after pulling the fix; this does not delete the named AWS volume or modify the Atlassian service. Do not use `--remove-orphans` or `down -v`.

- `x509: certificate signed by unknown authority`: the Python runtime and AWS CLI use different trust paths. For trusted Debian/Ubuntu host CA bundles, see `compose.aws.ca.example.yaml`; apply **only** after verifying your CA roots. Never disable TLS verification.
- AWS `AccessDenied`: confirm the designated `aws-mcp-readonly` console-login profile, `SignInLocalDevelopmentAccess` login permission and separately granted downstream read access. Modern AWS managed MCP Server authorizes downstream AWS API actions using IAM; legacy `aws-mcp:InvokeMcp` grants are no longer required.
- `ExpiredToken` / `LoginRefreshRequired`: repeat `aws-auth login --remote --profile aws-mcp-readonly`. The upstream MCP proxy has reported refresh-boundary problems (see aws/mcp-proxy-for-aws issues #304 and #321); after re-login, check `aws-auth sts get-caller-identity` and restart **only aws-tunnel** if requests remain stuck. Do not delete `aws-sso-data` to refresh a session.
- Missing AWS tools: check `--read-only` tool annotations, logged auth errors and `/health/mcp`; no guarantees that the full resource-inspection toolset is exposed.
- AWS CLI cannot write to cache: use the one-time `aws-sso-init` helper and verify UID/GID 10001 write access. The helper name is historical and does not imply Identity Center is in use. Do not use `down -v` to repair ownership.
- `docker compose down -v` **deletes SSO tokens**; never use `-v` casually.
- The AWS `aws login` cache requires `boto3[crt]` in the Python MCP proxy image, not only AWS CLI v2 in the auth helper. A successful CLI `sts get-caller-identity` does **not** prove the Python proxy can resolve it.
- AWS endpoint region is distinct from the default AWS API target region (the latter comes from `--metadata AWS_REGION=...`).
- If `public.ecr.aws/aws-cli/aws-cli:...` fails with `toomanyrequests: Rate exceeded`, that is a container registry **pull quota**, not an AWS SSO/IAM error. The default now uses AWS's officially published Docker Hub image `amazon/aws-cli:2.37.12`, configurable with `AWS_CLI_IMAGE`. Docker Hub may have its own rate limits; do not disable auth or change IAM as a workaround. `orphan containers` warnings are expected when the same Compose project has the separate Atlassian service: **never run with `--remove-orphans`** or it could remove that service.
- Runtime proxy is pinned to `mcp-proxy-for-aws-cli==1.7.0`, Boto3+CRT to `1.43.82`; Python and AWS CLI base images are version-tagged, not immutable digests. Retest security and credential-refresh compatibility when upgrading.

## References

- [AWS managed MCP Server setup](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/getting-started-aws-mcp-server.html)
- [MCP Proxy for AWS CLI](https://github.com/aws/mcp-proxy-for-aws)
- [AWS MCP Server IAM integration](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/security_iam_service-with-iam.html)
- [AWS CLI console credential login](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sign-in.html)
- [Boto3 login credentials provider](https://docs.aws.amazon.com/boto3/latest/guide/credentials.html)
- [AWS CLI Docker image](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-docker.html)
