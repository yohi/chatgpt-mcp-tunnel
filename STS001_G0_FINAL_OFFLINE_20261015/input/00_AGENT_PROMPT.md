# AWS MCP STS-001 Investigation B — G0 Final Unsigned Decision Record Drafting

**Assignment:** Prepare a decision-ready **UNSIGNED** G0 human approval record using already-selected human policies. This is **DOCUMENT PREPARATION ONLY**, not authorization for P0, credential access, deletion, or AWS operations.

## 1. Role and immutable references

You are a document-preparation AI agent, NOT the Human Operator, G0 Approver, Data Custodian, Credential Custodian, Requirements Owner, independent reviewer, or execution agent. Do not impersonate a human or certify authority.

- Repository: `yohi/chatgpt-mcp-tunnel`
- Integration branch: `feat/aws-broad-iam-read-api-tools`
- Verified branch HEAD at handoff preparation: `2b10b5eab33cde6d4d7869473e5c9bee7583865c` (PR #12 merge). This is a verification anchor; if the branch moved, STOP and report drift. Never silently substitute a later HEAD.
- Historical code reference commit: `05f4b92e7ff2de76dc79cf8d5dc9f563a03af209`. This is NOT the current branch HEAD.
- R1 plan SHA-256: `15a9adad32011a6f1f660875d877c25092afc8eaa38a8c6a4b2486c1c451b9b1`
- R1 decision record SHA-256: `a0d9d175e1c280bee1eab856783bf356c5cde33dd2383fc591395f68c79771c6`
- R1 change record SHA-256: `88b46081efe54c40175b610ec98019642e941acd543960b05d4376a3fa3bf2c8`
- G0 packet SHA-256: `7a47ddaa5c8d9109d65d3ef59e8090a7c2fc9428a646913cca819e4f50026d60`
- G0 independent review handoff SHA-256: `ee05fa9c9d2ac43506f6be266e2b18da82b2c2ffaff9e11baa0c84bf061643d7`
- G0 independent static review SHA-256: obtain from `sha256sum` of included reference; do not infer from a filename.

The independent G0 static-review verdict was `ACCEPTED_FOR_HUMAN_G0_DECISION_CONSIDERATION` with no formal material finding. This validates the draft as a human-decision candidate, not G0 authorization or operational controls. If required bytes are missing or hashes mismatch, report `BLOCKED_REFERENCE_INTEGRITY` and STOP.

## 2. Inputs and source priority

1. Verify the attached handoff ZIP's member paths, CRC, `SHA256SUMS`, and expected referenced-file SHA-256 values **offline**; read `README_FIRST.md`, `00_AGENT_PROMPT.md`, and `01_HUMAN_SELECTIONS.md` IN FULL.
2. Read the included immutable R1 plan, R1 decision record, R1 change record, merged G0 unsigned packet, independent-review handoff, and independent static-review report IN FULL.
3. Optionally use GitHub **read-only** to verify pinned merged sources at the named HEAD. Do not read other repository files or obtain runtime/environment data. The attached references remain review inputs, not a new normative baseline. Stop on material inconsistency; never silently reconcile it.
4. Governing R1 plan prevails for execution/approval boundaries. The latest `01_HUMAN_SELECTIONS.md` records the **user's policy preferences** in this conversation; it is not identity proof, operational attestation, or an independently attributable signed grant. Do not equate a chat acknowledgment, PR review, or merge with G0 authorization.

## 3. Human selections already made — do not ask again, do not over-promote

- `OD-01`: one human (the user) selected as Human Operator. **Identity/verified ID/verification method and local scope are NOT VERIFIED.** Do not infer from GitHub name, user metadata, or account ID.
- `OD-02`: same human selected as G0 Approver and Data Custodian; Retention/Deletion Owner is the same human **as a candidate**, subject to scope/authority evidence. A **separate, independently attributable G0 approval act** and verified local authority remain required, even though roles can be combined.
- `OD-08`: select **human-supplied, independently approved minimized candidate metadata**; no agent access to AWS config originals, environment/provider processes, credentials, caches, or raw extractor inputs. Do not implement an extractor. No approved sanitized metadata document/digest yet: `P0_CONFIG_DISCOVERY_BLOCKED` for discovery until supplied. Full actual-mode source-provider/request-path GO is required only later (during authorized P0, before G1); no AWS call now.
- `OD-09`: the proposed symbolic root `$HOME/local-restricted-evidence/AWS-MCP-STS001-SEC04-RESOURCE/<approved-run-id>/` was accepted **as a candidate only**. Actual canonical path, verified owner/custodian, mount, ACL/default ACL, parent traversal, encryption/access choice, Git/sync/backup exclusions are `PENDING`; no filesystem inspection or directory creation here.
- `OD-10`: the user accepted class-specific duration **policies**, not absolute expiry dates, review/escalation timestamps, legal-hold authority, or standing deletion authorization. Preserve accepted durations: restricted raw originals 30 days; aliases/mappings/salts 30 days; transient/input/filter files 7 days; QA 90 days; human audit 180 days; share candidates 30 days; approved local shared copies `NOT_CREATED_NO_WRITE`; external distribution copies `NOT_CREATED_NO_WRITE`; approval records 180 days; deletion receipts 180 days. The permitted uses, scope, class-specific reviewer cutoff, backup/custodian, timestamp anchor, `review_due_utc`, `escalate_at_utc`, `retention_expires_utc`, legal-hold handling, residual copies, and prior case-limited **standing deletion instruction** are NOT yet approved.

**Never fabricate absolute UTC dates from a supposed current or past execution date.** Present completion fields to be determined before the first case-owned file write. If helpful, include clearly labeled candidate review/escalation offsets, but do not adopt them without a separate human selection. For each created class, require expiry as an absolute UTC timestamp and review/escalation before expiry, based on an approved anchor; don't let unknowns count as G0 complete.

## 4. Required draft deliverables (locally as planning documents only)

Create exactly these candidate documents under `.omo/drafts/` **in an offline working copy or return them as attachments if GitHub is not writable**. Do not create operational evidence-case directories/files or commit/push/PR.

A. `aws-mcp-sts001-investigation-b-g0-final-decision-record-unsigned.md`
   - `DRAFT_UNSIGNED_NOT_AUTHORIZED`; case/stage/scope and immutable revision/digest references.
   - A two-column map of `selected human policy` versus `still requires evidence/formal human decision` for OD-01/02/08/09/10.
   - A JSON draft approval record with `decision=UNDECIDED`, `approval_state=APPROVAL_PENDING`, verified identity/authority, exact input/outputs, runtime IDs, scope, version/digest, final-record digest binding, approval event/time and expiry ALL visibly pending; `signature=""`.
   - G0 local-operation allowlist **only as candidates**, exact path/tool bindings pending, AWS API budget **zero**, no AWS Region/endpoint grants, no credential/provider resolution, no source-profile fallback, no deletion grant.
   - Distinguish (i) pre-G0 requirements, (ii) separately approved P0 local activities, (iii) pre-G1 source/request-path attestation/STS-IAM endpoints/P1 limits and fresh grant, (iv) post-P1 G1b principal adoption, (v) independent G2–G5/G5-release.
   - Approval authenticity: actual human approver must bind a complete finalized immutable record digest + scope + expiry to an existing trusted channel outside the agent; signing or approving cannot be done by agent. Do not place signed consent in the publicly accessible repository by default.
   - Stop conditions and explicit `NOT_AUTHORIZED` states. Mark unknown operational conditions as unknown, not acceptance.

B. `aws-mcp-sts001-investigation-b-g0-lifecycle-schedule-unsigned.md`
   - Cover all **10 classes** from the merged G0 packet without omission or duplicate.
   - Exact accepted durations, or `NOT_CREATED_NO_WRITE`, with no new permission to create forbidden classes.
   - For every creatable class include proposed anchor, human-approved use, absolute UTC review/escalation/expiry (PENDING), custodian + backup verified IDs (PENDING), exact case-owned scope, preauthorized human deletion instruction/event (PENDING), legal hold authority/process (PENDING), residual copies/snapshots handling, reviewer access cutoff.
   - Preserve distinctions: reviewer silence does not extend expiry; authorized hold is exceptional and recorded; technical deletion failure yields `RETENTION_BREACH`, collection/release stop; AI cannot delete human audit records. Keeping audit/approval/deletion proof has a separately approved lifecycle.
   - No actual file operations; this is a template for a human-owned lifecycle record, not a deletion authorization.

C. `aws-mcp-sts001-investigation-b-g0-finalization-review-handoff.md`
   - Instructions for an independent document-only reviewer to check source hashes, human-selection fidelity, completeness, no invented dates/identity/authority, scope boundaries, cross-document links and contradictions.
   - Explicitly distinguish DOCUMENT_ACCEPTANCE from human G0 decision and P0 execution.
   - Supply an open-items register and one of `ACCEPTED_FOR_HUMAN_G0_DECISION_CONSIDERATION`, `REVIEW_REQUIRED`, `BLOCKED_REFERENCE_INTEGRITY` as possible reviewer verdicts, without pre-assigning one.

Use a separate SHA256SUMS/QA receipt (outside the signed draft contents) to identify candidate bytes. Do not embed a document's own SHA-256 into itself. Rehash the **finalized human decision version** later, and bind its final immutable digest through a separately attributable trusted approval record. If fields change, the signature must bind the new bytes.

## 5. Required offline QA and delivery

- Verify all input hashes, all ZIP CRC/digests, source line references and cross-document links.
- Parse any fenced JSON with the Python 3 standard library; validate `UNDECIDED`/`APPROVAL_PENDING`/blank signature, all 10 classes, approved duration policy names, unchanged 0 AWS requests, no permissions to create disallowed class files, separate G0/G1 gates.
- Check for accidental credentials, token values, source-principal identifiers in outputs, actual private home directory paths, unapproved real names, and accidental public release of sensitive administrative metadata. Human review is still needed; static scanning is not confidentiality proof.
- Record exact byte hashes and test statuses/commands. No simulated PASS or claimed human attestation; failures remain failures.
- Deliver the three unsigned documents, their SHA-256 values, any formal blocking document findings, and explicit **next human decisions** in Japanese.

## 6. Prohibited operations

**Do not** call AWS APIs/STS/CLI/SDK, assume role, reauthenticate, inspect original AWS config/process environment/credential chain/login cache, run Docker, create a wrapper/Broker, mutate IAM, execute P0, capture evidence, create/delete case-owned files, create signatures/approvals/retention authorities, or make GitHub writes (no commit, push, PR, or merge). Do not quietly substitute current `master` for the fixed reference. Do not modify normative R1 sources or the already-merged G0 packet/handoff.

Stop with:

```
PLAN_PREPARED_PENDING_EXECUTION_APPROVAL
G0_NOT_AUTHORIZED
P0_NOT_EXECUTED
G1-G5 / G1b / G5-release NOT_AUTHORIZED
Gate STS-001 NOT VERIFIED
```

The work is complete when the unsigned **decision-ready draft**, lifecycle template, and independent review handoff are delivered, **not** when a human grant has been issued.
