# Investigation B - G0 independent static-review handoff

## 1. Review assignment and authorization boundary

Review the [unsigned G0 packet](aws-mcp-sts001-investigation-b-g0-approval-packet-unsigned.md)
in a separate independent session. This handoff requests document-only review,
not G0 approval, execution, human identity certification or evidence acquisition.
The preparation author does not act as the independent reviewer.

```json
{
  "document_status": "DRAFT_UNSIGNED_NOT_AUTHORIZED",
  "plan_status": "PLAN_PREPARED_PENDING_EXECUTION_APPROVAL",
  "g0": "G0_NOT_AUTHORIZED",
  "p0": "P0_NOT_EXECUTED",
  "gate_sts001": "Gate STS-001 NOT VERIFIED",
  "independent_packet_review": "PENDING",
  "decision": "UNDECIDED",
  "aws_api_count": 0
}
```

Do not run AWS API/STS/CLI/SDK, resolve providers, inspect AWS original config,
credentials, environment, login/SSO caches or network/execution environment.
No Docker, IAM changes, Broker/wrapper implementation, P0 Todo execution,
acquisition input extraction, evidence-case writes/deletion or GitHub writes.
Do not commit/push/create PRs. Do not inspect/create proposed storage roots.
Use only approved documentation and offline generated-document checks.

## 2. Immutable reference set and provenance

Repository `yohi/chatgpt-mcp-tunnel`; branch
`feat/aws-broad-iam-read-api-tools`. On 2026-10-15, GitHub branch and local HEAD
both were `9b6b1bca6ee089b1e1a10bcfc5139eb7bf1f9843`.
PR #11 merged at `2026-10-15T03:14:30Z` into that branch with that merge SHA;
PR #10 toward master remained open. Neither is an execution grant.
Historical code reference remains `05f4b92e7ff2de76dc79cf8d5dc9f563a03af209`.
Do not replace fixed code/baseline evidence with current branch content.

| Source | Exact SHA-256 |
| --- | --- |
| Preparation ZIP | `45c2c767fdf988e22004ac622b35a11ccb14fc335424dd19b4d7ebb1bc383f07` |
| P: `.omo/plans/aws-mcp-sts001-investigation-b.md` | `15a9adad32011a6f1f660875d877c25092afc8eaa38a8c6a4b2486c1c451b9b1` |
| D: `.omo/drafts/aws-mcp-sts001-investigation-b.md` | `a0d9d175e1c280bee1eab856783bf356c5cde33dd2383fc591395f68c79771c6` |
| C: `.omo/drafts/aws-mcp-sts001-investigation-b-r1-changes.md` | `88b46081efe54c40175b610ec98019642e941acd543960b05d4376a3fa3bf2c8` |
| R: ZIP `reference/R1_INDEPENDENT_DOCUMENT_RECHECK.md` | `cfaba82988d6e87c7b53aba18bd19bd2a35b820a7f1af2fe8225883948d6c3fe` |

Preparation checked all seven ZIP members via CRC, all six SHA256SUMS entries
and read README_FIRST/00_AGENT_PROMPT in full, without extraction. There was
no supplied external expected ZIP digest/signature; recorded hash is measured
identity, not independently authenticated publisher provenance.
P/D/C raw GitHub bytes at the pinned SHA matched the respective attached copies
and expected digests, with 1009/100/115 lines. P and D were read in full, as were
C and R. R is an attached reference, not a file in the pinned GitHub tree.
Original-document absence/hash mismatch must produce
`BLOCKED_REFERENCE_INTEGRITY`; do not reconstruct or substitute another HEAD.

The packet's source index covers P L169-217 (approval), L219-278 (discovery),
L365-449 (isolation/attestation), L453-585 (evidence/lifecycle), L587-624 (stops),
L645-675 (OD mapping), L682-721 (handoff), L742-786 (P0 tasks).
Check actual wording and line numbers, not just this index.
P/D/C's then-pending recheck and R's later document-only acceptance have
different timestamps/provenance. R supersedes CONDITIONAL_ACCEPT only for
document acceptability, not operational prerequisites or execution consent.
R0 diff/table checks in R are reviewer-reported and not rerun by preparation.

## 3. Required independent review questions

