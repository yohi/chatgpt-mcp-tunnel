# N1-P R4 Individual 22-Clause Disposition Matrix

Status: **UNSIGNED / PROPOSED / NOT_EFFECTIVE**

## 1. Scope, source and digest rules

All 22 clauses are **UNADOPTED**; all human decisions are **PENDING**. No row is
pre-approved or pre-rejected. Candidate disposition is advice for an eventual
human ADOPT / DEFER / REJECT / REVISE decision, not its result. All candidate ACs
are **NOT_EXECUTED**. Text adoption never authorizes a test or technical PASS.

Exact source aliases:

- `S`: `evidence/n1/evidence/expanded/R4/06-security-requirements-rev4.md`,
  whole-file SHA-256 `ffd47e848e8bba76a39f2732d92f6b8ba7cff652939e8d4fb6653604e84abb6f`.
- `A`: `evidence/n1/evidence/expanded/R4/07-acceptance-rev4.md`,
  whole-file SHA-256 `501874cc568350f224aad45b45f09dc1e746ec6f10e9e5796baf4c27ad21dcc7`.
- Both are preserved in the original R4 ZIP and byte-identical expanded copies.
  “Original path” below means original *submitted member*, not an authoritative
  original or an authenticated adoption record.

`H-S`: take raw UTF-8 bytes after the unique `### REQ-nnn` heading LF through
before the next such heading (for 059, before `## 3.`); strip outer whitespace
only, no normalization or terminal LF addition. Include all paragraphs, lists,
bold markup and qualifications in that span. `H-A`: take the complete exact
single table row beginning `| **AC-nnn**`, excluding its LF, including pipes,
ID, all cells, requirement references and NOT_EXECUTED. These are explicitly
different scopes: full requirement body versus full submitted AC row. Their
digests below were independently recomputed; they are not signatures. Surrounding
S §§0–1 and A §§2–7 are important interpretive/test constraints, retained as
source context, not automatically adopted by selecting a row. A future adopted
AC representation with status removed needs its own revision/digest mapping.

## 2. Ten requirement candidates

`OA` = fixed Option A three-body set; dependencies referring to 050–059 or
025–036 are other unadopted R4 clauses. Numeric requirement references below
carry prefix REQ unless explicitly AC. Source lines include heading and trailing
spacing; extraction follows H-S rather than a rendered Markdown selection.

