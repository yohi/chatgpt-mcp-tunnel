# 03 — Design / Implementation Gap Analysis

**Phase:** N0 — Normative Baseline Recovery & Adoption Readiness  
**Review date:** 2026-10-16 JST  
**Reviewer role:** independent read-only Requirements / Design Authority Investigator (not Owner/Approver)  
**Repository:** `yohi/chatgpt-mcp-tunnel`  
**Fixed HEAD:** `ac462699e0b1988eda63ea3d6dacfc2a030bb822` (branch `feat/aws-broad-iam-read-api-tools`)  
**Boundary:** Read-only GitHub and previous document/ZIP inputs; no AWS API/STS/IAM/credentials/Docker/Broker access, no GitHub writes.  
**Evidence qualification:** ZIP SHA and member content checks are independently recomputed; authority provenance and authenticated ratification are not.

```
NORMATIVE_BASELINE: NOT_VERIFIED
BROKER_RUNTIME_INTEGRATION: NOT_AUTHORIZED
G0_EXECUTION_APPROVAL: NOT_AUTHORIZED
AWS_API_BUDGET: 0
Gate STS-001: NOT VERIFIED
```


## 1. Compared layers

A. **Requirement copies**: submitted B1/B2/B3 archival snapshots; actual approved Design source missing.  
B. **Design candidates**: R4 `04/05/06/07`, unsigned STS-001 security contract, Investigation B G0 proposal; no authority to execute.  
C. **Existing legacy AWS tunnel** at `ac462699e0b1988eda63ea3d6dacfc2a030bb822`: [README-AWS.md](https://github.com/yohi/chatgpt-mcp-tunnel/blob/ac462699e0b1988eda63ea3d6dacfc2a030bb822/README-AWS.md), [scripts/aws-mcp-credential-broker.py](https://github.com/yohi/chatgpt-mcp-tunnel/blob/ac462699e0b1988eda63ea3d6dacfc2a030bb822/scripts/aws-mcp-credential-broker.py), [scripts/aws-mcp-bootstrap-role.py](https://github.com/yohi/chatgpt-mcp-tunnel/blob/ac462699e0b1988eda63ea3d6dacfc2a030bb822/scripts/aws-mcp-bootstrap-role.py), [compose.aws.api-tools.example.yaml](https://github.com/yohi/chatgpt-mcp-tunnel/blob/ac462699e0b1988eda63ea3d6dacfc2a030bb822/compose.aws.api-tools.example.yaml) and [tests/test_aws_sts_isolation.py](https://github.com/yohi/chatgpt-mcp-tunnel/blob/ac462699e0b1988eda63ea3d6dacfc2a030bb822/tests/test_aws_sts_isolation.py).  
D. **v1.1 isolated experiment**: [experiments/aws_mcp_broker_v11_offline/validation.py](https://github.com/yohi/chatgpt-mcp-tunnel/blob/ac462699e0b1988eda63ea3d6dacfc2a030bb822/experiments/aws_mcp_broker_v11_offline/validation.py) and [tests/test_aws_mcp_broker_v11_offline.py](https://github.com/yohi/chatgpt-mcp-tunnel/blob/ac462699e0b1988eda63ea3d6dacfc2a030bb822/tests/test_aws_mcp_broker_v11_offline.py).

**Not an adoption verdict:** Comparing a codebase with candidate documents reveals possible gaps, not conformity to a finalized approved spec.

## 2. Per-capability gap and evidence need

| ID | Requirement / candidate design | Fixed-code observation | Gap, risk and closure evidence | Current scope |
|---|---|---|---|---|
| G-01 | Complete official B1/B2/B3 + approved Design/AC/Security Contract | No approved canonical full v1.1 set in fixed Git tree; R4 and draft records held separately | Obtain authenticated owner adoption and exact revision/SHA; no integration before this | `BLOCKED_NORMATIVE` |
| G-02 | Req subject/operation/target/parameters, expiry, one-time, revocation/replay and independent grant issuer | Offline `boundary_status` always returns `NOT_VERIFIED`; no v1.1 auth gateway | Authorization contracts, offline deterministic negative tests only after separate implementation scope approval | `NOT_IMPLEMENTED` |
| G-03 | Multi-account, explicit registration, per-user/agent scoped access, task account selection | Legacy issuer uses one source profile and role record | Identity-to-account/role map, task-scoped grants, independent selector security | `NOT_IMPLEMENTED` |
| G-04 | One human authorization per **AWS write**; independent Web UI; 15m/5m, no auto retry | Legacy AWS tunnel exposes generic AWS tool; no v1.1 approval UI/grant pipeline in inspected tree | Write operation contract, signed approval artifact, expiry, revoke, idempotency/outcome_unknown tests | `NOT_IMPLEMENTED` / writes prohibited |
| G-05 | STS-001 `PolicyArns` plus **mandatory** canonical inline explicit Deny `Policy` | Legacy issuer calls `assume_role` with managed ReadOnlyAccess session policy, **without inline `Policy`** | F-001 critical; design/Owner safe action set, no fallback, deterministic argument tests | `SEC04-POLICY: NOT_VERIFIED` |
| G-06 | STS role immutable account/role/RoleId/trust binding, unique session name, matched STS session identity | Legacy issuer checks ARN/source data; uses constant `RoleSessionName` and validates ARN string, not pinned issued RoleId/UserId | F-007/011; audited RoleId/trust snapshot and independent identity checks | `SEC04-RESOURCE: NOT_VERIFIED` |
| G-07 | AWS-wide reviewed safe catalog, SAR pinned input, IAM API-dependency closure, response secrecy | Policy R2 candidates are 21/22 narrow actions, `lambda:GetFunctionConfiguration` flagged sensitive; not an approved AWS-wide set | F-002/003; obtain original SAR bytes, approved API/parameter/output catalog, explicit deny negative suite | `NOT_PROVEN` |
| G-08 | Managed ReadOnlyAccess policy version drift, session packed size, IAM resource-policy exception paths | Candidate local policy-size exercise; no live version/drift, packed size, resource grants validation | F-004/005/006/010; independent authorized later-stage controls, not N0 | `NOT_VERIFIED` |
| G-09 | Credential separation and no existing IAM long-term keys/ambient fallback | Legacy Docker broker accesses source `aws login` cache; MCP role-only volume in sample Compose; no v1.1 platform-wide proof | REQ-009/045/047/049, runtime mount/provider/log tests, source/Broker compromise trust-limit declaration | `NOT_PROVEN` |
| G-10 | Independent Bitwarden Secret Adapter, dedicated Machine Account/Project, pre-fetch content origin safety | No validated v1.1 Adapter/independent store/operation API in fixed tree | REQ-046/AC-022/INT-003; value-only replacement/approved poisoning and privileged bypass cases; feature stays off | `BLOCKED` |
| G-11 | Deno Deploy / Cloudflare Workers / Docker equivalent auth and control safety | Fixed repo primarily Docker+legacy tunnel. No environment-parity proof | REQ-041/042, AC-021 and REQ-047/049 test matrix per platform | `NOT_IMPLEMENTED/UNVERIFIED` |
| G-12 | Phishing-resistant 8h absolute/15m idle reauth; service principal separation | No v1.1 interactive IdP/session enforcement evidenced | REQ-048 + B2-S1, AC-024; authenticated-person-only idle extension, revoke/re-auth tests | `NOT_IMPLEMENTED` |
| G-13 | Audit, backup, encryption, policy cost limits, fail closed, no write outcome replay | Offline test covers parse/byte bounds/digest/clock diagnostics, not durable records or actual runtime | Approved retention, cost cap, audit integrity, back-up and failure matrix | `NOT_IMPLEMENTED` |
| G-14 | Existing shared privileged ECS role must not be modified or used without Owner evaluation | Legacy `aws-mcp-bootstrap-role.py` can create/delete temporary IAM role with explicit flags; draft forbids any mutations to reused role | Code path must be excluded/hardened by later authorized redesign; ECS non-interference evidence required | `NOT_AUTHORIZED` |
| G-15 | G0 Investigation B evidence retention and separate execution approvals | Git contains final candidate signed-off? **No**: file explicitly `DRAFT_UNSIGNED_NOT_AUTHORIZED` | Human role authority/source root/OD decisions/stage budgets remain PENDING | `G0_NOT_AUTHORIZED` |

## 3. Confirmed implementation observations vs test assertions

- **Actual fixed source observation:** `scripts/aws-mcp-credential-broker.py` passes `PolicyArns=[{"arn": SESSION_POLICY_ARN}]` without an inline `Policy`; `RoleSessionName` is the static `chatgpt-mcp-readonly`. The separate test `tests/test_aws_sts_isolation.py` asserts that legacy call contract; it does not prove the stricter draft STS-001 contract.
- **Actual fixed source observation:** `validation.py` is explicitly I/O-free and always returns `NOT_VERIFIED` at its authorization boundary. It implements strict JSON UTF-8/bytes, nested duplicate keys, exact SHA256 and clock shape checks; this is reusable **only as a structural experiment**.
- **GitHub PR observation:** PR #14/#15 are merged; PR #15 touched only 2 isolated experiment files. Reported I1-TEST-001 / I1-API-002 closure is limited to those test findings (we did not independently rerun a live integration suite in N0).
- **Architecture gap:** The existing `README-AWS.md` and Docker Compose instructions are **legacy operational descriptions**, not evidence of a v1.1-approved security architecture.
- **Existing-role threat model:** draft assumes a potentially administrator-level shared ECS role; a compromised trusted source/Broker may evade assumed-role-only guards by requesting other STS sessions. This is a deployment architecture issue and cannot be closed through an isolated validator.

## 4. SEC04-POLICY / SEC04-RESOURCE and STS-001 dependency

```text
Authenticated normative Requirements/Design/AC/Security Contract
     → independent normative review
     → owner-approved tool/action/output safe set and API/IAM semantics
     → SEC04-POLICY offline design and policy digest contract
     → role identity / resource-policy / ECS non-interference for SEC04-RESOURCE
     → stage-specific human authorization (including G0; currently NOT_AUTHORIZED)
     → independently checked AWS live evidence (none collected in N0)
     → Gate STS-001 technical verdict (NOT VERIFIED)
     → Broker/runtime integration authorization (NOT_AUTHORIZED)
```

No arrow may be collapsed by PR merges, document hashes, proposed JSON policy syntax, or offline synthetic tests. In archived policy R2, F-001 and F-004..F-012 remain OPEN and F-002/F-003 OPEN_PARTIAL; later claims of SAR raw-byte acquisition are not equivalent to an independently completed authorization and do not close the findings without examined original bytes.

## 5. I2 implementability decision boundary

- **Possible with separate offline-only authorization:** provenance manifest parser, immutable candidate-revision inventory, SHA256/ZIP/MANIFEST checkers, no-secret schema validators, static contract test fixtures, deterministic unauthorized/fail-closed behavior; isolated experiment only, never a prod integration.
- **Not permissible under current N0:** changing Broker issuer, policy issuance parameters, IAM role reuse, BWS Adapter actual access, authenticated user/session services, Docker runtime, MCP surface, real AWS/Bitwarden calls, deployment or master branch merges.
- **Requires Owner normative decision first:** even isolated runtime-like authorization architecture that selects real permission grants, scope/writes or adopts a candidate policy semantics. A current test may validate structural error handling; it cannot pronounce `ALLOW`.
