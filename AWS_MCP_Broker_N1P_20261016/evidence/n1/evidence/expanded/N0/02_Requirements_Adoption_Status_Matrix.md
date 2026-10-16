# 02 — Requirements Adoption Status Matrix

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


## 1. Rules

`ARCHIVED_BASELINE_TEXT` = immutable submitted B1/B2/B3 text exists, **not proof of official adoption**. `ADOPTION_INTENT_ONLY` = Option A willingness exists, but no authenticated ratification. `R4_PROPOSAL_ONLY` = proposed and unadopted. `OPEN_BLOCKER` = a known technical/normative conflict. Keep **source-text version**, **adoption authority**, **implementation evidence** separate.

## 2. Clauses explicitly requested

| Clause | Recovered text / source | Adoption classification | Open issue / acceptance boundary |
|---|---|---|---|
| **REQ-009** | B1: protect all credentials inside Broker's protected execution boundary. Option A R1 changes to type-specific Broker/Executor vs independent Secret Adapter boundaries; proposed clause SHA `f17db0565942501a39c3302912dcb161e2f3e38e168f29a51491a711e0851bb9` | `ARCHIVED_BASELINE_TEXT` + `ADOPTION_INTENT_ONLY` for proposed replacement | Revision changes a normative trust boundary; formal full-text Owner adoption and independent review needed; no live proof |
| **REQ-045** | B2: prohibit existing AWS IAM long-term key acquire/decrypt/copy/cache/transfer/use by Broker/components, including fallback/recovery/backup | `ARCHIVED_BASELINE_TEXT / ORIGINAL_ADOPTION_NOT_AUTHENTICATED` | Unconditional prohibition, even if two admins approved poisoning; pre-fetch enforcement not proven |
| **REQ-046** | B2: Broker-dedicated Bitwarden Machine Account/Project, least privilege; Option A R1 changes to installation-dedicated **independent Secret Adapter** account/project with six controls and disabled-by-default, proposed SHA `6362d06bfe5d1c1184057f84c42f2f6ed4c19d6dc47b8662cfe039105e21d931` | `ARCHIVED_BASELINE_TEXT` + `ADOPTION_INTENT_ONLY` for entire replacement | Full-text amendment and explicit separation necessary; original/renumbered text must not be silently combined |
| **REQ-047** | B2: approved AWS credential methods only; no IAM long-term-key fallback including ambient SDK chain | `ARCHIVED_BASELINE_TEXT / ORIGINAL_ADOPTION_NOT_AUTHENTICATED` | Three-environment failure-path enforcement not demonstrated |
| **REQ-048** | B2: phishing-resistant interactive re-auth, absolute/idle deadlines, revocation; B2-S1 later decision: **8h absolute, 15m idle**, renew idle only by authenticated human | `ARCHIVED_BASELINE_TEXT`; B2-S1 human decision summarized | Authn runtime and authoritative confirmation of B2-S1 decision still missing |
| **REQ-049** | B2: minimize high-value credentials and prevent unnecessary leaks to agent/MCP/HTTP/logs/exceptions/traces | `ARCHIVED_BASELINE_TEXT / ORIGINAL_ADOPTION_NOT_AUTHENTICATED` | End-to-end runtime boundary and leak-negative tests not demonstrated |
| **AC-021** | B2: real AWS auth without existing IAM keys in Deno, Cloudflare and Docker, record methods without secrets | `ARCHIVED_BASELINE_TEXT / ORIGINAL_ADOPTION_NOT_AUTHENTICATED` | No approved live tests of all three environments; no result can be inferred from PR #14/#15 |
| **AC-022** | B2: Broker-dedicated Machine Account test-secret acquisition & protected-project denial; Option A changes positive acquisition actor to independent Adapter with Broker denial and **pre-fetch** content provenance control. Proposed SHA `3a02643899b8d79683f6c13300e0ee655b4b00fe20d23f87a3c35efb4e521a39` | `ARCHIVED_BASELINE_TEXT` + `ADOPTION_INTENT_ONLY` for replacement | If pre-fetch authenticity/non-poisoning cannot be proven, positive fetch MUST remain BLOCKED; mock IAM keys only; no new test authorization |
| **AC-023** | B2: inject OIDC, STS, expiry, Bitwarden and ambient credential failures; confirm no long-term-key fallback | `ARCHIVED_BASELINE_TEXT / ORIGINAL_ADOPTION_NOT_AUTHENTICATED` | Runtime fault injection not performed |
| **AC-024** | B2: absolute/idle expiry, explicit revoke, reauth policy reevaluation, no interactive-session borrowing by unattended agent | `ARCHIVED_BASELINE_TEXT / ORIGINAL_ADOPTION_NOT_AUTHENTICATED` | Actual identity provider integration unproven |
| **INT-003** | R4 reconciliation: independent 2-human high-risk change control covering **all effective** Bitwarden Owner/Admin, cloud privileged, CI/CD, Secret Store, issuer, backup/restore paths; authorized single-person emergency **reductions** are distinct | `OPEN_BLOCKER / R4_PROPOSAL_ONLY` for detailed integration design | `CRITICAL OPEN / BLOCKING`; no proof of complete management-path enforcement, no waiver by textual R1 correction |

