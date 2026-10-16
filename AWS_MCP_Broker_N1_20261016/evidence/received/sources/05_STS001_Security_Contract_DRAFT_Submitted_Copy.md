# AWS MCP Gate STS-001 — Existing-Role Credential Broker Security Contract

- Date: 2026-10-14 (JST)
- Status: **DRAFT FOR INDEPENDENT REVIEW — NOT APPROVED; NO IMPLEMENTATION AUTHORIZATION**
- Repository: `yohi/chatgpt-mcp-tunnel`
- Reference branch: `feat/aws-broad-iam-read-api-tools` (reviewed at GitHub HEAD `05f4b92e7ff2de76dc79cf8d5dc9f563a03af209`)
- Scope: Broker, STS session policy, credential publication/consumption, security tests and runtime isolation for reusing an **existing** IAM role
- Out of scope: IAM resource mutations, new IAM role/policy, production activation, AWS MCP connection, or edits to PR #10

## 1. Objective and boundary

Allow broad AWS information retrieval through an MCP runtime without handing it the administrator's `aws login` credentials or granting it AWS write powers. Reuse an existing IAM role **only if** restrictions can be independently verified. This document does **not** assert SEC-04 or Gate STS-001 has passed.

**Candidate — not production-approved:**

| Attribute | Evidence / pinned candidate |
|---|---|
| AWS account | `168975706502` |
| Role ARN | `arn:aws:iam::168975706502:role/scs2-stg-ecs-tasks-role` |
| Role ID | `AROASOV54VGDAC4S2255I` |
| Role maximum session duration | 3,600 seconds |
| Role permissions boundary | None |
| Existing attached permissions | `AdministratorAccess` observed earlier; shared with existing workloads |
| Original source | `aws login` profile `aws-mcp-readonly`; administrator credentials visible only to authenticated source/Broker container |
| Managed session policy | `arn:aws:iam::aws:policy/ReadOnlyAccess` |
| Additional policy | **Reviewed inline explicit-Deny session policy, canonical digest to be fixed** (not yet approved) |

A role name, profile name, `--read-only` flag, prompt, or IAM policy name is never evidence of write prohibition. The role's administrative permissions make the session-policy control safety-critical. The source administrator and the Broker itself remain privileged trust components; these guarantees address a normally operating or compromised *MCP runtime*, **not** an attacker who has already taken over the source or Broker and can issue unrestricted STS requests.

## 2. Normative Broker contract (proposal)

**B-01 — No IAM mutation.** Neither Broker, bootstrap flow, nor activation path may call IAM Create/Update/Delete/Attach/Detach or alter the existing role, trust policy, ECS use, or account policies. Reuse of the candidate role is conditioned on an independent owner/security decision. Historical temporary-role bootstrap is excluded from this deployment and must not be invoked with `--apply` or `--cleanup` against the existing role.

**B-02 — Pinned identity.** Before each issuance, use source credentials only inside Broker to validate exact account, source principal, expected role ARN and `iam:GetRole().RoleId` and role configuration. Fail closed on missing or mismatched data. Trust-policy/config drift must trigger reevaluation, not silent adoption. Runtime-configurable role ARN is not sufficient without immutable approved configuration and digest verification.

**B-03 — Required STS request.** The sole issuance call is `sts:AssumeRole` on the pinned ARN with exactly the reviewed managed `PolicyArns=[{"arn":"arn:aws:iam::aws:policy/ReadOnlyAccess"}]` and a canonical, digest-pinned inline `Policy`. Both arguments are mandatory and asserted in code; no retry may omit either. Session duration <= 3600 seconds, session name begins `aws-mcp-sts001-` and includes an issuance-unique nonce. Disallow role chaining, additional target ARNs, session tags, and policy substitutions unless separately reviewed.

**B-04 — Inline policy and action safety.** The inline policy must include an applicable explicit `Deny` for every action *not* in an independently reviewed, machine-checkable safe action catalog (e.g., `Deny`/`NotAction`). The previous demonstration's `iam:Get*`, `s3:Get*`, `ec2:Describe*`, etc. are **test candidates**, not an approved safe catalog. Expand every proposed wildcard against version-pinned AWS service authorization data; require review of write/permissions-management/tagging and side-effectful APIs; treat unknown/unmapped/new actions as **unsafe**. Version and SHA-256 pin the generator inputs and canonical policy. Do not claim a universal proof merely because action names begin with Get/List/Describe. Confirm feasibility with the STS plaintext policy size limit (2,048 characters) and packed policy limits before implementation. Do not truncate the policy or drop Deny on size errors.

