# AWS MCP Broker v1.1 — Requirements Owner Decision Request R4

**Decision status:** `PENDING / NOT_APPROVED`  
**Review trigger:** RG-BRK-NR-R2-001およびRG-BRK-NR-R3-001  
**Decision maker:** Requirements Ownerのみ。提案作成者・独立Reviewerは代決しない。  
**Baseline:** B1のREQ-009、B2のREQ-046・AC-022原文。`01`、`02`は一字も変更していない。  

## 判断対象と推奨

**Option A — 正式採用（推奨候補）:** 以下の3条項を全文単位で改訂して正式採用し、Ownerの識別子・UTC/JST日時・承認根拠・新規確定Digestを別の決定記録に残す。独立レビュアーが固定した採用版に対し非退行審査を行う。採用だけでは技術的な保証は`PROVEN`とならない。

**Option B — 採用しない:** 旧条項を維持し、独立Secret Adapterとの規範競合を`OPEN / BLOCKED`のまま保持する。代替案が必要となり、既存条項を勝手に再解釈してはならない。

以下は**全条項の原文・全条項の改訂候補・逐行差分**である。旧文面の「項目6」を誤って「Broker専用」とするRev3の位置指定は撤回する。

## REQ-009 — Full-text amendment candidate

**Old-clause SHA-256:** `d75233273042089564339a9b5f7f39ccb36e62367b4212b64849fed3abc49b18`  
**Proposed-clause SHA-256:** `f17db0565942501a39c3302912dcb161e2f3e38e168f29a51491a711e0851bb9`  
**Hash rule:** UTF-8、見出しを除く本文を両端`strip()`し、終端改行は追加せずSHA-256。

### 固定原文（全文）

```text
AWS認証情報、一時クレデンシャル、Bitwarden認証情報をAIエージェント、MCP応答、通常ログへ公開してはならない。

認証情報はBrokerの保護された実行境界でのみ使用すること。
```

### 正式改訂候補（全文・**未承認**）

```text
AWS認証情報、一時クレデンシャル、Bitwarden認証情報をAIエージェント、MCP応答、通常ログへ公開してはならない。

認証情報は種類ごとに明示的に認可された、実効的に保護され相互に隔離された実行境界内でのみ使用すること。AWS STS一時認証情報はBroker/AWS Executorの保護領域で必要なAWS API署名に限り使用できる。BWS Access TokenはBrokerから独立したSecret Adapter専用のSecret Store・実行主体の保護領域内でのみ使用できる。外部サービス用Secretは独立Secret Adapter内で、認可済みの外部サービス操作に限り利用できる。

Broker本体、AWS Executor、管理Web画面、AIエージェントにBWS Access Tokenまたは外部サービス用Secretを取得・復号・使用できる権限や経路を設けてはならない。既存AWS IAM長期アクセスキーはBroker、AWS Executor、独立Secret Adapter、独立認可主体その他の関連構成要素のいずれも取得・復号・使用してはならない。これらの境界は、システム全体を指す「Broker」という集合名によって同一実行・管理境界とみなしてはならない。
```

### 原文との行単位差分

```diff
--- REQ-009 original (B1/B2)
+++ REQ-009 proposed R4
@@ -1,3 +1,5 @@
 AWS認証情報、一時クレデンシャル、Bitwarden認証情報をAIエージェント、MCP応答、通常ログへ公開してはならない。
 
-認証情報はBrokerの保護された実行境界でのみ使用すること。
+認証情報は種類ごとに明示的に認可された、実効的に保護され相互に隔離された実行境界内でのみ使用すること。AWS STS一時認証情報はBroker/AWS Executorの保護領域で必要なAWS API署名に限り使用できる。BWS Access TokenはBrokerから独立したSecret Adapter専用のSecret Store・実行主体の保護領域内でのみ使用できる。外部サービス用Secretは独立Secret Adapter内で、認可済みの外部サービス操作に限り利用できる。
+
+Broker本体、AWS Executor、管理Web画面、AIエージェントにBWS Access Tokenまたは外部サービス用Secretを取得・復号・使用できる権限や経路を設けてはならない。既存AWS IAM長期アクセスキーはBroker、AWS Executor、独立Secret Adapter、独立認可主体その他の関連構成要素のいずれも取得・復号・使用してはならない。これらの境界は、システム全体を指す「Broker」という集合名によって同一実行・管理境界とみなしてはならない。
```

## REQ-046 — Full-text amendment candidate

**Old-clause SHA-256:** `410aacaeb42a90880e988fd86f84dd9fa09c780f575b6c78d14a8497d7658a94`  
**Proposed-clause SHA-256:** `6362d06bfe5d1c1184057f84c42f2f6ed4c19d6dc47b8662cfe039105e21d931`  
**Hash rule:** UTF-8、見出しを除く本文を両端`strip()`し、終端改行は追加せずSHA-256。

