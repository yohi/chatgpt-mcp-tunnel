#!/usr/bin/env python3
"""Check actual OpenAI polling success, not just local process liveness.

This does *not* validate SSO freshness, IAM permissions, MCP tool listing,
or the AWS account currently selected. Those require functional testing.
"""
import json
import sys
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

BASE = "http://127.0.0.1:18081"


def main() -> int:
    try:
        with urlopen(BASE + "/readyz", timeout=4) as resp:
            if resp.status != 200:
                return 1
        with urlopen(BASE + "/health/control-plane", timeout=4) as resp:
            if resp.status != 200:
                return 1
            data = json.load(resp)
        if data.get("component") != "control-plane":
            return 1
        return 0 if data.get("status") == "ok" else 1
    except (OSError, ValueError, HTTPError, URLError):
        return 1


if __name__ == "__main__":
    sys.exit(main())
