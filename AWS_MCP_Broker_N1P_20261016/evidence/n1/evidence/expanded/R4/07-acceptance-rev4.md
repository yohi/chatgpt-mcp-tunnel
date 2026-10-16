# AWS MCP Broker v1.1 — Acceptance Test Contract Revision 4

**Status:** `CANDIDATE / ALL_NOT_EXECUTED / OWNER_DECISION_PENDING`  
**Prior fixed AC:** AC-001〜020 (B1)、AC-021〜024 (B2) は原文をそのまま維持。AC-022の変更候補はOwner承認待ちの別紙に分離。  
**Candidate AC:** AC-025〜031（改訂）、AC-032〜036（追加候補）。現時点で試験実施・環境検証は行っていない。

## 1. AC-025〜036 契約

| ID | 試験対象 | 合格条件 | 要件 | 状態 |
|---|---|---|---|---|
| **AC-025** | Broker完全侵害模擬・Credential境界 | Broker runtime/管理UI侵害下でもBWS Token、独立認可発行鍵、別Projectの模擬IAMキー取得不可。STSはBroker/AWS Executor保護域、BWS Tokenと外部Secretは独立Adapter保護域に限り、Broker→AdapterのToken出力経路なし。REQ-009/046・AC-022改訂をOwnerが承認しない限り、境界変更をPASSとして扱わない | 009/045/046/049/051/053/054/055 | NOT_EXECUTED |
| **AC-026** | Adapter管理独立 | Broker/Executor/AI/管理Web主体によるAdapterコード・環境・Secret binding・Secret Store・許可リスト・発行主体の信頼先・CI/CD・ロールバック・監査変更を拒否。実際に付与された権限を検証 | 051/055/056 | NOT_EXECUTED |
| **AC-027** | 高リスク変更二者承認 | 異なる2人の認証済み管理者による**具体的な同一変更**のみ1回適用。単独、同一人別アカウント、変更Digest差替え、操作契約差替え、旧承認/ロールバック/リプレイ、将来包括Tokenローテーション、承認期限切れ、並行競合は拒否 | 052/056/058 | NOT_EXECUTED |
| **AC-028** | 全管理迂回経路と取得前強制 | Bitwarden Owner/Admin、Secret**値のみの差替え**（ID/Project/Versionメタデータが同一と見える場合を含む）、Cloud/CI/CD/deploy/復元/Store権限を対象に未承認変更経路0件を権限実体で検証。**正規2名の承認済み変更による禁止内容混入**は別途AC-036で検査し、承認を取得前安全性の根拠としない。Secret値の事後検出を取得前強制の証拠にしない。事前検証が不成立ならBitwarden読み取り0件・Adapter連携無効と記録 | 045/046/051/055/056 | NOT_EXECUTED |
| **AC-029** | 緊急停止、C/S/D/R時系列 | 管理者1名の縮小操作を再現。`C<S`ではS拒否、`S<C`かつD未開始では初回送信0、`C<D`ではD拒否、`D<C`のみ残存到着可能として追跡。クラッシュ、復旧、複数Adapter、未送信バッファ、独立監査/台帳障害、Bitwarden既存セッション残存を注入 | 053/057/058 | NOT_EXECUTED |
| **AC-030** | 初期無効運用 | BWS Token/Adapter起動/Bitwarden通信なしで認可済みAWS読み取りが動作。Bitwarden停止にAWS初期認証が依存しない。外部操作はすべて拒否され、初期許可リストは空 | 007/025/045/047/050 | NOT_EXECUTED |
| **AC-031** | 3環境別の状態と保証 | Deno Deploy、Cloudflare Workers、Docker/Linux、Docker/macOSごとにAWS-only初期無効、Adapter有効、Owner改訂承認、秘密内容取得前強制、実送信C/S/Dを独立評価。保証が満たせない環境はAdapter連携を無効・非完全準拠として表示、N/Aには規範根拠必須 | 008/041/042/059 | NOT_EXECUTED |
| **AC-032** | 非本番肯定的E2E（取得前保証付き） | 明示許可を得た隔離非本番の安全なテストSecretだけについて、取得前の独立した内容不変性/Version拘束・主体証明・契約Digest・Adapterの限定的Secret利用・安全な固定テスト先からのread・レスポンス秘匿化・独立監査をE2Eで確認。取得前強制が未成立なら**実Secret取得試験を実行せずBLOCKED**とする。ローカル非Secretモックの成功のみでPROVEN不可 | 050/052/053/054/055 | NOT_EXECUTED |
| **AC-033** | 値だけ差替えの取得前否定試験 | 特権者が許可済みSecretの**値だけ**を模擬IAMキーへ置換し、Secret ID/Project/見かけのVersion/契約/参照を変えずに取得を誘発。**未承認の変更と、正規2名が誤認のまま承認した変更の両方**について、Adapterの**BWSからの値取得リクエスト送信前**に独立強制点が拒否し、Secret値を一切取得しない証拠を確認。値を取得した後でDigest/形式検査・破棄する方式はFAIL。事前強制不能なら当該Secretの全取得を禁止して機能BLOCKED（隔離保証PROVENではない） | 045/046/054/055/056 | NOT_EXECUTED |
| **AC-034** | **証明発行根拠/契約束縛** | Brokerが認証済みユーザーID/承認/operationを偽装して発行要求しても証明されない。独立本人/サービス主体確認と元要求の完全性がない発行を拒否。旧契約Digest、出力Schema変更、宛先変更、単回証明再利用、別Broker/Adapterチャネルでの横流し、取消Epoch相違を拒否 | 010〜013/052/053/056 | NOT_EXECUTED |
| **AC-035** | 取消・最終送信境界・単回性 | Sは単回消費の送信解放、Dは最終transportへの実送信開始、Cは取消確定、Rは受理観測として別に記録。S<C/未送信で停止→C→再開後の**初回送信0**、C<D拒否、D<Cなら再送せず残存記録。複数Adapter同時、キュー、停止、ロールバック、分断、物理transport送信の強制点を検証。Dを帳簿に記録しただけで実送信を制御できない場合はFAIL | 017/032〜035/053/057 | NOT_EXECUTED |
| **AC-036** | **正規二者承認済みの禁止Secret混入** | 隔離非本番で異なる2名が正当に承認した具体的な変更として、許可済みSecretの値だけを**無効な模擬IAM長期アクセスキー**へ変更するケース、ID/Project/メタデータ変更ケース、許可された生成元を装ったケースを検証。正規承認・署名・許可操作契約が存在してもAdapterは**Secret取得リクエスト前**に禁止内容の取得を拒否する。変更承認者の誤認を含む。独立した禁止値混入防止の強制が成立せずBWS呼出しを許すならFAIL。機能全停止のみの場合は連携`BLOCKED`であり、Bitwarden有効動作のPASSではない | 045/046/054/055/056/059 | NOT_EXECUTED |

