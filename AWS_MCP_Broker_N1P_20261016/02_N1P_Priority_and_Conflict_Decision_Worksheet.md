# N1-P Priority and Conflict Decision Worksheet

Status: **UNSIGNED / PROPOSED / NOT_EFFECTIVE**

All human decision cells are **PENDING**. Recommendations are investigator
advice, not adopted text. Source aliases and exact file digests are in document
01. No generic “latest version wins” or “B3 overrides everything” rule is proposed.

## 1. D-025 — REQ-025 / INT-001

Source conflict: B1 lines 179–183 require Secrets Manager as secret storage and
runtime protected Secrets for its bootstrap credentials. B3 Q34/Q38 limit it to
external-service secrets, make it initially disabled and keep AWS/STS/role and
internal authentication/encryption independent. R4 `04` §5 INT-001 and `06`
lines 26–28 call the *capability* mandatory but deployment initially disabled.
That restatement is a proposal, not an already adopted amendment to B1.

| Human choice offered | Consequence | Recommendation / human decision |
| --- | --- | --- |
| Commission explicit REQ-025 revision retaining external integration capability, initially disabled, AWS-independent, Adapter-only bootstrap custody | Replace both B1 paragraphs in a distinct reviewed revision; define when capability must exist and when activation is forbidden; align 026/027 settings scope | RECOMMENDED: REVISE; PENDING |
| Prospectively adopt exact B3 summary plus a precise REQ-025-specific override map | Must identify both displaced B1 sentences and exact new governing text; cannot just invoke Q34/Q38 without resolving bootstrap custody and mandatory capability | Possible only after full explicit text/map review; PENDING |
| Preserve REQ-025 without integration amendment and defer conflicting integration | Complete combined baseline remains unresolved; keep Adapter/Token/fetch disabled; no full-v1.1 claim | Honest partial disposition; PENDING |

Dependency reconciliation, including unchanged provisions:

| Dependencies | What must remain / what must be specified |
| --- | --- |
| REQ-007/008/045/047; AC-001/005/021/023 | Keyless unattended AWS must not depend on BWS availability or fall back to long-term keys; AC-023's BWS outage case tests independence, not use of BWS for AWS authentication |
| REQ-009/046/049; AC-012/022 | Fixed Option A credential-specific boundaries; runtime protected Secrets means Adapter-only Store for Token, not Broker-visible bootstrap credentials |
| REQ-023/024 | No arbitrary secret retrieval, unsafe composite AWS call or exemption from 045; AWS data-access exceptions cannot waive IAM-key prohibition |
| REQ-026/027/028/038/043 | Broker internal settings/UI remain, but cannot become authority to place Token or change Adapter policy/Store; separate installation and multi-instance state; Git not required for operational configuration |
| REQ-029/030/032–040; AC-011/013–017 | Independent external quotas/audit/cancellation/recovery must supplement rather than replace original AWS duties |
| REQ-041/042; AC-018 | Disabled mode is not full feature parity |
| R4 050/051/054/055/056/058; AC-025/026/028/030/032/033/036 | Candidate closure for external capability; all remain UNADOPTED; approved poisoning and all ingress paths must be denied pre-fetch |

Deliverable required from Requirements drafter: exact replacement text, old/new
full-body digests, both-paragraph diff, above dependency dispositions, scope and
effective event reference. None has been silently substituted here.

## 2. D-042 — REQ-042 / INT-002

B1 041 requires three platform families including both Docker host systems;
042 permits internal differences but not reduced features or safety. B3 Q38/39
and R4 059 prohibit enabling unverified environments. Feature-off is a safety
response, not equivalence. INT-002's AWS-only profile is expressly non-complete.

