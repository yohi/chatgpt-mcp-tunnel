# AWS MCP STS-001 Investigation B — Human Policy Selections (NOT G0 Approval)

Date of conversation: 2026-10-15 (JST). This note faithfully records the human's accepted **policy options** from the ongoing conversation. It is **not** a separately attributable approval record, proof of identity/authority, a signature, a technical attestation, or permission to execute P0.

## Selected choices

| Decision | User-selected policy | Still pending before effective G0 |
| --- | --- | --- |
| OD-01 | The user personally acts as the Human Operator | Verified identity/ID, scope and consent evidence via trusted mechanism |
| OD-02 | The same person also acts as G0 Approver, and Data Custodian; the same person is the **candidate** Retention/Deletion Owner | Verified G0-local authority, independent attributable decision event, approval scope and immutable digest/expiry; no inferred AWS-level authority |
| OD-08 | Human-managed, independently approved **sanitized metadata supplied to the agent**, not original AWS config | Sanitized input identity, exact approved provenance, allowed output/recipient, hash and safe boundary proof. No original config read by AI |
| OD-09 | Symbolic root candidate `$HOME/local-restricted-evidence/AWS-MCP-STS001-SEC04-RESOURCE/<approved-run-id>/` | Actual canonical root, custodian evidence, file/mount/ACL/encryption decisions, Git/sync/backup exclusions and scope-specific human authorization |
| OD-10 | Accept the 10-class duration/creation policy below | Explicit anchors and absolute UTC dates, review/escalation deadlines, custodians, uses, exact deletion/hold/backup scope, separately authorized standing deletion instruction |

The user has consented to the **choices** above. Neither the assistant nor AI agent has verified identity/authority, storage isolation or any operative G0 approval channel. A human may fill this information later through an existing trusted channel and formally approve only after binding a finalized record digest and expiry.

## OD-10 duration/creation policy accepted by the user

| # | Class in the 10-class G0 packet | User-selected duration/policy |
| --- | --- | --- |
| 1 | Restricted raw originals | 30 days |
| 2 | Aliases / mappings / salts | 30 days |
| 3 | Transient / input / filter copies | 7 days |
| 4 | QA records | 90 days |
| 5 | Audit records | 180 days |
| 6 | Share-candidate copies | 30 days |
| 7 | Local approved-share copies | `NOT_CREATED_NO_WRITE` for now |
| 8 | External distribution copies | `NOT_CREATED_NO_WRITE` for now |
| 9 | Approval records | 180 days |
| 10 | Deletion receipts | 180 days |

**Interpretation:** These are retention duration policies relative to an as-yet-unapproved anchor, not absolute deadlines or a deletion grant. Before any operational case-owned write, the human must approve exact UTC `review_due_utc`, `escalate_at_utc`, `retention_expires_utc` for every class to be created, plus custodian/backup, permitted uses, deletion scope, legal hold and residual-copy disposition. Classes 7/8 are prohibited from creation until a later separately approved scope/lifecycle decision.

## Boundaries not changed by the user's approvals

- `PLAN_PREPARED_PENDING_EXECUTION_APPROVAL`; `G0_NOT_AUTHORIZED`; `P0_NOT_EXECUTED`; all later gates `NOT_AUTHORIZED`; `Gate STS-001 NOT VERIFIED`.
- No AWS calls, provider/cache/config access by AI, role assumption, STS renewal, Broker implementation, P0 execution, deletion permission, or GitHub mutation.
- Drafting documents does not count as creating operational case evidence or authorizing case-owned writes.
- Code reference commit `05f4b92e7ff2de76dc79cf8d5dc9f563a03af209` is distinct from merged G0 document HEAD `2b10b5eab33cde6d4d7869473e5c9bee7583865c`.
