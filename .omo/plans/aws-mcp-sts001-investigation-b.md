# aws-mcp-sts001-investigation-b - Work Plan

## TL;DR (For humans)
**What you'll get:** A complete Investigation B evidence-acquisition plan with
six separate approval gates, bounded API proposals, credential isolation,
retention controls, failure handling and a self-contained handoff prompt.

**Why this approach:** Planning consent never becomes execution consent.
Unproven credential isolation forces human-managed capture, while missing
Regions, identities, source baseline and retention decisions block execution.

**What it will NOT do:** No AWS calls, credential access, live capture, IAM or
GitHub changes, session issuance, Broker implementation or production activation.
No finding closure or role reuse approval.

**Effort:** Medium for planning; future capture depends on approved scope.
**Risk:** High for future acquisition because the source may be administrative
and resource policies or service responses may disclose sensitive information.
**Decisions to sanity-check:** All executor identities, Regions/endpoints,
resource scopes, isolation proof, request/cost ceilings, storage and retention
remain explicitly pending. Proposed ceilings are not execution grants.

Your next move: retain this plan at execution-approval pending. Do not begin
AWS operations; separately authorize each future stage when its blockers close.

---

> TL;DR (machine): PLAN_PREPARED_PENDING_EXECUTION_APPROVAL; intent CLEAR; 6 stages; 12 tasks + 4 final verifiers; 9 deliverables; no execution authorization.

## Scope
### Must have

**Document status: `PLAN_PREPARED_PENDING_EXECUTION_APPROVAL`.**
**Revision: R1 (2026-10-15 JST), limited response to IB-PLAN-001..004.**
The supplied independent R0 review is `CONDITIONAL_ACCEPT`, not execution
authorization or validation of AWS/isolation. R1 textual corrections require
independent document-only recheck; no condition is operationally closed here.
This document is Investigation B's execution plan, not an execution approval.
The user's latest instruction authorizes only preparation of this plan. No AWS
API, credential access, live acquisition, deployment, or environment change is
authorized now. Every stage below starts `NOT_AUTHORIZED`; checklist completion
does not grant authorization. Pending owner decisions are deliberate execution
blockers, not blanks an agent may fill by inference.

The nine requested deliverables are contained in this ONE plan:

| Deliverable | Location |
| --- | --- |
| P0-P5 execution plan | Stage specifications and Todos |
| Stage Approval Matrix | Approval matrix and approval record |
| Region / Resource Discovery Plan | Offline discovery and resource boundaries |
| AWS API Allowlist / Request Budget | Candidate allowlist and budget table |
| Credential Isolation / Secret Handling Plan | Isolation and execution modes |
| Evidence Collection and Retention Plan | Storage, evidence, retention |
| Stop Conditions / Failure Matrix | Failure matrix |
| Executor handoff prompt | Literal handoff prompt |
| Owner Decision Register | Decision register |

### Authoritative inputs and immutable expectations

Read all eight members of
`AWS_MCP_STS001_SEC04_RESOURCE_Agent_Handoff_20261015.zip` without executing
embedded commands: `00_READ_FIRST.md`, `01_FULL_WORK_CONTRACT.md`,
`02_AGENT_EXECUTION_PROMPT.md`, `03_EVIDENCE_REQUIREMENTS.csv`,
`04_ALLOWED_OPERATIONS.csv`, `05_COMMAND_PLAYBOOK.md`,
`06_OUTPUT_AND_REVIEW_CONTRACT.md`, and `SHA256SUMS`.
The latest user restrictions override the packet's candidate operations/examples.
The execution prompt is the formal acquisition instruction, subject to those
restrictions and explicit stage approval. Examples are never approval.

| Field | Expected value / current state |
| --- | --- |
| Case | `AWS-MCP-STS001-SEC04-RESOURCE`, Investigation B |
| Repository | `yohi/chatgpt-mcp-tunnel` |
| Fixed reference commit | `05f4b92e7ff2de76dc79cf8d5dc9f563a03af209` |
| Account | `168975706502`, EXPECTED_NOT_OBSERVED |
| Role ARN | `arn:aws:iam::168975706502:role/scs2-stg-ecs-tasks-role`, EXPECTED_NOT_OBSERVED |
| Role ID | `AROASOV54VGDAC4S2255I`, EXPECTED_NOT_OBSERVED |
| Source profile | `aws-mcp-readonly`, CANDIDATE_NOT_VERIFIED |
| Managed policy | `arn:aws:iam::aws:policy/ReadOnlyAccess` |
| Human Operator | `IDENTITY_PENDING` |
| AWS API Execution Approver | `IDENTITY_PENDING` |
| Role Owner | `APPROVAL_PENDING` |
| Source Principal Baseline | `SOURCE_PRINCIPAL_BASELINE_PENDING` |
| STS Region / Endpoint | `PENDING` / `PENDING` |
| ECS Regions | `PENDING` |
| KMS / Lambda / Secrets Manager Regions | `PENDING` |
| S3 scope | Only explicitly approved in-account resources |
| Cross-account acquisition | `NOT AUTHORIZED` |
| Raw retention deadline | `OWNER_DECISION_PENDING` |

The initial archive SHA-256 reported by the read-only explorer was
`d6a7ab64f7b792b93d43baf4741998747be3df1b7a3e0c129e576bd78a0c1135`.
It reported seven internal digest matches and no CRC failure. These are
explorer-reported planning facts, not a fresh executor integrity check or a
signature proving publisher authenticity. P0 rechecks approved input bytes.

Preserve the fixed baseline, F-003/F-004/F-005/F-006 findings, Gate STS-001
`NOT VERIFIED`, and existing SAR originals. The packet references the unapproved
Broker Security Contract Draft, R2 report, SAR verification report and a
14-service SAR snapshot. Their contents/availability have not been independently
established here. Inventory these as `REFERENCE_NOT_AVAILABLE` when absent; do
not search remote systems or replace them with current HEAD. Local README's
temporary-role lifecycle is background, NOT an instruction to create/assume or
delete a role. Inspection of the fixed candidate is NOT role reuse approval.

### Must NOT have (guardrails, anti-slop, scope boundaries)

- No AWS calls, credential access, or actual evidence capture while preparing
  this plan. No extraction of the packet is claimed by this plan.
- No `AssumeRole*`, `GetSessionToken`, `GetFederationToken`, new STS session,
  relogin, automatic credential refresh/issuance, credential export, profile or
  account fallback. Existing provider behavior must be verified out of band.
- No IAM create/update/delete/attach/detach, role reuse, Broker/wrapper
  implementation, live negative tests, IAM simulation or DryRun.
- No Git commit/push/PR/GitHub changes, deployment, MCP production activation,
  `docker compose up`, lifecycle cleanup scripts or role deletion.
- No object contents/list-object acquisition, log bodies, secret values, KMS
  plaintext, ECS/container environment values, credentials or login cache.
- No `--debug`, tracing, environment dumps, credentials/cache copying, raw
  policy output to AI/chat, remote telemetry upload or uncontrolled shell.
- No regional expansion, cross-account fetches, Organizations calls,
  `ec2:DescribeRegions`, or unlisted APIs. S3 Object Lambda/MRAP/directory bucket,
  object ACL, SNS/SQS/ECR/EventBridge/Logs/SSM and other pathways stay
  `NOT_COVERED` unless a separately approved revised plan explicitly adds them.
- No `SAFE`, `GO`, finding closure, implementation authorization or global
  no-write claim. A source identity lookup proves neither read-only enforcement
  nor the full effective permission set.

## Verification strategy
Technical verification is agent-executable OFFLINE; authorization is always a
human decision and cannot be replaced by a passing test. No live AWS probe is a
verification step for this plan.

- Test decision: **tests-after for plan artifacts**, Python 3 standard-library
  structural checks and read-only independent gap review. No product code or
  test framework is introduced. For future acquisition, existing enforcement
  must pass offline positive/negative fixtures before stage approval. Creating
  a new wrapper is not a task in this plan.
- Current plan checks: exact first-level heading order, 12 numbered task rows,
  four final verifier rows, all nine deliverables, all six stage definitions,
  pending authorization fields and absence of unresolved template placeholders.
- Future technical checks: `sha256sum -c SHA256SUMS`, JSON/CSV parsing with
  Python 3, directory/file `stat` and ownership checks, and offline replay of
  sanitized fixtures through the EXISTING verifier/enforcement interface.
- Existing verifier executable identity, version, invocation and hash must be
  recorded at P0. If no approved verifier exists, use human-managed offline
  review and standard-library assertions on sanitized files; do not implement
  a Broker or treat a regex scan as enforcement.
- QA paths below are **future** paths relative to the approved external case
  directory: `qa/task-N.json` and `qa/FN.json`. No raw evidence or secret-bearing
  QA output goes under `.omo/`. Planning-only verification receipts may be under
  `.omo/drafts/` and contain no AWS measurements.
