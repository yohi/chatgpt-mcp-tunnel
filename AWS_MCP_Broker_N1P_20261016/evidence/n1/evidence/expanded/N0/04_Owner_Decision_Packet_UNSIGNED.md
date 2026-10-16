# 04 — Owner Decision Packet — UNSIGNED

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


**Packet state:** `DRAFT_UNSIGNED / NO_DECISION_RECORDED / NO_AUTHORIZATION`. This document is not a decision and grants no AWS/API, GitHub, or integration privilege. Explicitly preserve the signatures and events blank until real Owner action.

## 1. Minimal decision queue (do not pre-answer for the Owner)

| ID | Decision required | Available choices for authorized human | Blocking record/evidence |
|---|---|---|---|
| **N0-OD-01 — Authority chain** | Designate authoritative custodian, Requirements Owner and optional distinct Security/Design approvers for B1/B2/B3, full Design, AC, Security Contract | A: identify and prove existing governance; B: newly establish prospective governance **without retroactive approval**; C: hold | Owner identity/role authority evidence; official immutable source URIs, revision, SHA; historical adoption events |
| **N0-OD-02 — Normative clause adoption** | Set official B1/B2/B3 status and decide Option A for **full texts** REQ-009, REQ-046, AC-022 | A: ratify exactly the 3 individually digested R1 candidate texts prospectively; B: retain originals/mark clash blocked; C: request a separately reviewed alternate | Formal decision ID; authenticated Owner actor; UTC event time; 3 SHA-256 values; superseded text; independent subsequent review. No pre-selection by AI |
| **N0-OD-03 — Remaining security/acceptance set** | Decide treatment of R4 REQ-050–059 / AC-025–036, INT-003 and complete v1.1 Design/Security Contract | A: leave unadopted and prohibit affected features; B: review/ratify a coherent bounded set; C: commission new design independently without presumed adoption | Full normative consistency review, independent management-path feasibility, explicit exclusions; INT-003 remains CRITICAL OPEN absent proof |
| **N0-OD-04 — I2 work envelope** | If normative closure is not yet complete, choose whether future work is restricted to synthetic **offline, unintegrated** checks | A: allow only named offline structural work under new separate limited authorization; B: hold all I2; C: revisit after normative PASS | Explicit task/paths allowed, accountable human decision, forbidden imports/calls, independent review plan; **neither choice grants G0 or runtime integration** |

**Separate later decisions, NOT combined with OD-01..04:** existing privileged ECS-role reuse risk/SEC04 threat model and Role Owner assent; STS-001 safe action/inline policy, source managed drift, resource-policy analysis; every AWS access stage/G0; full production integration and release. These must remain distinct gates.

## 2. Candidate text digests requiring real Owner action

| Clause | Candidate full-text SHA-256 | Submission source |
|---|---|---|
| REQ-009 | `f17db0565942501a39c3302912dcb161e2f3e38e168f29a51491a711e0851bb9` | Option A R1 ZIP `adopted-text-REQ-009.txt` |
| REQ-046 | `6362d06bfe5d1c1184057f84c42f2f6ed4c19d6dc47b8662cfe039105e21d931` | Option A R1 ZIP `adopted-text-REQ-046.txt` |
| AC-022 | `3a02643899b8d79683f6c13300e0ee655b4b00fe20d23f87a3c35efb4e521a39` | Option A R1 ZIP `adopted-text-AC-022.txt` |

R1 limited correction status: `ODR-IR-001 CLOSED (STATIC TEXT ONLY)` as reported. Owner ratification `ODR-IR-002 PENDING`; external authority provenance `ODR-IR-003 NOT_VERIFIED`; independent post-ratification Normative PASS `NOT_GRANTED`.

## 3. Empty attestable decision/event record

```yaml
record_type: AWS_MCP_BROKER_V11_N0_OWNER_DECISION
record_status: DRAFT_UNSIGNED_NOT_EFFECTIVE
official_decision_id: null
owner_authenticated_identity: null
owner_authority_reference: null
custodian_authority_reference: null
formal_originals:
  B1: {uri: null, revision: null, sha256: null, adoption_event: null}
  B2: {uri: null, revision: null, sha256: null, adoption_event: null}
  B3: {uri: null, revision: null, sha256: null, adoption_event: null}
  Design: {uri: null, revision: null, sha256: null, adoption_event: null}
  Acceptance: {uri: null, revision: null, sha256: null, adoption_event: null}
  SecurityContract: {uri: null, revision: null, sha256: null, adoption_event: null}
option_a_req009_selected: null
option_a_req046_selected: null
option_a_ac022_selected: null
r4_other_clauses_decision: null
i2_offline_scope_decision: null
real_approval_utc_timestamp: null
real_signed_commit_or_audit_event_url: null
independent_post_adoption_normative_review: null
normative_baseline_verified: false
g0_execution_approved: false
broker_runtime_integration_approved: false
aws_api_budget: 0
sts001_gate_verified: false
```

Do **not** fill nulls with inferred dates, GitHub username, ChatGPT statements, or this investigator's name. Approval must be recorded later in an authenticated authority-controlled system, and must be verified against its independent role assignment.

## 4. Stop/invalidation rules

- A digest mismatch, unresolved former clause, undefined Revision, or undocumented adopter keeps `NORMATIVE_BASELINE: NOT_VERIFIED`.
- Two human signatures on an insecure Bitwarden value are not proof of pre-fetch forbidden-secret exclusion. REQ-045 is not waived.
- `G0_EXECUTION_APPROVAL` requires separate, attributable, stage-scoped authorization and local evidence/custodian/retention prerequisites; no default approval.
- A decision to pursue implementation is not an implementation execution authorization, and a draft cannot activate Bitwarden, Docker or AWS.
- Re-review if canonical byte streams or approved scope change.

## 5. Handoff

**Next decision owner:** authenticated Requirements Owner/authority custodian (human).  
**Next technical reviewer:** separate fresh independent Normative Reviewer **only after** complete source/decision events are fixed.  
**Next engineering agent:** future offline-only I2 implementer **only if** human issues a separate limited authorization; otherwise HOLD.
