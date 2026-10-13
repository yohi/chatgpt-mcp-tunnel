# Download a *published* OpenAI release and verify its SHA-256 checksum.
# The v1.x tags in upstream Docker docs are examples, not published as of 2026-10-13.
FROM debian:bookworm-slim AS tunnel-downloader

ARG TARGETARCH
ARG TUNNEL_VERSION=v0.0.16

RUN set -eu; \
    apt-get update; \
    apt-get install -y --no-install-recommends ca-certificates curl unzip; \
    case "$TARGETARCH" in amd64|arm64) ;; *) echo "Unsupported arch: $TARGETARCH" >&2; exit 1 ;; esac; \
    archive="tunnel-client-${TUNNEL_VERSION}-linux-${TARGETARCH}.zip"; \
    base="https://github.com/openai/tunnel-client/releases/download/${TUNNEL_VERSION}"; \
    cd /tmp; \
    curl -fL --retry 3 -o "$archive" "$base/$archive"; \
    curl -fL --retry 3 -o SHA256SUMS.txt "$base/SHA256SUMS.txt"; \
    grep -F "  $archive" SHA256SUMS.txt > archive.sha256; \
    test -s archive.sha256; \
    sha256sum --check archive.sha256; \
    mkdir extracted; \
    unzip -q "$archive" -d extracted; \
    binary="$(find extracted -type f -name tunnel-client -print -quit)"; \
    test -n "$binary"; \
    install -m 0755 "$binary" /usr/local/bin/tunnel-client

FROM node:22-bookworm-slim

# Pin the OAuth bridge; host Node.js/npm installation is unnecessary.
RUN npm install --global --omit=dev mcp-remote@0.14.3 \
    && npm cache clean --force

COPY --from=tunnel-downloader /usr/local/bin/tunnel-client /usr/local/bin/tunnel-client

RUN install -d -m 0700 -o node -g node /home/node/.mcp-auth

USER node
ENV MCP_REMOTE_CONFIG_DIR=/home/node/.mcp-auth

ENTRYPOINT ["tunnel-client"]
CMD ["run"]
