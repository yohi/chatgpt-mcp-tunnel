#!/usr/bin/env python3
"""Read *only* an already-issued STS role session for botocore credential_process.

Called by the MCP child process; never accesses source aws login credentials,
STS AssumeRole or an administrative AWS profile. The broker owns renewal.
"""
import datetime as dt
import json
import os
from pathlib import Path
import stat
import sys

STORE = Path("/run/aws-mcp-credentials")
CREDENTIALS = STORE / "credentials.json"
MIN_VALIDITY_SECONDS = 180
FIELDS = ("AccessKeyId", "SecretAccessKey", "SessionToken", "Expiration")


def read_role_credentials(directory=STORE, now=None):
    now = now or dt.datetime.now(dt.timezone.utc)
    directory = Path(directory)
    directory_stat = directory.lstat()
    if (not stat.S_ISDIR(directory_stat.st_mode)
            or directory_stat.st_uid != os.geteuid()
            or directory_stat.st_mode & 0o077):
        raise ValueError("unsafe credential directory")

    file_path = directory / "credentials.json"
    file_stat = file_path.lstat()
    if (not stat.S_ISREG(file_stat.st_mode)
            or file_stat.st_uid != os.geteuid()
            or file_stat.st_mode & 0o077):
        raise ValueError("unsafe credential file")

    with file_path.open("r", encoding="utf-8") as source:
        item = json.load(source)
    if (not isinstance(item, dict)
            or item.get("Version") != 1
            or any(not isinstance(item.get(k), str) or not item[k] for k in FIELDS)):
        raise ValueError("malformed role credential document")

    expiration = dt.datetime.fromisoformat(item["Expiration"].replace("Z", "+00:00"))
    if (expiration.tzinfo is None or
            (expiration - now).total_seconds() < MIN_VALIDITY_SECONDS):
        raise ValueError("role credentials unavailable or nearing expiration")
    return {key: item[key] for key in ("Version", *FIELDS)}


def main():
    try:
        credentials = read_role_credentials()
    except (OSError, ValueError, TypeError, KeyError, json.JSONDecodeError):
        # Never print the token, paths to auth cache, or a remote error body.
        print("AWS MCP role session unavailable; check credential broker", file=sys.stderr)
        return 1
    if len(sys.argv) == 2 and sys.argv[1] == "--check":
        return 0
    if len(sys.argv) != 1:
        print("Usage: aws-mcp-credential-process.py [--check]", file=sys.stderr)
        return 2
    json.dump(credentials, sys.stdout, separators=(",", ":"))
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
