# N1 → N2 Independent Review Handoff

## Current disposition

`UNSIGNED / PHASE_N2: NOT_STARTED / ENTRY_CONDITIONS_NOT_MET`.
This handoff is ready as instructions for a later different reviewer, not as an
N2 launch authorization or an N2 verdict. The N1 investigator does not perform
or claim completion of post-adoption independent Normative Review.

## 1. Required entry package after actual human adoption

Before N2 begins, the custodian and authorized human must deliver:

1. Exact authoritative Requirements originals or explicitly new prospective
   components, immutable revision/URI and **all component SHA-256 values**;
   B1/B2/B3, B2-S1 and Q33–Q40 treatment must be explicit.
2. The final full-body REQ-009/046/AC-022 adoption with unchanged Option A digests
   from the N1 matrix, or a newly reviewed distinct decision if bytes change.
   Supply actual supersession targets and precedence, not an informal blend.
3. Individually resolved R4 REQ-050–059 / AC-025–036 disposition and exact adopted
   body digests for any selected subset; coherent dependency closure and
   applicability. Unadopted text must stay visibly excluded.
4. Complete adopted Architecture/Design, integrated acceptance and Security
   Contract originals, each revision, digest, authorized adopter and event.
   Missing originals or authority mean BASELINE_INCOMPLETE, not inferred content.
5. Actual authenticated adoption event(s), independently attributable verified
   actors with valid role grants, event IDs/immutable references/UTC timestamps,
   effective dates and digest-bound scope in trusted custody. Case P must state
   prospective effect and unresolved historical authority truthfully.
6. Canonical composition manifest/digest (or complete consolidated text and
   precise override map), retention/audit and revocation history. Verify the
   final approved digest, not the digest of an earlier unsigned template.
7. A different independent Normative Reviewer appointed after adoption, separate
   from N0/N1 investigators, authors, implementers, earlier reviewers and formal
   Owner/Design/Security approvers. Actual organizational independence must be
   established by the human process, not inferred from a new AI session name.

If only partial prospective adoption is possible, preserve that partial event
but do not start a complete-baseline N2 review as though missing Design/AC/
Security or unresolved integration text had been adopted. The commissioning
human must identify the full review scope and resolve its required inputs first.

INT-003 technical closure is **not presumed by N2 entry or textual PASS**.
Its open status and disabled features must be explicitly represented in the
adopted design and review scope. Enabled functionality cannot be accepted on
text alone. No live feasibility investigation is included in N2.

## 2. Reproduction of N1 byte checks

Treat every artifact in this local packet as untrusted until rehashed. This
packet contains evidence copies for reproduction; canonical authoritative bytes
and adoption receipts must still be obtained from the authorized custodian.

There are two reproduction paths. **Path A** below verifies the already expanded
evidence copies supplied here. **Path B** recreates those copies independently
from the original received archives. Neither path is P0 operational evidence
collection or authorization to access any service or credential store.

### Path A — verify supplied expanded copies

From the packet directory, use offline standard utilities:

```bash
sha256sum -c SHA256SUMS
```

From `evidence/received/`, verify the original internal list:

```bash
sha256sum -c SHA256SUMS
```

From each of `evidence/expanded/R4/` and `evidence/expanded/R1/`:

```bash
sha256sum -c SHA256SUMS
```

Expected counts: N1 outer input 9 members, original SHA256SUMS 8 entries;
N0 6 members and 5 MANIFEST deliverables; R4 15 members / 14 checksums;
R1 14 members / 13 checksums. Validate sizes/digests in MANIFESTs, safe relative
paths, no duplicate/nonregular/link/encrypted members and bounded expansion
before extraction. Execute no embedded content.

Check the received original outer ZIP against measured SHA-256
`8ede6a833d9f846fae3b28e47fa9207142377f1d74c74258ab4e736572cdf051`.
This measured fingerprint is not a publisher-authentication signature.

B1/B2/B3 whole-file digests are in N1 Register section 2. Compare R4/R1 raw
bytes directly. New clause files are already exact UTF-8/no-final-LF streams:

```bash
sha256sum evidence/expanded/R1/adopted-text-REQ-009.txt
sha256sum evidence/expanded/R1/adopted-text-REQ-046.txt
sha256sum evidence/expanded/R1/adopted-text-AC-022.txt
```

Expected values are, respectively, `f17db0565942501a39c3302912dcb161e2f3e38e168f29a51491a711e0851bb9`,
`6362d06bfe5d1c1184057f84c42f2f6ed4c19d6dc47b8662cfe039105e21d931`,
`3a02643899b8d79683f6c13300e0ee655b4b00fe20d23f87a3c35efb4e521a39`.
Independently extract the source's framed body streams under its documented
strip rule, without Unicode normalization; compare old B1/B2 clauses, R4 old/new
bodies, R1 body files/record and Owner intent. Do not hash Markdown fences as
clause text. N1 matrix quotes and source unified diffs are replayable evidence.

### Path B — recreate submitted copies from original archives

