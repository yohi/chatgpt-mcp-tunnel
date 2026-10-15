# Investigation B - R1 controlled document changes

## Status and authorization

- Plan status: `PLAN_PREPARED_PENDING_EXECUTION_APPROVAL`.
- Supplied independent R0 verdict: `CONDITIONAL_ACCEPT`.
- R1 corrects IB-PLAN-001..004 in planning documents only.
- G0-G5, G1b and G5-release remain separately gated and NOT_AUTHORIZED.
- No AWS environment, credential provider, isolation, network path or retention
  mechanism was tested. Gate STS-001 remains NOT VERIFIED.
- In-session read-only static correction review passed all four textual items.
  The original independent reviewer has NOT rechecked R1; do not lift its
  conditional verdict or claim operational conditions closed on that basis.

## Controlled artifact identities

| Artifact | Revision | Logical lines | SHA-256 |
| --- | --- | ---: | --- |
| Plan | R0 reviewed | 861 | `11ce1cae1fc7f209f472c3e9ba0b696019ba1b64fe142ab72abd2822072fe1f9` |
| Plan | R1 | 1009 | `15a9adad32011a6f1f660875d877c25092afc8eaa38a8c6a4b2486c1c451b9b1` |
| Decision record | R0 reviewed | 88 | `2395a5e388f2e40bce459482a616459d2614659fb74f202326f5e69f2b69a363` |
| Decision record | R1 | 100 | `a0d9d175e1c280bee1eab856783bf356c5cde33dd2383fc591395f68c79771c6` |

Paths: `.omo/plans/aws-mcp-sts001-investigation-b.md` and
`.omo/drafts/aws-mcp-sts001-investigation-b.md`. The supplied reviewed download
names are matched by R0 hash, not by assuming their parenthesized names are
local authoritative paths. This change record does not alter either artifact.

## Limited R1 diff - disposition and exact locations

| Item | Correction | Principal R1 locations |
| --- | --- | --- |
| IB-PLAN-001 | Original config and process environment remain outside AI; existing trusted human extractor or separately approved sanitized metadata only; otherwise P0_CONFIG_DISCOVERY_BLOCKED. Parser fixtures are filtering tests, not production isolation proof. | Plan 225-249, task 2 at 763-788, handoff 717-721; decision record 32-33 |
| IB-PLAN-002 | BOTH modes require attributable source-provider/request-path GO before G1: effective provider category, refresh/assume blocking, endpoint/proxy/redirect control, runtime/config provenance, one physical attempt and independent accounting, offline failure fixtures plus production-boundary equivalence attestation. Unknown/unobservable means no identity probe. | Plan 173-217, 339-356, 413-449, task 2/3 at 763-805; decision record 34-35 |
| IB-PLAN-003 | Choose the review's FIRST alternative: OD-02 explicitly applies to G0 AND AWS gates. Verified same approver needs local-scope authority and signs exact local scope; operator consent alone fails. No additional approver role is inferred. | Plan 173, 185-190, 653, 668-675; decision record 32-33 |
| IB-PLAN-004 | Before first operational case write, approve per-class review deadline, actual expiry, escalation/custodian and standing deletion authority. Cover all evidence classes. Missing review reply does not defer preauthorized expiry deletion; legal hold is an attributed exception, failed deletion is RETENTION_BREACH. This plan grants neither writes nor deletion. | Plan 466-477, 538-585, 604-605, 661, 668-675, task 1 at 742-761, task 12 at 933-955; decision record 36-37 |

The following is an **exact unified-diff hunk index**, not an executable patch
or the full changed text. Each tuple is `R0 start,count -> R1 start,count`,
including one context line on each side where available. The verifier computed
it using Python difflib only AFTER reconstructing R0 in memory by reversing
the known R1 replacements and matching BOTH reviewed R0 hashes exactly.
The full diff is 29,634 characters; the complete R1 files remain the normative
text. Independent reviewers with R0 can reproduce the full comparison without
AWS/config/credential access.

