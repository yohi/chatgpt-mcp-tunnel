# N1 INT-003 Governance Feasibility Gaps

## Verdict and evidence boundary

`UNSIGNED / INT-003: CRITICAL_OPEN / FEASIBILITY_NOT_PROVEN`.
No live management-plane permissions were inspected under this N1 contract.
The following is a complete **evidence-demand inventory for identified path
classes**, not proof that the actual deployment inventory is complete or that
any platform supports the required enforcement. Unknown additional paths remain
open until an authorized independent investigator reconciles the real inventory.

Source basis: B3 Q33/Q39/Q40, Option A R1 clauses, R4 INT-003 and proposed
REQ-051/055/056/058/059, AC-026/027/028/033/036. R4 detail remains unadopted;
the user's present safety constraints independently prohibit relaxing the
two-person boundary, IAM-key exclusion or pre-fetch conditions.

## 1. Distinct people, distinct authority, actual enforcement

Required evidence, collected later through authorized private governance:

1. A verified human-person identifier mapping for every approving account,
   authentication method, credential issuer, recovery owner and delegated role.
   Two accounts, two roles, two tokens or two signatures under one person's
   effective control are **not two independent humans**.
2. Valid administrative role grants and delegation chains for both humans;
   one cannot impersonate, reset, recover, enroll or replace the other alone.
   Identify shared supervisors, break-glass and root recovery paths explicitly.
3. A specific change object binding actor, resource, old/new state, parameters,
   operation-contract revision/digest, expiry, target deployment and use count 1.
   The applied bytes must match the approved change atomically.
4. Both independently authenticated approvals must be necessary **before**
   high-risk/expanding application. Notifications, optional reviews, later audit,
   policy documents and two-person meetings are not permission enforcement.
5. Trusted enforcement/issuer/policy/audit roots must themselves resist unilateral
   replacement, rollback, disablement and recovery. Evidence includes denial
   paths, fault cases and direct API/CLI bypasses, not only the approval UI.
6. Independent tamper-resistant audit of request, both approvals, application,
   refusal and revocation, with protected retention and reviewer access.

G0 preparation records permit some same-human G0/Custodian role candidates.
Those are a different decision domain and provide **zero evidence** of INT-003
independent two-person enforcement. Requirements/Design/Security role titles
likewise do not establish separate human control by themselves.

## 2. Effective management-path inventory and required evidence

For **every row**: current actual actor/permission inventory = NOT_RECOVERED;
independent pair = NOT_VERIFIED; enforcement = NOT_PROVEN; unilateral bypass
test = NOT_EXECUTED. The named next role is responsible for future authorized
evidence, not a currently authenticated appointment.

| Path | Bypass or high-risk effect to cover | Minimum closure evidence | Next responsible role |
| --- | --- | --- | --- |
| Bitwarden Organization Owner/Admin | Regrant Project/Machine Account access, replace admins, override ordinary workflow | All effective roles, inherited grants, direct UI/API/CLI paths, delegation/recovery and inability of one Owner/Admin to bypass concrete-change approval | Bitwarden governance custodian + independent Security investigator |
| Machine Account/Project administration | Issue/rotate/place Token, widen scope, move Secret or account assignment | Exact account/project/install binding, issuance and placement each separately approved once, Token capability isolation; no blanket future rotation | Secret platform custodian |
| Secret value ingress | Create/import/overwrite/value-only change/move/reference remap/version alias/restore | All writers and indirect writers, independent provenance of permitted content, immutable version binding and atomic fetch relation | Secret content provenance designer |
| Password Manager/Vault | Expose existing IAM keys via shared Vault, CLI session, export or migration | Both Password Manager and Secrets Manager protected while location unknown; actual access exclusions, no linked Vault credentials for any Broker/Adapter-related principal | Vault custodian |
| Cloud organization/account/root privilege | Replace runtime identity, attach permission, debug memory, change Secret binding or enforcement | Organization/root/delegated-admin/inherited control inventory, support/recovery routes, independent pre-change enforcement at highest effective authority | Cloud governance owner |
| Runtime host/hypervisor/container control | Mount Store, inspect memory/env/files, substitute image/entrypoint/network, exec/debug | Host root, virtualization/Desktop ownership, daemon/socket and filesystem/mount permissions; no single privileged route around boundary | Platform owner |
| Deno deployment administration | Redeploy, change environment/secret binding, manage org/project members or rollback | Actual org/project roles and effective deploy/secret/debug/recovery paths; separate Broker versus Adapter administration | Deno governance owner |
| Cloudflare deployment administration | Account/API-token rights, Workers/secret bindings, routes and deployment replacement | Actual account/member/token scope plus inherited rights and direct API bypass; enforcement outside compromised Broker's reach | Cloudflare governance owner |
| Docker Linux and macOS administration | Host/daemon/Desktop/VM, bind mounts, volumes, privileged container or rollback | Separate evidence for both host configurations; daemon/root authority cannot be omitted as merely outside container | Host governance owner |
| CI/CD and repository administration | Change workflow, required checks, branch rules, environment approval, deploy identity or rerun artifact | Repo/org admin, bypass lists, Actions permissions, runners, artifacts, dependency registries, deployment credentials; protected apply path requires two real people | Delivery governance owner |
| Supply chain/build/artifact promotion | Replace Adapter/issuer/enforcer binary/image, mutable tag, malicious dependency or rollback | Reviewed artifact digest, build provenance, signing-key control, promotion/revocation and rollback controls over exact bytes | Release custodian |
| Adapter-specific Secret Store | Read/replace Token, change ACL/encryption key, snapshot/export/import | Effective Store/key administrators, data and control plane, replication and recovery; Broker cannot fetch/place/update Token or Store bindings | Secret Store owner |
| Independent issuer/authentication | Mint grant, replace trust/key/policy, fake original request/person or service identity | Issuer administration, IdP enrollment/reset/recovery, signing keys, original-request integrity, independent policy and channel/contract binding | Identity/issuer owner |
| Operation catalog/egress/output controls | Change destination, DNS/TLS/proxy/redirect/Secret ID/output schema or expand allowlist | Exact contract revision/digest; network/PKI/DNS admins and lower-level bypasses; old grant invalid after contract change | Design + network governance owners |
| Cancellation/single-use state | Rewind revocation epoch, replay consumed proof, dispatch after C from queue | Protected stores and writers, transaction semantics, C/S/D/R final transport enforcement, partitions/restore tests and independent audit | State/transport designer |
| Backup/restore/replication/rollback | Restore old permissions, Token, approval, used-grant state, issuer keys or audit policy | Backup administrators, keys, snapshots, import/migration and disaster recovery; anti-rollback, no approval resurrection; approvals cover actual restore change | Recovery custodian |
| Audit/monitoring/retention | Disable logging, modify evidence or route secrets to telemetry, erase refusals | Independent write/protect/delete authorities, retention/hold and recovery controls; enforcer cannot silently suppress evidence | Audit custodian |
| Break-glass/support/account recovery | Vendor or enterprise recovery, emergency admin replacement, impersonation | Documented effective emergency and vendor-support paths, who can invoke them, technical restriction to reductions or independent controls before expansion | Governance/Security owner |
| Human control-plane recovery | One person controls both approvers' email, IdP, device reset or recovery channel | Independent-person control proof beyond account names, delegated access and recovery graph; separate attribution of approval acts | Governance identity verifier |

