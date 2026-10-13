# ChatGPT MCP Tunnel — Atlassian MCP v2 (Docker)

A **Linux-only, minimal Docker Compose experiment** for:

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

This is a proposed integration, **not a claim of end-to-end testing against Atlassian**. OAuth callback acceptance also depends on Atlassian organization policy.

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
curl -sS http://127.0.0.1:18080/health/mcp
```

The readiness endpoint can report healthy before the stdio child has completed MCP `initialize` / `tools/list`. Use `/health/mcp` and an actual ChatGPT tool-list test for functional verification.

In ChatGPT, create a **custom MCP** with connection type **Tunnel**, select your Tunnel ID, and select **No authentication** only for the ChatGPT-to-local-bridge hop. Atlassian OAuth is handled by `mcp-remote`, **not** by ChatGPT. Limit access to this Tunnel to your own account: anyone authorized to use the Tunnel may invoke Atlassian tools under the OAuth identity cached here.

Try a read-only prompt: "Use Atlassian MCP Tunnel to list accessible Jira projects. Do not modify anything."

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
- The image pins `tunnel-client` `v1.2.3` and `mcp-remote` `0.14.3` for repeatability. This is version pinning, not digest- or lockfile-level reproducibility. Review dependencies before updating.
- This is a connectivity experiment. It does **not** impose read-only permissions or tool-level authorization. Atlassian tools may mutate data. Never pass long-lived IAM access keys or other unrelated secrets through MCP arguments/results.
- `network_mode: host` exposes the health listener at `127.0.0.1:18080` on the host; it does **not** expose the MCP endpoint publicly. Use only on a trusted single-user Linux machine.

## Troubleshooting

| Symptom | What to check |
| --- | --- |
| No browser pops up | Expected in headless Docker: copy the authorization URL from `auth` output into the host browser. |
| Browser callback fails / `connection refused` | Confirm this is **Linux** with host networking, and `38677` is unused. Check `http://localhost:<port>/oauth/callback` in the redirect. |
| OAuth callback is blocked | Check the organization's Atlassian Rovo MCP domain/callback allowlist; a permitted localhost redirect is required. |
| `tunnel-client` reports missing credentials | Check `.env`, the runtime API key, and the tunnel's OpenAI workspace permission. |
| `/healthz` works but no tools | Inspect `docker compose logs tunnel` and `/health/mcp`; check ChatGPT's Tunnel selection. |
| Docker build fails copying `cloudflared` | The pinned official upstream image layout may have changed; verify upstream Dockerfile and pin a working image digest. |

## Upstream references

- [OpenAI Secure MCP Tunnel](https://developers.openai.com/api/docs/guides/secure-mcp-tunnels)
- [OpenAI tunnel-client Docker documentation](https://github.com/openai/tunnel-client/blob/master/docs/deployment/docker.md)
- [mcp-remote (OAuth flags and storage)](https://github.com/punkpeye/mcp-remote)
- [mcp-remote Docker OAuth limitation](https://github.com/punkpeye/mcp-remote/issues/60)
