# AWS MCP Broker v1.1 — isolated Phase I0 structural experiment

**OFFLINE_FOUNDATION_ONLY / NOT_AUTHORIZATION / NOT_INTEGRATED**

Standard-library-only functions:

- decode_json: bounded, strict UTF-8 JSON object decoding, nested duplicate-key rejection, explicit top-level required/optional type validation, unknown-field rejection.
- check_sha256: canonical lowercase SHA-256 match against exact input bytes.
- inspect_clock: validates an explicitly injected timezone-aware clock result.
- boundary_status: rejects structurally invalid input; otherwise always returns NOT_VERIFIED.

ValidationResult is immutable and exposes only predefined nonsecret reason codes.
STRUCTURALLY_VALID means only a local structural check passed; it never means
APPROVED, verified, executable or authorized. Nested field schemas are not
validated beyond JSON syntax, duplicate checks and declared top-level types.
Hash equality does not establish issuer authenticity, trust or approval.
There is deliberately no ALLOW state or AWS-authorizing function.

Current normative state: NORMATIVE_BASELINE_NOT_VERIFIED.
Requirement-dependent functions: BLOCKED_PENDING_NORMATIVE_BASELINE.
The authoritative Requirements, Design, Acceptance Criteria and Security Contract
(including REQ-009, REQ-045 through REQ-049, AC-021 through AC-024, INT-003,
SEC04-POLICY and SEC04-RESOURCE) have not been independently authenticated as
formally adopted. Option A adoption intent is not a ratified decision event.

A network-isolated synthetic test command, from the repository root after
preparing an empty directory designated EMPTY_HOME:

    unshare -Urn env -i PATH=/usr/local/bin:/usr/bin:/bin HOME="$EMPTY_HOME" \
      python -I -B tests/test_aws_mcp_broker_v11_offline.py

Requires working unprivileged user and network namespaces. The new test suite
does not invoke the existing AWS/ST​S isolation tests (which import botocore).
No AWS SDK, CLI, credential_process, IAM, STS, login cache, Secret Adapter,
Bitwarden, Docker, live networking or existing Broker integration is involved.
This test pass does not establish operational security, AWS authorization,
credential isolation, approval validity or any Gate closure.