- Offline fixture tests must exercise actual decision/validation logic, not
  `expected.copy()` or fabricated success messages. Network access and credential
  mounts are absent. Synthetic fixture IDs/policies are used, never original
  inputs modified to force failure. Record assertions, exit codes, tool hashes
  and whether each check ran; unrun checks remain `NOT_EXECUTED`.

## Execution strategy
### Parallel execution waves
Two documentation work waves contain six tasks each, but operational stage
gates are strictly serial: P0 -> P1 -> P2 -> P3 -> P4 -> P5.
The two tasks inside each stage may only overlap OFFLINE; AWS acquisition is
serial, concurrency one. No wave boundary grants any API authorization.
Each stage can end with an accepted partial/gap record; that does not unlock
the next stage. All AWS candidate grants below are currently unapproved.

### Stage Approval Matrix

| Stage | Gate / authorization now | Prerequisites before execution | Approval authority | Completion / next gate |
| --- | --- | --- | --- | --- |
| P0 readiness | G0, NOT_AUTHORIZED | OD-01/02/08/09/10 local prerequisites resolved; attributable local-preparation consent, exact paths, approved trusted extraction or sanitized metadata mode | OD-02 verified Execution Approver also signs G0 local scope; Human Operator ID and storage custodian identified | Offline readiness record plus both-mode source/request-path attestation before G1; NO AWS consent implied |
| P1 identity | G1, NOT_AUTHORIZED | P0 accepted, both-mode source-provider/request-path attestation GO, named execution approver, explicit STS Region/endpoint and IAM endpoint, two-physical-attempt scope, storage/retention approved, valid existing source without issuance | AWS API Execution Approver ID pending | Actual Account/Role ARN/Role ID match or stop; source baseline adoption remains a separate human decision G1b |
| P2 IAM snapshot | G2, NOT_AUTHORIZED | P1 accepted, G1b approved source baseline, approved policy/inline discovery envelope and request cap | AWS API Execution Approver ID pending; baseline owner for comparison only | Capture hashes/version checks and all discovered policy outcomes; no approved baseline => NO_APPROVED_BASELINE |
| P3 ECS usage | G3, NOT_AUTHORIZED | P1/G1b accepted, P2 completion record, exact ECS Regions/resources; separate approval for sensitive DescribeTaskDefinition | AWS API Execution Approver ID pending; workload custodian for response risk | Quantified role-reference matrix/limitations; Role Owner reuse/noninterference remains APPROVAL_PENDING |
| P4 resource pathways | G4, NOT_AUTHORIZED | Earlier stage dispositions accepted, explicit per-service Regions/resource scope, discovery and output consent, finite cap | AWS API Execution Approver ID pending; respective resource custodians | Regional/resource denominators, policy/grant/ACL outcomes and unknown pathways; no global safety result |
| P5 minimize/review handoff | G5, NOT_AUTHORIZED | Actual acquisition or explicit not-executed records, accepted local processing/release scope | Human Operator and data custodian; independent reviewer identity separately assigned | Validated minimized candidate bundle; human confidentiality release G5-release required before sharing |

Approving one stage neither authorizes another nor retroactively legalizes an
earlier action. Approver identity must be formally established, not an arbitrary
name generated by the agent. Role Owner's later reuse/adoption authority is
distinct from read-only inspection approval; nothing here approves reuse.

OD-02 applies to **G0 as well as every AWS gate**. Its verified approver signs
G0's exact local paths, metadata extraction mode/output, initial executor
identity, storage/custodian and lifecycle decisions. Operator consent alone is
insufficient. The same identified authority must also have local-scope authority;
if that authority cannot be established, G0 remains NOT_AUTHORIZED. This does
not grant any AWS calls. A decision-register entry is not an approval record.

#### Approval record (required for each separate gate)

Use an existing trusted approval channel. An agent-written JSON file is only a
proposal until independently attributable human approval is bound to it.
Record `case_id`, `stage`, `scope_id`, revision/digest, approver verified ID,
operator ID, approval timestamp/expiry, approved execution mode, executor/wrapper
identity/hash, source candidate and approved principal baseline, account, role
identity, exact service/API/endpoint/Region tuples, resource IDs OR precisely
bounded discovery envelope, output field whitelist, risk exceptions, storage
root/custodian/retention deadline, request/page/resource caps, retry/rate limits,
cost acceptance and permitted recipient(s). Record explicit denial/expiry too.
G0 additionally binds trusted extractor/sanitized-input identity and digest,
initial isolation mode, and the per-class lifecycle/standing-deletion record.
Before G1, bind the source-provider/request-path attestation revision and digest
for the actual chosen execution mode. None of these records is created by
probing credentials or AWS during plan preparation.

All fields needed by that stage must be nonempty, current and verifiable. No
`PENDING`, wildcard Region, broad endpoint, all-service grant, or inferred consent
passes. G1 is the sole bootstrap exception for principal baseline: it may
observe the approved source's Account/Arn/UserId with the baseline pending, then
STOPS for G1b before any P2-P4 calls. A mismatch against an already approved
principal baseline stops immediately. Operator and approver identities are never
bootstrap exceptions. Reaching any unapproved tuple asks for NEW approval; it
does not mutate the old approval. Grant invalidation, expiry, source/tool drift
or changed input digest pauses execution.

### Region / Resource Discovery Plan

**Nothing in this subsection is executed during plan preparation.** P0's
offline preparation requires its own local-access consent. It makes no AWS
calls and does not resolve credentials.

1. G0 must select either an EXISTING human-controlled trusted extractor or a
   human-supplied, separately approved sanitized candidate-metadata document.
   The agent receives neither original AWS config read access nor a host home
   tree, credential/cache mounts or the extractor's process/debug access.
   There is no extractor implementation task. If neither safe mode exists,
   record `P0_CONFIG_DISCOVERY_BLOCKED` and ask the human for approved sanitized
   values; do not read the original config to resolve the block.
2. Only inside the trusted human boundary may an approved regular config file
   be parsed with Python `configparser` (interpolation disabled). Parsing the
   whole INI ingests its other sections/values; output whitelisting is NOT
   agent isolation. Reject symlink/path escapes and keep those contents outside
   AI access. Release only validated candidate Region, candidate STS mode,
   conflict and override-presence fields, plus approved nonsecret provenance
   and timestamp. Never release credential_process arguments, credentials,
   other profile contents or override URLs/userinfo/query strings. Synthetic
   parser tests prove filtering only, never production isolation.
3. Any separately approved inspection of `AWS_REGION`, `AWS_DEFAULT_REGION`
   or `AWS_STS_REGIONAL_ENDPOINTS` also occurs only inside that trusted boundary
   using exact-name lookups, never an environment dump. The agent may inspect
   sanitized metadata only. Overrides become the boolean
   `OVERRIDE_PRESENT_REQUIRES_HUMAN_REVIEW`; missing/conflicting values stay
   unknown. No credentials/cache/provider executables are opened or invoked
   for candidate discovery. Do not run `aws configure list`, credential export,
   an SDK session or `aws login`. The candidate profile is not a verified
   identity. Original config inspection consent is not agent filesystem access.
4. Output offline `region_candidates.json` with `source`, `candidate_region`,
   `candidate_sts_mode`, `conflict`, `observed_local_utc` and
   `authorization_state: NOT_AUTHORIZED`. Missing/conflicting/default-derived
   values remain candidates or `UNKNOWN`; no Region is silently selected.
5. An identified human explicitly selects STS Region AND exact official HTTPS
   endpoint, IAM global endpoint/signing Region, and each service's regional
   endpoints. Validate against human-approved partition/endpoint metadata
   offline. Reject custom endpoints, redirects, proxy credential interception,
   TLS bypass and unapproved endpoint configuration. Do not call AWS to resolve
   endpoints/Regions. IAM global scope is not an authorization for all Regions.
6. ECS clusters, services, tasks and task-definition ARNs must fit an approved
   Region and discovery envelope. Discovery may authorize one page at a time or
   a bounded in-account set; returned names are not automatically authorized
   for follow-up unless the approval explicitly covers discovered members.
7. S3 `ListBuckets` is account-wide discovery and may reveal out-of-Region
   names: it needs explicit account-inventory consent. If only a subset is
   approved, use human-supplied bucket IDs and mark account denominator unknown.
   A bucket `GetBucketLocation` is allowed only within approved bucket scope,
   with expected owner `168975706502`. It yields a candidate Region; null maps
   to `us-east-1` and legacy `EU` to `eu-west-1` for reporting only. No policy,
   ACL or ownership request in that Region until approved. Disable unapproved
   redirect/Region correction behavior in BOTH modes; if not demonstrable,
   no AWS calls (human-managed capture is not an exception).