### 固定原文（全文）

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

### 正式改訂候補（全文・**未承認**）

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

### 原文との行単位差分

```diff
--- REQ-046 original (B1/B2)
+++ REQ-046 proposed R4
@@ -1,14 +1,14 @@
-BrokerがBitwarden Secrets Managerを利用する場合、専用Machine Accountと専用Projectを使用する。
+BrokerがBitwarden Secrets Managerとの連携機能を提供する場合、Brokerインストール単位で専用のMachine Accountと専用Projectを用意し、当該Machine AccountのAccess TokenとSecret取得能力はBroker本体から独立したSecret Adapterのみに付与する。Bitwarden連携は初期状態で無効とし、必要な検証済み外部サービス操作が認可されるまでMachine AccountのToken配置、Adapter起動およびSecret取得を必須としてはならない。
 
 以下を必須とする。
 
-1. Broker専用Machine Accountに必要最小限のProjectアクセスのみ付与する。
-2. 既存IAM長期アクセスキーを含むProjectへのアクセスを禁止する。
-3. Brokerの実行主体にBitwardenの管理者権限・権限割当変更権限を付与しない。
-4. Broker専用Projectに既存IAM長期アクセスキーを保存してはならない。
-5. Machine AccountのProject割当と権限を管理者が検証できること。
-6. 権限が意図せず拡大した場合、安全性を確認できるまでBrokerの秘密情報取得を拒否すること。
+1. 独立Secret Adapter専用Machine Accountには、当該Brokerインストールに専用のProjectへの必要最小限の読み取りアクセスのみ付与する。Broker本体、AWS Executor、AIエージェントおよびBroker管理Web画面には当該Access Tokenの取得・使用権限を付与しない。
+2. 既存IAM長期アクセスキーを含むProjectへのMachine AccountとAdapterのアクセスを禁止する。Secret ID、Project、権限が不変であっても内容差替えによって既存IAMキーが流入し得る経路については、REQ-045と独立取得前強制の両方を満たすまで取得しない。
+3. Brokerの実行主体と管理主体にBitwarden管理者権限、Machine Account権限割当変更権限、Adapter専用Secret Storeへのアクセス権限を付与しない。Adapterに対する特権変更の迂回経路も独立二者承認の検証対象とする。
+4. 当該Brokerインストールに紐付くAdapter専用Projectに既存IAM長期アクセスキーを保存してはならない。正式な二者承認の有無によらず、禁止内容の追加・移動・値のみの差替えを許容してはならない。
+5. Machine AccountのProject割当、実効権限、Secret変更の全実効経路を管理者が独立して検証できること。単独のOrganization Owner/Adminや基盤特権者による変更経路を検査から除外しない。
+6. Adapterの権限が意図せず拡大した場合、または取得前内容保証・独立認可・監査が不明となった場合、安全性を再検証できるまでAdapterによる秘密情報取得を拒否すること。Broker側からこの拒否を解除できてはならない。
 
-既存キーがPassword Managerに保管されている場合、Brokerには当該Vaultを読み取れる認証情報を一切付与しない。
+既存キーがBitwarden Password Managerに保管されている場合、BrokerおよびAdapterとその関連実行主体には当該Vaultを読み取れる認証情報を一切付与しない。保管先が不明な間はPassword ManagerとSecrets Managerの両方を保護対象とする。
 
-Bitwarden CLIの利用を許可する場合でも、Broker専用Secrets Managerの権限境界を越える操作を許可してはならない。
+Bitwarden CLIの利用を許可する場合でも、独立Secret Adapterの実行・認証・権限境界の内側だけで実行し、Broker本体からのCLI操作、Password ManagerのVaultへのアクセス、専用Secrets Manager Projectの権限越境、任意Secret取得を禁止する。CLIへの代理要求によってこれらを迂回してはならない。
```

## AC-022 — Full-text amendment candidate

**Old-clause SHA-256:** `58c7b2b6b562c7bc06b224c0daa2413764360c0e50954e3bc22a6c86b69a9aba`  
**Proposed-clause SHA-256:** `3a02643899b8d79683f6c13300e0ee655b4b00fe20d23f87a3c35efb4e521a39`  
**Hash rule:** UTF-8、見出しを除く本文を両端`strip()`し、終端改行は追加せずSHA-256。

### 固定原文（全文）

