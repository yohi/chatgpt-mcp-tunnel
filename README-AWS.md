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

The existing Atlassian MCP uses `compose.yaml` and the `oauth-data` volume. **AWS uses an independent Tunnel ID, key, image, Compose file, credential cache volume, and health port (18081)**. The preexisting volume and initializer retain their `aws-sso-*` names for backward compatibility; **IAM Identity Center is not required**. The AWS containers use Docker bridge networking, not host networking; only the loopback diagnostic endpoint is published.

## Security decision: read-only is enforced by IAM

This starter uses two independent layers:

1. **Dedicated IAM console identity or federated role with effective read-only access.** For a proof of connectivity, `ReadOnlyAccess` is a broad starting point, not a production least-privilege policy; scope services and resources further before production. Never authenticate the MCP using AWS root or an administrator. `ReadOnlyAccess` can read sensitive S3 data, DynamoDB records and service configurations.
2. **Login privilege separate from resource access.** AWS CLI `aws login` requires `SignInLocalDevelopmentAccess` on the console principal. This grants console-to-CLI sign-in capability, **not** downstream AWS resource write permissions. Scope both login privileges and AWS resource permissions to the dedicated principal.
3. **`mcp-proxy-for-aws-cli --read-only`** filters tools using MCP `readOnlyHint` annotations. These annotations **are not a security boundary**. An AWS MCP tool that can execute API calls/scripts might be filtered out even when you want resource inventory. Do not remove `--read-only` just to bypass this without explicitly reviewing the IAM policy and tool risks.

Use `AWS_PROFILE=aws-mcp-readonly` only. The proxy is given exactly **one** AWS profile and the login cache is not shared with Atlassian. No IAM access key is created or stored by this project. The Boto3 `login_session` provider requires `boto3[crt]` (Boto3 >=1.41.0); the runtime image installs that extra explicitly.

**Explicit operational rules:** No AWS mutation, IAM changes or live service operations are performed automatically. Do not grant write permissions to this role as a convenient workaround. A future write-capable route needs independent review and a separate role, Tunnel and approval path. At-rest access to the Docker volume permits use of its cached console-login credentials; protect Docker administrative access and backups.

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

curl -fsS http://127.0.0.1:18081/health/control-plane | python3 -m json.tool
curl -fsS http://127.0.0.1:18081/health/mcp | python3 -m json.tool
```

A `control-plane.status: ok` with `last_success` proves a successful OpenAI poll, **not** AWS authorization. The stdio MCP health may say `not_observed` until actual ChatGPT traffic flows. If the login has expired, repeat `aws login --remote` using the `aws-auth` helper; if the proxy continues to report stale credentials after re-login, restart only `aws-tunnel`.

In ChatGPT, add a **custom MCP with connection type Tunnel** using the newly created AWS Tunnel ID. The ChatGPT-to-local-Tunnel hop uses *No authentication*, while the Docker proxy signs AWS requests with SigV4; these are different authentication boundaries. Restrict Tunnel access to the intended users, as the cached AWS console identity is shared by callers of this Tunnel.

**First read-only test:** "Use the AWS Tunnel to list the available AWS Regions and search AWS documentation. Do not modify anything." Then inspect `/health/mcp`. To verify actual AWS account access, test an IAM-permitted, non-mutating resource-listing tool if that tool is available under `--read-only`. If no such tool is exposed, mark **AWS-resource-read acceptance unproven** and review the filtered tool list and IAM policy rather than turning off controls.

## Troubleshooting and local trust

- OpenAI poll in `backoff` or `network_error`: inspect `/health/control-plane` and TLS errors. `/readyz` alone is not proof of a successful poll.
- `x509: certificate signed by unknown authority`: the Python runtime and AWS CLI use different trust paths. For trusted Debian/Ubuntu host CA bundles, see `compose.aws.ca.example.yaml`; apply **only** after verifying your CA roots. Never disable TLS verification.
- AWS `AccessDenied`: confirm the designated `aws-mcp-readonly` console-login profile, `SignInLocalDevelopmentAccess` login permission and separately granted downstream read access. Modern AWS managed MCP Server authorizes downstream AWS API actions using IAM; legacy `aws-mcp:InvokeMcp` grants are no longer required.
- `ExpiredToken` / `LoginRefreshRequired`: repeat `aws-auth login --remote --profile aws-mcp-readonly`. The upstream MCP proxy has reported refresh-boundary problems (see aws/mcp-proxy-for-aws issues #304 and #321); after re-login, check `aws-auth sts get-caller-identity` and restart **only aws-tunnel** if requests remain stuck. Do not delete `aws-sso-data` to refresh a session.
- Missing AWS tools: check `--read-only` tool annotations, logged auth errors and `/health/mcp`; no guarantees that the full resource-inspection toolset is exposed.
- AWS CLI cannot write to cache: use the one-time `aws-sso-init` helper and verify UID/GID 10001 write access. The helper name is historical and does not imply Identity Center is in use. Do not use `down -v` to repair ownership.
- `docker compose down -v` **deletes SSO tokens**; never use `-v` casually.
- The AWS `aws login` cache requires `boto3[crt]` in the Python MCP proxy image, not only AWS CLI v2 in the auth helper. A successful CLI `sts get-caller-identity` does **not** prove the Python proxy can resolve it.
- AWS endpoint region is distinct from the default AWS API target region (the latter comes from `--metadata AWS_REGION=...`).
- If `public.ecr.aws/aws-cli/aws-cli:...` fails with `toomanyrequests: Rate exceeded`, that is a container registry **pull quota**, not an AWS SSO/IAM error. The default now uses AWS's officially published Docker Hub image `amazon/aws-cli:2.37.12`, configurable with `AWS_CLI_IMAGE`. Docker Hub may have its own rate limits; do not disable auth or change IAM as a workaround. `orphan containers` warnings are expected when the same Compose project has the separate Atlassian service: **never run with `--remove-orphans`** or it could remove that service.
- Runtime proxy is pinned to `mcp-proxy-for-aws-cli==1.7.0`, Boto3+CRT to `1.42.84`; Python and AWS CLI base images are version-tagged, not immutable digests. Retest security and credential-refresh compatibility when upgrading.

## References

- [AWS managed MCP Server setup](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/getting-started-aws-mcp-server.html)
- [MCP Proxy for AWS CLI](https://github.com/aws/mcp-proxy-for-aws)
- [AWS MCP Server IAM integration](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/security_iam_service-with-iam.html)
- [AWS CLI console credential login](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sign-in.html)
- [Boto3 login credentials provider](https://docs.aws.amazon.com/boto3/latest/guide/credentials.html)
- [AWS CLI Docker image](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-docker.html)