| ID | Original submitted path / extraction | Clause SHA-256 | Applies to | Existing dependency | Mutual / AC dependency | Risk | Candidate disposition | Human decision | Effect / unresolved issue |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| REQ-050 | S L44–49 / H-S | `e63bb0012fbadafbe0d894d7b2992aed7fc5003f86767d486b272c52839b172b` | Initial-off external mode; AWS independence | 007/008/025/045/047; Q34/Q38 | 051–059 for activation; AC-030/032 | Silent change to mandatory storage; nonproduction exception mistaken for permit | REVISE with D-025, or ADOPT exact with explicit conflict resolution | PENDING | Empty initial external list; no mandatory Token/Adapter; test exception itself grants no execution |
| REQ-051 | S L50–55 / H-S | `ff541ad090b0ab518f9481ca04f7ae2cbe92b8cd0ac018aefc8181d189481b82` | Adapter runtime/auth/admin independence | OA; 045/049; Q33/Q39 | 055/056/059; AC-025/026 | Process separation mistaken for privilege separation | ADOPT exact only after OA/text consistency, otherwise DEFER | PENDING | Independent actual execution and control planes; platform feasibility and INT-003 remain open |
| REQ-052 | S L56–61 / H-S | `c369ae89e686a8d3fa7f7ed3f6d2fb5ade3fc7a94089d1600a98a4f6181f431f` | External read/status operation contracts | 014–024/029/030; Q35/Q36 | 053/054/056/057; AC-027/032/034 | GET side effects, DNS/redirect, secret output, stale contract | ADOPT exact as contract requirement, or REVISE after protocol design | PENDING | Pin host/path/method/parameters/secret/output/retry limits and digest; external writes stay prohibited |
| REQ-053 | S L62–69 / H-S | `a6c4271691bfbd34da23e0c40126b97d119ffe408a23e81e68e9e0c25271a4fd` | Independent issuer and per-operation grant | 010–013/016/017/029/032–035; Q37 | 052/056/057; AC-025/029/034/035 | Broker-confused-deputy, request tamper, replay/channel transfer | ADOPT exact only with complete issuer protocol, otherwise DEFER | PENDING | Independent original-request/identity verification, contract digest, expiry/epoch/single-use/channel binding; not an implemented issuer |
| REQ-054 | S L70–75 / H-S | `7ac4e9d3f0cc140d3fdf05cb8035f37f7f575078919018e94646c9b4dd23911d` | Adapter-only secret use and safe outputs | OA; 023/045/049 | 052/055; AC-025/032/033/036 | Post-fetch discard misrepresented as no acquisition | ADOPT exact prohibition, or DEFER dependent feature | PENDING | No-fetch if 055 not established; response/log/telemetry confidentiality must be designed |
| REQ-055 | S L76–95 / H-S | `b09181d46376124043fa746ae6fbd142c2e0abfe05b3e48f8410fd555f1dd157` | Store/Project and pre-fetch content provenance | OA; 045/047/049; Q33/Q39 | 051/054/056/058; AC-025/026/028/032/033/036 | Approved or unauthorized value poison, restore/Version TOCTOU | ADOPT exact safety obligation; DEFER activation while unproven | PENDING | Independent non-value-reading provenance and atomic version binding; FEAS-007-C NOT_PROVEN; no checker-acquires-first assumption |
| REQ-056 | S L96–105 / H-S | `43a40bfc7d12de98fca15ae9b380581a5cc9517d9101a678d5d2f0637c0dc430` | Every high-risk/expanding administrative path | 045/046; Q40 | 051–055/057/058; AC-026/027/028/033/034/036 | Single Owner/Admin/root/CI/restore bypass; same-person pair | ADOPT exact control requirement, not closure; otherwise DEFER feature | PENDING | Two distinct humans, concrete change once; approved poison still forbidden; INT-003 CRITICAL_OPEN |
| REQ-057 | S L106–126 / H-S | `7713ffccf3f1e1fbbe179207a2b68e3c6c8951c45006892005a61705af9d4e13` | One-human reduction, dispatch/cancel and residual state | 017/020/031–040; Q40 | 053/056/058; AC-029/035 | Ledger-only dispatch flag, post-cancel queue send, unknown-result retry | REVISE ambiguous “AWS external integration writes” wording in L119 without changing AWS-vs-external policy, or ADOPT with reviewed precise scope map | PENDING | C/S/D/R final-transport contract; reduction never licenses restoration; no new candidate wording silently substituted |
| REQ-058 | S L127–132 / H-S | `3d3c55f46b6d24b3485f377ab2833f4a9b418286b8ca4a050972e88acb0cae09` | Token issue/place/permission change | 045/046/047; Q39/Q40 | 055/056/057; AC-027/029 | Blanket future rotation; Token revoke assumed session kill | ADOPT exact per-change rule, or DEFER Token features | PENDING | Each issuance/placement/permission change approved once by distinct pair; session residuals separately tracked |
| REQ-059 | S L133–138 / H-S | `d3b238b90cf8e89e880a0e51cbeb0efa983a2209a7b6533b20e6e433eef98e44` | Deno/Workers/Docker Linux+macOS × modes | 008/041/042/043; Q38/Q39 | 050–058; AC-031/036 and enabled suite | Disabled-only success mislabeled parity; unjustified N/A | ADOPT with D-042 explicit applicability, or REVISE scoped release | PENDING | Four concrete configurations, two modes each; no full compliance where unproven |

## 3. Twelve acceptance candidates

