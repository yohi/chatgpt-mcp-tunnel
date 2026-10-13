# AWS MCP (read-only by default) via Secure MCP Tunnel

**No ChatGPT plugin/app/connector to AWS is used by this design.** ChatGPT connects only to the explicitly configured **OpenAI Secure MCP Tunnel**. The AWS CLI and SigV4 proxy run in Docker; no host AWS CLI, Python, uv, Node.js, or npm installation is required.

## Architecture

```text
ChatGPT (custom MCP > Tunnel > AWS-specific Tunnel ID)
  ↕ OpenAI Secure MCP Tunnel
Docker: aws-tunnel = tunnel-client → stdio mcp-proxy-for-aws-cli (SigV4)
  ↕ HTTPS signed with AWS SSO-derived temporary credentials
AWS managed MCP Server (Tokyo by default)
  ↕ IAM evaluation on downstream AWS APIs
AWS account, dedicated read-only IAM Identity Center permission set

One-time / periodic interactive login:
Host browser ↔ AWS IAM Identity Center device authorization
Docker: aws-auth (official AWS CLI v2 image)
  ↕ shared AWS-only named volume aws-sso-data
Docker: aws-tunnel
```

The existing Atlassian MCP uses `compose.yaml` and the `oauth-data` volume. **AWS uses an independent Tunnel ID, key, image, Compose file, SSO volume, and health port (18081)**. The AWS containers use Docker bridge networking, not host networking; only the loopback diagnostic endpoint is published.

## Security decision: read-only is enforced by IAM

This starter uses two independent layers:

1. **IAM Identity Center dedicated permission set/role.** For an initial test, attach AWS-managed `ReadOnlyAccess` **only** to a dedicated role; do not add administrator or write policies to the same effective principal. Verify the effective access against SCPs, resource policies and other permissions. `ReadOnlyAccess` can read sensitive resource contents (for example S3 data, DynamoDB records and security/billing configurations), so restrict to necessary services and resources before sharing access or production use.
2. **`mcp-proxy-for-aws-cli --read-only`** filters tools using MCP `readOnlyHint` annotations. These annotations **are not a security boundary**. An AWS MCP tool that can execute API calls/scripts might be filtered out even when you want resource inventory. Do not remove `--read-only` just to bypass this without explicitly reviewing the IAM policy and tool risks.

Use `AWS_PROFILE=aws-mcp-readonly` only. The proxy is given exactly **one** allowed AWS profile and the auth volume is not shared with Atlassian. No fixed IAM access key is generated or stored by this project.

**Explicit operational rules:** No AWS mutation, IAM changes or live service operations are performed automatically. Do not grant write permissions to this role as a convenient workaround. A future write-capable route needs independent review and a separate role, Tunnel and approval path. At-rest access to the Docker volume permits use of its cached SSO credentials; protect Docker administrative access and backups.

## One-time AWS and OpenAI preparation (human administrator)

1. Enable/configure AWS IAM Identity Center, a user assignment to the intended AWS account, and a dedicated least-privilege permission set (e.g. `AWSMCPReadOnly`). For an initial proof of connectivity, `ReadOnlyAccess` is an intentionally broad starting point, **not the desired final least-privilege policy**.
2. Create a **second** OpenAI Tunnel dedicated to AWS, separate from the existing Atlassian Tunnel. Ensure the runtime key and ChatGPT operator have Tunnels Read+Use privileges for the correct workspace. Do not use a Platform admin API key for the daemon.
3. Copy the AWS environment template locally and edit only the new AWS Tunnel credentials. Keep the existing Atlassian `.env` unchanged:

```bash
cp .env.aws.example .env.aws
chmod 600 .env.aws
${EDITOR:-vi} .env.aws
```

Do not commit this file, account IDs, SSO portal URLs, one-time device codes, authorization links, runtime API keys or credentials.

## First-time Docker build and SSO profile setup

These commands run in the repository root. The existing published-tunnel-binary verification in `Dockerfile` is **reused**, so build it first:

```bash
docker compose build tunnel
docker compose --env-file .env.aws -f compose.aws.yaml build aws-tunnel
```

Before running the auth helper, create the AWS volume with the correct non-root ownership:

```bash
docker compose --env-file .env.aws -f compose.aws.yaml \
  run --rm --no-deps --entrypoint sh aws-tunnel \
  -c 'test -d /home/awsuser/.aws && test -w /home/awsuser/.aws'
```

This command only tests the volume permissions. It does not use AWS credentials or start the tunnel daemon.

