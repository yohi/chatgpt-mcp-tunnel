# 01 — Normative Source & Authority Register

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


## 1. Evidence classification

- **V-BYTE**: independently rehashed exact local source bytes. Proves submitted-copy integrity, not official adoption.
- **V-GIT**: fetched a named GitHub Git object/ref at the exact fixed commit; Git *blob SHA-1* is not a SHA-256 digest or approval signature.
- **D-RECORDED**: declaration in submitted material, without independent authority validation.
- **PENDING**: source, identity, authority, or event not established; never infer approval.
- **CANDIDATE / DRAFT**: exists as text but is not effective normative source.

## 2. Main source register

| ID / file | Role; revision | SHA-256 of checked bytes | Origin/chain | Authority / adoption |
|---|---|---|---|---|
| B1 `01-fixed-baseline-v1.0.md` | Requirements v1.0, REQ-001–044 & AC-001–020 | `39002fc2ce5f21e9e686a427c793a7fd42fc84e5bdb02684be9e1e3a4305f4bc` | R4 and Option A R1 archives, identical checked copies | **PENDING** external adopted original, owner, event |
| B2 `02-fixed-baseline-v1.1.md` | Security Requirements Addendum v1.1, REQ-045–049, AC-021–024, B2-S1 | `3078acc5c31b5e900697dbb585e5ed604dfca89fe82b56cfc9528ac3c91350e2` | R4 and Option A R1 archives, identical checked copies | **PENDING** external adopted original, owner, event |
| B3 `03-fixed-decisions-Q33-Q40.md` | User decisions Q33–40 summary | `f287966ac61f467704f99c545f2d7a9756b9f21a70a5f90a814367ab7a113aa4` | R4 and Option A R1 archives, identical checked copies | **PENDING** authenticated decision events (summary alone insufficient) |
| R4 `04-normative-reconciliation-rev4.md` | Reconciliation R4 candidate | `4582d85fec1c403854e4fa4f2b4010d0fb2254290f57fe6f01b273a8b146798b` | R4 ZIP | `REVISION_CANDIDATE / OWNER_DECISION_PENDING` |
| R4 `05-nonregression-matrix-rev4.md` | 49 REQ / 24 AC traceability, proposed nonregression | `8c6ce4ea0ac06adc0d4aa6d89dc3293e329ac16051aece5ee205cabb3c1e78b8` | R4 ZIP | Analytical candidate, not adopted |
| R4 `06-security-requirements-rev4.md` | Candidate REQ-050–059 | `ffd47e848e8bba76a39f2732d92f6b8ba7cff652939e8d4fb6653604e84abb6f` | R4 ZIP | Candidate, **NOT ADOPTED** |
| R4 `07-acceptance-rev4.md` | Candidate AC-025–036 | `501874cc568350f224aad45b45f09dc1e746ec6f10e9e5796baf4c27ad21dcc7` | R4 ZIP | Candidate, tests **NOT EXECUTED** |
| R4 `08-owner-decision-request.md` | Requirements Owner R4 decision request | `021f2ca95d6f769881150bc00df067692eccc0cb3fc174a567fe3f83fa255d90` | R4 ZIP and Option A R1 ZIP | `PENDING / NOT_APPROVED` request, not event |
| Option A R1 `01-owner-decision-record-option-a-limited-correction-r1.md` | 3-clause proposed adoption; R1 static correction | `92cef5b23ca9696ede0c9a6d5ca979056c20b6c17853598afcf6af914f60865e` | Option A R1 ZIP | Correction accepted; ratification **PENDING / NOT_EFFECTIVE** |
| Attestation `aws_mcp_broker_v11_owner_approval_attestation_20261014(1).md` | Requirements Owner intent; proposed ODR | `5b9fd27668d7a47cfeff5c09fc6aae79decbd5929b159e953b7274ce4355c34a` | Prior ChatGPT Library upload | `OWNER_APPROVAL_INTENT_RECORDED`; authenticated adoption absent |
| `AWS_MCP_STS001_Broker_Security_Contract_Draft_20261014.md` | Gate STS-001 security design contract proposal, 2026-10-14 | `0cc08ad3a1970be2ba4a73e47240d96fc9300afb5747da48db2d2bd9bdac102c` | Prior ChatGPT Library upload, pinned historical code reference | Explicitly **DRAFT / NOT APPROVED** |
| `Independent_Feasibility_Report.md` | Independent static SEC04 review, 2026-10-14 | `4243627dffe205334cd093bbb43401ddf6dbb77e32348f233251b748eb0b8e08` | Feasibility ZIP | Conditional feasibility/no-go; not specification adoption |
| `08_Review_Report.md` | SAR/policy evidence R2 2026-10-15 | `b3fbb91396b8e81193614700794be48d4e74c6819d2b9d6aa2e1044c4cd495bc` | Policy evidence R2 ZIP | F-002/003 OPEN_PARTIAL in this archival snapshot; not approval |
| `.omo/plans/aws-mcp-sts001-investigation-b.md` | Investigation B planned stages, not Broker Design | *NOT CALCULATED* (fixed Git blob `f4ef99a15636db044eeb2da18c6e0423fc75fcb1`) | [.omo/plans/aws-mcp-sts001-investigation-b.md](https://github.com/yohi/chatgpt-mcp-tunnel/blob/ac462699e0b1988eda63ea3d6dacfc2a030bb822/.omo/plans/aws-mcp-sts001-investigation-b.md) | Plan only, P0/G0 not approved |
| `.omo/drafts/aws-mcp-sts001-investigation-b-g0-final-decision-record-unsigned.md` | G0-FINAL-CANDIDATE-1 | *NOT CALCULATED* (fixed Git blob `b4ab1d65ad9fc8bed7ed87a098b8abee737a7a28`) | [.omo/drafts/aws-mcp-sts001-investigation-b-g0-final-decision-record-unsigned.md](https://github.com/yohi/chatgpt-mcp-tunnel/blob/ac462699e0b1988eda63ea3d6dacfc2a030bb822/.omo/drafts/aws-mcp-sts001-investigation-b-g0-final-decision-record-unsigned.md) | `DRAFT_UNSIGNED_NOT_AUTHORIZED` |
| Full Broker technical Design authority original | **UNKNOWN**, revision UNKNOWN | **NOT_AVAILABLE** | Not present as approved artifact in inspected fixed-tree or R4/R1 packages | **PENDING** source custodian + Owner event |
| Full approved v1.1 AC/security policy integration | **UNKNOWN**, revision UNKNOWN | **NOT_AVAILABLE** | B1/B2 are source copies, R4 additions are candidates | **PENDING** formally merged/adopted canonical text |

## 3. Archive byte-integrity evidence (independent in N0)

| Input | SHA-256 | ZIP CRC | Internal SHA256SUMS |
|---|---|---|---|
| `aws-mcp-broker-v1.1-normative-reconciliation-rev4 (1).zip` | `cd9611654f17d5eee73d47d5d32ce6d94459c24016c2dc3a1a157f90fbd8a15c` | PASS | 14/14 MATCH |
| `aws-mcp-broker-v1.1-option-a-limited-correction-r1(1).zip` | `cedf39f04a1733e42fe00e22f9c262a0bd5ad62a682a6ee50efdced287e85912` | PASS | 13/13 MATCH |
| `AWS_MCP_STS001_SEC04_POLICY_Evidence_Acquisition_R2_20261015.zip` | `846ffe1e79852e6a50a70d417e0e64266413897de84ef3203319ca5cf615bbe4` | PASS | 19/19 MATCH |
| `AWS_MCP_STS001_SEC04_Independent_Feasibility_20261014.zip` | `c049372a49be3656b866eaa75047aa3bf72eec05f8e569c3dd54e039f917e862` | PASS | 7/7 MATCH |

The three B1/B2/B3 byte streams in R4 and Option A R1 are mutually identical. They are **submitted text snapshots**, not yet authenticated originals. We did not contact an AWS endpoint; policy R2 has historical acquisition limitations. A later assertion of raw SAR acquisition requires its actual manifest and original bytes for independent validation before changing any F-002 disposition.

## 4. Git evidence and code provenance

- Repository tree listing at `ac462699e0b1988eda63ea3d6dacfc2a030bb822` reported `truncated=false`, and contains no files explicitly named as a full approved v1.1 Requirements, full Design, full AC, or approved Security Contract.
- [PR #14](https://github.com/yohi/chatgpt-mcp-tunnel/pull/14): merged as `8f4c7c880d74c44e640d6ea3a423e167c942b051`, isolated experiment, four added files.
- [PR #15](https://github.com/yohi/chatgpt-mcp-tunnel/pull/15): merged as `ac462699e0b1988eda63ea3d6dacfc2a030bb822`, modified only `experiments/aws_mcp_broker_v11_offline/validation.py` and `tests/test_aws_mcp_broker_v11_offline.py`.
- `validation.py` Git blob SHA-1 `07aaa67cfd80a24aef83c5dc6e1d7cf2becd1d82`; test blob SHA-1 `5c9371458b4f518958602691f8ca0b393ae7999b`. **Do not mislabel these Git IDs as SHA-256.**
- PR #14/#15 claims and reported I1 finding closures concern synthetic structural tests only; no real AWS authorization or normative compliance proof.
- Code entrypoint for legacy issuer: [scripts/aws-mcp-credential-broker.py](https://github.com/yohi/chatgpt-mcp-tunnel/blob/ac462699e0b1988eda63ea3d6dacfc2a030bb822/scripts/aws-mcp-credential-broker.py), Git blob `db2a966b6542803d9ce775953f6cc888b191e7d4`.

## 5. Minimum retrieval/authority chain required

1. Identify an authorized original custodian and official storage for B1/B2/B3 and the standalone Design, Acceptance Criteria, Security Contract. Capture canonical URI/repository, immutable version/commit, exact bytes and SHA-256, creation/revision timeline.
2. For each original, obtain an **independently attributable** actual adopter, decision body/role grant, authenticated event ID/URL and UTC timestamp; compare covered text and SHA-256 to the recovered candidate. Do not backdate.
3. Establish which B1/B2/B3 artifacts are approved vs historical summaries and which R4/Option A R1 texts are only candidate. Resolve missing revision chain and any later adopted edits without overwriting the old originals.
4. Obtain the canonical full Design and independent post-adoption Normative Review only after ratification. Leave `NOT_VERIFIED` if unavailable.
5. Sign/evidence-bind an I2 implementation scope decision separately; **no GitHub PR merge implies any of these steps**.

## 6. Source authority conclusion

**`NORMATIVE_BASELINE: NOT_VERIFIED`**. Evidence supports versioned copies and a human-expressed direction, not a complete authenticated adopted baseline.