| ID | Original submitted path / extraction | Clause SHA-256 | Applies to | Existing dependency | Mutual / requirement dependency | Risk | Candidate disposition | Human decision | Effect / unresolved issue |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AC-025 | A L11 / H-A | `9f7315df9edf58b5dc708464e9479a4685c819813b78a66da49e7e770f717d4e` | Compromised Broker credential isolation | OA; 045/049; AC-012 | 051/053/054/055 | Narrow MCP-only threat model substituted for Broker-compromise model | ADOPT exact contract after boundary reconciliation, or DEFER | PENDING | Requires original replacement approval; no current compromised-runtime experiment |
| AC-026 | A L12 / H-A | `5523d5e5b718e2d3b0741a770e08b1ab58bcfd95fe831d89e7fcf44fdd80a880` | Effective Adapter/Store/deploy/issuer/audit management rights | OA; 045/046 | 051/055/056 | Separate process falsely counted as isolation | ADOPT exact evidence demand, or DEFER feature | PENDING | Actual granted privileges must deny Broker-family management paths |
| AC-027 | A L13 / H-A | `0cb8aab7a7e86ddd1108c80a63dc748b8aab13ca44b47beb3cdf046b75c05084` | Two distinct humans, one concrete change once | Q40; 046 | 052/056/058; AC-028 | Same-human accounts, replay, digest substitution, indefinite rotation | ADOPT exact test contract, or DEFER high-risk feature | PENDING | Authenticated identity and actual apply-path enforcement needed; no technical closure |
| AC-028 | A L14 / H-A | `5f88af29f2046f9f6f29bd8fc3a27c1576875f4d2f7ccd96bb6d44d67989e547` | All bypass paths and pre-fetch enforcement | 045/046 | 051/055/056; AC-033/036 | Omitted root/support/restore path; audit-only detection | ADOPT exact; otherwise DEFER activation | PENDING | No unmanaged path; approved poison separately AC-036; no-fetch/off is BLOCKED not enabled PASS |
| AC-029 | A L15 / H-A | `53d6e74c28e67bdcc768d1ee89e6188603536022d7ff8e422435502ee0277768` | Emergency reduction and C/S/D/R fault cases | 017/032–035; Q40 | 053/057/058; AC-035 | S consumed before C but queued first send after C | ADOPT exact with completed transport specification | PENDING | Crash, multi-Adapter, buffer, audit/store outage and BWS residual-session evidence required |
| AC-030 | A L16 / H-A | `08354b13d540f07a300e5d702f291604937aca4dfff127ac6c9f3661eb5b1724` | Initial-disabled AWS-only mode | 007/025/045/047 | 050; AC-021/023/031 | AWS-only pass treated as full integration readiness | ADOPT exact after D-025, or REVISE conflict text | PENDING | No BWS Token/Adapter/traffic; external denied; real AWS execution still separately prohibited now |
| AC-031 | A L17 / H-A | `50ca864e88e6bc649e6faea8d4155d12ae8c59fbeda64ed3428010ed52ce826e` | Four configurations and enabled/disabled modes | 008/041/042; AC-001/018/021 | 059; AC-025–030/032–036 | Docker host conflation; N/A used to hide missing feature | ADOPT exact with D-042, or REVISE applicability | PENDING | Separate evidence cells and normative N/A basis; no environment PASS inherited |
| AC-032 | A L18 / H-A | `c937561b4fa8d830b067d74f2d6f18a4667e7b0580fce7b5dab433c9f9ea19f5` | Isolated positive nonproduction E2E | OA; 045/049; AC-020 retained separately | 050/052/053/054/055; AC-033/036 | Positive fetch before proof; mock-only PROVEN claim | ADOPT exact prerequisite, DEFER execution | PENDING | No positive fetch until pre-fetch evidence; operation-specific later authorization; no real IAM keys |
| AC-033 | A L19 / H-A | `60b110e6030dea18b9ac3bfc3ac6791cbd5ff005660476fa509e3d6427dbcb54` | Same-ID value-only unauthorized and approved poison | 045/046; OA AC-022 | 054/055/056; AC-028/036 | Reject-after-fetch falsely counts as pre-fetch refusal | ADOPT exact negative obligation, DEFER experiment | PENDING | Refuse before BWS value request; if indistinguishable then no-fetch/feature BLOCKED |
| AC-034 | A L20 / H-A | `2dc745aac1613ea5a105b751349b165656aba6a768d666363f34ce7b173ab02f` | Issuer basis, request intent, contract and channel binding | 010–013/016/017 | 052/053/056; AC-025/035 | Broker-supplied user accepted as independent identity | ADOPT exact with issuer Design, otherwise DEFER | PENDING | False user/operation, old contract, schema/destination/channel/epoch mutation all refused |
| AC-035 | A L21 / H-A | `6955f3aae656f2cc032ebb6e5358a0312ee41cca582a1ce291d9ae4028732210` | Multi-Adapter single-use and final transport | 017/032–035/040 | 053/057; AC-029 | D flag without actual transport enforcement | ADOPT exact with final-send Design, otherwise DEFER | PENDING | Cancel-unsent zero initial sends, D-before-C residual no resend; fault and rollback evidence |
| AC-036 | A L22 / H-A | `517aceefe27d4909cba76c9a2b3c1e689724ee0e03534640c3c09b08ad2dc79e` | Valid distinct-pair-approved forbidden-content insertion | 045/046; OA AC-022 | 054/055/056/059; AC-028/033 | Correct approvals mistaken for content safety | ADOPT exact prohibition/test contract, DEFER experiment | PENDING | Invalid dummy IAM only in later isolated authorized work; before-request refusal; whole shutdown is BLOCKED |

