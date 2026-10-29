#!/bin/sh
set -eu

case "${FILESYSTEM_HOST_PATH:-}" in
  /*) ;;
  *)
    printf '%s\n' 'FILESYSTEM_HOST_PATH must be an absolute path' >&2
    exit 1
    ;;
esac

exec /usr/local/bin/tunnel-client "$@"