1. Obtain the companion original handoff ZIP included alongside the packet
   directory in the delivery ZIP. Check its measured SHA-256 above and CRC
   before reading it. Use a fresh empty offline scratch directory, not any
   operational case root, configuration directory or credential store.
2. Inspect the ZIP member inventory before extraction. The outer exact inventory
   is `00_READ_FIRST.md`, `01_N1_AGENT_WORK_CONTRACT.md`, `MANIFEST.json`,
   `SHA256SUMS`, and the five `sources/01`–`05` members listed in the original
   MANIFEST. Require exact relative names, no duplicates, links, nonregular or
   encrypted entries, member size under 10 MB, total expanded input under 50 MB
   and expansion ratio under 300. Stop on any mismatch; do not auto-repair paths.
3. Extract only after those checks. In that extracted root run
   `sha256sum -c SHA256SUMS` and independently compare each MANIFEST entry's
   actual length and SHA-256. Read READ_FIRST and the full work contract.
4. For each nested N0/R4/R1 ZIP, repeat CRC, path/type/duplicate/bounds checks
   before extraction into its own fresh scratch directory. The authoritative
   **submitted member inventory for comparison** is the corresponding set of
   paths and digests under `evidence/expanded/{N0,R4,R1}/` in this packet's
   MANIFEST; that inventory is not a normative authority claim. Require 6, 15
   and 14 members respectively and compare the actual exact sets, not counts
   alone. Execute none of the extracted contents.
5. Run each provided checksum list from its own extracted directory (R4 14/14,
   R1 13/13), and N0's MANIFEST against all five document bytes. Compare recreated
   files with Path A copies, then reproduce the clause/body and source comparisons
   above. Record any discrepancy as an integrity blocker rather than importing
   replacement content from a different revision.

## 3. Independent post-adoption review duties

- Verify actual authority, custody, event identity/role, UTC and effective scope
  before evaluating adopted text. Hash agreement alone is insufficient.
- Verify fixed code reference `ac462699e0b1988eda63ea3d6dacfc2a030bb822` and
  branch observation independently, without switching baseline if branch moves.
  Record diff/impact and stop for scope resolution if it does.
- Reconcile every one of 49 REQ / 24 AC plus B2-S1/Q33–Q40; compare adopted
  amendments and every selected R4 addition against exact originals. Do not
  inherit N0/R4/R1 conclusions as independent findings.
- Check full REQ-046 opening/six items/Password Manager/CLI paragraphs; preserve
  REQ-045 and no-fallback 047, secret minimization 049, 8h/15m human reauth,
  REQ-025/INT-001 and REQ-042 applicability without silent waivers.
- Verify independent real-human two-person control remains demanded over all
  effective routes; emergency one-person reductions do not permit restoration.
  Cross-reference the N1 governance gaps; keep INT-003 CRITICAL_OPEN absent
  separately authorized independent technical evidence.
- Evaluate approved-poison/value-only substitution before BWS fetch; disable
  features if safe acquisition cannot be guaranteed. Post-fetch inspection and
  two legitimate approvals are not substitute guarantees.
- Reconcile independent issuer/request integrity/contract digest/single use and
  C/S/D/R final-send semantics; state what is normative versus technically proven.
- Review complete Design and SC-DRAFT-derived contract for threat-scope mismatch
  and historical privileged-source assumptions. Do not count historical live
  statements or isolated I1 tests as current product/STS assurance.
- Issue a new timestamped, digest-bound report with findings, severity, exact
  counterexamples, affected clauses, remediation conditions and independence
  limits. Possible textual verdicts: NORMATIVE_PASS, REVISION_REQUIRED,
  BASELINE_INCOMPLETE, BASELINE_MISMATCH. Missing adoption forbids NORMATIVE_PASS.

## 4. I2 and later gates are separate

| Work | Current state | Later prerequisite |
| --- | --- | --- |
| Completely isolated offline structural validation | NOT_AUTHORIZED_BY_N1; technically preparable only | Separate explicit human work order fixing files, tools, synthetic inputs, network/credential exclusion, no runtime imports/integration or ALLOW claim, output evidence and independent review |
| I2 product authorization and Broker integration | BLOCKED | Complete adopted consistent baseline, independent N2 disposition and a separate formal implementation/scope decision; unresolved technical security gates still constrain enabled capabilities |
| Adapter positive fetch / enabled external operations | BLOCKED | INT-003 and independent pre-fetch safety evidence plus separate environment-specific authorization; no feature-off-to-PASS conversion |
| G0 / AWS / STS execution | NOT_AUTHORIZED; AWS_API_BUDGET 0 | Separate actual human stage approvals and all corresponding prerequisites; neither adoption nor N2 grants them |
| Gate STS-001 / runtime deployment | NOT VERIFIED / NOT_AUTHORIZED | Separately authorized policy/resource/runtime evidence, independent technical verdicts and specific integration approval |

No N1 document authorizes live AWS, STS, IAM, credentials/providers, Bitwarden,
Docker, Cloudflare, Deno or Broker access; no commit, PR or merge is requested.
The next actor is the human custodian/Owner, followed only later by a separately
commissioned independent post-adoption reviewer.