8. S3Control access points are only in approved account/Regions. KMS ListKeys,
   SecretsManager ListSecrets and ECS list APIs require explicit regional
   discovery consent and bounded pagination. Never dereference external ARNs.
   For Lambda prefer exact human-provided function/version/alias ARNs and
   explicitly record qualifier coverage. No inventory approval means
   `LAMBDA_INVENTORY_NOT_COVERED`, not zero functions.

### AWS API Allowlist / Request Budget

**Candidate only; no row is approved.** Exact parameter schemas must be bound
to each scope record. Reject unknown fields, arbitrary command strings, shell
metacharacters, input files/URLs, endpoint/profile overrides, credential flags,
unapproved pagination/retry settings and caller-supplied queries. The trusted
operator chooses fixed output serializers; the agent cannot replace them.

| Stage | Candidate APIs | Resource boundary | Output whitelist / restricted data |
| --- | --- | --- | --- |
| P0 | NONE | Local approved packet/config metadata only | Sanitized metadata/candidate Regions; no provider resolution |
| P1 | `sts:GetCallerIdentity`; `iam:GetRole` | Existing source only; fixed role name/ARN/Role ID | Caller Account/Arn/UserId local only; Role Arn/RoleId/MaxSessionDuration/Path/PermissionsBoundary and trust document restricted |
| P2 | `iam:ListAttachedRolePolicies`, `iam:ListRolePolicies`, `iam:GetRolePolicy`, `iam:GetPolicy`, `iam:GetPolicyVersion` | Fixed role; approved discovered inline names; ReadOnlyAccess and attached managed ARNs within approval envelope; observed default versions only | Policy identity/dates/version metadata and full documents restricted; raw and canonical hashes shared after review |
| P3 | `ecs:ListClusters`, `ecs:ListServices`, `ecs:DescribeServices`, `ecs:ListTasks`, `ecs:DescribeTasks`; separately approved `ecs:DescribeTaskDefinition` | Only approved Regions/clusters and approved discovered services/tasks/definition ARNs | IDs/role linkage/status/counts only, specified below; never env/overrides payload |
| P4 S3 | `s3:ListBuckets`, `s3:GetBucketLocation`, `s3:GetBucketPolicy`, `s3:GetBucketAcl`, `s3:GetBucketOwnershipControls` | Approved in-account buckets, expected owner required on supported calls | Names/locations local restricted; policies/ACL/ownership data restricted; no objects |
| P4 S3Control | `s3:ListAccessPoints`, `s3:GetAccessPointPolicy` | Explicit account `168975706502`, approved Regions/access points | Inventory and policies restricted; distinguish S3Control CLI namespace from S3 IAM permission prefix |
| P4 KMS | `kms:ListKeys`, `kms:GetKeyPolicy`, `kms:ListGrants` | Approved regional in-account keys, policy name `default` | Key IDs/policy/grant principal and operation structures restricted; no decrypt |
| P4 Lambda | `lambda:GetPolicy` | Exact approved function/qualifier ARNs only | Resource policy/revision restricted; inventory denominator explicitly scoped |
| P4 Lambda exception | `lambda:ListFunctions` ONLY under separate G4-L approval | Approved Regions and maximum pages; API response sensitivity accepted by human | Emit FunctionArn only; response may contain env values, no full response retained/displayed |
| P4 Secrets Manager | `secretsmanager:ListSecrets`, `secretsmanager:GetResourcePolicy` | Approved regional in-account discovered secret ARNs | Name/ARN metadata and policy restricted; no value/description/tag disclosure in AI output |
| P5 | NONE | Approved local evidence/summary paths | Minimized artifacts and integrity/coverage metadata |

P3 field sets: DescribeServices emits `serviceArn`, `clusterArn`,
`taskDefinition`, `status`, counts and deployment task-definition references;
DescribeTasks emits `taskArn`, `clusterArn`, `taskDefinitionArn`, `lastStatus`
and necessary role-reference override ARNs only; DescribeTaskDefinition emits
`taskDefinitionArn`, `taskRoleArn`, `executionRoleArn`, `status`, `revision`.
Missing schema fields remain unknown. Env, secret refs, command overrides,
network details and arbitrary response fields are dropped. Record response
filtering in the trusted local boundary, not an agent-controlled `--query`.
DescribeTaskDefinition/GetRole/GetPolicy responses are not interchangeable:
only approved policy/trust originals may be stored; task-definition originals
must not be saved. The raw/semantic hash fields for discarded bodies are null,
not hashes invented from an unobserved raw file.

#### Proposed quantitative ceilings (NOT approved budgets)

| Stage | Initial estimate / budget model | Proposed absolute ceiling including all pages and attempts |
| --- | --- | --- |
| P0 | No AWS request | 0 |
| P1 | One caller identity + one GetRole; no pagination | 2 |
| P2 | `La + Li + I + 3*(1+M)` | 60 |
| P3 | `Lc + sum(Ls+Lt) + Ds + Dt + Dtd` | 200 |
| P4 | `Lb + 4*B + sum(Lap+AP + Lk+K+Lg + Lsec+S + F+Lf)` | 600 |
| P5 | No AWS request | 0 |

Total proposed upper bound is **862**, not a promise that all resources fit.
`L*` counts actual paginated service requests, not CLI invocations; `I` inline
policies; `M` distinct attached managed policies other than ReadOnlyAccess;
`C/B/AP/K/S/F` approved discovered clusters/buckets/access points/keys/secrets/
function qualifiers; `Ds/Dt/Dtd` actual ECS describe requests under the selected
batch size; `Lg` all grant pages summed across approved keys; `Lf` exceptional
function-inventory pages (zero by default). `La/Li` are role list pages.
Three managed-policy requests are pre GetPolicy, version document and post
GetPolicy for each approved ARN. Deduplicate by ARN/version but retain request
records. Known-list discovery APIs omitted from approval have zero requests and
unknown overall denominators. Actual inventory sizes are unknown now; do not
insert historical counts such as 162 buckets or 73 policies.

At stage approval the human replaces these ceilings with explicit per-API,
per-Region/resource-count, list-page and cumulative caps plus the formula's
current estimate. Initial proposals: concurrency 1, at most 1 AWS request/sec,
one attempt per request, **zero automatic retries**, maximum 10 pages per list
chain subject to smaller cumulative stage cap. Page size and ECS batch sizes
must be explicitly fixed by the approved tool and service limits. Missing
numeric caps block execution. Every page, denied request, hidden retry and
redirect would consume budget; an executor unable to count/control all of them
does not pass the isolation gate. Before each request verify remaining budget.
At cap, stop with `PARTIAL`/`BUDGET_EXHAUSTED`; never silently drop remaining
resources or renew the cap. A retry after throttling/timeout requires a newly
attributable human decision and remains in the cumulative ledger.

Count physical HTTP attempts at the approved egress/request boundary, including
provider traffic, retries and redirects, not just CLI invocations. The P0
attestation below must prove this in BOTH modes before G1. Unexpected auth,
destination or retry traffic remains prohibited even if budget is available;
record it as a violation, never as an allowed budget addition.

Charges are not assumed zero. The approver reviews then-current service pricing,
existing CloudTrail/data-event configuration, request quantities and account
throttle limits; no AWS billing/log/config lookup is authorized to estimate
cost. Record pricing basis/date, estimated monetary upper bound or uncertainty,
and accepted ceiling. If material cost/throttle impact cannot be bounded, reduce
approved scope or leave blocked; an agent must not accept risk for the owner.

### Credential Isolation / Secret Handling Plan

**Default while enforcement is unproven: HUMAN_MANAGED_CAPTURE_ONLY.**
No evidence currently establishes an eligible wrapper. An unrestricted agent
shell with an AWS profile is prohibited even if an API list is written down.

Mode A is available only if an EXISTING independently administered execution
boundary is demonstrated and approved at P0. It must:

- Hold source credentials and provider configuration outside the agent's
  filesystem, environment, process/debug permissions and tool surface. No AWS
  credentials/cache volume is mounted in the agent sandbox. No arbitrary CLI,
  shell, Docker daemon, credential endpoint or unrestricted network route is
  exposed. The agent cannot edit the wrapper, approvals, serializers or audit
  ledger. A script in the same unrestricted shell is NOT an isolation boundary.
- Accept typed operation requests only; validate exact API/Region/endpoint,
  account, ARN/name/qualifier, discovery membership, arguments, approval
  identity/expiry/digest and request budget. Enforce fail closed before any AWS
  connection. No wildcard API/profile/Region or generic `aws ...` tool.
- Enforce official endpoint/TLS/redirect behavior and provider settings; no
  automatic STS, reauthentication, credential export or permission escalation.
  If the existing login provider needs issuance/refresh to run, stop. Do not
  inspect cache contents to work around this. Human custodian checks existing
  credential validity without disclosing values.
- Keep full sensitive responses, stderr and exceptions inside its restricted
  boundary, discard forbidden fields before any agent visibility, never log
  response bodies in general telemetry, and enforce safe local persistence.
  Sensitive response reception requires separate consent even when filtered.