| Candidate decision | Requirements effect | Human decision |
| --- | --- | --- |
| Retain 042 unchanged; record eight environment/mode cells and withhold complete compliance until all applicable cells proven | RECOMMENDED; no reduction in original feature/safety floor | PENDING |
| Commission explicitly narrower release/applicability revision | New revision must name excluded features/platforms, negative guarantees, dependency changes, AC scope and labeling; may not be called unchanged full v1.1 | PENDING |
| Treat AWS-only/Adapter-disabled as full equivalence | Not supportable against current text; do not adopt this interpretation | PENDING; not pre-filled REJECTED |

Impacted originals: REQ-007/008/041/042/043/044/045/047/048/049;
AC-001/004/005/012/016/017/018/020/021/022/023/024. Impacted candidates:
REQ-050/051/055/056/059 and AC-025–036, especially 030/031/032/036.
REQ-044 does not permit requiring Lambda to patch a platform gap. Docker/Linux
evidence cannot stand in for Docker/macOS host/VM/Desktop privilege evidence.

| Environment configuration | AWS-only, Adapter disabled | Adapter-enabled external capability | Full equivalence |
| --- | --- | --- | --- |
| Deno Deploy | NOT_PROVEN | BLOCKED / NOT_PROVEN | NOT_PROVEN |
| Cloudflare Workers | NOT_PROVEN | BLOCKED / NOT_PROVEN | NOT_PROVEN |
| Docker on Linux | NOT_PROVEN | BLOCKED / NOT_PROVEN | NOT_PROVEN |
| Docker on macOS | NOT_PROVEN | BLOCKED / NOT_PROVEN | NOT_PROVEN |

These are evidence states, not observations of deployed settings. An N/A needs
adopted normative inapplicability, actual enforced-disabled evidence and impact
approval. Missing implementation, absent tests or disabled state alone is not N/A.

## 3. D-B3-33 through D-B3-40 — eight independent scope decisions

For **each row** the human must choose exact received-summary content as new
prospective text, or request a distinct reviewed revision, or defer. The exact
source is B3, lines 8–15 respectively, plus file qualifications lines 3–4/17–19.
Whole-file digest is in document 01; no original messages were recovered.

| Item | Precise application and relation | Remaining decision / hazard | Human decision |
| --- | --- | --- | --- |
| D-B3-33 / Q33 | Separate Adapter runtime/auth/authz/admin; dedicated account/project; Option A 009/046 and 045/049 | Define actual privilege roots; separate process does not prove independence; no broad override of B1 | PENDING |
| D-B3-34 / Q34 | External secrets only; AWS/STS/role/internal keys nondependent | Resolve D-025 explicitly, including both original paragraphs | PENDING |
| D-B3-35 / Q35 | Adapter performs approved authenticated external operation; secrets not returned; no arbitrary fetch API | Separate from AWS Executor and AWS 024 partial MCP compatibility | PENDING |
| D-B3-36 / Q36 | Initial external reads/status only, empty list, no arbitrary HTTP/writes | AWS 014–021 still separate; GET may mutate or expose secrets; 023 cannot waive 045 | PENDING |
| D-B3-37 / Q37 | Independent identity + operation proof bound to principal/instance/action/target/parameters/expiry/revocation/reuse | 010–013/016/017/032–035 retained; exact issuer, original request integrity, contract digest and final transport controls need Design | PENDING |
| D-B3-38 / Q38 | Initially off; no initial Adapter/Token; enable only verified environment; AWS independent | D-025 and D-042 remain; summary's administrator activation is not a unilateral high-risk activation exception to Q40 | PENDING |
| D-B3-39 / Q39 | Independent Adapter Store; Broker cannot get/update/place Token or modify Store | Consistent with Option A; Token issuance/placement authority and platform control paths still unproven | PENDING |
| D-B3-40 / Q40 | Separate Adapter administration and distinct-human pair on high-risk changes across BWS/Cloud/CI/CD/Store; one-human emergency reduction | D-INT003; administrative setting rights 026/027 do not authorize bypass; restoration/re-enable is expansion | PENDING |

