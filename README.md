# ChatGPT MCP Tunnel — Atlassian MCP v2 (Docker)

A **Linux-only Docker Compose configuration** for:

```text
ChatGPT custom MCP (Tunnel)
    ↕ OpenAI Secure MCP Tunnel
Docker container: tunnel-client → stdio mcp-remote
    ↕ HTTPS + locally managed OAuth
Atlassian Rovo MCP v2 (https://mcp.atlassian.com/v2/mcp)
```

No host installation of Node.js, npm, or `tunnel-client` is required. Only Docker Engine, the Docker Compose plugin, and a browser are needed.

## Important network trade-off

`mcp-remote`'s browser OAuth flow redirects to a **loopback address** (`localhost:<port>`). On Linux, `network_mode: host` gives the container the host network namespace so the **host browser** can complete the callback without publishing a port or changing the OAuth redirect URI. **Host networking reduces network isolation**; do not use this setup for untrusted container images or on a shared machine. Docker Desktop / macOS / Windows are outside the tested scope.

**Observed verification (2026-10-13, JST):** on one Linux workstation, the operator completed local Atlassian OAuth, observed `tunnel-client` metadata fetch and `mcp-remote` STDIO proxy establishment, and successfully listed an accessible Bitbucket workspace **through ChatGPT's connected Atlassian MCP Tunnel** (read-only). This establishes one real end-to-end path; it is **not** automated CI evidence or a guarantee for other tenants, identities, scopes, networks, or operating systems. OAuth callback acceptance still depends on Atlassian organization policy.

## Prerequisites

- Linux with Docker Engine + `docker compose`.
- OpenAI Platform Tunnel ID connected to the desired ChatGPT workspace.
- **Runtime** OpenAI API key allowed to use that Tunnel (**not** an admin API key).
- Permission to sign in to Atlassian Rovo MCP v2, including an allowed localhost OAuth callback if your organization restricts domains.
- Nothing already listening on the selected callback port (`38677` by default) or local health port (`18080`).

## Quickstart

```bash
# Clone your own repository, then:
cp .env.example .env
chmod 600 .env
${EDITOR:-vi} .env

# Build both utilities inside the image (host Node.js is not needed):
docker compose build

# One-time OAuth: prints a URL to the terminal; open it on this Linux host.
# Keep this command running while authenticating.
docker compose --profile auth run --rm auth
```

When the `mcp-remote-client` output says `Please authorize this client by visiting:`, copy the **entire URL** into a browser running **on the same Linux host**, then complete the Atlassian login/consent flow. OAuth returns to `http://localhost:38677/oauth/callback` (or your configured port). A prior Atlassian browser session can skip the login UI. Once the CLI reports that it connected and lists tools, the OAuth token is saved in the Docker named volume.

Then start the tunnel:

```bash
docker compose up -d tunnel
docker compose logs -f --no-log-prefix tunnel
```

Check readiness in another terminal:

```bash
curl -i http://127.0.0.1:18080/healthz
curl -i http://127.0.0.1:18080/readyz
curl -sS http://127.0.0.1:18080/health/control-plane
curl -sS http://127.0.0.1:18080/health/mcp
```

**Health interpretation:** `/healthz` only proves that the process is alive, and even `/readyz` may return 200 while `/health/control-plane` reports `degraded`. The Docker healthcheck now requires both a successful `/readyz` and an observed `control-plane.status == "ok"` (polling success); it may remain `starting` until the first long poll completes. The STDIO transport skips initial MCP probing, so `/health/mcp` may report `unknown / not_observed` until ChatGPT actually sends `initialize` and `tools/list`. **Docker healthy does not prove Atlassian authorization or tool access.**

In ChatGPT, create a **custom MCP** with connection type **Tunnel**, select your Tunnel ID, and select **No authentication** only for the ChatGPT-to-local-bridge hop. Atlassian OAuth is handled by `mcp-remote`, **not** by ChatGPT. Limit access to this Tunnel to your own account: anyone authorized to use the Tunnel may invoke Atlassian tools under the OAuth identity cached here.

Try a read-only prompt: "Use Atlassian MCP Tunnel to list accessible Bitbucket workspaces. Do not modify anything." Then check `/health/mcp` again for the observed `initialize` and `tools_list` evidence. Results can differ across Atlassian accounts and workspaces.

## Day-to-day commands

```bash
docker compose ps
docker compose logs --tail=100 tunnel
docker compose stop tunnel
docker compose start tunnel
# Re-run the OAuth diagnostic after stopping tunnel if auth expires:
docker compose --profile auth run --rm auth
# Stop and delete containers, but retain the OAuth named volume:
docker compose down
```

If `mcp-remote` needs a **fresh sign-in**, stop the tunnel and use an intentionally new named Docker volume or delete the old volume deliberately. **`docker compose down -v` permanently deletes cached OAuth credentials** and must not be used casually.

## Security / constraints

- The `.env` file is ignored by Git, but Compose environment variables can be inspected by Docker administrators. Do **not** commit `.env` or paste it into issue reports/logs. For a stronger secret-at-rest model, migrate the runtime key to a file-backed Docker secret and the official `--control-plane.api-key=file:...` flag.
- OAuth refresh tokens and client registration state persist in the `oauth-data` Docker volume, **unencrypted by this project**; restrict host access and protect backups. The authentication and tunnel containers should **not** run concurrently during a new login to avoid callback port conflicts.
- The image pins the **published** `tunnel-client` `v0.0.16` (downloaded with SHA-256 validation) and `mcp-remote` `0.14.3` for repeatability. This is version pinning, not digest- or lockfile-level reproducibility. Review dependencies before updating.
- This is a connectivity integration, **not a read-only enforcement mechanism**. The Atlassian OAuth authorization URL can request broad scopes, including Jira write/delete/manage. A read-only prompt alone is not an authorization boundary. Review consent scopes, restrict upstream permissions and Tunnel access, and use an actual policy-enforcing MCP boundary if writes must be impossible. Never pass long-lived IAM access keys or other unrelated secrets through MCP arguments/results.
- OAuth authorization URLs in logs contain one-time flow details (`state`, PKCE challenge, scopes); **do not share unredacted authentication URLs or tokens** in tickets, issues, or public logs.
- `network_mode: host` exposes the health listener at `127.0.0.1:18080` on the host; it does **not** expose the MCP endpoint publicly. Use only on a trusted single-user Linux machine.

