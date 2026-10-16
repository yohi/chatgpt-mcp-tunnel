# N1 Baseline and Clause Diff Matrix

## Status, exact-byte rule and baseline composition

`UNSIGNED / NOT_EFFECTIVE`. Option A intent is preserved for all three clauses;
no re-selection is requested. The formal ratification event is missing.

The B1/B2/B3 file bytes and hashes are fixed in [Register section 2](01_N1_Authority_Chain_Evidence_Register.md#2-b1b2b3-authority-chain-one-to-one).
B1 contains 44 REQ and 20 AC; B2 adds 5 REQ and 4 AC plus B2-S1; B3 is an
8-decision summary. The R4 nonregression matrix covers all 49 REQ / 24 AC
references but does not establish adoption, implementation or release compliance.

The full old/new bodies below are evidence quotations, not newly authored
normative text. For their digests, take only the UTF-8 body between each `text`
fence, remove framing leading/trailing whitespace as specified by the source,
and add no terminal newline. No Unicode normalization is applied. The three raw
R1 `.txt` members already equal the exact new byte streams, without a final LF.
Whole-file SHA-256 and body SHA-256 are different scopes.

| Clause | Old source and body bytes / SHA-256 | New R1 bytes / SHA-256 | Supersession candidate |
| --- | --- | --- | --- |
| REQ-009 | B1 v1.0 body, 235 / `d75233273042089564339a9b5f7f39ccb36e62367b4212b64849fed3abc49b18` | 1241 / `f17db0565942501a39c3302912dcb161e2f3e38e168f29a51491a711e0851bb9` | Replace this entire B1 clause only at an authenticated human-set effective time |
| REQ-046 | B2 v1.1 body, 1025 / `410aacaeb42a90880e988fd86f84dd9fa09c780f575b6c78d14a8497d7658a94` | 2939 / `6362d06bfe5d1c1184057f84c42f2f6ed4c19d6dc47b8662cfe039105e21d931` | Replace whole clause, including all six items and Password Manager/CLI paragraphs |
| AC-022 | B2 v1.1 body, 436 / `58c7b2b6b562c7bc06b224c0daa2413764360c0e50954e3bc22a6c86b69a9aba` | 1213 / `3a02643899b8d79683f6c13300e0ee655b4b00fe20d23f87a3c35efb4e521a39` | Replace entire acceptance clause, not merely actor names |

For **each row**, formal adoption authority = NOT_VERIFIED, authenticated
event ID = NOT_RECOVERED, UTC approval time = NOT_RECOVERED, effective date =
NOT_SET, current replacement effect = NOT_EFFECTIVE. B1/B2 labels are submitted
revision labels, not proven historical official revisions. Other clauses are
not repealed or amended by this packet. Preserve originals as evidence.

## 1. REQ-009 full old and new bodies

### Old REQ-009 — submitted B1

```text
AWS認証情報、一時クレデンシャル、Bitwarden認証情報をAIエージェント、MCP応答、通常ログへ公開してはならない。

認証情報はBrokerの保護された実行境界でのみ使用すること。
```

### New REQ-009 — Option A R1 candidate

```text
AWS認証情報、一時クレデンシャル、Bitwarden認証情報をAIエージェント、MCP応答、通常ログへ公開してはならない。

認証情報は種類ごとに明示的に認可された、実効的に保護され相互に隔離された実行境界内でのみ使用すること。AWS STS一時認証情報はBroker/AWS Executorの保護領域で必要なAWS API署名に限り使用できる。BWS Access TokenはBrokerから独立したSecret Adapter専用のSecret Store・実行主体の保護領域内でのみ使用できる。外部サービス用Secretは独立Secret Adapter内で、認可済みの外部サービス操作に限り利用できる。

Broker本体、AWS Executor、管理Web画面、AIエージェントにBWS Access Tokenまたは外部サービス用Secretを取得・復号・使用できる権限や経路を設けてはならない。既存AWS IAM長期アクセスキーはBroker、AWS Executor、独立Secret Adapter、独立認可主体その他の関連構成要素のいずれも取得・復号・使用してはならない。これらの境界は、システム全体を指す「Broker」という集合名によって同一実行・管理境界とみなしてはならない。
```

## 2. REQ-046 full old and new bodies

### Old REQ-046 — submitted B2

```text
BrokerがBitwarden Secrets Managerを利用する場合、専用Machine Accountと専用Projectを使用する。

以下を必須とする。

1. Broker専用Machine Accountに必要最小限のProjectアクセスのみ付与する。
2. 既存IAM長期アクセスキーを含むProjectへのアクセスを禁止する。
3. Brokerの実行主体にBitwardenの管理者権限・権限割当変更権限を付与しない。
4. Broker専用Projectに既存IAM長期アクセスキーを保存してはならない。
5. Machine AccountのProject割当と権限を管理者が検証できること。
6. 権限が意図せず拡大した場合、安全性を確認できるまでBrokerの秘密情報取得を拒否すること。

既存キーがPassword Managerに保管されている場合、Brokerには当該Vaultを読み取れる認証情報を一切付与しない。

Bitwarden CLIの利用を許可する場合でも、Broker専用Secrets Managerの権限境界を越える操作を許可してはならない。
```

### New REQ-046 — Option A R1 candidate

```text
BrokerがBitwarden Secrets Managerとの連携機能を提供する場合、Brokerインストール単位で専用のMachine Accountと専用Projectを用意し、当該Machine AccountのAccess TokenとSecret取得能力はBroker本体から独立したSecret Adapterのみに付与する。Bitwarden連携は初期状態で無効とし、必要な検証済み外部サービス操作が認可されるまでMachine AccountのToken配置、Adapter起動およびSecret取得を必須としてはならない。

以下を必須とする。

1. 独立Secret Adapter専用Machine Accountには、当該Brokerインストールに専用のProjectへの必要最小限の読み取りアクセスのみ付与する。Broker本体、AWS Executor、AIエージェントおよびBroker管理Web画面には当該Access Tokenの取得・使用権限を付与しない。
2. 既存IAM長期アクセスキーを含むProjectへのMachine AccountとAdapterのアクセスを禁止する。Secret ID、Project、権限が不変であっても内容差替えによって既存IAMキーが流入し得る経路については、REQ-045と独立取得前強制の両方を満たすまで取得しない。
3. Brokerの実行主体と管理主体にBitwarden管理者権限、Machine Account権限割当変更権限、Adapter専用Secret Storeへのアクセス権限を付与しない。Adapterに対する特権変更の迂回経路も独立二者承認の検証対象とする。
4. 当該Brokerインストールに紐付くAdapter専用Projectに既存IAM長期アクセスキーを保存してはならない。正式な二者承認の有無によらず、禁止内容の追加・移動・値のみの差替えを許容してはならない。
5. Machine AccountのProject割当、実効権限、Secret変更の全実効経路を管理者が独立して検証できること。単独のOrganization Owner/Adminや基盤特権者による変更経路を検査から除外しない。
6. Adapterの権限が意図せず拡大した場合、または取得前内容保証・独立認可・監査が不明となった場合、安全性を再検証できるまでAdapterによる秘密情報取得を拒否すること。Broker側からこの拒否を解除できてはならない。

既存キーがBitwarden Password Managerに保管されている場合、BrokerおよびAdapterとその関連実行主体には当該Vaultを読み取れる認証情報を一切付与しない。保管先が不明な間はPassword ManagerとSecrets Managerの両方を保護対象とする。

Bitwarden CLIの利用を許可する場合でも、独立Secret Adapterの実行・認証・権限境界の内側だけで実行し、Broker本体からのCLI操作、Password ManagerのVaultへのアクセス、専用Secrets Manager Projectの権限越境、任意Secret取得を禁止する。CLIへの代理要求によってこれらを迂回してはならない。
```

## 3. AC-022 full old and new bodies

### Old AC-022 — submitted B2

```text
Broker専用Machine Accountから、許可されたテストSecretは取得できること。

別の保護対象Projectにある模擬IAM長期アクセスキーについては、秘密値の取得が権限によって拒否されること。

実際のIAM長期アクセスキーをテストに使用してはならない。

さらに、Brokerの実行主体からMachine Accountの権限を拡大できないことを確認する。
```

### New AC-022 — Option A R1 candidate

```text
Brokerインストール単位で割り当てたAdapter専用Machine Accountについて、認可された独立Secret Adapterだけが、許可された隔離テスト用Secretを取得・使用できることを検証する。ただしSecretの取得前に独立した内容不変性・真正性・Version拘束と禁止値混入防止を実証できない場合は肯定的取得試験を開始せず、当該機能を`BLOCKED`とする。実際のIAM長期アクセスキーを試験に使用してはならない。

Broker本体、AWS Executor、AIエージェント、Broker管理Web画面からはAdapterのBWS Access Tokenおよび外部サービスSecretを取得・復号・使用できないこと。別の保護対象Projectにある模擬IAM長期アクセスキーの取得は権限によって拒否されること。

Brokerの実行・管理主体からMachine Accountの権限を拡大できないことを確認する。さらに独立した二者承認が成立していても、禁止対象の模擬IAMキーを許可Secretへ混入させる変更が取得前に拒否されることを検証する。取得後の検出・破棄を取得前隔離の合格として扱ってはならない。
```

## 4. Exact line diffs and semantic impact

The full line-by-line unified diffs are preserved, without regeneration or
editing, in [R4 Owner Decision Request](evidence/expanded/R4/08-owner-decision-request.md),
lines 40–52, 98–127 and 157–173, SHA-256
`021f2ca95d6f769881150bc00df067692eccc0cb3fc174a567fe3f83fa255d90`.
Those exact old bodies were independently matched to B1/B2, and new bodies to
the R1 raw text, R1 record and Owner intent. Thus these are diffs of the byte
streams above, not summaries substituted for missing originals.

| Clause | Complete change scope | Safety/consistency condition |
| --- | --- | --- |
| REQ-009 | Old paragraph 1 retained; old paragraph 2 replaced; new paragraph 3 added | Credential-specific STS versus Adapter boundaries are a normative amendment, not a reinterpretation of the word Broker |
| REQ-046 | Opening, all items 1–6, Password Manager paragraph and CLI paragraph replaced; introductory mandatory-list sentence retained | Installation-specific account/project retained; Adapter alone holds Token/Secret capability; no forgotten old Broker acquisition path |
| AC-022 | Entire four-paragraph body replaced by three paragraphs, preserving real-IAM-key prohibition within new paragraph 1 | Positive fetch requires independent pre-fetch content/provenance/version proof; Broker denial, approved-poison refusal and no post-fetch substitute |

| Preserved provision / integration finding | Required consistency, not a new adoption |
| --- | --- |
| REQ-045 | No acquisition/decryption/copy/cache/transfer/use of existing IAM long-term keys by any related component, including tests, restore and emergencies. Two valid approvers cannot waive content prohibition |
| REQ-047 | Explicitly allowed AWS auth sources only; no ambient SDK/provider long-term-key fallback, role/account escalation or Bitwarden-dependent substitute |
| REQ-048 / B2-S1 | Phishing-resistant human authentication; 8h absolute / 15m idle; only authenticated human activity renews idle; unattended principals separate; authoritative adoption still unverified |
| REQ-049 | Minimal credential handling and no unnecessary disclosure in AI/MCP/HTTP/logs/exceptions/IPC/storage/backup/telemetry; STS runtime use is narrowly scoped |
| REQ-025 / INT-001 | B1 says Secrets Manager is storage; B3/R4 say external-only integration capability, initially disabled and AWS independent. Option A alone does not settle full REQ-025 integration or adopt REQ-050 |
| INT-003 / Q40 | Independent two distinct humans for all effective high-risk/privilege-expanding paths. One authorized human may stop/reduce/revoke; restoration and re-enable are not emergency-reduction exceptions |
| REQ-042 / INT-002 | Disabled Adapter or AWS-only is not full three-environment parity; Docker Linux/macOS distinguished |
| INT-004/005/006 | Per-specific-change Token approval, independent issuer/contract digest and C/S/D/R guarantees; AWS per-write approval cannot authorize external writes |
| STS-001 draft vs v1.1 | Historical privileged Broker trust assumption, legacy credentials and narrower runtime-isolation claim require explicit Design/Security consistency review; no automatic merge into v1.1 |

## 5. R4 additional candidates: individual disposition and dependencies

Every row below is **UNADOPTED_PROPOSAL**. Disposition = human decision pending;
none is implicitly accepted by Option A. Requirements Owner records adopt exact
digest / defer / reject / commission separately reviewed revision **per row**.
Deferral keeps dependent features disabled; it does not weaken safety floors.
Full source bodies remain in the digest-pinned R4-REQ and R4-AC files.

| Candidate | Dependency / corresponding acceptance | Impact if adopted; unresolved issue |
| --- | --- | --- |
| REQ-050 | REQ-025, Q34/Q38, 047; AC-030/032 | Initial empty external allowlist; no Token/Adapter/BWS dependency for AWS; REQ-025 integration requires explicit disposition |
| REQ-051 | Option A 009/046/022, Q33/Q39; AC-025/026 | Independent runtime/auth/admin boundary; platform enforcement and INT-003 unproven |
| REQ-052 | Q35/Q36, 014–021; AC-027/032/034 | Read/status only, pinned operation contract, endpoint/parameter/output/retry controls; GET alone insufficient |
| REQ-053 | 010–013, 052/057; AC-025/029/034/035 | Independent issuer, original-request integrity, principal/channel/contract-digest binding, short expiry and single use; no Broker self-assertion |
| REQ-054 | 045/049/055; AC-025/032/033/036 | Adapter-only Secret handling and safe output; post-fetch detection cannot satisfy no-acquisition |
| REQ-055 | 045/046/051/056; AC-025/026/028/032/033/036 | Independent Store, all-ingress content provenance and atomic version binding; approved poisoning also denied; FEAS-007-C unresolved |
| REQ-056 | Q40, 051–055/058; AC-026/027/028/033/034/036 | Independent two-person one-change enforcement across every privileged path; INT-003 CRITICAL_OPEN |
| REQ-057 | 032–035, 053/056; AC-029/035 | Single-human emergency reduction; separate S/D/C/R, final transport serialization, no post-cancel initial send or unknown-outcome resend |
| REQ-058 | 047/056/057; AC-027/029 | Per-issuance/per-placement/per-permission-change two-person concrete single-use approval; no blanket future rotation |
| REQ-059 | 008/041/042 and 050–058; AC-031/036 | Evidence per Deno/Workers/Docker Linux/macOS, disabled versus enabled separately; no unjustified N/A |

All following AC rows also remain **NOT_EXECUTED**; recording a test contract is
neither test permission nor a PASS.

| Candidate | Requirement dependencies | Acceptance impact / unresolved condition |
| --- | --- | --- |
| AC-025 | 009/045/046/049/051/053/054/055 | Compromised Broker cannot obtain Adapter Token/Secret/issuer key; Owner boundary amendment prerequisite |
| AC-026 | 051/055/056 | Actual Broker/Executor/UI inability to alter Adapter/Store/deploy/issuer/CI/audit, not process-name separation |
| AC-027 | 052/056/058 | Two distinct authenticated humans, exact same change, one application; same-human accounts/replay/blanket rotation fail |
| AC-028 | 045/046/051/055/056 | Zero unmanaged privilege-bypass paths and pre-fetch prevention; pair with AC-036 for approved poison |
| AC-029 | 053/057/058 | Emergency reductions, C/S/D/R, crash/queue/partition/session-residual cases; no post-C unsent dispatch |
| AC-030 | 007/025/045/047/050 | AWS-only initial-disabled mode without BWS/Adapter/Token; external calls denied; not full feature parity |
| AC-031 | 008/041/042/059 | Separate four deployment configurations and modes; N/A needs adopted applicability rule plus disabled-state evidence |
| AC-032 | 050/052/053/054/055 | Separately authorized nonproduction positive E2E only after pre-fetch proof; mocks alone do not prove live guarantees |
| AC-033 | 045/046/054/055/056 | Value-only poisoning with unchanged pre-fetch metadata, both unauthorized and validly approved; reject before value request |
| AC-034 | 010–013/052/053/056 | Independent issuance basis, request integrity, exact contract/channel binding, no forged Broker user or stale contract |
| AC-035 | 017/032–035/053/057 | Multi-Adapter single-use and final transport C/D ordering; ledger-only D flag insufficient |
| AC-036 | 045/046/054/055/056/059 | Valid distinct-human approved dummy-IAM poisoning still denied before fetch; whole-feature shutdown is BLOCKED, not enabled-mode PASS |

## 6. Findings and revision-history limitations

- R4 R2/R3 findings are author summaries, not recovered signed reviewer reports.
  Original external R2/R3 bytes and authenticated review events are missing.
- R1 static review evaluated the pre-correction Record. R1 limited patch narrows
  the summary to high-risk/expanding changes while preserving one-human emergency
  reduction; three candidate bodies are unchanged. The original pre-R1 Record
  and original Option A ZIP are referenced but not supplied as complete originals
  here. Full historical patch reconstruction is therefore not claimed.
- R1 README says independent ODR-IR-001 closure pending; Owner intent/N0 report
  it CLOSED (STATIC TEXT ONLY). Preserve this chronology/evidence distinction.
  N1 confirms corrected wording is present but issues no new formal closure.
- ODR-IR-002 remains PENDING / NOT_EFFECTIVE; ODR-IR-003 NOT_VERIFIED.
  INT-003 remains CRITICAL_OPEN. No adopted consolidated revision exists in
  recovered evidence. The human must set a new immutable revision and precedence
  map if adopting prospectively; old evidence must not be overwritten.