**B-05 — Managed policy drift.** Before issuing refreshed sessions, verify the AWS-managed `ReadOnlyAccess` default version/document against an approved snapshot/digest (or an equivalently strong independent policy-revision gate). If mismatched or unreachable when verification is mandatory, fail closed; do not silently accept an unreviewed new version.

**B-06 — Verify the actual session identity.** Check STS `AssumedRoleUser.Arn`, `AssumedRoleUser.AssumedRoleId`, and `GetCallerIdentity()` using the *issued credentials*. The ARN must match the exact expected account, role name and issued session name; the ID/UserId must match `AROASOV54VGDAC4S2255I:<session_name>`. A successful `AssumeRole` response or matching ARN alone does not prove policies were correctly attached. Session policy request arguments require separate deterministic unit tests and authorization evidence.

**B-07 — Credential handoff.** Only short-lived STS credentials are written into the private `aws-mcp-role-credentials` volume using atomic replacement, strict UID/mode validation and a bounded expiration. MCP mounts it read-only and has no mount or environment path to `aws-sso-data`. Disable metadata and alternate credentials providers; verify actual runtime paths, environment and effective mounts, not only Compose rendering. The `credential_process` protocol legitimately writes secret JSON to a private child stdout pipe; it must **never** expose those values to shell output, logs, telemetry, MCP results or user-facing errors.

**B-08 — Fail closed across lifecycle.** A missing/incorrect role, missing Policy/PolicyArns, policy drift, identity mismatch, invalid credential file, stale/near-expiry credential, role replacement or any security invariant failure must block new credential publication and runtime readiness. On renewal transport/login failures, only previously verified unexpired STS credentials may remain usable for their remaining lifetime, according to a documented degradation policy; once stale, access must fail rather than fall back to administrative credentials. A previously issued STS session cannot be assumed instantly revoked simply by deleting a local file or stopping a container; emergency revocation requires separately approved AWS control.

**B-09 — Audit without secrets.** Structured logs record issuance result, pinned role reference, policy digest, managed-policy version, session identifier, expiration and failure category; do not log AccessKeyId, SecretAccessKey, SessionToken, source login cache, or complete credential-process JSON. Validate that AWS audit/CloudTrail records and Broker logs can be reconciled without relying on secrets.

**B-10 — Existing workload noninterference.** Do not modify the reused ECS role, policies, trust relationship, instance profiles, workload bindings or live ECS tasks. Read-only inspection and sandboxed STS calls only until owner review.

## 3. Existing implementation gaps observed in PR #10

| ID | Finding | Required disposition |
|---|---|---|
| G-01 | `derive_role_arn()` depends on a local timestamp-created role lifecycle state (`ReadOnlyIAMRole_*`); does not support a vetted existing role | Replace with pinned existing role identity verification, with no IAM creation/deletion |
| G-02 | `acquire()` supplies `PolicyArns` for `ReadOnlyAccess`, but **no** inline `Policy` argument | Implement mandatory, digest-checked explicit-Deny policy |
| G-03 | Existing code checks issued ARN but does not bind `AssumedRoleId` / `GetCallerIdentity.UserId` to the approved Role ID | Add Role ID checks |
| G-04 | Current `SESSION_NAME` uses a historical naming scheme | Replace with `aws-mcp-sts001-*` without changing unrelated legacy service identifiers |
| G-05 | Broker logs successful renewals, while credential_process checks expiry; security config drift and renewal failure readiness semantics are not yet fully defined | Add invariant drift/failure-state and expiry tests |
| G-06 | `--read-only` MCP annotation cannot secure arbitrary AWS API access from a generic `run_script` tool | IAM/session-layer deny must hold independently of MCP tool metadata |
| G-07 | Bootstrap / cleanup scripts manage disposable IAM roles | Ensure existing-role activation cannot invoke these mutation paths |

## 4. Evidence status (not inferred beyond the tests conducted)