## Troubleshooting

| Symptom | What to check |
| --- | --- |
| No browser pops up | Expected in headless Docker: copy the authorization URL from `auth` output into the host browser. |
| Browser callback fails / `connection refused` | Confirm this is **Linux** with host networking, and `38677` is unused. Check `http://localhost:<port>/oauth/callback` in the redirect. |
| OAuth callback is blocked | Check the organization's Atlassian Rovo MCP domain/callback allowlist; a permitted localhost redirect is required. |
| `tunnel-client` reports missing credentials | Check `.env`, the runtime API key, and the tunnel's OpenAI workspace permission. |
| Docker says `healthy` but Tunnel calls fail | Check `/health/control-plane` for `status`, `state`, `consecutive_failures`, and `last_success`. `/readyz` alone is not conclusive. |
| `/health/mcp` reports `not_observed` | Expected before a real forwarded STDIO `initialize` / `tools/list`; test a read-only tool call through ChatGPT. |
| `/healthz` works but no tools | Inspect `docker compose logs tunnel` and `/health/mcp`; check ChatGPT's Tunnel selection. |
| `poll transport failed (network_error)` with `x509: certificate signed by unknown authority` | Investigate the **container** CA trust store first; compare certificate issuers from the same network route. See [TLS trust troubleshooting](#tls-trust-troubleshooting). |
| Docker build cannot download OpenAI release | Check access to GitHub Release assets and the matching `SHA256SUMS.txt` entry; never bypass checksum verification. |

## TLS trust troubleshooting

One observed failure was an OpenAI control-plane poll in `backoff` while `/readyz` returned 200. The full log provided the actual root cause: `tls: failed to verify certificate: x509: certificate signed by unknown authority`. After local CA trust was corrected, `/health/control-plane` reported `status: "ok"`, `state: "polling"`, `consecutive_failures: 0`, and a `last_success` timestamp.

**First identify which TLS trust boundary fails**; do not assume that a working host `curl` implies the container trusts the same certificate:

```bash
# Host check: unauthenticated 401 means an HTTPS response was received.
curl -sS -o /dev/null -w 'HTTP %{http_code}\n' https://api.openai.com/v1/models

# Container CA presence and basic HTTPS check:
docker compose exec -T tunnel sh -c 'test -s /etc/ssl/certs/ca-certificates.crt && echo "CA bundle present"'
docker compose exec -T tunnel node -e 'fetch("https://api.openai.com/v1/models").then(r=>console.log(r.status)).catch(e=>{console.error(e.cause?.code||e.message);process.exit(1)})'

# Health: do not infer poll success merely from /readyz = 200.
curl -fsS http://127.0.0.1:18080/health/control-plane | python3 -m json.tool
```

The Dockerfile installs the Debian `ca-certificates` package explicitly into the **runtime image**. If your Linux host trusts a required organizational or locally installed CA which the container does not, you may **opt in** to sharing its trusted CA bundle. On Debian/Ubuntu where `/etc/ssl/certs/ca-certificates.crt` exists:

```bash
cp compose.override.example.yaml compose.override.yaml
docker compose config --quiet
docker compose up -d --force-recreate tunnel
```

This mounts the host bundle read-only and sets `SSL_CERT_FILE` for Go's `tunnel-client` and `NODE_EXTRA_CA_CERTS` for Node's `mcp-remote`. The override applies to both `tunnel` and `auth`. Check that your host CA store is trustworthy; **do not disable TLS verification**. This example is unsuitable for hosts whose trust bundle is at a different path; customize the file locally. `compose.override.yaml` is intentionally ignored by Git and Docker build context.

If the issue remains, inspect proxy environment configuration, certificate chain, DNS, and the actual TLS issuer seen **inside** the container before changing trust roots. The exact way CA trust was corrected on the first verified workstation was not recorded; this override is a documented remediation option, not a claim about the specific past action.

## Optional AWS read-only MCP Tunnel

A separate Docker-managed **AWS MCP Tunnel** can be added without changing
the working Atlassian credentials or installing ChatGPT AWS plugins/apps.
It uses AWS CLI console login (`aws login --remote`, **no IAM Identity Center requirement**), a SigV4 proxy, a distinct OpenAI
Tunnel ID and an independent credential cache volume. It also defaults to
`--read-only`, with AWS IAM as the actual authorization boundary.

See **[AWS setup and security walkthrough](README-AWS.md)**.
Do not use the Atlassian `.env` for the AWS service.

## Upstream references

- [OpenAI Secure MCP Tunnel](https://developers.openai.com/api/docs/guides/secure-mcp-tunnels)
- [OpenAI tunnel-client Docker documentation](https://github.com/openai/tunnel-client/blob/master/docs/deployment/docker.md)
- [mcp-remote (OAuth flags and storage)](https://github.com/punkpeye/mcp-remote)
- [mcp-remote Docker OAuth limitation](https://github.com/punkpeye/mcp-remote/issues/60)