- Record tamper-resistant operator-controlled append-only pre-call and
  post-call events, canonical request digest, approval scope ID, request ordinal,
  service/operation/Region/resource alias, UTC time, attempt/page, outcome/error
  class, output hash and remaining budget. Do not log credentials, signed URLs,
  headers, raw stderr/policies or bearer material. Reconcile pre-call without
  post-call as `OUTCOME_UNKNOWN`, not success.
- Pass network-disabled synthetic fixtures for allowed requests, missing or
  expired approvals, disallowed API/endpoint/Region/resource, argument injection,
  unexpected output fields, budget exhaustion and audit failure. Record actual
  interface invocation/hash/results, not merely grep results or a vendor claim.

Mode B is mandatory if ANY requirement cannot be demonstrated: the human runs
approved operations in a separately controlled local environment; the AI has
no credentialed shell/API capability and receives only human-approved minimized
results. The human environment must still follow API scopes, no issuance,
finite budgets, output filtering, logs and restricted storage. Human execution
is not permission to broaden scope. If it also cannot protect outputs/credentials
or enforce approval, no acquisition occurs; report `BLOCKED_ISOLATION`.

#### P0 source-provider and request-path attestation (BOTH modes; before G1)

Mode B is not a bypass for provider/egress controls. During separately approved
P0, the human credential/execution custodian produces an attributable,
signed-or-equivalently-authenticated GO/NO_GO record for the ACTUAL selected
Mode A or B. It is bound to tool/runtime version/hash, configuration provenance
and digest, executor identity, scope revision and expiry. Do not include secret
values or config/cache originals. Required fields/evidence are:

- Effective provider category and chosen source; identify whether auto-assume,
  login/SSO refresh, credential_process or other refresh paths exist and how
  execution/issuance is blocked without invoking them. Unknown effective chain,
  expired source or any necessary issuance is NO_GO; an assertion that the
  profile name is readonly is not proof. This is a trusted human inspection
  outside AI access, not a request to expose or read credential secret values.
- Exact permitted egress destinations and effective endpoint/redirect/proxy
  behavior, TLS policy, request-path controls and configuration precedence.
  Block unapproved destinations/redirects before transmission. Do not use an
  AWS request, including GetCallerIdentity, to discover whether controls work.
- Effective retry configuration with one physical attempt per approved
  request, zero automatic retry/redirect, all paginated attempts accounted for.
  A setting such as `AWS_MAX_ATTEMPTS=1` is corroborating configuration only,
  not proof of provider/network behavior. Record the actual CLI/runtime's
  effective settings and how physical HTTP attempts are independently counted.
- Reproducible network-disabled tests using the existing approved interface
  or trusted human harness with synthetic provider/transport fixtures: normal
  attempt, attempted auth refresh/auto-assume, alternate destination, retry,
  redirect, lost attempt visibility and audit failure. Record invocation, tool
  identities, fixture digests, actual exit codes and observed blocking result.
  Synthetic tests alone do not prove production deployment: custodian attests
  configuration equivalence and the real enforced boundary, without live probes.
- Explicit GO/NO_GO and its limits, with fail-closed rejection on unexpected
  issuance/destination/retry OR an unobservable physical attempt. If one-attempt
  enforcement/accounting cannot be demonstrated, set
  `SOURCE_REQUEST_PATH_NOT_ATTESTED` and perform NO AWS calls, including
  GetCallerIdentity. GO does not approve G1; changed mode/tool/config/source or
  request path invalidates it and requires reassessment before further calls.

No task installs, creates or repairs a wrapper/Broker. Existing raw CLI playbook
examples are reference data only and must never be pasted into the AI shell.

### Evidence Collection and Retention Plan

Proposed external root (not created now):
`$HOME/local-restricted-evidence/AWS-MCP-STS001-SEC04-RESOURCE/<approved-run-id>/`.
This is a **proposal**, not proof of Git/sync exclusion. Before any local
evidence write the custodian approves the actual canonical path, filesystem,
access control and retention deadline. Reject paths inside ANY Git worktree,
cloud-sync root, credential/cache directory, symlink, shared/temp directory,
automatic upload/backup destination or unresolved mount. A pathname and
`.gitignore` alone do not establish exclusion. If sync/backup coverage cannot
be verified by the custodian without leaking unrelated config, stop.

Before ANY operational case-owned file write, including P0 input extraction,
metadata, audit or QA files, resolve OD-09/10 and obtain the G0-bound lifecycle
record below. This rule concerns future evidence-case execution, not `.omo/`
planning-artifact preparation. The human records prerequisite approvals through
the existing trusted approval channel, not by writing into an unapproved case
root. Otherwise `P0_CASE_WRITE_BLOCKED`; create no case directories/files.
Create only after these prerequisites and P0 local consent with `umask 077`;
directories `0700`, regular
files `0600`, approved owner only. Check ACLs/default ACLs and parent traversal
permissions as well as mode bits. Keep separate `restricted/`, `share-candidate/`,
`approved-share/`, `audit/`, `qa/` and `input/` paths. AI cannot read `restricted/`
or human audit storage. Filesystem encryption/access method is an owner choice;
no new credentials/keys or cloud storage is provisioned by this plan.
Keep human approval for each release. A share-candidate is NOT yet shareable.

P0 may safely extract the packet into the approved `input/` path: validate
member paths, reject absolute/parent traversals, symlinks, device files,
duplicates and excessive expanded sizes; extract regular expected members only,
then `sha256sum -c SHA256SUMS`. No ZIP scripts are run. Do not move/change the
original ZIP, baseline, SAR or other user files. This plan's preparation did
not perform this extraction.

Restricted records: approved trust/policy/ACL/grant originals, each with exact
saved bytes SHA-256, UTC/JST capture time, operation/target/Region/tool identity,
encoding/parse state, error/pagination state, approval scope ID and file locator.
Also retain pre/post policy version metadata. Separate CLI-output raw bytes from
wire-response bytes: if only CLI JSON is saved, label `raw_kind: CLI_JSON_BYTES`,
never imply a signed AWS wire original. Hash nested policy strings before
decoding separately when applicable. Canonical document hashing uses UTF-8,
`json.dumps(sort_keys=True,separators=(',',':'),ensure_ascii=False)` and SHA-256;
record algorithm/version, decoded representation and reject duplicate JSON
keys. Do not silently URL-decode twice. Preserve raw hash and semantic hash as
different fields. Record `RESTRICTED_METADATA_ONLY` when body retention is not
permitted; hash fields for unretained originals are null with reason.

Shared deliverables, after G5-release:

| File | Required content |
| --- | --- |
| `00_Capture_Manifest.json` | Case/status, expected vs observed IDs, approvals, source/tool/times, approved/completed Regions, operations approved/invoked, counts, page/retry budgets, errors and explicit exclusions |
| `01_IAM_Role_and_ReadOnlyAccess_Evidence.md` | Identity match facts, trust types, baseline state, policy versions, pre/post drift, raw/canonical hashes |
| `02_ECS_Role_Usage_Matrix.csv` | Stable resource aliases, Region, task/execution-role match, denominator and missing coverage; no env |
| `03_Resource_Policy_Coverage.csv` | Per-service/Region discovered/authorized/attempted/success/no-policy/denied/unknown counts and pagination state |
| `04_Principal_Grant_Risk_Register.csv` | Statement index, principal types/matches, effect, action/condition classes, path risks, raw digest, inference vs fact |
| `05_Finding_Disposition.md` | F-004/F-006 evidence/gaps and owner decisions; F-003/F-005/SEC04 boundaries unchanged |
| `06_Errors_and_Limitations.csv` | Sanitized API/error class/scope/attempt and nonexecution reason; no raw stderr |
| `07_Restricted_Raw_Index.json` | Opaque local locator aliases/relative restricted paths and hashes, custodian/retention; no raw payload, home path or secrets |
| `README_FOR_INDEPENDENT_REVIEW.md` | Acquisition vs inference, review procedure, exclusions, restricted-original access limits, owner questions |
| `SHA256SUMS` | All released files except itself; no restricted-original inclusion |

Each source record additionally includes `service`, `operation`, target alias,
`region`, `observed_utc`, raw/shared digest or null+reason, `result_state`,
`error_code`, `pagination_complete`, `sensitivity_tier`, request ordinal and
approval ID. Full locator mapping and any pseudonymization salt stay local.
Use stable opaque aliases, not guessable unkeyed hashes of names as a promise
of confidentiality. Preserve target-match booleans, PrincipalType,
AccountScope, MatchesTargetRoleArn, MatchesRoleId, MatchesSessionArnPattern,
UsesWildcardPrincipalArn, ActionWritePotential, ConditionClasses and
RawPolicySHA256. A digest or match boolean alone cannot independently prove
Statement interpretation; record `INDEPENDENT_REVIEW_RESTRICTED` and require a
different authorized raw reviewer when needed.