## 3. Other relevant normative provisions

| Set | Recovered scope | State |
|---|---|---|
| REQ-001–044 / AC-001–020 | Fixed B1 submitted v1.0 text, including individual human approval per AWS write, per-principal auth, multi-account/3 environments, rate/cost, audit | Original official authority unverified; not retroactively invalidated by R4 |
| B3 Q33–Q40 | Independent Adapter, no existing IAM keys, external read/status only initially, operation-proof, default-disabled, independent store, two-person high-risk changes | `USER-CONFIRMED DECISION REGISTER` as submitted summary; original individual authenticated events not established |
| REQ-050–059 | R4 security normative candidates | `R4_PROPOSAL_ONLY / NOT_ADOPTED` |
| AC-025–036 | R4 acceptance candidates | `R4_PROPOSAL_ONLY / NOT_EXECUTED` |
| REQ-025 + INT-001 | B1 Bitwarden Secrets Manager wording vs B3 optional/default-disabled architecture | Contract alignment unresolved; do not silently waive original wording |
| REQ-042 + INT-002 | Guarantee parity across Deno/Cloudflare/Docker vs unverified environments | No equivalence proven; unverified environment must not be counted compliant |
| INT-004–006 | Change-by-change two-person control, operation contract binding/revocation, AWS-vs-external write boundary | R4 candidate and feasibility unverified |

## 4. Competing clause versions (do not merge informally)

| Clause | Old submitted B1/B2 paragraph SHA-256 (as reported in Option A R1 review) | New **proposed**, independently byte-checked R1 SHA-256 |
|---|---|---|
| REQ-009 | `d75233273042089564339a9b5f7f39ccb36e62367b4212b64849fed3abc49b18` | `f17db0565942501a39c3302912dcb161e2f3e38e168f29a51491a711e0851bb9` |
| REQ-046 | `410aacaeb42a90880e988fd86f84dd9fa09c780f575b6c78d14a8497d7658a94` | `6362d06bfe5d1c1184057f84c42f2f6ed4c19d6dc47b8662cfe039105e21d931` |
| AC-022 | `58c7b2b6b562c7bc06b224c0daa2413764360c0e50954e3bc22a6c86b69a9aba` | `3a02643899b8d79683f6c13300e0ee655b4b00fe20d23f87a3c35efb4e521a39` |

**Important:** R1 filenames start `adopted-text-*`, but these filenames are **not** adoption events. The actual state remains `OWNER_ATTESTATION_PENDING / NOT_EFFECTIVE`.

## 5. Normative adoption test (currently FAIL / UNKNOWN)

For each clause: authoritative original URI + SHA-256 + revision + adoption authority evidence + authenticated event ID/time + independent post-adoption review + clear supersession of earlier text. None of these can be inferred from a candidate ZIP, ChatGPT declaration, repository push rights, or a successful unit test.