Configure an SSO profile **inside** the AWS CLI image (interactive prompts). Use **exactly** `aws-mcp-readonly` as the profile name; choose the correct *read-only* AWS account role. The SSO region (Identity Center region) can differ from the AWS MCP endpoint region:

```bash
docker compose --env-file .env.aws -f compose.aws.yaml \
  run --rm aws-auth configure sso --use-device-code
```

Login using a separate browser/device with the displayed verification URL and code. **Do not post codes or full login URLs** to chats or issue trackers:

```bash
docker compose --env-file .env.aws -f compose.aws.yaml \
  run --rm aws-auth sso login \
  --profile aws-mcp-readonly --no-browser --use-device-code
```

Verify which principal was selected (read-only API, but account/role information should not be posted publicly):

```bash
docker compose --env-file .env.aws -f compose.aws.yaml \
  run --rm aws-auth sts get-caller-identity --profile aws-mcp-readonly
```

SSO caches are persistent, but sessions expire and **re-login is required**. This setup does not perform unattended reauthorization, and will not bypass MFA. The proxy resolves SSO-derived temporary credentials through the standard SDK chain.

## Start, inspect and connect to ChatGPT

```bash
docker compose --env-file .env.aws -f compose.aws.yaml up -d aws-tunnel
docker compose --env-file .env.aws -f compose.aws.yaml ps
docker compose --env-file .env.aws -f compose.aws.yaml logs --tail=100 aws-tunnel

curl -fsS http://127.0.0.1:18081/health/control-plane | python3 -m json.tool
curl -fsS http://127.0.0.1:18081/health/mcp | python3 -m json.tool
```

A `control-plane.status: ok` with `last_success` proves a successful OpenAI poll, **not** AWS authorization. The stdio MCP health may say `not_observed` until actual ChatGPT traffic flows. If the login has expired, refresh the `aws-auth` SSO session; depending on the proxy state, a tunnel restart may be necessary.

In ChatGPT, add a **custom MCP with connection type Tunnel** using the newly created AWS Tunnel ID. The ChatGPT-to-local-Tunnel hop uses *No authentication*, while the Docker proxy signs AWS requests with SigV4; these are different authentication boundaries. Restrict Tunnel access to the intended users, as the cached AWS SSO identity is shared by callers of this Tunnel.

**First read-only test:** "Use the AWS Tunnel to list the available AWS Regions and search AWS documentation. Do not modify anything." Then inspect `/health/mcp`. To verify actual AWS account access, test an IAM-permitted, non-mutating resource-listing tool if that tool is available under `--read-only`. If no such tool is exposed, mark **AWS-resource-read acceptance unproven** and review the filtered tool list and IAM policy rather than turning off controls.

## Troubleshooting and local trust

- OpenAI poll in `backoff` or `network_error`: inspect `/health/control-plane` and TLS errors. `/readyz` alone is not proof of a successful poll.
- `x509: certificate signed by unknown authority`: the Python runtime and AWS CLI use different trust paths. For trusted Debian/Ubuntu host CA bundles, see `compose.aws.ca.example.yaml`; apply **only** after verifying your CA roots. Never disable TLS verification.
- AWS `AccessDenied`: confirm the designated SSO profile and IAM permission set. Modern AWS managed MCP Server authorizes downstream AWS API actions using IAM; legacy `aws-mcp:InvokeMcp` grants are no longer required.
- `ExpiredToken`: re-run `aws-auth sso login` above. Do not delete `aws-sso-data` to refresh a session.
- Missing AWS tools: check `--read-only` tool annotations, logged auth errors and `/health/mcp`; no guarantees that the full resource-inspection toolset is exposed.
- AWS CLI cannot write to cache: create/inspect `aws-sso-data` using the non-root runtime image and confirm UID/GID 10001 ownership.
- `docker compose down -v` **deletes SSO tokens**; never use `-v` casually.
- AWS endpoint region is distinct from the default AWS API target region (the latter comes from `--metadata AWS_REGION=...`).
- Runtime proxy version is pinned to `mcp-proxy-for-aws-cli==1.7.0` (transitive pins provided by AWS); the base Python and AWS CLI images are version-tagged, not immutable digests.

## References

- [AWS managed MCP Server setup](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/getting-started-aws-mcp-server.html)
- [MCP Proxy for AWS CLI](https://github.com/aws/mcp-proxy-for-aws)
- [AWS MCP Server IAM integration](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/security_iam_service-with-iam.html)
- [AWS CLI IAM Identity Center](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html)
- [AWS CLI Docker image](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-docker.html)
