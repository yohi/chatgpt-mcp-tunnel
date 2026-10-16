# AWS MCP Broker v1.1 — Requirements Owner 採用意思表明・正式決裁証跡固定用 Record

> **現時点の判定:** `OWNER_APPROVAL_INTENT_RECORDED / OWNER_RATIFICATION_PENDING / NOT_EFFECTIVE`  
> このファイルは**承認対象本文を固定した決裁記録の準備版**である。ChatGPT上の意思表示、ファイルのSHA-256、プロジェクトの編集権限だけでは、正式な本人認証済み決裁・B1/B2/B3の権威証明・Normative PASSにならない。

## 1. 決裁メタデータ

| フィールド | 記録値・扱い |
|---|---|
| 決裁対象 | AWS MCP Broker v1.1 Option A — `REQ-009`, `REQ-046`, `AC-022` の全文改訂 |
| Owner意思 | **採用意思あり（2026-10-14 JST、ChatGPT上の本人申告）** |
| Ownerの立場 | 本会話で本人がRequirements Ownerとして最終決定権限ありと申告 |
| 決裁の方針 | 採用候補3本文を変更せず採用する意思。Gate解除・実装許可とは独立 |
| Proposed Decision ID | `AWS-MCP-BROKER-V1.1-ODR-20261014-001` （予約案。正式発番前） |
| Formal Decision ID | `PENDING — 認証済み決裁システムの正式IDを固定` |
| Owner識別子・役割の根拠 | `PENDING — 権威あるプロジェクト規約・委任記録等を参照` |
| 承認時刻 | `PENDING — 認証済みシステムに記録された実際のUTC/JST時刻` （ChatGPTの発話日を正式承認時刻に流用しない） |
| 署名・監査記録 | `PENDING — 署名済みコミット・承認イベント等の検証可能なURL / ID` |
| 発効判定 | `NOT_EFFECTIVE` （B1/B2/B3原本 provenance とOwner決裁証跡の固定完了まで） |
| Independent Normative Review | `NOT_EXECUTED / NOT_GRANTED` |

## 2. 凍結した審査根拠

| 対象 | SHA-256 | 状態 |
|---|---|---|
| R1 Decision Record `01-owner-decision-record-option-a-limited-correction-r1.md` | `92cef5b23ca9696ede0c9a6d5ca979056c20b6c17853598afcf6af914f60865e` | この出力の作成時にローカル再計算一致 |
| R4 Owner Decision Request `08-owner-decision-request.md` | `021f2ca95d6f769881150bc00df067692eccc0cb3fc174a567fe3f83fa255d90` | この出力の作成時にローカル再計算一致 |
| R1 ZIP `aws-mcp-broker-v1.1-option-a-limited-correction-r1(1).zip` | `cedf39f04a1733e42fe00e22f9c262a0bd5ad62a682a6ee50efdced287e85912` | 既存R1再審査報告書に記載。今回ZIP直接再検証は未実施 |

### B1/B2/B3 Baseline参照

| ID | 同梱ファイル名 | 記録されたSHA-256 | 外部の権威ある原本参照・承認根拠 |
|---|---|---|---|
| B1 | `01-fixed-baseline-v1.0.md` | `39002fc2ce5f21e9e686a427c793a7fd42fc84e5bdb02684be9e1e3a4305f4bc` | `PENDING` |
| B2 | `02-fixed-baseline-v1.1.md` | `3078acc5c31b5e900697dbb585e5ed604dfca89fe82b56cfc9528ac3c91350e2` | `PENDING` |
| B3 | `03-fixed-decisions-Q33-Q40.md` | `f287966ac61f467704f99c545f2d7a9756b9f21a70a5f90a814367ab7a113aa4` | `PENDING` |

B1/B2/B3 のファイル名とSHA-256は R1 Recordから転記した**既存提出物内の固定識別子**であり、原本を保有する公式リポジトリ／承認済み記録との照合までは済んでいない。版・正式な承認者・承認日・保管先 URL/commit はそれぞれ追記・検証すること。

## 3. 採用意思を表明した条項（全文・Digest一致）

**ハッシュ計算規則:** 本文だけをUTF-8で符号化し、前後空白を `strip()` してSHA-256。見出し・Markdownコードフェンス・終端追加改行は除外する。以下の全文はR1 Decision Recordから抽出し、3件ともDigest一致を再計算した。

### REQ-009 — 採用対象全文

- 本文SHA-256: `f17db0565942501a39c3302912dcb161e2f3e38e168f29a51491a711e0851bb9`

```text
AWS認証情報、一時クレデンシャル、Bitwarden認証情報をAIエージェント、MCP応答、通常ログへ公開してはならない。

認証情報は種類ごとに明示的に認可された、実効的に保護され相互に隔離された実行境界内でのみ使用すること。AWS STS一時認証情報はBroker/AWS Executorの保護領域で必要なAWS API署名に限り使用できる。BWS Access TokenはBrokerから独立したSecret Adapter専用のSecret Store・実行主体の保護領域内でのみ使用できる。外部サービス用Secretは独立Secret Adapter内で、認可済みの外部サービス操作に限り利用できる。

Broker本体、AWS Executor、管理Web画面、AIエージェントにBWS Access Tokenまたは外部サービス用Secretを取得・復号・使用できる権限や経路を設けてはならない。既存AWS IAM長期アクセスキーはBroker、AWS Executor、独立Secret Adapter、独立認可主体その他の関連構成要素のいずれも取得・復号・使用してはならない。これらの境界は、システム全体を指す「Broker」という集合名によって同一実行・管理境界とみなしてはならない。
```

### REQ-046 — 採用対象全文

