# Investigation B G0 Approval Packet - DRAFT UNSIGNED, NOT AUTHORIZED

## 1. Status and purpose

This is an unsigned Owner Decision Packet for human consideration, prepared on
2026-10-15. It records no approval event and grants no execution or deletion
authority. The preparation agent is neither operator, approver, custodian nor
independent reviewer. Blank signature fields are intentional.

```json
{
  "document_status": "DRAFT_UNSIGNED_NOT_AUTHORIZED",
  "plan_status": "PLAN_PREPARED_PENDING_EXECUTION_APPROVAL",
  "decision": "UNDECIDED",
  "approval_state": "APPROVAL_PENDING",
  "g0": "G0_NOT_AUTHORIZED",
  "p0": "P0_NOT_EXECUTED",
  "later_gates": "G1-G5/G1b/G5-release NOT_AUTHORIZED",
  "gate_sts001": "Gate STS-001 NOT VERIFIED",
  "aws_api_count": 0,
  "operational_validation": "NOT_PERFORMED / NOT_VERIFIED"
}
```

Preparation changes only this document and the companion
[independent-review handoff](aws-mcp-sts001-investigation-b-g0-independent-review-handoff.md).
These are planning artifacts, not operational evidence-case files (R1 plan
L465-470). No P0 acquisition ZIP extraction, case creation, source inspection,
fixture execution or AWS evidence acquisition occurred.

## 2. Reference integrity and distinct commit identities

