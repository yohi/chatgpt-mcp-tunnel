# N1 Authority Chain Evidence Register

## Conclusion and scope

`UNSIGNED / EVIDENCE_REGISTER_ONLY`. Submitted bytes are verified; authoritative
custody and authenticated adoption are **NOT_VERIFIED**. This is a new N1
investigation, separate from N0, implementers, prior reviewers, Requirements
Owner and Design/Security approvers. Organizational independence is not proven
by this AI role declaration. No human identity or authority is certified here.

- Repository: `yohi/chatgpt-mcp-tunnel`.
- Branch: `feat/aws-broad-iam-read-api-tools`.
- Fixed commit: `ac462699e0b1988eda63ea3d6dacfc2a030bb822`.
- Investigation date: 2026-10-16 JST. Observed host UTC during investigation:
  `2026-10-15T20:32:35Z`; this is an observation, not an approval timestamp.
- All paths below are relative to this local packet. `evidence/received/`
  preserves the handoff members; `evidence/expanded/{N0,R4,R1}/` preserves
  extracted submitted members without edits. These are evidence copies, not
  newly established canonical sources.

## 1. Independently recomputed integrity

This table verifies submitted-package integrity only. **No row authenticates
the publisher, official custody or adoption authority.**

| Input | Bytes | SHA-256 | Independent result |
| --- | ---: | --- | --- |
| Outer `AWS_MCP_Broker_N1_Handoff_20261016.zip` | 126254 | `8ede6a833d9f846fae3b28e47fa9207142377f1d74c74258ab4e736572cdf051` | CRC 9/9; outer SHA256SUMS 8/8; MANIFEST 7/7 size/digest matches |
| `sources/01_N0_Submitted_Result.zip` | 21730 | `1e532707f4241fece3ef63fa889048bbae62facadd8ef6fdae413815e09409d4` | CRC 6/6; N0 MANIFEST deliverables 5/5 match |
| `sources/02_R4_Submitted_Copy.zip` | 51161 | `cd9611654f17d5eee73d47d5d32ce6d94459c24016c2dc3a1a157f90fbd8a15c` | CRC 15/15; SHA256SUMS 14/14 match; N0 archive_members 14/14 match |
| `sources/03_Option_A_R1_Submitted_Copy.zip` | 35057 | `cedf39f04a1733e42fe00e22f9c262a0bd5ad62a682a6ee50efdced287e85912` | CRC 14/14; SHA256SUMS 13/13 match |
| `sources/04_Owner_Intent_Submitted_Copy.md` | 13475 | `5b9fd27668d7a47cfeff5c09fc6aae79decbd5929b159e953b7274ce4355c34a` | Outer MANIFEST and N0 source digest match |
| `sources/05_STS001_Security_Contract_DRAFT_Submitted_Copy.md` | 14724 | `0cc08ad3a1970be2ba4a73e47240d96fc9300afb5747da48db2d2bd9bdac102c` | Outer MANIFEST and N0 source digest match |

The outer digest is **measured**, not authenticated against an independently
trusted publisher signature or external expected digest. Internal hash agreement
does not establish publisher identity. ZIP checks found no traversal, absolute
paths, duplicate names or symbolic links; bounded member sizes and expansion
ratios were checked. No archive content was executed. Nested ZIPs were checked
before expansion. Outer member names were inspected before outer extraction;
the explicit path/type scan followed and confirmed the inspected names.

All five N0 documents were read in full. B1/B2/B3, R4 reconciliation,
49-REQ/24-AC matrix, new requirement and AC candidates, decision request,
R2/R3 finding summaries, feasibility handoff, R1 record/static review/patch,
ratification checklist, Owner intent and STS-001 draft were read in full.

## 2. B1/B2/B3 authority chain, one-to-one

| ID | Candidate and declared revision | Bytes / SHA-256 | Candidate provenance |
| --- | --- | --- | --- |
| B1 | `evidence/expanded/R4/01-fixed-baseline-v1.0.md`; Requirements v1.0, REQ-001–044, AC-001–020 | 13633 / `39002fc2ce5f21e9e686a427c793a7fd42fc84e5bdb02684be9e1e3a4305f4bc` | Reference transcription claiming conversation source 2026-10-12; R4 and R1 copies byte-identical |
| B2 | `evidence/expanded/R4/02-fixed-baseline-v1.1.md`; Addendum v1.1 plus B2-S1, REQ-045–049, AC-021–024 | 7247 / `3078acc5c31b5e900697dbb585e5ed604dfca89fe82b56cfc9528ac3c91350e2` | Reference transcription claiming conversation acceptance; external original explicitly unconfirmed; R4/R1 identical |
| B3 | `evidence/expanded/R4/03-fixed-decisions-Q33-Q40.md`; Q33–Q40 summary, no authenticated revision identifier | 2506 / `f287966ac61f467704f99c545f2d7a9756b9f21a70a5f90a814367ab7a113aa4` | Explicitly a summary, not original messages; R4/R1 identical |