- 本文SHA-256: `6362d06bfe5d1c1184057f84c42f2f6ed4c19d6dc47b8662cfe039105e21d931`

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

### AC-022 — 採用対象全文

- 本文SHA-256: `3a02643899b8d79683f6c13300e0ee655b4b00fe20d23f87a3c35efb4e521a39`

```text
Brokerインストール単位で割り当てたAdapter専用Machine Accountについて、認可された独立Secret Adapterだけが、許可された隔離テスト用Secretを取得・使用できることを検証する。ただしSecretの取得前に独立した内容不変性・真正性・Version拘束と禁止値混入防止を実証できない場合は肯定的取得試験を開始せず、当該機能を`BLOCKED`とする。実際のIAM長期アクセスキーを試験に使用してはならない。

Broker本体、AWS Executor、AIエージェント、Broker管理Web画面からはAdapterのBWS Access Tokenおよび外部サービスSecretを取得・復号・使用できないこと。別の保護対象Projectにある模擬IAM長期アクセスキーの取得は権限によって拒否されること。

Brokerの実行・管理主体からMachine Accountの権限を拡大できないことを確認する。さらに独立した二者承認が成立していても、禁止対象の模擬IAMキーを許可Secretへ混入させる変更が取得前に拒否されることを検証する。取得後の検出・破棄を取得前隔離の合格として扱ってはならない。
```

## 4. Ownerによる承認対象と明示的な非承認範囲

**採用対象:** 第3節のREQ-009、REQ-046、AC-022の全文と指定SHA-256の組み合わせを承認対象とする。テキストやDigestが変われば**新たな決裁対象**とし、この意思表明を流用しない。

**採用対象外:** R4提案REQ-050〜059・AC-025〜036の一括採用、二者承認の迂回、既存IAM長期アクセスキーへの取得経路、仕様の実装可能性の保証、Gate解除、本番運用認可。R1の二者承認例外は認可済み管理者1名の緊急縮小操作に限定され、権限拡大・権限復旧・再有効化は含まれない。

## 5. 実行する正式決裁・証跡固定（人間Ownerが実施）

1. **B1/B2/B3原本を指定:** 公的な保管先の固定URL・version/commit・SHA-256・当初の承認記録を収集する。原本と一致しないものをこのRecordで追認しない。
2. **本人・権限を結びつける:** プロジェクトのRequirements Ownerを定めた規約・任命/委任記録を、この文書のOwner識別子および決裁アカウントにリンクする。自己申告しかなければ `NOT_VERIFIED` を維持する。
3. **認証済みシステムに正式決裁を記録:** この全文（または参照先と改変不能なDigest）について、Owner自身が認証済みアカウントで `APPROVE — Option A / REQ-009, REQ-046, AC-022` を記録する。GitHubを使う場合は、署名検証可能なコミットまたは監査可能な承認イベントを推奨。認証イベントだけで役割権限が証明できるとは扱わない。
4. **事実に基づくメタデータを補完:** 実際に生成されたDecision ID、イベント/署名 URL、UTC/JSTの実時刻、承認主体のID、権限根拠、B1/B2/B3証拠をそのまま記録する。**過去に遡った承認時刻は付けない。**
5. **独立レビュアーへ引き継ぎ:** 認証済み決裁と原本照合が成立した後にのみ採用後Normative Reviewを別の主体が行う。レビューのPassと技術GateのPassを混同しない。

### 本人による正式承認イベントに貼る一文

> 私はAWS MCP Broker v1.1のRequirements Ownerとして、`REQ-009`（`f17db0565942501a39c3302912dcb161e2f3e38e168f29a51491a711e0851bb9`）、`REQ-046`（`6362d06bfe5d1c1184057f84c42f2f6ed4c19d6dc47b8662cfe039105e21d931`）、`AC-022`（`3a02643899b8d79683f6c13300e0ee655b4b00fe20d23f87a3c35efb4e521a39`）について、本Decision Recordの第3節に固定された全文を変更なく採用すると決裁します。B1/B2/B3の権威原本参照が未確認である限り発効を保留し、INT-003・Gate S0/S1/Cは未証明のまま維持します。実装・本番利用は別途承認します。

## 6. 登録後に埋める証跡欄（現時点では未記入）

| Evidence key | 実際の値 |
|---|---|
| Official Decision ID | `PENDING` |
| Owner account identifier | `PENDING` |
| Owner authority reference | `PENDING` |
| UTC approval timestamp | `PENDING` |
| JST approval timestamp | `PENDING` |
| Signed commit SHA / approval event ID | `PENDING` |
| Immutable event URL | `PENDING` |
| B1 authoritative source and approval | `PENDING` |
| B2 authoritative source and approval | `PENDING` |
| B3 authoritative source and approval | `PENDING` |
| Provenance verification | `NOT_VERIFIED` |
| Ratification status | `PENDING / NOT_EFFECTIVE` |

## 7. Gate status（本記録では変更しない）

| 項目 | 状態 |
|---|---|
| R1限定修正 | `ACCEPTED` |
| ODR-IR-001 | `CLOSED (STATIC TEXT ONLY)` |
| ODR-IR-002 | `OWNER_APPROVAL_INTENT_RECORDED / ATTESTATION_PENDING` |
| ODR-IR-003 | `NOT_VERIFIED` |
| INT-003 | `CRITICAL OPEN` |
| Gate S0/S1/C | `NOT_PROVEN` |
| Normative Review | `NOT_GRANTED` |
| Effective normative baseline | `UNCHANGED / NOT_EFFECTIVE` |

**この準備文書を単に生成・保存しただけでは `ODR-IR-002` はCLOSEDにならず、新規規範は発効しない。**