## 2. 必須否定試験の具体例

1. **Secret内容の毒入れ:** 許可された読み取りIDのSecretを模擬IAMキーに**値のみ**置換し、ID・Project・読取り前メタデータとMachine Account権限自体は変えない。**取得後の検出は不合格**（試験は隔離したダミーSecretのみ）。
2. **正規二者承認の誤認:** 2名の別人管理者が正当に承認した変更でも、その内容が模擬IAM長期キーなら取得前に拒否されること。承認成功・Secret署名・用途ラベルを「IAMキーではない」ことの証明と誤認しない。
3. **権限迂回:** Bitwarden Organization特権者がProjectを変更する、CI/CDがAdapterを差し替える、クラウド特権がSecret bindingを再設定する。二者承認を強制できなければFAIL。
4. **発行者のconfused-deputy:** Brokerがuser_idを偽装し、本人確認証拠のない署名証明を請求。単にBrokerのmTLSが有効でも発行しない。
5. **同じoperation ID・変更後定義:** 宛先、HTTPメソッド、Secret ID、応答検証・秘匿化規則などを差し替え、古い証明を使用。全ケース拒否。
6. **C/S/D競合:** S前取消、S後D前取消、D後取消、S後停止→取消→再起動、複数Adapter同時、送信キュー/ソケット、状態ストア分断、監査書込み失敗を別々に検証。
7. **自動Tokenローテーション:** 二者承認した単一変更だけ実行成功し、2回目の発行/配置および無期限/無件数の予約での新規変更は拒否。
8. **外部読み取りも副作用可能:** GETで秘密値/副作用/307リダイレクト/DNS差替えを起こすテスト先を許可しない。
9. **資格情報フォールバック:** AWS認証が失敗した環境に長期キーに相当するダミー環境変数を設置しても、使用せず拒否する。