Completeness closure requires an Actor × Action × Resource × Effective Authority
graph for each deployment/mode, including inheritance, federation, delegation,
service identities and ultimate roots. Every path to a high-risk effect must
cross the independent two-person pre-application control. One reachable bypass
is enough to keep INT-003 open. A custodian's attestation alone is not a dynamic
test result; platform guarantees and actual effective grants both need evidence.

## 3. Two-person authorization is not content safety

The following properties must be proven separately:

- **Change authorization:** two distinct authorized humans approved this exact
  change once; no unilateral change or approval substitution is possible.
- **Pre-fetch content safety:** even a validly approved change cannot cause any
  related component to acquire an existing IAM long-term key. Safe provenance,
  independent trust root, rollback resistance and exact fetched-version binding
  must be established before issuing a BWS Secret-value request.

Counterexample: approved Secret ID/Project/metadata/contract stay the same while
the value becomes a dummy IAM key. Two humans may approve in error. Labels,
regex checks, recorded digests, signatures on approval, or detecting the value
after acquisition cannot distinguish the forbidden acquisition beforehand.
An additional checker that first reads the value is not an approved workaround;
its inclusion in the no-acquisition boundary requires formal Owner adjudication.

AC-022 positive fetch remains BLOCKED if this proof is unavailable. AC-033/036
remain unadopted/unexecuted proposed tests; no real key, BWS experiment or cloud
operation is authorized by this evidence plan.

## 4. Disabled boundaries and emergency reductions

- Keep affected Adapter integrations disabled; no Token placement, Adapter
  activation, Secret-value request or external operation is authorized here.
- Initial external production allowlist remains empty in the candidate design.
  Arbitrary Secret retrieval, arbitrary HTTP and external writes remain forbidden.
- Preserve REQ-045 unconditional exclusion and REQ-047 no-fallback, including
  setup, failure, test, backup and recovery paths.
- Single authorized human emergency stop/disable/revoke/reduce is a reduction,
  not a second-person waiver. Restoration, re-enable, broader destinations,
  replacement Token placement or disguised expansion requires the high-risk
  controls; no new exception is created by N1.
- Feature-off is fail-closed disposition, **not enabled-mode safety PROVEN** and
  not full v1.1/environment parity. Unknown path applicability is not N/A.

## 5. Human escalation and closure test

Requirements Owner retains the safety requirements. Design/Security authority
must determine whether a credible enforceable design exists, inventory missing
platform guarantees and decide a bounded independently authorized investigation.
If a platform cannot enforce the boundary, the feature remains disabled/blocked;
AI must not invent an exception or lower the two-person standard.

Future independent feasibility review must produce exact deployment/config and
policy digests, actor-to-real-human mapping verified privately, complete path
graph, per-path negative/positive evidence, approved-poison pre-fetch evidence,
independent audit and residual limitations. Different approval acts by the same
person never satisfy INT-003. N2 textual review also cannot close this technical
finding. `INT-003: CRITICAL_OPEN` remains the N1 exit state.