Evidence requirement states follow all rows in `03_EVIDENCE_REQUIREMENTS.csv`:
`NOT_EXECUTED`, `CAPTURED_PENDING_REVIEW`, `PARTIAL`, `DENIED`, `UNKNOWN`,
`NOT_APPLICABLE` with justification; `VERIFIED_LOCAL_INTEGRITY` means hashes
only. Source result codes additionally distinguish `NO_POLICY`,
`ACCESS_DENIED`, `NOT_SUPPORTED`, `FAILED`. Never use empty cells for gaps.
This plan remains `PLAN_PREPARED_PENDING_EXECUTION_APPROVAL`. Only AFTER actual
authorized acquisition and P5 technical validation may the evidence bundle use
`CAPTURED_PENDING_INDEPENDENT_REVIEW`, even if explicitly partial. A run with
zero actual evidence must use `NOT_EXECUTED` or `BLOCKED`, never captured.
Confidentiality release and independent review remain separate thereafter.

OD-10 remains `OWNER_DECISION_PENDING`. Before the first operational case-owned
write, the data owner must approve a case-limited lifecycle schedule covering
ALL classes below, with separate `review_due_utc`, `retention_expires_utc`,
pre-expiry `escalate_at_utc`, named custodian/backup, permitted uses and an
attributable standing deletion instruction. Review deadline must precede expiry;
review completion is not deletion authorization. Proposed values or this plan
do NOT authorize deletion. No enforceable schedule/instruction means no case
writes or raw capture, rather than a claimed guaranteed expiry.

| Class | Required lifecycle decision before first case write |
| --- | --- |
| Restricted originals | Review deadline and actual expiry, exact case-scoped deletion authority, reviewer-access cutoff and legal-hold process |
| Local aliases/mappings/salts | Separate expiry and deletion authority; no longer retention inferred from raw deletion |
| Transient/filter/input working copies | Defined shortest necessary lifetime/expiry, cleanup trigger and standing deletion authority; never credential/cache contents |
| QA and audit records | Their own review/expiry and authorized independent custodian deletion, including append-only/immutable retention constraints; AI cannot erase human audit storage |
| Share-candidate and local approved-share copies | Explicit per-class expiry and deletion scope; release does not silently extend retention |
| External recipient copies | Separate retention/deletion acknowledgement before release via OD-14; sending party cannot attest remote deletion it cannot verify |

The schedule may distinguish class deadlines; none is silently indefinite.
If a class is not yet permitted to exist, mark `NOT_CREATED_NO_WRITE` with an
explicit prohibition on creating it until its lifecycle decision is approved.
Reviewer identity/recipient decisions can remain pending for G0 only while no
release occurs. Approval records and deletion receipts also need a separately
approved custodian/retention disposition; do not delete the authority record
before its authorized actions can be audited.

At the pre-agreed escalation time, missing reviewer disposition or risk of a
legal hold is escalated to the named data/legal owner. At expiry, if no valid
hold exists, the custodian executes the PRIOR standing case-limited instruction
even if review or a fresh deletion reply is absent. No additional ad hoc consent
is required for that preauthorized action. Earlier deletion or a scope change
needs specific new consent. An applicable legal hold overrides scheduled
deletion only through the documented authorized hold process: record hold
authority/reason, restricted access, next review deadline and notify the owner;
mark `RETENTION_EXCEPTION_LEGAL_HOLD`, stop ordinary processing/new collection,
and do not claim the original expiry was met. Review incompletion or silence
alone is not a hold. If deletion is technically blocked/fails without a valid
hold, record `RETENTION_BREACH`, cease collection/release, restrict access and
escalate immediately; never silently extend expiry or report deletion success.

For authorized cleanup enumerate exact case-owned files/classes from the
manifest; verify canonical root/no symlinks and ownership before deletion.
Exclude home trees, AWS config/cache/credentials, Git and unrelated files.
Record hashes/aliases, deletion UTC, operator, authority reference and residual
copies; verify listed files absent and reconcile approved local backup/snapshots.
Unlink is not guaranteed erasure on SSD/COW/backups; existing owner-approved
cryptographic erasure only if available, otherwise disclose residual risk.
Neither this R1 nor independent review grants a standing deletion instruction.

### Stop Conditions / Failure Matrix

Global stop action: stop scheduling, preserve only permitted safe local evidence
and audit events, emit a sanitized failure code to the named approver, invalidate
the current gate when applicable, and wait. No fallback/privilege escalation.
Do not echo unexpected secret data while reporting a stop.

| Trigger | State / disposition | Resume condition |
| --- | --- | --- |
| Missing approver/operator, scope, Region, endpoint, retention or expiry | `BLOCKED_APPROVAL` | New complete attributable approval; no API attempted |
| Candidate Region differs/conflicts or new Region/resource discovered | `SCOPE_PENDING` / `NOT_COVERED` | Separate explicit scope amendment, never auto-select |
| Account, Role ARN or Role ID mismatch | `STOP_IDENTITY_MISMATCH` | Human incident review; no automatic resume or retargeting |
| Principal baseline pending after P1 | `SOURCE_PRINCIPAL_BASELINE_PENDING` | G1b baseline decision then separate next-stage approval |
| Approved source principal/provider/tool changes or credentials expired | `STOP_SOURCE_DRIFT` | Human reassessment; no issuance/refresh under this plan |
| Isolation, audit, output filter or endpoint enforcement unproven | `BLOCKED_ISOLATION` | Human-managed safe alternative approved; otherwise no capture |
| No trusted config extractor or approved sanitized metadata | `P0_CONFIG_DISCOVERY_BLOCKED` | Human supplies approved sanitized candidate values; agent never opens original config |
| Both-mode provider/request-path attestation missing, stale or NO_GO | `SOURCE_REQUEST_PATH_NOT_ATTESTED` | Attributable GO with demonstrated no-issuance/one-attempt/egress controls before G1; no identity probe |
| Per-class lifecycle or standing deletion instruction absent | `P0_CASE_WRITE_BLOCKED` | G0-bound lifecycle approval before any operational case-owned write |
| Expiry reached with authorized legal hold / failed deletion without hold | `RETENTION_EXCEPTION_LEGAL_HOLD` / `RETENTION_BREACH` | Restrict access and escalate under lifecycle schedule; no silent extension or false deletion success |
| Unexpected API/network request, redirect, write or issuance | `STOP_UNEXPECTED_OPERATION` | Incident handling by human; do not conceal or self-remediate |
| Suspected secret exposure | `STOP_SECRET_EXPOSURE` | Human incident procedure; do not copy/exfiltrate evidence or rotate credentials autonomously |
| AccessDenied | `DENIED` / `UNKNOWN_ACCESS_DENIED` | No retry; optional new approval, never another profile |
| NoSuchBucketPolicy / valid missing resource policy | `NO_POLICY` for that exact path/time | Continue only other explicitly approved independent targets |
| NoSuchRole after identity lookup, inconsistent resource identity | `STOP_IDENTITY_OR_RESOURCE_CHANGED` | Human review; not evidence of no permission |
| NoSuch resource after fresh discovery | `UNKNOWN_RESOURCE_CHANGED` | Record race; further independent targets only within scope |
| UnsupportedRegion/API | `NOT_SUPPORTED` / `NOT_COVERED` | No regional/service expansion |
| Timeout/throttle/5xx or transport uncertainty | `FAILED` / `OUTCOME_UNKNOWN` | Stop current chain; retry only newly approved within ledger |
| Request/page/resource/cost cap reached | `PARTIAL`, `BUDGET_EXHAUSTED` | New scoped budget approval; preserve unfinished token locally only |
| Token loop/truncated listing/missing last page | `PARTIAL_PAGINATION` | Investigate offline; never claim denominator complete |
| Default policy version changes pre/post | `DRIFT_DURING_CAPTURE` | Preserve both metadata records; owner decides bounded recapture |
| No approved policy baseline | `NO_APPROVED_BASELINE` | Owner baseline decision; no drift-safe claim |
| Cross-account/extra-service pathway | `NOT AUTHORIZED`, `NOT_COVERED` | No acquisition under current plan |
| Raw unavailable to independent reviewer | `INDEPENDENT_REVIEW_RESTRICTED` | Approved separate raw reviewer, not hash-only closure |
| Storage modes/ACLs/sync boundary/hash integrity fail | `STOP_STORAGE_OR_INTEGRITY` | Human-controlled remediation/new approved storage; no silent chmod/move of unrelated files |

AccessDenied/no-policy are recorded target outcomes, not global safety claims.
Unexpected behavior stops the stage; expected per-target denials may proceed
only if the approved scope expressly permits independent remaining targets.

### Stage specifications P0-P5

Each row complements the common approval schema, allowlist and budget above;
none is an executable approval.