## 3. Test-only positive operation の条件

- 操作名（例）は `test.status.read` とするが、これ自体は本番許可を意味しない。
- 対象は**明示承認された隔離非本番環境**で用意した外部サービス模擬エンドポイントと**使い捨て模擬Secretのみ**。実際のBitwarden既存IAM長期キーを試験材料にしてはならない。
- 認可サービスとAdapterの独立性を維持した実行契約を固定し、Secretの利用はAdapter内部で終わる。
- 正常応答には秘密値を含めず、出力検査の否定ケースとしてだけ模擬秘密値を利用する。
- テスト終了後に操作許可リストを初期空状態へ復帰させ、復帰の監査・残存権限を検証する。
- 本文は受け入れ条件の定義であり、テスト環境構築、資格情報発行、Bitwarden Secretの取得、実AWS操作を**許可する文書ではない**。

## 4. Environment evidence matrix（空欄があればNOT_PROVEN）

| 実行環境 | Bitwarden無効AWS-only: AC-030,AC-021 | Bitwarden有効Adapter: AC-025〜029,032〜036 | AC-031完全準拠 | 現状 |
|---|---|---|---|---|
| Deno Deploy | 未実施 | 未実施 | 未判定 | NOT_PROVEN |
| Cloudflare Workers | 未実施 | 未実施 | 未判定 | NOT_PROVEN |
| Docker on Linux | 未実施 | 未実施 | 未判定 | NOT_PROVEN |
| Docker on macOS | 未実施 | 未実施 | 未判定 | NOT_PROVEN |

**NOT_APPLICABLE制限:** `N/A`は当該ACを無効化した機能・構成にそもそも要求しないという規範上の根拠、無効化を強制した具体的な証拠、承認者、影響を記した場合だけ許可。単なる「未実装」「試していない」はN/A不可。Bitwarden有効のv1.1完全準拠を主張するには、必要なAdapter試験をN/Aで回避できない。

## 5. Evidence Package の必須内容

- テスト対象の固定版、対象環境/ランタイムとRegion・ホストOS、ファイル/設定/政策Digest、試験者/独立Reviewerの役割分離。
- Broker、Adapter、発行者、Secret Store、Bitwarden Org管理者、Cloud/CI/CD特権、ユーザー/サービス主体間の実効権限マトリクス。
- Secret ID・内容・参照・配置先の変更を含む全経路の一覧、二者承認の強制点、未検証経路。
- C/S/D/Rの単一順序・単回使用・失効Epoch・実送信境界の競合再現ログと、失効済みBWS認証セッションの残存追跡。
- タスク実行の前後で独立監査・権限を照合する証拠。秘密値、実AWS長期キー、BWS Access Tokenは証拠に出力しない。
- 各AC×環境を`PROVEN/PARTIALLY_PROVEN/NOT_EXECUTED/BLOCKED/NOT_APPLICABLE`で表示。PASS見込みや静的文書だけをPROVENにしない。

## 6. Gate

- Gate S0（既存IAMキー隔離）＝NOT_PROVEN。AC-021〜023,025〜028,033,036が必要。
- Gate S1（Adapterの安全操作）＝NOT_PROVEN。AC-025〜036とFEAS-007が必要。
- Gate C（全3環境同等）＝NOT_PROVEN。AC-031とFEAS-001/011、Docker Linux/macOS実証が必要。
- INT-003（単独特権経路での二者承認迂回）＝OPEN/BLOCKING。いかなる文書審査のPASSも動的保証の解除を意味しない。

## 7. Rev4の判定留保（AcceptanceのPASSを先取りしない）

- `REQ-009/046/AC-022`の保護主体再定義はRequirements Owner未承認。AC-025/022の部分一致を正式PASSとして扱わない。
- Secret値だけが変わる反例について、取得前に判定する観測値が同じなら、取得を許せば禁止値も取得できる。**本番許可リスト空/Adapter無効はFail Closedの証拠にはなるが、Bitwarden連携機能の安全な肯定的E2E成立の証拠ではない。**
- `S`だけでは送信開始を証明しない。`D`と`C`の実効的直列化、および未送信キューの再開時廃棄を動的検証する。
- AC-025〜036はすべてNOT_EXECUTED。FEAS-007-C、INT-003はBLOCKING。
