# N1-P Candidate Composition Manifest

Status: **UNSIGNED / PROPOSED / NOT_EFFECTIVE**

## 1. Decision scope and identity

Candidate label: `AWS-MCP-BROKER-v1.1-P-CANDIDATE-N1P-r0`.
This is a working label, not an official immutable revision or approval ID.
Case P is **PROPOSED_NOT_YET_SELECTED_BY_OWNER**. Option A intent is preserved;
its policy direction is not submitted for re-selection. No historical adoption
is reconstructed. This packet proposes a composition with explicitly unresolved
components; it is not yet an approvable complete, consistent baseline.

| Field | Value |
| --- | --- |
| Repository | `yohi/chatgpt-mcp-tunnel` |
| Fixed commit | `ac462699e0b1988eda63ea3d6dacfc2a030bb822` |
| Observed branch | `feat/aws-broad-iam-read-api-tools` |
| Local and remote branch drift | None at this investigation's read-only checks |
| Final canonical source URI / immutable revision | PENDING |
| Custodian / authority-verification receipt | PENDING |
| Requirements Owner identity / authority reference | PENDING |
| Final adopted composition digest | PENDING |
| Actual approval event / UTC / effective-from UTC | PENDING / PENDING / PENDING |
| Owner / Design / Security signatures | Empty; no signatures supplied |

The SHA-256 of this preparation file and the transport `MANIFEST.json` are not
the final adopted composition digest. Decisions or new text require a new frozen
composition and a new actual authenticated human event, not edits to this packet
represented as if already approved.

## 2. Source coordinates and integrity

All coordinates below are packet-relative. `N1` means `evidence/n1/`;
`R4` means `evidence/n1/evidence/expanded/R4/`; `R1` means
`evidence/n1/evidence/expanded/R1/`; `Received` means
`evidence/n1/evidence/received/sources/`. These aliases identify evidence copies,
not canonical authority locations. Exact original ZIPs are retained under
`sources/`; N1's own original handoff and nested copies are retained too.

| Source component | Bytes | Whole-file SHA-256 | Qualification |
| --- | ---: | --- | --- |
| `sources/AWS_MCP_Broker_N1P_Handoff_20261016.zip` | 410946 | `cf09ba905dfb8ab2721ed5c873924829a2e4f9d5d0f79dd6b20d5b560e5c780f` | Expected digest supplied by user; integrity only |
| `sources/01_N1_Deliverables_20261016.zip` | 412744 | `b26add50668cf2bdc7929513a7a8c1e3a2325b7c6d8e45e0ab9dd35ca67e0ef6` | Expected digest in work contract |
| B1: R4 `01-fixed-baseline-v1.0.md` | 13633 | `39002fc2ce5f21e9e686a427c793a7fd42fc84e5bdb02684be9e1e3a4305f4bc` | Submitted transcription; 44 REQ + 20 AC |
| B2: R4 `02-fixed-baseline-v1.1.md` | 7247 | `3078acc5c31b5e900697dbb585e5ed604dfca89fe82b56cfc9528ac3c91350e2` | Submitted addendum; 5 REQ + 4 AC + B2-S1 |
| B3: R4 `03-fixed-decisions-Q33-Q40.md` | 2506 | `f287966ac61f467704f99c545f2d7a9756b9f21a70a5f90a814367ab7a113aa4` | Summary, not original utterances |
| R4 ZIP: Received `02_R4_Submitted_Copy.zip` | 51161 | `cd9611654f17d5eee73d47d5d32ce6d94459c24016c2dc3a1a157f90fbd8a15c` | Unadopted submission |
| R1 ZIP: Received `03_Option_A_R1_Submitted_Copy.zip` | 35057 | `cedf39f04a1733e42fe00e22f9c262a0bd5ad62a682a6ee50efdced287e85912` | Unauthenticated decision preparation |
| Owner intent: Received `04_Owner_Intent_Submitted_Copy.md` | 13475 | `5b9fd27668d7a47cfeff5c09fc6aae79decbd5929b159e953b7274ce4355c34a` | Intent, not authority/event proof |
| Security draft: Received `05_STS001_Security_Contract_DRAFT_Submitted_Copy.md` | 14724 | `0cc08ad3a1970be2ba4a73e47240d96fc9300afb5747da48db2d2bd9bdac102c` | Historical draft, not adopted contract |

R4 and R1 copies of B1/B2/B3 are independently byte-identical. That proves
submitted-copy identity only. B1/B2/B3's official custodian, canonical URI,
authorized adoption event, valid delegation and historical effective times are
**NOT_RECOVERED / NOT_VERIFIED**. The file labels claiming adoption are quoted
claims. Case P would establish new current content prospectively, without making
those historical claims true.

## 3. Composition and precedence proposal

All rows require human disposition. No row currently takes effect.

