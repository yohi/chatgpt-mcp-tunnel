# N1-P Design, Integrated Acceptance and Security Completion Gaps

Status: **UNSIGNED / PROPOSED / NOT_EFFECTIVE**

## 1. Authority search and classification

Complete authenticated Architecture/Design, integrated Acceptance Criteria and
adopted Security Contract: **NOT_RECOVERED / MISSING_AUTHORITY**. No private
authority repository or authenticated custody channel was supplied. N1's reports,
the complete submitted B1/B2/B3 and R4/R1 candidates, Owner intent and Security
draft were read. The local fixed Git tree was listed; no complete adopted set is
identified there. This is a bounded recovery result, not a claim that no private
original exists. No proposed section below is a recovered or adopted Design.

Classification uses separate dimensions: **TEXT_SUFFICIENT** means a candidate
requirement states a local invariant, not formal authority; **INSUFFICIENT** means
the protocol/contract remains unwritten; **CONTRADICTORY** identifies incompatible
scope; **NO_IMPLEMENTATION_PROOF** means no product guarantee established by this
investigation. A source assertion of historical verification does not change it.

## 2. Concrete sections to recover or commission

Role names below are future responsible roles, not authenticated appointments.
Each section needs exact revision/digest, normative traceability, failure and
recovery behavior, applicable environments/modes and actual human approval.

| Proposed section / responsibility | Text status and source | Required completion and acceptance scope | Responsible drafter / approver |
| --- | --- | --- | --- |
| D-01 Scope, domains and threat boundaries | INSUFFICIENT / CONTRADICTORY: B1/B2 + OA vs trusted-admin Security draft | Distinguish Broker, Executor, independent Authorizer/Issuer, Adapter, Stores, UI, AI, platform admins and recovery roots; compromised Broker, one privileged admin and valid-pair poisoning threats; name out-of-scope threats without weakening requirements; AC-012/022/025/026 | Architect / Design + Security; Owner for changed requirements |
| D-02 AWS account/task/read authorization | TEXT_SUFFICIENT local 001–008/022–024/029–031/043; overall Design INSUFFICIENT | Per-call principal/task/account/resource/action checks; validated operation catalog including composite calls; keyless unattended sources and refresh; cross-account budget aggregation, no ambient fallback; AC-001–006/014/015/019/020/021/023 | AWS authorization designer / Design + Security |
| D-03 AWS per-operation write approval | TEXT_SUFFICIENT local 014–021; protocol INSUFFICIENT | Independent authenticated Web approval, exact full parameters, 15m pending/5m execution-start deadlines, atomic single-use across instances/restart/restore; deny high-risk actions even if approved; uncertain outcome no retry; AC-007–010/013/017 | Authorization/state designer / Design + Security |
| D-04 Independent Authorizer and Issuer | INSUFFICIENT: Q37 and unadopted 053 | Independently verify original request intent, human/service + agent + instance, Portal/direct channels, policy/quota; canonical parameter/operation-contract digest, issuer trust/key/rotation, audience/channel, nonce, expiry/epoch, failure modes; AC-006/019/024/034/035 | Identity/protocol designer / Design + Security |
| D-05 AWS session restriction / Explicit-Deny | INSUFFICIENT / CONTRADICTORY: Draft B-01–06/T-01–06 vs v1.1 | Define independent AWS-enforced limits under Broker compromise; safe-action catalog and versioned expansion, unknown-action refusal, inline Deny + managed policy binding and STS size limits; role ID/source/session binding; role/trust/managed/resource-policy drift and refresh/expiry; AC-004/010/021/023 plus separate STS acceptance | IAM-policy specialist / Security + Design, role owner for any reuse |
| D-06 Credential acquisition and isolation | OA TEXT_SUFFICIENT invariant; mechanism INSUFFICIENT | Per-credential readers/signers/administrators, no existing IAM-key acquisition by any component; no provider/cache fallback; STS minimal use, BWS/secret exclusive Adapter Store; no secret data in result/error/IPC/log/backup; actual effective rights and hostile-runtime tests; AC-012/021/022/023/025/026 | Credential-boundary designer / Security + Design |
| D-07 Bitwarden external capability and Store | CONTRADICTORY D-025; mechanism INSUFFICIENT | Mandatory capability vs initially disabled deployment; no AWS/internal-key dependency; per-install account/project, Store principals, safe issuance/placement/rotation; exact operation contracts, output controls and external-write prohibition; AC-022/025–028/030/032/034 | Adapter designer / Design + Security; Owner D-025 |
| D-08 Secret content provenance before fetch | INSUFFICIENT; FEAS-007-C NOT_PROVEN | Independent non-value-reading enforcement, immutable safe issuance provenance, every ingress/restore/alias path, atomic exact-version binding, approved and unauthorized poison; unknown means zero value-fetch requests; AC-022/028/032/033/036 | Provenance/Secret security designer / Security; independent later feasibility reviewer |
| D-09 Two-distinct-human governance | INSUFFICIENT; INT-003 CRITICAL_OPEN | Real person/control and delegation/recovery mapping, every effective admin path, exact one-change two-party pre-application enforcement, protected enforcer/issuer/audit roots; one-human reduction only; AC-026/027/028/036 | Governance/platform owners / Security; actual independent humans separately verified |
| D-10 Environment profiles | CONTRADICTORY D-042; implementation evidence absent | Four configurations: Deno, Workers, Docker/Linux, Docker/macOS; AWS-only and enabled separate; keyless unattended auth, isolation, state, audit and recovery proof per cell; justified normative N/A only; AC-001/018/021/023/024/031 and enabled suite | Each platform designer / Design + Security; Owner applicability decision |
| D-11 Revocation, replay and final dispatch | TEXT_SUFFICIENT AWS 017/032–035; external protocol INSUFFICIENT | Separate S consumption/release, D actual final-transport start, C global cancellation, R observation; serialize D/C, discard unsent S<C queues forever, no unknown-result resend, multi-instance and partition behavior; distinguish Token/session/STS residuals; AC-008/009/011/013/029/035 | State/transport designer / Design + Security |
| D-12 State, audit and disaster recovery | TEXT_SUFFICIENT local 026/028/036–040/043; integrated mechanism INSUFFICIENT | Independent append/protect/read rights, >=90d retention, encrypted backups without secrets, anti-rollback epochs/used approvals, crash/partition/recovery consistency, protected CI/deploy/restore path and audit reconciliation; AC-016/017/026/029/035 | State/audit/recovery designer / Design + Security |