| ID | Official custodian / authority basis | Canonical URI / immutable revision | Authorized adopter / role grant | Authenticated adoption event ID / UTC / target digest / effective date | Verdict |
| --- | --- | --- | --- | --- | --- |
| B1 | NOT_RECOVERED | NOT_RECOVERED | NOT_RECOVERED | NOT_RECOVERED in every field | NOT_VERIFIED |
| B2, including B2-S1 | NOT_RECOVERED | NOT_RECOVERED | NOT_RECOVERED | NOT_RECOVERED in every field | NOT_VERIFIED |
| B3, each Q33–Q40 | NOT_RECOVERED | Original message events and revision chain NOT_RECOVERED | NOT_RECOVERED | NOT_RECOVERED in every field | NOT_VERIFIED |

B2's statement that text was adopted and B3's `USER-CONFIRMED` label are
submitted declarations, not independently authenticated events. B2-S1 records
8-hour absolute / 15-minute idle expiry and human-only idle renewal; its
historical adoption authority is also unverified. B3 Q32's storage assumption
does not establish where existing IAM keys actually reside.

Historical chain needed for each row: original custodian authority → immutable
source bytes/revision → adopter identity and valid delegation at that time →
authenticated event covering the exact digest → actual effective date and
supersession/revocation history → independent comparison. No chain is complete.

## 3. Other evidence and missing authorities

| ID | Source / revision | SHA-256 | Authority qualification |
| --- | --- | --- | --- |
| R4-REC | R4 `04-normative-reconciliation-rev4.md`, 2026-10-13 JST | `4582d85fec1c403854e4fa4f2b4010d0fb2254290f57fe6f01b273a8b146798b` | REVISION_CANDIDATE; not an adoption event |
| R4-NR | R4 `05-nonregression-matrix-rev4.md` | `8c6ce4ea0ac06adc0d4aa6d89dc3293e329ac16051aece5ee205cabb3c1e78b8` | Analytical 73-entry matrix; dynamic proofs 0 |
| R4-REQ | R4 `06-security-requirements-rev4.md` | `ffd47e848e8bba76a39f2732d92f6b8ba7cff652939e8d4fb6653604e84abb6f` | REQ-050–059 UNADOPTED_PROPOSAL |
| R4-AC | R4 `07-acceptance-rev4.md` | `501874cc568350f224aad45b45f09dc1e746ec6f10e9e5796baf4c27ad21dcc7` | AC-025–036 UNADOPTED_PROPOSAL / NOT_EXECUTED |
| OA-REQUEST | R4/R1 `08-owner-decision-request.md` | `021f2ca95d6f769881150bc00df067692eccc0cb3fc174a567fe3f83fa255d90` | Old/new full texts and line diffs; not approval |
| OA-R1 | R1 `01-owner-decision-record-option-a-limited-correction-r1.md` | `92cef5b23ca9696ede0c9a6d5ca979056c20b6c17853598afcf6af914f60865e` | OWNER_ATTESTATION_PENDING / NOT_EFFECTIVE |
| OA-REVIEW | R1 `02-independent-static-review-20261014.md` | `bf783e7720c590a5d85349efd755bf10ecbdf46ce171c9785c1c1b846f7b3d0e` | Pre-correction static review; not post-adoption N2; organizational independence not established |
| OWNER-INTENT | Received source 04, 2026-10-14 JST | `5b9fd27668d7a47cfeff5c09fc6aae79decbd5929b159e953b7274ce4355c34a` | Option A intent preserved; proposed ID is not official; actual identity, authority, UTC and event pending |
| SC-DRAFT | Received source 05, 2026-10-14 JST | `0cc08ad3a1970be2ba4a73e47240d96fc9300afb5747da48db2d2bd9bdac102c` | DRAFT / NOT APPROVED; historical code reference `05f4b92e7ff2de76dc79cf8d5dc9f563a03af209`, not fixed N1 HEAD |
| ARCH-DESIGN | Complete authoritative v1.1 Architecture/Design | NOT_AVAILABLE | MISSING_AUTHORITY: no canonical original, revision, custodian, authorized event or digest recovered |
| AC-INTEGRATED | Complete authoritative integrated acceptance contract | NOT_AVAILABLE | MISSING_AUTHORITY: B1/B2/R4 copies are not an approved integrated contract |
| SC-ADOPTED | Authoritative adopted Security Contract | NOT_AVAILABLE | MISSING_AUTHORITY: SC-DRAFT is not a substitute |

