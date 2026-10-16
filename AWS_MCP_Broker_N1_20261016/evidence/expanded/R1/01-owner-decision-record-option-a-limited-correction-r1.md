# AWS MCP Broker v1.1 — Requirements Owner Decision Record (Option A / 未認証)

> **重要：この文書はChatGPT会話上の「Option Aの方向で進める」という意思表示を固定するための未認証記録です。Requirements Ownerの身元・権限の独立認証および正式な承認証跡はありません。既存確定規範への自動反映、Normative PASS、Feasibility/設計/実装/本番許可を意味しません。**

## 1. Decision metadata

| Field | Value |
|---|---|
| Working record ID | `DRAFT-AWS-MCP-BROKER-V1.1-OWNER-OPTION-A-20261013` (正式Decision IDではない) |
| Decision intent | `OPTION_A — 3条項全文採用の方向で進める` |
| Source of intent | 2026-10-13 JSTの当該ChatGPT会話におけるユーザーの指示「この判断で進む」およびOption A推奨 |
| Intent interpretation | Option Aを採用する方向で記録を準備。ただし本人・権限の独立証拠がないため正式な採用確定とは区別 |
| Decision date | `2026-10-13 (JST)` (独立時刻証明なし) |
| Exact decision timestamp / timezone attestation | `NOT_VERIFIED` |
| Requirements Owner identity | `NOT_AUTHENTICATED / NOT_RECORDED` |
| Requirements Owner authority | `NOT_VERIFIED` |
| Independent approval evidence | `NOT_ATTACHED` |
| Formal ratification status | `OWNER_ATTESTATION_PENDING / NOT_EFFECTIVE` |
| Original authoritative B1/B2 provenance | `NOT_INDEPENDENTLY_ESTABLISHED` (同梱B1/B2との逐字照合はPASS) |
| Independent normative review after Owner ratification | `NOT_EXECUTED` |

## 2. Frozen evidence inputs

| Input | SHA-256 |
|---|---|
| B1 `01-fixed-baseline-v1.0.md` | `39002fc2ce5f21e9e686a427c793a7fd42fc84e5bdb02684be9e1e3a4305f4bc` |
| B2 `02-fixed-baseline-v1.1.md` | `3078acc5c31b5e900697dbb585e5ed604dfca89fe82b56cfc9528ac3c91350e2` |
| B3 `03-fixed-decisions-Q33-Q40.md` | `f287966ac61f467704f99c545f2d7a9756b9f21a70a5f90a814367ab7a113aa4` |
| R4 Review ZIP | `cd9611654f17d5eee73d47d5d32ce6d94459c24016c2dc3a1a157f90fbd8a15c` |
| Owner decision request (individual upload, equals ZIP member) | `021f2ca95d6f769881150bc00df067692eccc0cb3fc174a567fe3f83fa255d90` |

**Verified in this artifact session:** R4 ZIP CRC PASS、Manifest 14/14 SHA-256 MATCH。3条項それぞれの旧本文は同梱B1/B2本文と逐字一致し、旧本文および採用候補本文のSHA-256は独立再計算で申告値と一致した。

**Provenance limit:** B1/B2の権威ある外部原本・署名済み原本との完全な一致、および意思表示者がRequirements Owner本人であることは未証明。

## 3. Option A — 3条項の採用候補全文と確定予定Digest

**Digest canonicalization:** UTF-8で本文のみを`strip()`したバイト列をSHA-256。見出し・Markdown fenced code marker・終端の追加改行は含めない。下記Digestは本文値の計算結果であり、Owner署名のハッシュではない。

### REQ-009

- Source old-clause SHA-256: `d75233273042089564339a9b5f7f39ccb36e62367b4212b64849fed3abc49b18`
- Proposed adopted-clause SHA-256: `f17db0565942501a39c3302912dcb161e2f3e38e168f29a51491a711e0851bb9`
- Text state: **R4 full-text candidate, to be made authoritative only after authenticated Owner ratification**

```text
AWS認証情報、一時クレデンシャル、Bitwarden認証情報をAIエージェント、MCP応答、通常ログへ公開してはならない。

認証情報は種類ごとに明示的に認可された、実効的に保護され相互に隔離された実行境界内でのみ使用すること。AWS STS一時認証情報はBroker/AWS Executorの保護領域で必要なAWS API署名に限り使用できる。BWS Access TokenはBrokerから独立したSecret Adapter専用のSecret Store・実行主体の保護領域内でのみ使用できる。外部サービス用Secretは独立Secret Adapter内で、認可済みの外部サービス操作に限り利用できる。

Broker本体、AWS Executor、管理Web画面、AIエージェントにBWS Access Tokenまたは外部サービス用Secretを取得・復号・使用できる権限や経路を設けてはならない。既存AWS IAM長期アクセスキーはBroker、AWS Executor、独立Secret Adapter、独立認可主体その他の関連構成要素のいずれも取得・復号・使用してはならない。これらの境界は、システム全体を指す「Broker」という集合名によって同一実行・管理境界とみなしてはならない。
```