The exact file may be frozen as the current-text candidate with individual
decisions recording scope; mixed decisions must produce a new immutable
composition/selection map. Removing source qualifications or substituting a
paraphrase requires a distinct explicit revision. No original utterance is
inferred from a summary. B2-S1 specifically resolves only REQ-048's duration
parameters; it is not a general override of identity or session controls.

## 4. D-INT003 — distinct-human enforcement

Recommendation: retain `CRITICAL_OPEN`, allow only separately authorized
stop/revoke/reduce actions, block expansion/restore/re-enable pending actual
technical enforcement evidence. Human disposition of the requirement: PENDING.
No N1-P decision closes the technical finding.

Two accounts, roles, tokens or signatures controlled by one human are not two
independent people. Role compatibility for Requirements/Custodian does not
satisfy this rule. Verify identity and delegation privately, including credential
reset, enrollment, impersonation and recovery ownership. Pair approval must bind
one concrete old/new change, target, contract digest, expiry and application
count one, before effective application, with independent audit.

The required real inventory is Actor × Action × Resource × Effective Authority
for every environment/mode. Include BWS Organization Owner/Admin, Project/Machine
Account and every Secret writer; Password Manager/Vault; cloud root/org/admin;
host/hypervisor/Docker daemon/Desktop/VM; Deno/Workers deploy administration;
repository/org rules, CI/CD/runners and build/artifact/dependency promotion;
Store/KMS/snapshot/export; independent issuer/IdP/recovery/signing roots; operation
catalog/DNS/TLS/proxy/output policy; cancel/single-use stores; audit retention;
restore/rollback/replication; break-glass/vendor support and human-account recovery.
For each path identify actual holder, inherited/delegated rights, both persons,
pre-application enforcement, direct UI/API/CLI bypass refusal and audit receipt.
The retained [N1 governance evidence table](evidence/n1/03_N1_INT003_Governance_Feasibility_Gaps.md)
provides the 18 path classes; this is not N1-P document 03. Actual inventory and
all path tests remain NOT_RECOVERED / NOT_EXECUTED. One reachable bypass suffices
to retain CRITICAL_OPEN. A policy document or notification is not enforcement.

## 5. D-PREFETCH — FEAS-007-C independent content safety

Recommendation: maintain NOT_PROVEN; keep Adapter, Token placement and every
affected value-fetch path disabled. Human design disposition: PENDING.

Counterexample: a permitted Secret retains ID/Project/visible Version metadata
and contract, while its value is replaced by a dummy IAM key, restored from a
backup, remapped by a reference or selected through a mutable Version alias.
Even two legitimately authenticated distinct approvers may authorize this in
error. Approval integrity proves authorization, not non-IAM content provenance.
Reading the value first to check format/digest or discard it already violates
the no-acquisition guarantee. A second checker fetching first is not a workaround
authorized by this packet or by the fixed Option A text.

Closure requires independent non-value-reading trust, safe issuance/content
provenance over all ingress/restore paths, nonforgeable/nonrollback proof, exact
immutable fetched-version binding and atomic relation between proof and value
return. Unknown proof/version/races/partition means **no value request sent**.
Both unauthorized poisoning and valid-pair-approved poisoning need separately
authorized negative evidence; positive AC-022/032 cannot start beforehand.
Actual IAM long-term keys may not be used in tests. Feature shutdown is BLOCKED,
not an enabled-mode PASS. R4 055/056/AC-033/036 remain unadopted candidates.

## 6. D-SC — historical Security Contract draft

Human disposition: PENDING; recommendation is commission a distinct integrated
Security revision, not adopt the historical draft wholesale. Specific conflicts
and completion conditions are in document 04. Draft static/liveness assertions,
review conclusions and PR merges are neither current product evidence nor
Owner/Design/Security adoption. Fixed Option A, 045/047, Q40 independence and
pre-fetch prohibition cannot be weakened by copying its trusted-admin-Broker
assumption into v1.1.