| Topic | Review question / expected boundary | Normative source |
| --- | --- | --- |
| OD-01 | Are operator name, verified ID, contact and scope explicitly pending, with no author self-appointment? | P L173/L652/L672 |
| OD-02 | Does local authority need verification and an attributable exact-scope event? If same person, are authority and distinct approval still required? | P L185-217/L653 |
| OD-08 initial | Are both existing human extractor and separately approved minimized input selectable, with ID/digest pending and original config outside AI? Is no-safe-choice blocked? | P L225-249/L659 |
| OD-09 | Are exact canonical root, custodian, ACL/encryption, Git/sync/backup exclusion future human decisions, with no real-root inspection claimed? | P L455-477/L660 |
| OD-10 | Are review, actual expiry, escalation, custodian/backup, independent deletion scope and hold process required per class before any operational write? | P L538-585/L661 |
| Class coverage | Are originals, aliases/salts, transient/input/filter, QA/audit, candidate/local approved share, recipient copies and approval/deletion records covered? Does NOT_CREATED_NO_WRITE forbid future creation until approval? | P L547-562 |
| Lifecycle edge cases | Does expiry follow prior exact standing authority despite no fresh reply, while valid hold and deletion failure remain distinct? Are audit custody and residual copies protected without invented deletion grants? | P L564-585 |
| G0 grain | Are case/stage/scope/revision/digest, input/tool paths, metadata whitelist, identities, channel/authority, time/expiry, root/lifecycle and stops present but unsigned? Are AWS calls/budget zero? | P L192-217/L290/L319 |
| Timing | Are OD-01/02/08 initial/09/10 pre-G0, full selected-mode OD-08 and OD-03/04/11 pre-G1, and observed baseline adoption post-P1/G1b? | P L668-675 |
| Actual mode proof | Do both modes require actual chosen-mode provider/request-path attestation, no refresh/issuance, one physical attempt, synthetic failures and real-boundary equivalence? No live identity bootstrap? | P L412-449 |
| Scope fidelity | Are 862 unapproved, later grants independent, baseline/findings/SAR unchanged, role reuse and Broker implementation excluded? | P L98-128/L315-363/L677-680 |
| Approval authenticity | Are blank signatures/default UNDECIDED retained? No inferred authority from past PR approvals, document creation, account ownership or broad "proceed" wording? | P L185-217 |

Specifically attempt these failure readings: unknown approver interpreted as
owner approval; AI opening original config to resolve metadata; first QA write
before lifecycle consent; hash mismatch silently ignored; synthetic filtering
promoted to Mode A/B GO; expired grant reused; G0 treated as G1 or G1b; approval
record deleted before audit; absent review reply treated as indefinite hold.
Each must be rejected explicitly by the packet. Report material ambiguities
instead of inventing missing owner decisions.

## 4. Finding and verdict protocol

Use the following finding fields in the independent review response; no new
operational evidence files are requested:

```text
finding_id: IB-G0-DOC-NNN
severity: HIGH | MEDIUM | LOW
packet_path_and_lines:
normative_reference_path_digest_and_lines:
observation_or_exact_excerpt:
contradiction_or_missing_field:
affected_gate_or_owner_decision:
required_document_correction_or_human_decision:
status: OPEN | DOCUMENT_CORRECTED_OPERATIONAL_UNVERIFIED
```

Allowed document-review outcomes:

- `ACCEPTED_FOR_HUMAN_G0_DECISION_CONSIDERATION`: static packet is complete as
  an unsigned proposal; owner answers/signature remain pending. Not execution.
- `REVIEW_REQUIRED`: material ambiguity, contradiction or missing contract field;
  list findings without operational remediation.
- `BLOCKED_REFERENCE_INTEGRITY`: required original unavailable/hash mismatch;
  identify exact failed reference and stop, without alternate-source substitution.

Do not certify the author's or human's identity, approval authenticity,
isolation, production signing path, storage protection, retention enforcement,
AWS identity, effective IAM permissions or evidence completeness from text QA.
Do not close IB-PLAN operational boundaries, F-004/F-006 or Gate STS-001.
No review verdict grants G0. Later human approval requires exact verified
operator/approver, authority, digest-bound scope, channel event and validity.

## 5. QA evidence and human handoff

Preparation QA is limited to the two generated Markdown files: JSON parsing,
required statuses/OD/lifecycle fields, line-bound references, relative document
links, ASCII/no machine-specific absolute paths, and SHA-256. The delivery
summary contains actual command results and both final hashes. Recompute them
from delivered bytes before review; any edit requires a new digest. Neither
file carries its own self-referential hash. This is not P0 fixture QA and does
not create a case/audit receipt outside these two planning documents.

Review receipt should identify reviewer/session, exact packet digest, original
digests, checks actually run/not run, findings and one of section 4's verdicts.
Independent review of this new packet has not been performed by its author.

Human next decisions are OD-01 verified operator, OD-02 attributable local
authority, OD-08 initial safe metadata selection, OD-09 canonical root/custody,
OD-10 all allowed classes' lifecycle/deletion/hold instructions, followed by
an explicit exact-scope G0 event through a trusted channel if the human chooses.
Full mode/source/request-path proof, endpoints/budgets and G1 remain later
conditions; G1b requires actually observed P1 source and separate adoption.

Stop with `PLAN_PREPARED_PENDING_EXECUTION_APPROVAL`, `G0_NOT_AUTHORIZED`,
`P0_NOT_EXECUTED`, `Gate STS-001 NOT VERIFIED`. G1-G5, G1b and G5-release remain
NOT_AUTHORIZED. Do not transition to P0.