| Stage | Resources / Regions | Output / main sensitivity risk | Stop / completion |
| --- | --- | --- | --- |
| P0 | Approved packet, sanitized config metadata and external storage candidate; no AWS Region authorized | Trusted human extraction only, never agent config access; readiness and both-mode provider/request-path attestations | G0 requires OD-02 local approver and lifecycle authority before case writes; full source/request-path GO completed during approved P0 before G1; otherwise blocked |
| P1 | Fixed account/role and source; STS Region/endpoint PENDING, IAM endpoint/signing Region separately pending | Caller fields and role trust restricted; principal names/ExternalId sensitive | Two request ceiling proposed; mismatch stops immediately; complete observed expected-ID comparisons, then pause at G1b if principal baseline pending |
| P2 | Fixed role/ReadOnlyAccess and approved attached/inline discovery; IAM global endpoint only | Full approved policy docs local restricted; raw/canonical hashes, observed versions and baseline state | 60 ceiling proposed; unknown list completion/cap/drift explicit; complete snapshot disposition of all discovered entries or accepted partial record |
| P3 | Approved ECS Regions/clusters/services/tasks/definitions, all Region choices PENDING | Minimized role usage matrix/counts; full env-bearing responses prohibited from persistence | 200 ceiling proposed; unexpected sensitive output/schema stops; complete bounded inventory and task/execution role matches with service-external tasks and override gaps stated |
| P4 | Approved in-account S3 scope; S3Control/KMS/Lambda/Secrets Regions PENDING; cross-account NOT AUTHORIZED | Restricted policy/ACL/grant originals and minimized risk register; no payload | 600 ceiling proposed; new scope, redirection, cap or leak stops; complete per-resource/path outcomes, denominator/page state and explicit unknowns |
| P5 | Local approved captured records only; Region fields summarize actual scope, not new calls | Candidate then approved summary package; inference and mapping can leak identity | Zero AWS; stop release on confidentiality/integrity failure; complete all manifest/CSV/schema/hash/coverage checks and human release record or retain local candidate |

For each stage's approver, prerequisites and completion gate use the Stage
Approval Matrix. P2/P3/P4 completion may be `PARTIAL` with exact missing rows;
the approver explicitly accepts that disposition before the next gate. No later
stage is automatically authorized by recording partial completion.

### Owner Decision Register

All entries remain open. They are decisions for future stage approval, not
questions that block writing this plan.

| ID | Decision / current value | Owner | Blocks |
| --- | --- | --- | --- |
| OD-01 | Human Operator `IDENTITY_PENDING` | Human organization | P0 local execution onward |
| OD-02 | Execution Approver verified ID plus local G0 and AWS authority `IDENTITY_PENDING` | Account/local authorization authority | G0 local scope AND every AWS gate; operator consent alone insufficient |
| OD-03 | STS Region and exact endpoint `PENDING`; IAM endpoint/signing Region pending | Execution Approver | P1 |
| OD-04 | Existing valid source and both-mode source-provider/request-path attestation GO pending; principal baseline pending | Credential/execution custodian / Execution Approver | GO before G1; no identity-probe exception; G1b baseline separately blocks P2-P4 |
| OD-05 | ECS Regions, clusters/enumeration envelope and DescribeTaskDefinition response-risk consent | Workload custodian / Execution Approver | P3 |
| OD-06 | S3 account inventory consent vs exact subset, bucket/AP scope and approved Regions | Resource custodian / Execution Approver | P4 S3 |
| OD-07 | KMS/Lambda/Secrets Regions and resource/qualifier envelopes; Lambda ListFunctions exception default denied | Resource custodian / Execution Approver | P4 respective subscopes |
| OD-08 | Initial human-only/trusted extraction mode before G0; full eligible Mode A proof or Mode B controls during approved P0 | Security/execution custodian | G0 metadata boundary selection; full proof plus both-mode attestation before G1 |
| OD-09 | Canonical storage path, sync/backup exclusion, ACLs/encryption/custodian | Data custodian | Before G0 case-owned writes, not just raw capture |
| OD-10 | Per-class review deadline, actual expiry, escalation and attributable standing deletion/hold instruction `OWNER_DECISION_PENDING` | Data owner / authorized audit custodian | Before ANY operational case-owned write; actual deletion requires separately granted authority |
| OD-11 | Per-stage/per-API numeric page/resource/request/cost/rate caps | Execution Approver | Each AWS stage |
| OD-12 | Owner-approved policy baseline and missing Draft/R2/SAR references | Requirements/policy owner | Comparison conclusions only; missing reference explicit |
| OD-13 | Role reuse/noninterference `APPROVAL_PENDING` | Role Owner | Reuse/adoption (always out of scope), not inferred from inspection |
| OD-14 | Summary/original release recipients, confidentiality approval, independent raw reviewer | Data owner / independent reviewer | Sharing and restricted independent checks |
| OD-15 | Future cross-account/other-path investigation | Account/resource owners | NOT AUTHORIZED; requires new approved scope, not automatic follow-up |

#### OD / G0 eligibility mapping (R1)

| Timing | Must close / may remain pending | Result if incomplete |
| --- | --- | --- |
| Before G0 local execution | OD-01 verified operator; OD-02 verified local approver and attributable G0 scope; OD-08 initial isolation/extraction mode; OD-09 exact allowed paths/custodian; OD-10 per-class lifecycle/standing deletion authority before first write | G0 NOT_AUTHORIZED; no sensitive local execution or case-owned writes |
| During authorized P0, before G1 | OD-04 effective provider validity and both-mode request-path attestation; OD-08 full selected execution-mode proof; OD-03 exact STS/IAM endpoint/Region; OD-11 P1 physical-attempt/cost scope; separate G1 approval | No AWS calls, including GetCallerIdentity |
| After P1, before G2 | G1b observed source-principal baseline adoption; separate G2 scope | No P2-P4 calls |
| May stay pending at G0 | OD-03/04 (until above gate); OD-05 ECS at G3; OD-06/07 resources at G4; OD-11 AWS budgets until corresponding gate; OD-12 comparison baseline; OD-13 out-of-scope reuse; OD-14 before sharing/raw review; OD-15 NOT AUTHORIZED | No inferred later-stage approval; G0's exact local sub-scope still needs consent |

Equal pre/post ReadOnlyAccess versions are a time-bounded observation, not a
permanent managed-policy pin or future drift prevention. Preserve version ID,
digest and capture times; any future operational use requires its independently
approved later comparison. This adds no API to the current plan or approval.

### Executor handoff prompt (literal)

> You are Investigation B's acquisition planning/execution handoff recipient,
> not Role Owner, Gate approver, Broker implementer or the independent evidence
> reviewer. Read this ENTIRE plan and all packet contracts, with the user's
> latest restrictions taking precedence. Current status is
> PLAN_PREPARED_PENDING_EXECUTION_APPROVAL. Receipt of this prompt, a start-work
> command or a checked task is NOT AWS/local-sensitive execution approval.
> Preserve the fixed commit, expected Account 168975706502, Role ARN
> arn:aws:iam::168975706502:role/scs2-stg-ecs-tasks-role and Role ID
> AROASOV54VGDAC4S2255I. They are not observed matches. aws-mcp-readonly is only
> a source candidate. Operator/approver identities, STS endpoint/Region,
> regional/resource scopes, principal baseline and retention decisions remain
> pending. Stop and present the exact next-stage approval record to a human.
> Do not resolve pending fields yourself. P0 has zero AWS calls and must itself
> have local-read/storage consent. Each P1-P4 stage needs a fresh attributable
> scope approval; no approval propagates. P5 sharing needs confidentiality
> release. Use an existing proven independent enforcement boundary only, never
> arbitrary credentialed AI CLI. If unproven use HUMAN_MANAGED_CAPTURE_ONLY,
> or report BLOCKED_ISOLATION. Do not implement a wrapper/Broker. Do not access,
> export, issue, refresh or print credentials/cache, change IAM/GitHub, deploy,
> activate MCP, switch profiles/Regions, perform DryRun/simulation or fetch
> secret/object/log contents. Capture only authorized policy/metadata evidence
> locally outside Git/sync, with approved retention and 0700/0600/umask077.
> Record every request/page/attempt, error, denominator and explicit gap. Stop
> on mismatched identity, scope/endpoint drift, exhausted budget, unexpected
> request, isolation failure or suspected disclosure. Never turn a denial or
> incomplete inventory into NO_GRANTS/SAFE. Hash raw and canonical documents
> separately; preserve all baseline/findings/SAR originals unchanged. Generate
> the ten specified shared files only as minimized candidates, release only
> after human confidentiality approval, and mark inaccessible raw verification
> INDEPENDENT_REVIEW_RESTRICTED. Only after actual authorized capture may the
> evidence package say CAPTURED_PENDING_INDEPENDENT_REVIEW. Never close a
> finding or approve reuse/implementation. After any completed stage, STOP for
> its separate next gate. If no execution approval exists, do no AWS work.
> R1: Before G0 resolve the local approver, trusted metadata boundary and
> per-class lifecycle/standing deletion authority; never read original AWS config
> in the AI sandbox. Before G1 require the attributable both-mode source-provider
> and physical-request-path GO record; human execution is not an exception. An
> unobservable attempt or required refresh blocks even GetCallerIdentity.