### REQ-046

- Source old-clause SHA-256: `410aacaeb42a90880e988fd86f84dd9fa09c780f575b6c78d14a8497d7658a94`
- Proposed adopted-clause SHA-256: `6362d06bfe5d1c1184057f84c42f2f6ed4c19d6dc47b8662cfe039105e21d931`
- Text state: **R4 full-text candidate, to be made authoritative only after authenticated Owner ratification**

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

### AC-022

- Source old-clause SHA-256: `58c7b2b6b562c7bc06b224c0daa2413764360c0e50954e3bc22a6c86b69a9aba`
- Proposed adopted-clause SHA-256: `3a02643899b8d79683f6c13300e0ee655b4b00fe20d23f87a3c35efb4e521a39`
- Text state: **R4 full-text candidate, to be made authoritative only after authenticated Owner ratification**

```text
Brokerインストール単位で割り当てたAdapter専用Machine Accountについて、認可された独立Secret Adapterだけが、許可された隔離テスト用Secretを取得・使用できることを検証する。ただしSecretの取得前に独立した内容不変性・真正性・Version拘束と禁止値混入防止を実証できない場合は肯定的取得試験を開始せず、当該機能を`BLOCKED`とする。実際のIAM長期アクセスキーを試験に使用してはならない。

Broker本体、AWS Executor、AIエージェント、Broker管理Web画面からはAdapterのBWS Access Tokenおよび外部サービスSecretを取得・復号・使用できないこと。別の保護対象Projectにある模擬IAM長期アクセスキーの取得は権限によって拒否されること。

Brokerの実行・管理主体からMachine Accountの権限を拡大できないことを確認する。さらに独立した二者承認が成立していても、禁止対象の模擬IAMキーを許可Secretへ混入させる変更が取得前に拒否されることを検証する。取得後の検出・破棄を取得前隔離の合格として扱ってはならない。
```

## 4. Explicit decision scope and non-regression

- REQ-009はCredential種別ごとの独立実行境界を定義し、AWS STS一時認証情報、BWS Access Token、外部サービスSecretを区別する。旧Broker単一境界を黙示的に拡張した扱いはしない。
- REQ-046はBrokerインストールに専用のMachine Account/Projectを保持しつつ、実際のToken/Secret取得権限を独立Secret Adapterへ限定する。Bitwarden連携は初期無効。
- AC-022は独立Adapterの肯定的試験とBroker等からの取得拒否を要求し、取得前保証が証明できなければ機能を`BLOCKED`とする。
- 既存IAM長期アクセスキーの取得・復号・利用、代替Fallbackは全構成要素で禁止。2人が正規承認した場合も禁止値混入は免除しない。
- 全実効的な権限拡大・高リスク変更の経路には独立した2名の承認を要求する。一方、Q40およびR4候補REQ-057で認める、認可済み管理者1名による緊急停止・Bitwarden連携無効化・BWS Access Token失効・許可リスト縮小・権限取消を妨げない。縮小を装う権限拡大、権限復旧・再有効化、および二者承認の迂回は、この例外に含めない。認可証明の発行、Operation Contract Digest拘束、取消・実送信の保証境界は緩和しない。
- REQ-050〜059、AC-025〜036はR4規範候補であり、本Recordのみで正式採用されたと主張しない。旧REQ-009/046とAC-022の置換を実施しない。

## 5. Unresolved evidence and gates

| Item | Status |
|---|---|
| Ownerの独立した本人確認・承認権限の証明 | `PENDING` |
| Owner承認の証跡（署名済み/監査可能な文書、意思決定記録等） | `PENDING` |
| 正式Decision ID・検証可能なUTC/JST時刻・採用Digestの承認 | `PENDING` |
| Owner ratification後の独立Normative Review | `NOT_EXECUTED` |
| INT-003 二者承認の実効強制 | `CRITICAL OPEN / BLOCKING` |
| Gate S0 | `NOT_PROVEN` |
| Gate S1 | `NOT_PROVEN` |
| Gate C | `NOT_PROVEN` |
| FEAS-001 / 007-A/B/C / 011 / Authorization / E2E | `NOT_PROVEN` |

## 6. Owner attestation area — 未記入

以下を権限を持つOwnerが認証可能な手段で**別途**確定するまでは、正式採用済みと扱わない。

- Official Decision ID: `PENDING`
- Requirements Owner identity / authority evidence: `PENDING`
- Verified decision timestamp UTC and JST: `PENDING`
- Decision: `OPTION A — REQ-009, REQ-046, AC-022 full texts each adopted` / `NOT_YET_AUTHENTICATED`
- Ratified B1/B2/B3 authoritative original source references + Digests: `PENDING`
- Ratification of above 3 clause SHA-256 values: `PENDING`
- Owner attestation / audit record reference: `PENDING`
- Independent post-decision normative review report: `PENDING`

**Guardrail:** このRecordに記述された会話上の意思表示とDigestを、Requirements Ownerの独立認証、規範統合PASSまたは実装許可の代わりに使ってはならない。