| Component | Proposed current-text treatment | Exact override boundary / unresolved issue |
| --- | --- | --- |
| B1 REQ-001–044, AC-001–020 | Retain all source clause text except the specified replacement | REQ-009 alone has an Option A full-body replacement; REQ-025 and REQ-042 require separate explicit decisions, not silent editing |
| B2 REQ-045–049, AC-021–024 | Retain all source clause text except specified replacements | REQ-046 and AC-022 alone have Option A full-body replacements |
| B2-S1, B2 lines 148–152 | Retain as an explicit supplement to REQ-048 | Resolve only the open duration parameters: 8h absolute, 15m idle; authenticated human-only idle renewal; unattended identity separate |
| Option A REQ-009/046/AC-022 | Replace entire corresponding clause bodies prospectively | Never replace whole B1/B2 files; keep all old text as evidence; no partial six-item or tail-paragraph replacement |
| B3 Q33 | New-current-summary adoption candidate only | Independent execution/authentication/authorization/administration; coordinate with Option A, 045/046/049; not a blanket Broker redefinition |
| B3 Q34 | New-current-summary adoption candidate only | External-service secrets only; AWS/STS/role/internal-auth/encryption nondependency; explicit REQ-025 decision D-025 required |
| B3 Q35 | New-current-summary adoption candidate only | Authenticated external operation completes in Adapter; no arbitrary secret-fetch API or secret return; supplements 023/024/049 |
| B3 Q36 | New-current-summary adoption candidate only | External reads/status only; empty initial list; no arbitrary HTTP or external writes; does not repeal AWS 014–021 |
| B3 Q37 | New-current-summary adoption candidate only | Independent principal authentication and per-operation proof; supplements 010–013/016/017/032–035; detailed issuer/contract protocol still missing |
| B3 Q38 | New-current-summary adoption candidate only | Initially disabled; no initial Token/Adapter requirement; AWS independent; D-025 and D-042 remain necessary |
| B3 Q39 | New-current-summary adoption candidate only | Independent Adapter Store; Broker cannot obtain/update/place Token or alter Store; platform evidence absent |
| B3 Q40 | New-current-summary adoption candidate only | Independent two distinct humans for high-risk/expanding changes across all effective paths; one authorized human can reduce; never authorize restore/re-enable through that exception |
| B3 qualifications, lines 3–4, 17–19 | Preserve exact source qualifications as evidence and define prospective status explicitly | Summary provenance, uncertain key location, both stores protected, feasibility unproven; historical “confirmed” labels do not become event evidence |
| R4 REQ-050–059 / AC-025–036 | All excluded from adopted set until individually decided | See document 03; UNADOPTED, human decision PENDING for each |
| R4 explanatory restatements of REQ-025/042, INT-001–006 | Analytical evidence, not automatic normative overlays | D-025/D-042 and explicit selected revisions required |
| Architecture / integrated AC / adopted Security Contract | Required components absent as authenticated originals | NOT_RECOVERED; commission missing sections in document 04 |

B3 handling decision D-B3: the human may select the exact received summary file
bytes as new current content, with its precise eight-item applicability map, or
commission a distinct explicit revision for review. If selected clauses are
changed, expanded, translated as replacement text, or a qualification is removed,
that is a new candidate revision. An undifferentiated “B3 overrides B1/B2” is
unacceptable. Until D-025/D-042 are resolved, the composition remains incomplete
even if the summary is selected. No history is retroactively superseded.

## 4. Fixed Option A full-body references

The full texts are included without alteration at the following R1 paths and
also in R1 Record §3, R4 request and submitted Owner intent §3. `adopted-text`
is a historical filename, not a finding of adoption. For these raw `.txt` files,
hash the original bytes directly: UTF-8, embedded LF retained, no terminal LF,
no BOM insertion, no Unicode normalization. Do not run `strip()` on a future
edited file as a way to conceal changed bytes. Source fenced-text comparison
uses the source-defined outer-strip rule only when reproducing its body scope.

| Clause / R1 raw filename | Bytes | Body SHA-256 | Old body SHA-256 |
| --- | ---: | --- | --- |
| REQ-009: `adopted-text-REQ-009.txt` | 1241 | `f17db0565942501a39c3302912dcb161e2f3e38e168f29a51491a711e0851bb9` | `d75233273042089564339a9b5f7f39ccb36e62367b4212b64849fed3abc49b18` |
| REQ-046: `adopted-text-REQ-046.txt` | 2939 | `6362d06bfe5d1c1184057f84c42f2f6ed4c19d6dc47b8662cfe039105e21d931` | `410aacaeb42a90880e988fd86f84dd9fa09c780f575b6c78d14a8497d7658a94` |
| AC-022: `adopted-text-AC-022.txt` | 1213 | `3a02643899b8d79683f6c13300e0ee655b4b00fe20d23f87a3c35efb4e521a39` | `58c7b2b6b562c7bc06b224c0daa2413764360c0e50954e3bc22a6c86b69a9aba` |