### Dependency matrix
| Todo | Depends on | Blocks | Can parallelize with |
| --- | --- | --- | --- |
| 1 | Separate P0 local consent | 2 | Offline packet integrity only |
| 2 | 1 | 3, G1 | None requiring credentials |
| 3 | 2 + G1 | 4 | None |
| 4 | 3 | G1b, G2 | Offline only |
| 5 | 4 + G1b + G2 | 6 | None |
| 6 | 5 | G3 | Offline only |
| 7 | 6 + G3 | 8 | None |
| 8 | 7 | G4 | Offline only |
| 9 | 8 + G4 | 10 | None |
| 10 | 9 | G5 | Offline only |
| 11 | 10 + G5 | 12 | Offline coverage reconciliation |
| 12 | 11 + G5-release if sharing | F1-F4 | Final verifiers after completion |

## Todos
> Implementation + Test = ONE todo. Never separate.
<!-- APPEND TASK BATCHES BELOW THIS LINE WITH edit/apply_patch - never rewrite the headers above. -->
- [ ] 1. P0: establish local input, approval and storage readiness
  What to do / Must NOT do: Under separately approved P0 local consent, check
  packet integrity, safe extraction, source-reference availability, named
  actors and proposed external storage/retention. No AWS/config/credential
  access now. Before future case-owned writes require G0/OD-02 and OD-09/10
  per-class lifecycle authority; never give original config to the agent.
  Do not change original inputs.
  Parallelization: Wave 1; blocked by P0 consent; blocks 2.
  References: packet 00; 01 sections 1, 3 P0; 02 approval gate; 06 sections 1-2;
  this plan's approval/storage/decision-register sections.
  Acceptance: `sha256sum -c SHA256SUMS` in approved input directory succeeds;
  Python 3 `zipfile` member checks reject unsafe members; `stat` confirms all
  approved created directories/files 0700/0600 and approved owner. Written
  sync/backup and per-class lifecycle/standing deletion decisions exist before
  any case write; tests cannot grant that consent. G0 local approver is verified.
  QA: happy = Python 3 ZIP inspection plus sha256sum on valid packet; failure =
  synthetic ZIP with ../ member and copied fixture with wrong digest rejected,
  never mutate original. Missing approver/expiry/deletion-authority fixture
  rejects case writes. Evidence `qa/task-1.json` only after lifecycle approval.
  Commit: N; no Git/GitHub operation.

- [ ] 2. P0: document offline Region candidates and enforce isolation gate
  What to do / Must NOT do: After G0 consent, trusted human extractor or approved
  sanitized document supplies candidate metadata; agent cannot read AWS config.
  Determine existing wrapper proof or human-only mode. Record
  AWS executable version/hash through the human environment without invoking
  provider resolution. No provider/cache/credential inspection or AWS calls.
  Parallelization: Wave 1; blocked by 1; blocks G1/3.
  References: 01 P0; 04 candidate API list (superseded for DescribeRegions);
  05 Region/sensitivity caveats; this plan's discovery/isolation sections.
  Acceptance: candidate Regions have NOT_AUTHORIZED; all actual execution
  settings remain pending until human approval. Mode A proof binds real existing
  tool hash, exact fixture-test invocation and actor isolation; absent proof
  yields HUMAN_MANAGED_CAPTURE_ONLY, not claimed pass. BOTH modes require the
  attributable source-provider/request-path attestation GO before G1; otherwise
  no AWS calls including identity. Synthetic parser pass is not isolation proof.
  QA: happy = `python3` with `configparser` on synthetic config emits only
  region/mode; failure = fixture containing credential_process/secret-looking
  fields/custom URL produces no such values and override flag only. Existing
  boundary offline fixture rejects region/API injection; unavailable interface
  records BLOCKED. In both-mode synthetic transport fixtures, refresh/auto-assume,
  hidden retry/redirect, wrong endpoint or unobservable physical attempt rejects
  GO; inspect real boundary/configuration-equivalence attestation separately.
  Evidence `qa/task-2.json`.
  Commit: N.

- [ ] 3. P1: obtain explicitly approved source and role identity records
  What to do / Must NOT do: Only after G1, permitted execution environment
  performs GetCallerIdentity then GetRole under two-request cap. Compare
  expected account before role query; mismatch prevents second request.
  No role assumption, automatic login/refresh or alternative source.
  Parallelization: Wave 1; blocked by 2/G1; blocks 4.
  References: 01 P1; 03 E-ID-01..03; 04 STS/IAM P1; 02 fixed identity;
  this plan's G1 bootstrap exception and budget.
  Acceptance: actual request ledger length <= approved cap; sequence identity
  then role; expected/observed fields distinct; all raw data restricted. G1 binds
  current both-mode provider/request-path GO; no CLI-count substitute for
  physical-attempt accounting or provider-issuance exception.
  QA: happy = approved existing offline identity verifier run on matching
  synthetic fields using its P0-recorded invocation; failure = account mismatch
  fixture records STOP and zero subsequent requests; actual AWS mismatch is
  never intentionally induced. Evidence `qa/task-3.json`.
  Commit: N.

- [ ] 4. P1: reconcile source baseline and trust identity without adoption
  What to do / Must NOT do: Classify role trust Principal/Condition locally
  within human boundary, hash permitted raw; prepare source observation for
  human G1b decision. Pending baseline blocks P2-P4, not filled by the agent.
  Parallelization: Wave 1; blocked by 3; blocks G1b/G2.
  References: 01 P1; 06 principal/minimization contract; 03 E-ID-03;
  this plan's status/failure matrices.
  Acceptance: ARN and Role ID comparisons both recorded; source Arn/UserId not
  broadly shared; absent baseline remains SOURCE_PRINCIPAL_BASELINE_PENDING;
  no trust/role reuse approval inferred.
  QA: happy = Python 3 parse sanitized identity/trust summary and verify linked
  digest; failure = RoleId mismatch or missing baseline fixture blocks next
  stage using actual gate validation. Evidence `qa/task-4.json`.
  Commit: N.

- [ ] 5. P2: capture bounded role policies and managed-policy versions
  What to do / Must NOT do: After G2, enumerate approved role attached/inline
  policies with explicit pages, fetch approved default versions only and pre/post
  GetPolicy per ARN; deduplicate ReadOnlyAccess. No boundary-document fetch just
  because a boundary ARN was observed; no unrelated policy lookup.
  Parallelization: Wave 1; blocked by 4/G1b/G2; blocks 6.
  References: 01 P2; 03 E-IAM-01..05; 04 IAM P2; this plan's formula/boundaries.
  Acceptance: each discovered entry has outcome, page ledger and approved ARN;
  version document linked to pre/post metadata; no cap overshoot.
  QA: happy = Python 3 JSON/CSV parsing and ledger reconciliation of synthetic
  multipage policy capture; failure = repeated continuation token, unapproved
  attached ARN or next-page-over-cap rejects continuation and marks PARTIAL.
  Evidence `qa/task-5.json`.
  Commit: N.

- [ ] 6. P2: verify byte/semantic integrity and record baseline limitations
  What to do / Must NOT do: Compute approved saved-byte and canonical document
  hashes, compare default versions; report DRIFT_DURING_CAPTURE or
  NO_APPROVED_BASELINE honestly. Preserve originals and existing findings.
  Parallelization: Wave 1; blocked by 5; blocks G3.
  References: 01 P2/P5; 06 F-004; this plan's hashing/retention sections.
  Acceptance: `sha256sum -c` verifies permitted local captures; Python 3 stdlib
  canonicalization uses specified algorithm; no approved-baseline assertion
  without externally attributable owner evidence. Matching pre/post versions
  prove neither permanent pinning nor prevention of future drift.
  QA: happy = equivalent JSON with reordered keys has equal canonical hashes
  but different saved-byte hashes; failure = duplicate keys rejected and
  pre/post version drift blocks stable-version claim. Evidence `qa/task-6.json`.
  Commit: N.

- [ ] 7. P3: capture approved ECS reference inventory with field filtering
  What to do / Must NOT do: After G3 enumerate approved cluster/service/task
  scope, including approved non-service tasks; retrieve definition fields only
  with separate sensitive-response consent. No env/secret values/raw definition
  persistence, no execution/update or broad historical-definition scan.
  Parallelization: Wave 2; blocked by 6/G3; blocks 8.
  References: 01 P3; 02 item 4; 03 E-ECS-01..03; 04 ECS; field sets above.
  Acceptance: independent response filter produces only fixed fields; recorded
  definition/override omissions remain UNKNOWN; counts/pages fit approved scope.
  QA: happy = offline existing filter on synthetic task-definition response
  emits role refs only; failure = embedded env/secret/command fields absent
  from all files/output and filter failure stops processing. Use P0-recorded
  interface, not arbitrary AWS CLI query. Evidence `qa/task-7.json`.
  Commit: N.