```text
PLAN  33,2 -> 33,6
PLAN  168,4 -> 172,4
PLAN  179,2 -> 183,9
PLAN  191,2 -> 202,7
PLAN  208,23 -> 224,27
PLAN  250,3 -> 270,4
PLAN  329,2 -> 350,8
PLAN  384,2 -> 411,40
PLAN  399,3 -> 464,10
PLAN  465,16 -> 537,50
PLAN  495,2 -> 601,6
PLAN  522,3 -> 632,3
PLAN  542,5 -> 652,5
PLAN  548,5 -> 658,5
PLAN  556,2 -> 666,16
PLAN  592,2 -> 716,7
PLAN  616,3 -> 745,5
PLAN  623,6 -> 754,8
PLAN  630,4 -> 763,5
PLAN  640,3 -> 774,5
PLAN  645,3 -> 781,6
PLAN  657,3 -> 796,5
PLAN  702,3 -> 843,4
PLAN  794,3 -> 936,5
PLAN  803,3 -> 947,7
DRAFT 7,2 -> 7,3
DRAFT 30,2 -> 31,8
DRAFT 61,2 -> 68,7
DRAFT 85,3 -> 97,3
```

## OD / G0 eligibility

| Timing | Decisions and gates | Incomplete result |
| --- | --- | --- |
| Before G0 sensitive local execution | OD-01 operator; OD-02 local-authority approver and attributable G0 scope; OD-08 initial human-only/trusted extraction mode; OD-09 roots/custodian; OD-10 per-class lifecycle/deletion authority before any operational write | G0 NOT_AUTHORIZED; no case write or secret-bearing local access |
| During separately authorized P0, before G1 | OD-04 effective source validity/provider/request-path GO; OD-08 full chosen mode proof; OD-03 STS/IAM Regions/endpoints; OD-11 P1 physical-attempt/cost bounds; fresh G1 grant | No AWS call, including GetCallerIdentity |
| After P1, before G2 | G1b human principal-baseline adoption and separate G2 scope | No P2-P4 calls |
| May remain pending at G0 | Later ECS/resource scopes, comparison baseline, independent recipient/reviewer, out-of-scope role reuse and cross-account investigation | No later-stage permission inferred; sharing requires OD-14 and G5-release |

## Offline verification receipts and limits

- Python 3 standard-library verifier: final structural run exit code 0.
  Eight major headings in template order; numbered tasks 1-12 and F1-F4 in
  correct sections; nine planning deliverables, ten future output files; ASCII,
  no machine-specific absolute paths and pending statuses checked.
- Reconstructed R0 identity matched both reviewed SHA-256 values. API candidate
  table and numeric request-budget table were compared separately, byte-exact
  unchanged. Numeric ceilings remain 0/2/60/200/600/0, total 862, all unapproved.
- Current API-table extracted digest:
  `eb7a973b75d92d5ead168cedb03163026c48e78373096e591c8fb01741d838be`.
- Current numeric-budget-table extracted digest:
  `c2c98a3ad02ef13524597fadf215ca44b6adaed47edd854abe72fa87f8d048ef`.
- Earlier inverse-anchor and table-extraction attempts failed; no success was
  inferred from those. Corrections affected the read-only verification logic,
  not plan contents. Final narrow table comparisons and structure assertions
  were reported separately. These are static text checks, not acquisition QA.
- Separate read-only Metis correction review accepted all four textual changes.
  Its initial request to support BOTH local-approver alternatives was withdrawn
  after checking the literal EITHER/OR requirement. No unnecessary scope change
  was made to satisfy that misreading.
- Fixed baseline, findings and SAR originals were not edited or newly inspected.
  No API candidate, Region scope, operational budget grant, wrapper/Broker
  implementation or deletion authorization was added.

Next action: independent document-only R1 recheck. Operational source-provider,
network/isolation, storage and approvals remain NOT PERFORMED / NOT VERIFIED.
Stop; do not transition to P0 or AWS execution.