## 4. Dependency closure and deferral rules

The 49 original REQ, 24 original AC and B2-S1 are individually accounted for in
document 01 §5. None is removed by this table. The R4 nonregression matrix
(`R4/05-nonregression-matrix-rev4.md`, digest
`8c6ce4ea0ac06adc0d4aa6d89dc3293e329ac16051aece5ee205cabb3c1e78b8`)
is an analytical cross-reference, not a substitute adopted baseline.

For each selected clause, compute transitive dependencies from both matrices,
including existing requirements, B3 scope decisions, OA, D-025/D-042 and Design
sections. A dependency can be satisfied by exact adopted text or a separately
reviewed adopted equivalent with explicit mapping; never by assuming an unadopted
reference was adopted automatically. Record unresolved dependencies and hold the
feature. Circular safety dependencies form a joint review set, not an ordering
that enables unsafe intermediate states.

| Partial set offered | Minimum textual closure | Feature status while incomplete |
| --- | --- | --- |
| Initial-off declaration only | 050/AC-030 plus D-025, retained 007/008/045/047 and adopted mode applicability; no implication that other 21 clauses are adopted | External capability remains disabled; no Token placement; no full-system N2 |
| Credential/Store safety obligations | OA, 051/054/055/056, Q33/Q39/Q40, 045/049 plus corresponding AC-025/026/028/033/036 and compatible 059/applicability; resolve outgoing dependencies explicitly | Obligations can be adopted prospectively with no enabled implementation; INT-003 and FEAS-007-C still open |
| Token lifecycle | 055/056/057/058, identities/Store/issuer boundaries, AC-027/028/029 and all reachable dependencies | No issue/place/re-enable while enforcement unproven |
| Enabled external read operation | 050–059 and AC-025–036 with all dependencies, or reviewed exact equivalents; full integrated Design/AC/Security; independent content and governance technical gates | BLOCKED; neither a partial adoption nor full textual adoption permits operation |
| Full environment claim | 059/AC-031 + original 008/041/042/AC-001/018/021 and every required enabled-mode obligation | No parity claim from disabled-only evidence; Docker/Linux and macOS separate |

A human may DEFER or REJECT any candidate but must resolve what happens to its
dependent mandatory capability and safety obligations: keep it disabled, provide
a reviewed equivalent, or commission an explicit requirements amendment. Rejecting
a proposed test does not establish the underlying guarantee. Deferral never
waives 045, 047, independent-human enforcement or the fixed pre-fetch condition.
