# AWS MCP STS-001 Investigation B — Independent G0 Approval Packet Static Review

- **Review date:** 2026-10-15 (JST)
- **Reviewer:** GPT-6, independent document-only reviewer
- **Verdict:** `ACCEPTED_FOR_HUMAN_G0_DECISION_CONSIDERATION`
- **Scope:** two submitted G0 preparation documents, authoritative R1 planning documents, attached R1 review reference, immutable hashes, stage boundaries; **no G0 grant / no AWS validation**.
- **Finding count:** 0 blocking; 0 formal open findings. One non-blocking human-completion note appears below.

## 1. Source identity and independently run integrity checks

| File | Lines | SHA-256 | Result |
|---|---:|---|---|
| G0 unsigned approval packet | 321 | `7a47ddaa5c8d9109d65d3ef59e8090a7c2fc9428a646913cca819e4f50026d60` | MATCH |
| G0 independent-review handoff | 148 | `ee05fa9c9d2ac43506f6be266e2b18da82b2c2ffaff9e11baa0c84bf061643d7` | MATCH |
| R1 plan | 1009 | `15a9adad32011a6f1f660875d877c25092afc8eaa38a8c6a4b2486c1c451b9b1` | MATCH |
| R1 decision record | 100 | `a0d9d175e1c280bee1eab856783bf356c5cde33dd2383fc591395f68c79771c6` | MATCH |
| R1 change record | 115 | `88b46081efe54c40175b610ec98019642e941acd543960b05d4376a3fa3bf2c8` | MATCH |
| G0 preparation ZIP | 7 members | `45c2c767fdf988e22004ac622b35a11ccb14fc335424dd19b4d7ebb1bc383f07` | MATCH to packet's recorded value |
| R1 independent document recheck | 71 | `cfaba82988d6e87c7b53aba18bd19bd2a35b820a7f1af2fe8225883948d6c3fe` | MATCH |

The attached preparation ZIP passed `zipfile.testzip()` (all member CRCs), 6/6 internal `SHA256SUMS` comparisons, and byte-for-byte equality against the three submitted R1 source copies. Both G0 Markdown files were read in full. A read-only GitHub comparison returned `identical` between the named integration branch and `9b6b1bca6ee089b1e1a10bcfc5139eb7bf1f9843`. The immutable code-reference commit `05f4b92e7ff2de76dc79cf8d5dc9f563a03af209` is correctly kept separate. The reviewer did not independently fetch raw GitHub file bytes this time; no new claim of independently established publisher authenticity is made.

## 2. Static contract tests actually run

The reviewer parsed both fenced JSON records successfully and checked that approval defaults are `UNDECIDED`/`APPROVAL_PENDING`, the signature field remains blank, G0 has **zero** approved AWS APIs/requests/Regions, and all five pre-G0 OD items (`OD-01`, `OD-02`, `OD-08`, `OD-09`, `OD-10`) are represented. The 10 named lifecycle classes were independently counted, including approval records and deletion receipts. Cross-document relative links, plan digest references, explicit guard states (`P0_CONFIG_DISCOVERY_BLOCKED`, `P0_CASE_WRITE_BLOCKED`, `SOURCE_REQUEST_PATH_NOT_ATTESTED`, `RETENTION_EXCEPTION_LEGAL_HOLD`, `RETENTION_BREACH`), ASCII encoding and plan line-reference bounds passed static checks. No live or P0 fixture test was run.

## 3. Normative R1 mapping and reviewer judgments

| Review topic | Packet / handoff evidence | R1 plan authority | Judgment |
|---|---|---|---|
| OD-01: operator identity | Packet L98–110, L187–225, L283–307 | Plan L173, L652, L672 | PASS: identity/scope remain pending |
| OD-02: verified G0-local approver; separate attributable act | Packet L104–110, L182–258, L285–287 | Plan L185–217, L653, L672 | PASS: operator consent alone cannot authorize G0 |
| OD-08: existing trusted extractor or independently approved sanitized metadata | Packet L112–129, L229–245, L288–289 | Plan L225–249, L659 | PASS: original AWS config not an agent input; no safe mode implies block |
| OD-09: exact canonical path and custodian with Git/sync/backup exclusions | Packet L104–110, L131–138, L234–245 | Plan L455–477, L660 | PASS: only proposal; no filesystem verification claimed |
| OD-10: before-first-write lifecycle | Packet L140–180, L262–269, L290–293 | Plan L465–477, L538–585, L661 | PASS: all 10 classes; legal hold, silence and breach distinguished |
| G0 approval's exactness and non-propagation | Packet L182–258, L260–281 | Plan L169–217, L668–675 | PASS: digest, local mode/scope, channel, expiry pending; AWS budget 0 |
| Actual provider/request-path proof, only after G0 / before G1 | Packet L262–281 | Plan L412–449, L673–674 | PASS: both modes subject to actual selected-mode GO, no bootstrap API |
| Integrity / historical fixed-code reference | Packet L31–96; handoff L30–65 | Plan L71–105 | PASS: versions and expected hashes correctly separated |
| No execution or operational closure | Packet L1–29, L318–321; handoff L109–148 | Plan L33–43, L98–128 | PASS: no claim of G0 grant, isolation proof, F-004/F-006 closure or Gate STS-001 verification |