- [ ] 8. P3: reconcile ECS role usage and noninterference limitations
  What to do / Must NOT do: Build stable-alias matrix of task/execution-role
  matches, service/deployment/running and non-service scope. Record missing
  overrides, old revisions, unavailable Regions and actual denominators.
  Do not claim production-wide noninterference or future safety.
  Parallelization: Wave 2; blocked by 7; blocks G4.
  References: 01 P3; 03 E-ECS-02/03; this plan's OD-05/13.
  Acceptance: CSV parses with Python 3 csv module; discovered/authorized/
  described distinct counts reconcile; Role Owner stays APPROVAL_PENDING unless
  separate external evidence says otherwise (never grants reuse in this plan).
  QA: happy = synthetic taskRole vs executionRole cases classify separately;
  failure = unobserved Region or missing definition produces UNKNOWN not false
  nonuse. Evidence `qa/task-8.json`.
  Commit: N.

- [ ] 9. P4: capture bounded resource policies, ACLs and grants
  What to do / Must NOT do: After per-service G4 approvals perform only
  allowlisted S3/S3Control/KMS/known Lambda/Secrets operations. Check expected
  bucket owner, approve candidate Regions before follow-up; collect all approved
  pages within budgets. Lambda inventory denied by default. No external fetch.
  Parallelization: Wave 2; blocked by 8/G4; blocks 10.
  References: 01 P4; 03 E-S3/E-KMS/E-LAMBDA/E-SECRET/E-EXT rows;
  04; 05 service caveats; this plan's budget/discovery sections.
  Acceptance: every approved resource/path has SUCCESS/NO_POLICY/DENIED/
  UNKNOWN outcome with scope/page evidence, never inferred absence; budget and
  exact endpoint/resource tuple verified before each request.
  QA: happy = synthetic multipage key/grant and bucket inventories reconcile;
  failure = AccessDenied differs from NoSuchBucketPolicy, external key and
  unauthorized bucket Region rejected without any follow-up request. Existing
  offline replay invocation recorded at P0. Evidence `qa/task-9.json`.
  Commit: N.

- [ ] 10. P4: classify policy pathways with evidence/inference separation
  What to do / Must NOT do: Analyze approved statements for direct session ARN,
  role ARN/RoleId, wildcard Principal plus PrincipalArn, cross-account and
  service principals, NotPrincipal/NotAction/conditions/tags, KMS grants and ACL
  pathways. Treat explicit Deny separately from implicit Deny. Do not execute
  authorization experiments or infer effective access without actual context.
  Parallelization: Wave 2; blocked by 9; blocks G5.
  References: 01 P4/P5 and its official IAM evaluation links; 06 F-006;
  this plan's minimized risk fields and external exclusions.
  Acceptance: every risk row points to approved original hash/statement index,
  classification rationale and unresolved condition/context; missing raw access
  explicitly INDEPENDENT_REVIEW_RESTRICTED.
  QA: happy = offline synthetic direct-session vs role-principal cases remain
  separate; failure = NotAction/unknown condition/NotPrincipal fixture cannot
  produce SAFE/no-write result. Verify with Python 3 parsed report and
  independent human-managed local policy review, not a live IAM simulator.
  Evidence `qa/task-10.json`.
  Commit: N.

- [ ] 11. P5: assemble minimized candidate bundle and full coverage ledger
  What to do / Must NOT do: After G5 create all ten named deliverables locally,
  map EVERY requirement CSV row, reconcile denominators/pages/errors and
  principal-risk evidence. No raw originals in candidate bundle or AI context.
  Parallelization: Wave 2; blocked by 10/G5; blocks 12.
  References: 02 submissions; all 03 rows; 06 manifest/review schema;
  this plan's output/retention/failure sections.
  Acceptance: Python 3 json/csv parsing confirms required manifest fields and
  no blank requirement states; counts reconcile with actual ledger, counts
  outside authorized Regions are UNKNOWN rather than zero. Zero capture means
  NOT_EXECUTED/BLOCKED, never CAPTURED.
  QA: happy = synthetic successful+denied+unexecuted entries remain distinct;
  failure = missing requirement, dangling source hash or fabricated global
  denominator fails validation. Evidence `qa/task-11.json`.
  Commit: N.

- [ ] 12. P5: verify release, independent-review access and retention handoff
  What to do / Must NOT do: Validate file integrity/minimization; obtain
  confidentiality G5-release before approved-share/recipient delivery; identify
  separate reviewer and raw-access gaps. Document future approved deletion
  procedure and preauthorized expiry schedule; this task grants no deletion or
  upload. Missing fresh consent/review does not suspend a valid standing
  expiry-deletion instruction; handle hold/failure as specified. Stop after handoff.
  Parallelization: Wave 2; blocked by 11, release gate for sharing; blocks F1-F4.
  References: 06 sections 1/4/5; this plan's retention and status rules.
  Acceptance: `sha256sum -c SHA256SUMS` on release candidate; stdlib JSON/CSV
  validation; custody record proves human approval bound to exact file hashes;
  evidence status only pending independent review, unchanged findings/Gate.
  QA: happy = approved synthetic bundle hash/list matches release record;
  failure = changed file after approval, absent confidentiality grant or raw
  policy accidentally packaged blocks release; restricted-original access
  denied to reviewer remains explicit. Offline expiry fixtures distinguish prior
  standing authority with no review reply (delete exact authorized class), legal
  hold (restrict/escalate), missing authority (block original writes), and failed
  deletion (RETENTION_BREACH); reconcile all local/recipient classes.
  Evidence `qa/task-12.json`.
  Commit: N.

## Final verification wave
> Runs in parallel after ALL todos. ALL must APPROVE. Surface results and wait for the user's explicit okay before declaring complete.
- [ ] F1. Plan compliance audit
  Scope: Independently check actual approval/request ledgers against every
  stage tuple/cap and actual evidence vs plan. Use Python 3 JSON/CSV
  reconciliation and approved audit export; no AWS calls. Happy: exact match;
  failure: one unapproved attempt prevents approval. `qa/F1.json`. Commit: N.
- [ ] F2. Code quality review
  Scope: No product code changes are expected. Review existing enforcement
  proof and offline validation evidence, serializer/schema/digest accuracy;
  absence of proof is not pass. Happy: hashes/interface tests attributable;
  failure: generic credentialed CLI or invented checker result rejected.
  Python 3/sha256sum read-only checks. `qa/F2.json`. Commit: N.
- [ ] F3. Real manual QA
  Scope: Hands-on LOCAL artifact QA by separate reviewer, never AWS probing.
  Parse actual delivered files, run `sha256sum -c SHA256SUMS`, inspect sanitized
  representative success/denial/unknown and pagination reconciliation; raw
  reviewer must be separately authorized. Happy: review reproducible; failure:
  unavailable raw evidence marked restricted, not independently verified.
  `qa/F3.json`. Commit: N.
- [ ] F4. Scope fidelity
  Scope: Compare final bundle and untouched baseline/findings/SAR references
  with fixed hashes and all exclusions. Happy: no unauthorized changes or
  closure; failure: current HEAD substituted, pending owner promoted, secret
  original included, or zero-evidence CAPTURED state rejects delivery.
  Python 3 metadata/hash checks. `qa/F4.json`. Commit: N.

These four checks concern FUTURE authorized evidence collection, not a claim
they ran during plan preparation. Run them only with approved local access;
all must report their scope, actual checks, gaps and verdict. A passing technical
check cannot manufacture confidentiality approval, raw access or owner adoption.

## Commit strategy

No commits, pushes, PR changes or GitHub operations. Plan artifacts only under
`.omo/`; future raw/shared evidence outside Git. Preserve the existing untracked
input ZIP and unrelated worktree changes. Do not stage or chmod original inputs.
Product-code and Broker/wrapper changes require a different authorized task.

## Success criteria

Plan preparation succeeds when this one document contains the nine requested
deliverables, all P0-P5 fields and six independent gates, explicit pending
identities/Regions/retention, a human-managed fallback, finite proposed request
caps, stop conditions and a self-contained executor prompt. Planning changes
only `.omo/` artifacts. Current completion means **execution approval pending**,
not an AWS stage completed.

Future acquisition succeeds only within independently approved stages and
measured scope: permitted hashes, request/page/count ledgers, limitations,
minimized human-released outputs and independent-review handoff. Partial/denied
coverage is acceptable only when explicit; it cannot establish global safety.
Never change baseline/finding/SAR evidence, approve reuse or close the Gate.
Stop at `PLAN_PREPARED_PENDING_EXECUTION_APPROVAL` now. No action follows until
the human grants the specific local/AWS stage approval in the execution session.