```text
Broker専用Machine Accountから、許可されたテストSecretは取得できること。

別の保護対象Projectにある模擬IAM長期アクセスキーについては、秘密値の取得が権限によって拒否されること。

実際のIAM長期アクセスキーをテストに使用してはならない。

さらに、Brokerの実行主体からMachine Accountの権限を拡大できないことを確認する。
```

### 正式改訂候補（全文・**未承認**）

```text
Brokerインストール単位で割り当てたAdapter専用Machine Accountについて、認可された独立Secret Adapterだけが、許可された隔離テスト用Secretを取得・使用できることを検証する。ただしSecretの取得前に独立した内容不変性・真正性・Version拘束と禁止値混入防止を実証できない場合は肯定的取得試験を開始せず、当該機能を`BLOCKED`とする。実際のIAM長期アクセスキーを試験に使用してはならない。

Broker本体、AWS Executor、AIエージェント、Broker管理Web画面からはAdapterのBWS Access Tokenおよび外部サービスSecretを取得・復号・使用できないこと。別の保護対象Projectにある模擬IAM長期アクセスキーの取得は権限によって拒否されること。

Brokerの実行・管理主体からMachine Accountの権限を拡大できないことを確認する。さらに独立した二者承認が成立していても、禁止対象の模擬IAMキーを許可Secretへ混入させる変更が取得前に拒否されることを検証する。取得後の検出・破棄を取得前隔離の合格として扱ってはならない。
```

### 原文との行単位差分

```diff
--- AC-022 original (B1/B2)
+++ AC-022 proposed R4
@@ -1,7 +1,5 @@
-Broker専用Machine Accountから、許可されたテストSecretは取得できること。
+Brokerインストール単位で割り当てたAdapter専用Machine Accountについて、認可された独立Secret Adapterだけが、許可された隔離テスト用Secretを取得・使用できることを検証する。ただしSecretの取得前に独立した内容不変性・真正性・Version拘束と禁止値混入防止を実証できない場合は肯定的取得試験を開始せず、当該機能を`BLOCKED`とする。実際のIAM長期アクセスキーを試験に使用してはならない。
 
-別の保護対象Projectにある模擬IAM長期アクセスキーについては、秘密値の取得が権限によって拒否されること。
+Broker本体、AWS Executor、AIエージェント、Broker管理Web画面からはAdapterのBWS Access Tokenおよび外部サービスSecretを取得・復号・使用できないこと。別の保護対象Projectにある模擬IAM長期アクセスキーの取得は権限によって拒否されること。
 
-実際のIAM長期アクセスキーをテストに使用してはならない。
-
-さらに、Brokerの実行主体からMachine Accountの権限を拡大できないことを確認する。
+Brokerの実行・管理主体からMachine Accountの権限を拡大できないことを確認する。さらに独立した二者承認が成立していても、禁止対象の模擬IAMキーを許可Secretへ混入させる変更が取得前に拒否されることを検証する。取得後の検出・破棄を取得前隔離の合格として扱ってはならない。
```

## 変更理由と非退行判定の境界

| 条項 | 既存保証 | 明示的な変更 | 禁止される非退行判定 |
|---|---|---|---|
| REQ-009 | AI/MCP/ログへの秘密非公開、Broker内での認証情報利用 | **資格情報種類ごとの独立実行境界**を新たに定義 | Adapter内のBWS Token使用を旧「Broker保護境界」と黙示同一視しない |
| REQ-046 | Broker専用Machine Account / Project分離、管理権限分離 | Brokerインストール専用の**Adapter保有**Machine Accountへ主体変更、全8相当の安全条件を全文整合 | CLI・末尾のBroker専用表現や元の第6項を取り残さない |
| AC-022 | テストSecret肯定的取得、保護Project拒否、権限拡大拒否 | **Adapter取得/Broker拒否**へ検査主体変更し、取得前保証を必須化 | Adapter無効だけで肯定的取得をPASSと扱わない |

REQ-045およびQ33〜Q40の「既存IAM長期キーへの一切のアクセス禁止」は不変。正式採用されても、2名承認済みの禁止Secret混入を認めることはない。

## Owner Decision Record（未記入。推測で埋めない）

- `decision_id`: **PENDING**
- `decision`: **UNDECIDED (A / B)**
- `requirements_owner_identity`: **NOT_RECORDED**
- `decision_timestamp_JST`: **NOT_RECORDED**
- `approved_source_baseline_digests`: **NOT_RECORDED**
- `adopted_clause_text_digests`: **NOT_RECORDED**
- `rationale_and_impact`: **NOT_RECORDED**
- `separate_independent_normative_review`: **NOT_EXECUTED**

この文書の作成、ZIPハッシュの一致、独立レビュアーからのコメント、またはChatGPTの推奨文はOwner承認の代用にならない。