Every row also has **NO_IMPLEMENTATION_PROOF** for the proposed complete product.
PR #14/#15 isolated offline results and reported I1 closures do not demonstrate
these product contracts or current live configuration. N1-P neither runs nor
reopens I1 technical testing, and does not extend its reported verdicts.

## 3. Specific Security draft inconsistencies

Source: `evidence/n1/evidence/received/sources/05_STS001_Security_Contract_DRAFT_Submitted_Copy.md`,
SHA-256 `0cc08ad3a1970be2ba4a73e47240d96fc9300afb5747da48db2d2bd9bdac102c`.
It targets historical commit `05f4b92e7ff2de76dc79cf8d5dc9f563a03af209`, not fixed HEAD.

| Draft scope / clause | Inconsistency or missing v1.1 scope | Required new contract decision |
| --- | --- | --- |
| §1 privileged login source/Broker trusted; compromised MCP only | Compromised Broker can omit restrictive policies or make privileged calls; independent issuer and wider v1.1 threat claims not covered | Define independently enforced AWS boundary or state unacceptable gap; do not simply relabel the old trusted Broker as independent |
| §1 aws-login administrator source, B-02 | Interactive login/session cache conflicts with keyless unattended three-environment objective if made mandatory | Pin permitted credential sources with workload-ID/role binding per environment; no ambient long-term key or Bitwarden AWS source |
| B-03/04/05 | Session-only administrative-role restriction, safe action catalog and policy size/drift unresolved | Mandatory reviewed Deny, managed policy digest, all action/resource-policy pathways; role/trust/resource drift; no broad Get/List prefix proof |
| B-06/B-07 | Issued STS identity checks and private file/pipe handoff do not prove parameter attachment, all component isolation or no source reachability | Distinct deterministic request assertions and actual permission evidence; new credential-specific boundary plus principal/account separation |
| B-07/T-07 | Compose/volume/credential_process isolation is Docker-focused | Define Deno/Workers and both Docker hosts independently; do not require Docker for all or infer live mounts from static Compose |
| B-08 renewal grace/readiness | Reuse of old unexpired STS on transport failure cannot override current revocation, drift or unknown authorization/audit/state | Explicit state machine: credential unexpired is necessary, not sufficient; stop new operations on invariant failure; residual tracking separate |
| B-01/B-10 and shared existing-role scope | No IAM mutation/reuse proposal is neither proof of safe shared-role reuse nor a general v1.1 design choice | Separate role-owner authorization, workload noninterference and no mutation; no bootstrap/cleanup against shared role; no execution now |
| No independent Adapter/BWS section | Q33–40/OA/045/046, all-admin pair and pre-fetch provenance absent | Add D-07/08/09 contract; draft cannot authorize Token placement or secrets |
| No AWS per-write approval architecture | Read-only STS draft cannot implement B1 014–021 write mode | Distinct approved-write credential and operation boundary with independent approval; external writes remain prohibited; no read-policy relaxation by implication |
| §4 historical PASS/VERIFIED claims and T-01–10 | Earlier operator assertions, a few read/DryRun results and S3 inventory are neither current universal no-write proof nor product runtime validation | Preserve as historical claims only; authenticate original evidence if later needed; independent coverage/limits and new scoped authorization before experiments |