### Negative-interpretation tests (manual static reading)

The packet rejects each of the handoff's enumerated failure readings: treating an unverified approver or prior PR as G0 authority (L100–110, L255–258, L285–287); providing original config to the agent (L112–129, L242–245); writing case files before lifecycle consent (L162–167, L290–293); ignoring source digest mismatch (L294–295); promoting synthetic tests into production GO (L271–278); reusing invalidated/expired scope (L297–298); using G0 to authorize G1/G1b (L260–281); deleting an authority receipt prematurely (L177–180); and treating reviewer silence as a legal hold or retention extension (L169–179).

## 4. Findings

**No formal material or blocking `IB-G0-DOC-NNN` finding is opened.** The required contract fields are either specified or explicitly marked pending for human decision. This acceptance is for the unsigned document's suitability for human decision consideration, **not** for the completeness of a future signed final G0 record.

**Non-blocking completion note:** Packet L142–147 requires per-class permitted uses, exact case-scoped scope, residual-copy handling, and authorized legal-hold/deletion records; the lifecycle decision table L149–160 has fewer columns than the full narrative requirement. At human completion, use a separately attributable per-class lifecycle schedule/record containing **all** those fields and bind its finalized digest in the G0 approval. Merely filling the visible date columns is insufficient. Packet L196–217 and L255–258 must be re-bound to the final immutable document bytes through the trusted channel; modifying the packet after approval requires a new hash and approval assessment. This is an operational completion caution, not a R1/G0 draft defect requiring a document rewrite.

## 5. What remains unresolved before G0

- `OD-01`: verified human operator, contact, precise local scope and consent.
- `OD-02`: verified approver with **local G0 authority**, separate attributable approval event, actual trusted channel, final scope/digest/expiry.
- `OD-08` initial: existing trusted human extractor **or** separately approved sanitized metadata, exact tool/input identity/digest and recipient/output restrictions; otherwise `P0_CONFIG_DISCOVERY_BLOCKED`.
- `OD-09`: human-approved canonical evidence root, custodian, permissions, encryption/access decision, filesystem/Git/sync/backup exclusions and related attestation.
- `OD-10`: creation classes, per-class review/escalation/actual expiry, human custodians/backup, case-limited standing deletion authority, hold handling and residual-copy policy **before any operational case file write**.

These are **owner decisions / subsequent verifications**, not independent-review findings closed through static text. Later P0 operational-mode proof, source validity, STS/IAM endpoints, P1 budgets, G1 approval, G1b baseline adoption and G2–G5 approval remain independent and unresolved.

## 6. Final disposition / prohibited inference

`ACCEPTED_FOR_HUMAN_G0_DECISION_CONSIDERATION` means the current unsigned G0 packet is usable as the basis for human decisions. It does **not** imply `G0_AUTHORIZED`, `P0_EXECUTED`, source-provider GO, AWS endpoint approval, Broker implementation approval, Role reuse authority, finding closure or a global write-prevention guarantee. The final human approval must be independently attributable, scope- and digest-bound, expiry-limited, and separately verified before any P0 operation.

**Preserved statuses:**

```text
PLAN_PREPARED_PENDING_EXECUTION_APPROVAL
G0_NOT_AUTHORIZED
P0_NOT_EXECUTED
G1-G5 / G1b / G5-release NOT_AUTHORIZED
Gate STS-001 NOT VERIFIED
```

**No AWS API, credentials, AWS configuration, credential provider, local operational evidence case, IAM or GitHub write, Broker implementation, or P0 execution was performed.**