REQ-046 replacement includes opening, all six mandatory items, Password Manager
and CLI paragraphs. AC-022 includes pre-fetch proof before positive acquisition,
Broker denial and validly approved poisoning refusal. REQ-045 remains unconditional;
two valid approvals never waive prohibited-content exclusion. REQ-047/049 and
B2-S1 remain intact. A changed body needs a distinct reviewed revision and cannot
inherit the fixed Option A digest or intent without a new explicit decision.

## 5. Complete retained-clause ledger

The following inventory accounts for every original ID. Exact text is the named
heading/body or AC table row in hash-fixed B1/B2; source headings are unique.
`RETAIN` means proposed unchanged current content, not verified historical law.
`RETAIN + D` preserves bytes while flagging integration conflict. This ledger
does not adopt the R4 nonregression matrix's interpretations. Its 73 entries are
independently counted; B2-S1 and eight Q items are additional components above.

| ID | Source | Proposed treatment |
| --- | --- | --- |
| REQ-001 | B1 | RETAIN |
| REQ-002 | B1 | RETAIN |
| REQ-003 | B1 | RETAIN |
| REQ-004 | B1 | RETAIN |
| REQ-005 | B1 | RETAIN |
| REQ-006 | B1 | RETAIN |
| REQ-007 | B1 | RETAIN |
| REQ-008 | B1 | RETAIN; D-042 environment dependencies |
| REQ-009 | B1 | OPTION_A_FULL_BODY_REPLACEMENT |
| REQ-010 | B1 | RETAIN |
| REQ-011 | B1 | RETAIN |
| REQ-012 | B1 | RETAIN |
| REQ-013 | B1 | RETAIN |
| REQ-014 | B1 | RETAIN |
| REQ-015 | B1 | RETAIN |
| REQ-016 | B1 | RETAIN |
| REQ-017 | B1 | RETAIN |
| REQ-018 | B1 | RETAIN |
| REQ-019 | B1 | RETAIN |
| REQ-020 | B1 | RETAIN |
| REQ-021 | B1 | RETAIN |
| REQ-022 | B1 | RETAIN |
| REQ-023 | B1 | RETAIN; no exception to 045 |
| REQ-024 | B1 | RETAIN |
| REQ-025 | B1 | RETAIN + D-025; no silent reinterpretation |
| REQ-026 | B1 | RETAIN; Broker settings exclude independent Adapter administration |
| REQ-027 | B1 | RETAIN; independent boundary must be adjudicated |
| REQ-028 | B1 | RETAIN |
| REQ-029 | B1 | RETAIN |
| REQ-030 | B1 | RETAIN |
| REQ-031 | B1 | RETAIN |
| REQ-032 | B1 | RETAIN |
| REQ-033 | B1 | RETAIN |
| REQ-034 | B1 | RETAIN |
| REQ-035 | B1 | RETAIN |
| REQ-036 | B1 | RETAIN |
| REQ-037 | B1 | RETAIN |
| REQ-038 | B1 | RETAIN |
| REQ-039 | B1 | RETAIN |
| REQ-040 | B1 | RETAIN |
| REQ-041 | B1 | RETAIN; D-042 applies |
| REQ-042 | B1 | RETAIN + D-042; no partial-mode equivalence |
| REQ-043 | B1 | RETAIN |
| REQ-044 | B1 | RETAIN |
| REQ-045 | B2 | RETAIN; unconditional no-acquisition |
| REQ-046 | B2 | OPTION_A_FULL_BODY_REPLACEMENT |
| REQ-047 | B2 | RETAIN; no ambient fallback |
| REQ-048 | B2 | RETAIN + B2-S1 explicit supplement |
| REQ-049 | B2 | RETAIN |
| AC-001 | B1 | RETAIN; D-042 applies |
| AC-002 | B1 | RETAIN |
| AC-003 | B1 | RETAIN |
| AC-004 | B1 | RETAIN |
| AC-005 | B1 | RETAIN |
| AC-006 | B1 | RETAIN |
| AC-007 | B1 | RETAIN |
| AC-008 | B1 | RETAIN |
| AC-009 | B1 | RETAIN |
| AC-010 | B1 | RETAIN |
| AC-011 | B1 | RETAIN |
| AC-012 | B1 | RETAIN |
| AC-013 | B1 | RETAIN |
| AC-014 | B1 | RETAIN |
| AC-015 | B1 | RETAIN |
| AC-016 | B1 | RETAIN |
| AC-017 | B1 | RETAIN |
| AC-018 | B1 | RETAIN; D-042 applies |
| AC-019 | B1 | RETAIN |
| AC-020 | B1 | RETAIN; real AWS evidence remains a later separately authorized obligation |
| AC-021 | B2 | RETAIN; D-042 applies |
| AC-022 | B2 | OPTION_A_FULL_BODY_REPLACEMENT |
| AC-023 | B2 | RETAIN; Bitwarden failure must not become an AWS credential dependency |
| AC-024 | B2 | RETAIN + B2-S1 test parameters |

No original requirement or acceptance condition is marked satisfied. Full-system
N2 entry requires the completed composition, authority evidence and adopted
Design/integrated AC/Security, as detailed in document 07.