## 4. Integrated Acceptance contract completion

Commission one authoritative integrated AC contract with a traceability row for
each original AC-001–024 (only AC-022 replaced by exact OA), each selected R4 AC,
B2-S1, each adopted B3 item and Design/Security section. Preserve all original
49 REQ/24 AC obligations; map selected additional requirements and decisions.
Each test case must specify subject/build/config/policy digests, environment and
mode, prerequisites, positive/negative/fault procedure, expected observable
denials or transitions, safe synthetic data, independent observer, evidence
schema, residual limitations and explicit status vocabulary.

Required acceptance groups:

1. AWS keyless source and allowed-source/no-fallback failures across all configs;
   accounts/task/quota, operation catalog/composite calls and bounded real-AWS
   nonproduction obligation retained (AC-020), with later separate authorization.
2. AWS write per-operation approval/replay/expiry/unknown result/high-risk denial;
   Portal/direct human/agent/service identities and 8h/15m session behavior.
3. Session Explicit-Deny effectiveness, identity/request binding, safe catalog
   drift, role/trust/managed/resource-policy paths, renewal/expiry and isolation.
4. Broker compromise and all management bypasses; distinct persons, each specific
   Token change and independent audit; no exemption for root/support/restore.
5. Pre-fetch unauthorized and approved poisoning, alias/restore/value-only race;
   zero fetch until proof. AC-022/032 positive paths remain BLOCKED beforehand.
6. C/S/D/R final transport, queues, multi-instance consumption, partition,
   crash/restore/rollback, Token/STS/session residuals and audit/state outages.
7. Four concrete environment configurations × two modes; no mock-only dynamic
   claim, no disabled-to-enabled PASS, no unjustified N/A or omitted Docker host.

## 5. Completion and approval conditions

Custodian first attempts recovery of real originals with immutable URI/revision,
digest and valid actual adopter event. If unavailable, authorized drafters create
new explicitly prospective Design/AC/Security revisions covering D-01–12. Resolve
D-025/D-042/B3 and selected R4 dependency closure; obtain Requirements authority
for every requirement change and Design/Security authority for their domains.
Freeze exact documents and consistency/override map before actual approvals.

INT-003 and FEAS-007-C must be stated as open with affected capabilities disabled.
A design may document blocked functionality and evidence obligations for future
investigation; it must not approve Adapter-enabled operation or high-risk
expansion as safe while those guarantees are unproven. Textual adoption, N2
review, technical feasibility, implementation approval and execution permission
remain distinct events. No such event is performed here.