Repository: `yohi/chatgpt-mcp-tunnel`.
Integration branch: `feat/aws-broad-iam-read-api-tools`.
Read-only GitHub branch lookup and local HEAD both returned
`9b6b1bca6ee089b1e1a10bcfc5139eb7bf1f9843` on 2026-10-15.
GitHub PR [#11](https://github.com/yohi/chatgpt-mcp-tunnel/pull/11) reports
`merged=true`, merge time `2026-10-15T03:14:30Z`, that merge commit and the named
integration branch as base. This verifies document integration, not G0 consent.
PR #10 remains open toward master; no master integration is asserted.

The historical **code reference**, not today's branch HEAD, remains
`05f4b92e7ff2de76dc79cf8d5dc9f563a03af209` (plan L71-105).
No code or baseline is substituted from the newer HEAD.

| ID | Source and provenance | SHA-256 | Result |
| --- | --- | --- | --- |
| ZIP | `AWS_MCP_STS001_G0_Approval_Preparation_Handoff_20261015.zip` | `45c2c767fdf988e22004ac622b35a11ccb14fc335424dd19b4d7ebb1bc383f07` | Computed; external expected digest/signature NOT_SUPPLIED |
| P | `.omo/plans/aws-mcp-sts001-investigation-b.md` | `15a9adad32011a6f1f660875d877c25092afc8eaa38a8c6a4b2486c1c451b9b1` | GitHub pinned HEAD = attached R1_EXECUTION_PLAN, 1009 lines |
| D | `.omo/drafts/aws-mcp-sts001-investigation-b.md` | `a0d9d175e1c280bee1eab856783bf356c5cde33dd2383fc591395f68c79771c6` | GitHub pinned HEAD = attached R1_DECISION_RECORD, 100 lines |
| C | `.omo/drafts/aws-mcp-sts001-investigation-b-r1-changes.md` | `88b46081efe54c40175b610ec98019642e941acd543960b05d4376a3fa3bf2c8` | GitHub pinned HEAD = attached R1_CHANGE_REGISTER, 115 lines |
| R | ZIP `reference/R1_INDEPENDENT_DOCUMENT_RECHECK.md` | `cfaba82988d6e87c7b53aba18bd19bd2a35b820a7f1af2fe8225883948d6c3fe` | Attached reference, 71 lines; not present in pinned GitHub tree |

GitHub originals were fetched as raw bytes with `gh api .../contents/<path>?ref=<full-SHA>`
and the raw media Accept header, hashed in memory and compared byte-for-byte
against the attachments. P and D were read in full; equality establishes that
the fully read attached text is identical to the pinned GitHub originals.
C and R were also read in full. No reconstructed text was used.

ZIP inspection used Python standard-library `zipfile` and `hashlib` in memory,
without extraction: `testzip()` returned `None` (all seven members' CRC checks
passed), and all six entries in internal `SHA256SUMS` matched. Both
`README_FIRST.md` and `00_AGENT_PROMPT.md` were read in full. Internal hashes and
CRC establish consistency, not publisher authenticity or human authorization.

### R1 source index (line numbers of the exact pinned plan P)

| Required topic | Plan lines | Binding point |
| --- | --- | --- |
| Stage Approval Matrix | L169-190 | G0 local authority; each subsequent grant independent |
| Approval Record | L192-217 | Exact digest-bound scope, identities and expiry |
| Region / Resource Discovery | L219-278 | Human trusted boundary; candidates never authorized Regions |
| Credential Isolation | L365-410 | Existing Mode A only if proven; otherwise controlled Mode B |
| P0 source-provider/request-path attestation | L412-449 | Actual selected mode GO required before G1 |
| Evidence / Retention | L453-585 | No case write before storage and class lifecycle authority |
| Stop Conditions | L587-624 | Stop, no fallback, no silent extension |
| Owner Decision Register | L645-666 | OD-01 through OD-15 remain open |
| OD/G0 eligibility mapping | L668-675 | Separates pre-G0, pre-G1 and post-P1 decisions |
| P0 Todo 1 | L742-761 | Future input/storage readiness, not executed here |
| P0 Todo 2 | L763-786 | Future candidate metadata and isolation evidence |
| Executor handoff | L682-721 | Receipt/checklists are not execution approval |

Direct governing excerpts: P L185-190 says "Operator consent alone is
insufficient" and "A decision-register entry is not an approval record."
P L465-470 requires approval "Before ANY operational case-owned file write".
P L446-448 requires "NO AWS calls, including GetCallerIdentity" without the
attestation; a GO itself does not approve G1.

D L30-41/L69-73/L93-98 retain pending execution and distinguish textual fixes
from operational proof. C L33-36 maps IB-PLAN-001..004; C L83-86 agrees with
P L672-675. C L11-13/L113-115 describes the then-pending independent recheck;
R L5/L67-71 subsequently accepts document consideration only. This chronology
does not amend P, establish an approval event or close operational findings.
R's R0 comparison and table-equality statements remain that reviewer's reported
results; this preparation did not independently rerun the R0 comparison.
The unchanged 862 ceiling is a proposal, not a grant (P L315-363; R L60-65).

## 3. Pre-G0 Owner Decision Questions - all UNDECIDED

Selection fields below are proposals; no name, authority, date or actual path
is inferred from repository ownership, login identity or personal development.
The named owner roles themselves still require attributable human assignment.

| Decision | Choices for human selection | Required human evidence / authority | Current hold and basis |
| --- | --- | --- | --- |
| OD-01 | Identify a human operator; nominate another qualified human; defer | Human organization: name, verified ID, verification method/reference, contact channel, exact local scope and consent | `IDENTITY_PENDING`; P L173/L652/L672 |
| OD-02 | Verify execution approver's G0 local authority; same person as operator with independent approval act and documented authority; defer/deny | Account/local authorization authority: verified ID, local-scope authority evidence, trusted attributable approval event bound to exact digest and expiry; AWS authority cannot be inferred | `APPROVER_AUTHORITY_PENDING`; P L185-217/L653/L672 |
| OD-08 initial | Existing human-managed trusted extractor; separately approved minimized candidate-metadata input; neither safe option | Security/execution custodian: selected mode, ID/version/digest, approved input/output scope and human-only original boundary | `P0_CONFIG_DISCOVERY_BLOCKED` until safe choice approved; P L225-249/L659/L672 |
| OD-09 | Human nominates a canonical external root and custodian; revise proposed location; defer | Data custodian: exact normalized root, filesystem/mount provenance, ownership, parent traversal, ACL/default ACL, encryption and Git/sync/backup exclusions; human-approved proof reference | `STORAGE_AUTHORITY_PENDING`, protections `NOT_VERIFIED`; P L455-477/L660 |
| OD-10 | Approve lifecycle for each allowed class; prohibit absent class via NOT_CREATED_NO_WRITE; defer | Data owner and authorized audit custodian: per-class dates, uses, custodian/backup, independently attributable case-limited standing deletion and legal-hold authority | `OWNER_DECISION_PENDING` and `P0_CASE_WRITE_BLOCKED`; P L538-585/L661 |

### OD-08 candidate metadata selection

`selection=UNDECIDED`; every candidate below is `PROPOSED_NOT_APPROVED`.
The extractor must already exist and remain human-controlled; this task creates
no extractor, wrapper or Broker. Alternative input must be independently
approved sanitized metadata, not a renamed or filtered original config file.

Human completion fields: extractor/input ID, version, SHA-256, exact human-only
input locator, sanitized-input locator/digest, provenance, allowed recipient,
inspection authority and trusted approval event: all `PENDING`.

Output whitelist proposed from P L236-253: `source` (approved nonsecret
provenance only), `candidate_region`, `candidate_sts_mode`, `conflict`,
`observed_local_utc`, `authorization_state=NOT_AUTHORIZED`; where applicable,
only boolean `OVERRIDE_PRESENT_REQUIRES_HUMAN_REVIEW`. Unknown/default-derived
or conflicting values remain candidates/UNKNOWN. No config sections, provider
commands, URLs/userinfo/query strings, environment dumps, credentials or cache
contents enter the AI boundary. Output filtering alone is not isolation proof.

### OD-09 location selection

R1's symbolic example `$HOME/local-restricted-evidence/AWS-MCP-STS001-SEC04-RESOURCE/<approved-run-id>/`
is `PROPOSED_NOT_APPROVED`, not an actual canonical root. This preparation did
not inspect or create that location. Actual normalized path, custodian ID,
backup ID, ACL/encryption method and exclusion attestations remain `PENDING`.
Reject Git worktrees, sync/backup destinations, shared/temp/cache roots,
symlinks and unresolved mounts. `.gitignore` is not evidence of exclusion.

### OD-10 class lifecycle decision sheet

Every row requires its own `review_due_utc`, `retention_expires_utc`,
`escalate_at_utc`, custodian and backup verified IDs, permitted use, exact
case-owned file/class scope, standing-deletion authority/event, legal-hold
authority/process and residual-copy disposition. `PENDING` cells are deliberate
blockers, not accepted indefinite retention. Review and escalation must precede
expiry; actual dates and ordering require human validation before writes.

| Evidence class | Creation selection | review_due_utc | retention_expires_utc | escalate_at_utc | Custodian / backup | Independent deletion / hold authority |
| --- | --- | --- | --- | --- | --- | --- |
| Raw originals | UNDECIDED; no creation now | PENDING | PENDING | PENDING | PENDING / PENDING | PENDING / PENDING |
| Aliases / mappings / salt | UNDECIDED; no creation now | PENDING | PENDING | PENDING | PENDING / PENDING | PENDING / PENDING |
| Transient / input / filter files | UNDECIDED; no creation now | PENDING | PENDING | PENDING | PENDING / PENDING | PENDING / PENDING |
| QA records | UNDECIDED; no creation now | PENDING | PENDING | PENDING | PENDING / PENDING | PENDING / PENDING |
| Audit records | UNDECIDED; no creation now | PENDING | PENDING | PENDING | PENDING / PENDING | PENDING / PENDING |
| Share-candidate copies | UNDECIDED; no creation now | PENDING | PENDING | PENDING | PENDING / PENDING | PENDING / PENDING |
| Local approved-share copies | UNDECIDED; no creation now | PENDING | PENDING | PENDING | PENDING / PENDING | PENDING / PENDING |
| External distribution copies | NOT_CREATED_NO_WRITE | PENDING | PENDING | PENDING | PENDING / PENDING | PENDING / PENDING |
| Approval records | UNDECIDED; no case write now | PENDING | PENDING | PENDING | PENDING / PENDING | PENDING / PENDING |
| Deletion receipts | NOT_CREATED_NO_WRITE | PENDING | PENDING | PENDING | PENDING / PENDING | PENDING / PENDING |

Human may select `NOT_CREATED_NO_WRITE` for any absent class, explicitly
prohibiting its creation until a new lifecycle decision. The operational input,
metadata, QA and audit classes cannot be skipped if the proposed operation
writes them. Preparation documents are not these operational case records.
Use the existing trusted approval channel before the first case write; do not
create a case approval file to bootstrap its own write authority.

At agreed escalation time, missing disposition or hold risk goes to the named
data/legal owner. At expiry without valid hold, the custodian follows the
previously independently granted exact case-limited instruction even if review
or a fresh reply is missing. Silence is not a hold or an extension. Earlier
deletion/scope changes need new authority. An authorized hold records reason,
authority, access restrictions and next review, stops collection/ordinary
processing and uses `RETENTION_EXCEPTION_LEGAL_HOLD`. Failed/blocked deletion
without valid hold means `RETENTION_BREACH`: stop collection/release, restrict
access and escalate. No deletion authority is granted here. AI cannot erase
human audit storage. Preserve authority/receipts long enough for audit under
their separately approved lifecycle. Unlink does not prove SSD/COW/backup
erasure; remote deletion cannot be asserted without verification (P L564-585).

## 4. Unsigned G0 Record proposal

Human choices: `APPROVE_EXACT_SCOPE`, `REQUEST_REVISION`, `DENY`, `DEFER`.
Default: `UNDECIDED`. No selection is made by this document.

```json
{
  "record_status": "DRAFT_UNSIGNED_NOT_AUTHORIZED",
  "decision": "UNDECIDED",
  "approval_state": "APPROVAL_PENDING",
  "case_id": "AWS-MCP-STS001-SEC04-RESOURCE",
  "investigation": "B",
  "stage": "G0",
  "scope_id_proposed": "IB-G0-LOCAL-READINESS-R1-PROPOSED_NOT_APPROVED",
  "plan_sha256": "15a9adad32011a6f1f660875d877c25092afc8eaa38a8c6a4b2486c1c451b9b1",
  "branch_head": "9b6b1bca6ee089b1e1a10bcfc5139eb7bf1f9843",
  "fixed_code_reference_commit": "05f4b92e7ff2de76dc79cf8d5dc9f563a03af209",
  "scope_revision_and_packet_digest": "PENDING_HUMAN_BINDING",
  "operator_name": "PENDING",
  "operator_verified_id": "IDENTITY_PENDING",
  "operator_contact_and_verification_reference": "PENDING",
  "approver_verified_id": "PENDING",
  "local_authority_basis": "APPROVER_AUTHORITY_PENDING",
  "authority_verification_reference": "PENDING",
  "trusted_approval_channel": "PENDING",
  "approval_event_reference": "PENDING",
  "approved_at_utc": null,
  "approval_expires_utc": null,
  "selected_initial_metadata_mode": "UNDECIDED",
  "extractor_or_sanitized_input_id": "PENDING",
  "extractor_or_sanitized_input_sha256": "PENDING",
  "exact_input_files_and_execution_paths": "PENDING",
  "executor_tool_runtime_identity_and_digest": "PENDING",
  "canonical_case_root": "PENDING",
  "custodian_verified_id": "PENDING",
  "lifecycle_record_digest_and_authority": "PENDING",
  "permitted_recipients": "PENDING_NO_RELEASE",
  "risk_exceptions": "NONE_GRANTED",
  "aws_api_count": 0,
  "aws_request_budget": 0,
  "aws_region_endpoint_grants": [],
  "source_principal_baseline": "SOURCE_PRINCIPAL_BASELINE_PENDING",
  "mode_a_b_full_proof": "PRE_G1_PENDING",
  "signature": ""
}
```

### Proposed bounded P0 operation types, only after valid G0

All entries are `PROPOSED_NOT_APPROVED`; unresolved exact locators/tool hashes
block the corresponding operation. This is no generic local shell grant.

| Type | Concrete candidate target / path to be bound by human | Candidate outputs / limits |
| --- | --- | --- |
| Input integrity / safe extraction | Acquisition input `AWS_MCP_STS001_SEC04_RESOURCE_Agent_Handoff_20261015.zip`; exact approved input file/digest and external `input/` destination PENDING | Future CRC/member safety/internal-hash results; only expected regular members, no embedded execution; this preparation did not open/extract that acquisition input |
| Reference inventory | Exact approved local reference files, fixed code reference and digests PENDING | Availability/digest only; absent references REFERENCE_NOT_AVAILABLE, no HEAD substitution |
| Candidate metadata receipt | Approved sanitized-input/extractor ID, digest and approved input/output paths PENDING | Only section 3 whitelist; source profile `aws-mcp-readonly` remains CANDIDATE_NOT_VERIFIED |
| Storage readiness | Exact canonical root and authorized `input/`, `qa/`, `audit/` paths PENDING | Human-owned ACL/mode/exclusion attestations; creation only under prior class lifecycle and exact G0 consent |
| Offline readiness / chosen-mode attestation | Existing approved verifier/human harness, synthetic fixture IDs, invocation and runtime/config digests PENDING | Network-disabled results and human configuration-equivalence attestation for actual mode; no implementation, provider invocation or live probe |

Raw original config and provider/cache/credential contents are never AI inputs.
Human custodian attestation of provider behavior is distinct from revealing
secrets. New or broader operation paths require new attributable consent.
G0 permits only the human-approved subset of these local types, never AWS calls.

Operator signature: ____________________

Execution Approver signature: ____________________

Data/lifecycle authority reference and separate grant: ____________________

Approval channel event/time/expiry: ____________________

These fields must be completed and independently validated through an existing
trusted channel, bound to final packet digest and exact scope. Their presence
as blank lines is no evidence of an event. Rehash final content before signing;
do not treat a digest of an earlier draft as approval of a changed packet.

## 5. Timing separation and remaining gates

| Timing | Required conditions | Status / consequence now |
| --- | --- | --- |
| Before G0 | OD-01/02/08 initial/09/10 plus exact attributable local scope, current digest and expiry | All pending; G0_NOT_AUTHORIZED; no P0 or case write |
| During separately approved P0 | Todo 1/2 local readiness; chosen-mode proof and human source/request-path assessment, within exact local consent | P0_AUTHORIZED_ONLY_AFTER_G0; P0_NOT_EXECUTED now |
| Before G1 | OD-04 effective existing source/provider validity and attributable actual-mode GO; OD-08 full selected A/B proof; OD-03 exact STS Region/endpoint, IAM endpoint/signing Region; OD-11 physical-attempt/API/page/resource/rate/cost bounds; separate G1 | PRE_G1_PENDING; all AWS requests prohibited |
| After P1, before G1b | Only independently approved G1 can observe the source; human adopts actually observed principal as separate baseline decision | SOURCE_PRINCIPAL_BASELINE_PENDING; no P2-P4 |
| After G1b | Separate G2/G3/G4 approvals and relevant OD-05/06/07/11/12 | NOT_AUTHORIZED; no propagation from G0 or baseline adoption |
| Processing / sharing | G5 processing; OD-14 recipient/raw-review entitlement and G5-release separately | NOT_AUTHORIZED; no evidence distribution |

Both Mode A and Mode B are subject to the pre-G1 requirement; only the actual
selected mode needs the corresponding full proof, never a Mode B exception.
Proof binds tool/runtime/config identity, effective provider category, blocked
issuance/refresh/auto-assume, endpoint/proxy/TLS/redirect controls, one physical
attempt, independent accounting, synthetic failure results and human production
boundary equivalence. Unknown or unobservable controls mean NO_GO and
`SOURCE_REQUEST_PATH_NOT_ATTESTED`. Even `GetCallerIdentity` is forbidden when
hidden STS issuance, refresh, retries or redirects cannot be excluded.
No live probe can bootstrap proof. Numeric 862 is still unapproved, not G0's
budget. G0's AWS budget is exactly zero. Role reuse, Broker implementation,
Finding closure, global no-write claims and Gate closure remain outside scope.

## 6. Stop / invalidation checklist and next human decisions

- [ ] Verify OD-01 operator identity; do not equate a GitHub username with a grant.
- [ ] Verify OD-02 local authority and a separate attributable event, including
  when operator and approver are the same person; otherwise BLOCKED_APPROVAL.
- [ ] Select safe OD-08 initial metadata boundary; any proposed AI original-config
  access means stop with P0_CONFIG_DISCOVERY_BLOCKED.
- [ ] Resolve OD-09 exact root and human protection attestations; no speculative
  filesystem inspection is permitted during preparation.
- [ ] Resolve OD-10 for each class to be written; missing dates/deletion authority
  means P0_CASE_WRITE_BLOCKED, not permission to retain indefinitely.
- [ ] Verify pinned reference hashes and source availability; mismatch or absent
  authoritative P/D/C means BLOCKED_REFERENCE_INTEGRITY; never silently replace.
- [ ] Reject premature Mode A/B GO, AWS identity bootstrap or inferred G1b adoption.
- [ ] Reject expired/revoked approval or changed scope/input/tool/config/source/
  request path/lifecycle/digest; pause and obtain reassessment/new exact grant.
- [ ] Stop on secret exposure, unexpected operation, storage/integrity failure,
  retention breach or unresolved material contradiction; no automatic fallback.

Next human questions: Who is the verified operator and who independently grants
this exact local scope? What proves their authority? Which existing safe
metadata option and digest is selected? What exact root/custodian/protections
are approved? Which classes may exist, with what dates, backup custodian,
case-limited deletion and hold authority? Which trusted approval event, final
digest and expiry will bind the decision? Answers remain pending.

## 7. Preparation QA receipt and stop

Offline generated-document QA checks JSON syntax/defaults, required OD fields,
lifecycle classes, line-reference bounds, local links, scope/status separation,
ASCII text and absence of machine-specific paths. Final command results and
both generated SHA-256 values are reported in the delivery summary; hashes are
not embedded into their own file. This QA does not attest actual isolation,
signing, filesystem protection, retention enforcement or AWS identity.

Independent static review of this new packet is PENDING. Human authority and
signature authenticity are NOT_VERIFIED. No operational tests were run.
Stop at `PLAN_PREPARED_PENDING_EXECUTION_APPROVAL`, `G0_NOT_AUTHORIZED`,
`P0_NOT_EXECUTED`, `Gate STS-001 NOT VERIFIED`.