| Gate / item | Current evidence | Status |
|---|---|---|
| STS using existing role with ReadOnlyAccess managed session policy | Operator obtained STS credentials successfully | VERIFIED (tested request) |
| Inline policy STS issuance | Operator obtained STS credentials with inline Deny + managed ReadOnlyAccess | VERIFIED (issuance) |
| IAM ListRoles/ListUsers, EC2 DescribeInstances | Operator's scoped session read tests | PASS (tested APIs only) |
| EC2 CreateVpc with DryRun | UnauthorizedOperation | PASS (one API); **does not isolate inline-Deny enforcement**, as ReadOnlyAccess also denies this API |
| MCP static volume isolation | Compose `aws-tunnel` has only STS volume (`:ro`); Broker sees source and STS volumes | PASS (static) |
| MCP runtime isolation | Not started or inspected under approved existing-role flow | NOT VERIFIED |
| S3 inventory | 162 buckets; 89 without bucket policy; 73 with bucket policy; 0 retrieval errors | PASS (policy-presence inventory) |
| S3 reviewed write candidates | `coord-app-stg`, `storecms2-stg-index` grants targeted at *other* principals / AWS services | No direct grant to candidate role found in inspected statements |
| Session-policy bypass through all resource-based policies | Other S3 statements/access points, KMS, Lambda, Secrets Manager, etc. and IAM semantics still require review | NOT PROVEN |
| SEC-04: effective AWS-wide write exclusion | No exhaustive action review/negative proof yet | NOT PROVEN |
| Gate STS-001 overall | Includes unverified policy safety and runtime isolation | NOT VERIFIED |

## 5. Acceptance tests required before any production activation

- **T-01 Identity:** pinned account, ARN, Role ID, source principal, trust baseline accepted; mismatches cause no `AssumeRole` / no publication.
- **T-02 Request:** unit/integration test asserts `PolicyArns`, inline `Policy` canonical digest, role ARN, session name, duration, and no policy-dropping retry. Tests for omission/mutation/packed-too-large are negative.
- **T-03 Session verification:** `AssumedRoleId` and STS `GetCallerIdentity().UserId` must both match pinned Role ID + session name; ARN/account mismatch rejected.
- **T-04 Safe action catalog:** independent action-level review of positive and negative permissions; wildcard expansion tested; generator version digest fixed; unknown AWS actions fail policy review; size constraints verified.
- **T-05 Real AWS no-mutation probes:** known read APIs succeed; representative write operations fail via **non-destructive authorization probes** (e.g. EC2 DryRun where supported); no actual mutation testing without separate authorization; neither IAM simulator nor a few DryRun requests alone prove universal prohibition.
- **T-06 Resource-based exceptions:** document effective direct-session, wildcard PrincipalArn, S3 access point, KMS, Lambda and other material policy pathways; explicitly distinguish unaudited services.
- **T-07 Isolation:** effective Compose and live container mount table, runtime env/providers, uid/capabilities, credential_process and absence of auth-cache/admin-secret access; inspect logs for secret leakage.
- **T-08 Failure behavior:** unavailable IAM/STS, expired `aws login`, policy digest drift, broker crash, stale credentials, partial atomic writes, permissions corruption, container restart and credential rotation all fail closed.
- **T-09 Renewal:** multiple consecutive renewals continue to use the pinned role and both Session Policies; previously issued sessions expire; no unexpected IAM changes.
- **T-10 Independent review:** independent reviewer signs off on policy coverage, deployment trust boundary and residual risks; role owner approves reuse, because candidate role is shared with ECS.

## 6. Blockers to design/plan FIX

1. **SEC04-POLICY:** An independently reviewed, versioned safe-action catalog, an inline Deny policy that fits STS limits, and confirmation that its exceptions cannot permit unintended writes are **NOT YET FIXED**.
2. **SEC04-BOUNDARY:** The trusted Broker holds administrator credentials. Broker takeover permits privileged AWS actions or AssumeRole without restrictive policies. The security claim must explicitly scope this threat boundary or require independent AWS-enforced controls (e.g. a separately authorized permission boundary/SCP/new constrained source). No such IAM change is approved.
3. **SEC04-RESOURCE:** Global resource-based permission pathways are not completely evaluated. The reviewed S3 statements do not alone prove SEC-04.
4. **SEC01-RUNTIME:** Actual container credential-provider isolation and fail-closed behavior remain to be tested after implementation, and must not be asserted as already verified.
5. **OWNER:** Shared ECS role reuse needs explicit owner approval before production adoption. This proposal is not that approval.

**Design decision:** Preserve prior findings and the PR #10 work, but keep **design acceptance conditional**, **implementation not authorized**, and **Gate STS-001 NOT VERIFIED** until blockers above are adjudicated. Next work item is a narrowly scoped, independent *session-policy action-catalog feasibility review*; only after that should Broker code changes be planned/authorized.

## 7. AWS authoritative references

- IAM explicit deny and role/session/resource-based permission evaluation: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic_policy-eval-denyallow.html
- IAM policies, boundaries, session policy interaction: https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html
- STS AssumeRole policy arguments and size limits: https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html
- IAM/STS quotas: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html
