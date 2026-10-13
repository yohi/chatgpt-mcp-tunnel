# Use the official, version-pinned OpenAI client binary rather than rebuilding it.
FROM ghcr.io/openai/tunnel-client:v1.2.3 AS upstream-tunnel

FROM node:22-bookworm-slim

# Pin the OAuth bridge version; dependencies are installed inside the image only.
RUN npm install --global --omit=dev mcp-remote@0.14.3 \
    && npm cache clean --force

COPY --from=upstream-tunnel /usr/bin/tunnel-client /usr/local/bin/tunnel-client
COPY --from=upstream-tunnel /usr/bin/cloudflared /usr/local/bin/cloudflared

RUN install -d -m 0700 -o node -g node /home/node/.mcp-auth

USER node
ENV MCP_REMOTE_CONFIG_DIR=/home/node/.mcp-auth

ENTRYPOINT ["tunnel-client"]
CMD ["run"]