SC-DRAFT includes a privileged source/Broker trust assumption and historical live
test assertions. N1 neither reran nor independently authenticated them. Its
limited MCP-compromise claim is not evidence of the broader v1.1 isolation
guarantees. It requires design adjudication, not automatic incorporation.

## 4. Retrieval log and coverage limit

Read-only GitHub access used the existing `gh` session; no credentials were
displayed, exported or changed. This access establishes repository evidence,
not Requirements Owner authority. No AWS/Bitwarden/Cloudflare/Deno/container
or Broker endpoints were accessed.

| Retrieval surface | Observation | Limit |
| --- | --- | --- |
| Local HEAD / named branch / GitHub ref | All equal fixed `ac462699e0b1988eda63ea3d6dacfc2a030bb822` | No HEAD substitution; no drift at observation |
| Local fixed tree and GitHub recursive tree | 34 blob paths; `truncated=false`; docs are README, G0 plans/unsigned drafts and isolated experiment README | No B1/B2/B3 or approved complete normative set identified in this tree; not a claim about inaccessible stores |
| PR #14 | MERGED `2026-10-15T10:14:22Z`; merge `8f4c7c880d74c44e640d6ea3a423e167c942b051` | Isolated offline foundation; no normative adoption |
| PR #15 | MERGED `2026-10-15T10:48:51Z`; merge fixed N1 HEAD | Limited offline correction; I1 closures remain reported, not a new N1 technical re-review |
| PR #11/#12/#13 bodies and review metadata | Plans and unsigned G0 records; explicit non-authorization statements | Review/merge is not baseline adoption or G0 approval |
| PR #13 human review | Event `5529960691`, `2026-10-15T08:03:24Z`, COMMENTED, empty body, commit `d5c1a58339df737f3a0ee4ed40f5dfe2dd87325a` | Does not bind B1/B2/B3 or Option A digests; no Requirements Owner delegation established |
| Repository issues/PR index | 14 entries on first page, second page empty; titles scoped to tunnel/code/G0 work | No named normative authority event located; index is not exhaustive proof of absent private governance |
| Releases | Empty result | No release authority package recovered |
| Local Git Markdown history | Available local refs inspected for documentation provenance | No trusted normative original located; un-fetched refs not asserted searched |
| Connected MCP resources/templates | No project document library or private approval archive exposed; templates empty | ChatGPT Library / original conversation / private governance system NOT_ACCESSIBLE in this session |
| Local additional `.omo/drafts` records | G0 candidates remain unsigned/pending | G0 roles, including same-human role selections, cannot establish INT-003 independence |

Reproducible GitHub locations:

- [Fixed tree](https://github.com/yohi/chatgpt-mcp-tunnel/tree/ac462699e0b1988eda63ea3d6dacfc2a030bb822).
- [PR 14](https://github.com/yohi/chatgpt-mcp-tunnel/pull/14),
  [PR 15](https://github.com/yohi/chatgpt-mcp-tunnel/pull/15).
- [PR 13 human review](https://github.com/yohi/chatgpt-mcp-tunnel/pull/13#pullrequestreview-5529960691).
- [Fixed G0 unsigned record](https://github.com/yohi/chatgpt-mcp-tunnel/blob/ac462699e0b1988eda63ea3d6dacfc2a030bb822/.omo/drafts/aws-mcp-sts001-investigation-b-g0-final-decision-record-unsigned.md):
  SHA-256 `e9eb28c665f8e8cb348b7f3e4d6f50c32f300d145c89182a05c8aedfc50a1bb0`,
  computed from the fixed Git blob, not a historical PR-body hash.

N0 references SEC04 feasibility/policy ZIPs that are not part of the N1 handoff.
Their source records are historical claims here; their internal evidence was
not recovered or independently revalidated in N1. No finding is closed from them.

## 5. Required authority recovery or prospective adoption

Custodian must supply, through an existing trusted private channel, immutable
originals and authenticated event receipts with role/delegation evidence.
Do not paste identity records, private audit data or secrets into public GitHub
or chat. If historical records cannot be recovered, use the explicit prospective
case in [the unsigned adoption record](04_N1_Owner_Adoption_Record_UNSIGNED.md).
It creates no historical approval and cannot become effective merely by saving
this packet. N1 ends with `NORMATIVE_BASELINE: NOT_VERIFIED`.
