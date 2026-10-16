# AWS MCP Broker v1.1 — Clause-by-clause Non-regression Matrix

**Status:** `STATIC_RECONCILIATION_CANDIDATE / INDEPENDENT_VERIFICATION_REQUIRED`

固定B1/B2の規範は削除・置換しない。B3ユーザー決定とREQ-050〜059/AC-025〜036候補の**条項ごとの意図した効果**を列挙する。これは静的な差分照合用であり、動的安全性や原本の真正性を証明するものではない。

## REQ-001〜049（49件）

| 原文ID | 原文要旨（照合用） | Rev4との関係/非退行評価 |
|---|---|---|
| REQ-001 | 登録済みAWSアカウント限定 | B1原文維持。050〜059はアカウント対象を追加しない |
| REQ-002 | 利用者/エージェント別アクセス | B1原文維持。053の主体認証は追加制約 |
| REQ-003 | タスク範囲内マルチアカウント | B1原文維持。053がタスク要求完全性を追加 |
| REQ-004 | 全AWS API事前認可/取消 | B1原文維持。053/057はAdapterへの追加境界 |
| REQ-005 | 読み取りがデフォルト | B1原文維持。Bitwarden外部操作も書込禁止 |
| REQ-006 | 短期read認証更新 | B1原文維持。BitwardenのBWS Token更新と混同不可 |
| REQ-007 | 長期AWSキー禁止 | 045/047で取得とSDK暗黙fallbackまで禁止を強化 |
| REQ-008 | 無人AWS認証 | 050でBitwarden未配置でも起動。048で人間セッションと分離 |
| REQ-009 | AI/MCP/通常ログへ非公開、**Brokerの保護された実行境界のみで認証情報を使用** | **Owner承認待ちの明示改訂**：STSはBroker/Executor、BWS Token/外部Secretは独立Adapter。原文からの境界変更であり非退行を自動認定しない。`08-owner-decision-request.md`の**全条項全文・diff・本文SHA**参照 |
| REQ-010 | 対話型の人/Agent双方認証 | 053が独立発行者の人間確認を必須化 |
| REQ-011 | 無人サービス主体/Agent検証 | 053が独立サービス主体検証を必須化 |
| REQ-012 | Portal/直接接続の同一保証 | 053の証明は接続経路を理由に省略不可 |
| REQ-013 | Portal identityの独立検証 | 053はBroker主張による証明発行不可 |
| REQ-014 | AWS書込は1操作1承認 | 外部連携は全面書込禁止。056の設定変更二者承認は別ドメイン |
| REQ-015 | AWS書込の独立Web承認 | 外部連携にAWSの個別承認を流用しない |
| REQ-016 | AWS書込対象とパラメータ固定 | 052の外部操作契約固定は別ドメインで追加 |
| REQ-017 | 承認再使用/二重実行禁止 | 053/057のAdapter証明も複数インスタンスで一回限り |
| REQ-018 | AWS承認15分/開始5分 | B1原文維持。Token発行の二者承認とは別 |
| REQ-019 | AWS書込は登録済み・検証済みだけ | 外部書込を許可する根拠にしない |
| REQ-020 | AWS書込の自動再試行禁止 | 052の外部read retry規則はAWSの制約を緩めない |
| REQ-021 | AWS高リスク変更は無条件禁止 | 056のAdapter設定変更承認はAWSの禁止例外とならない |
| REQ-022 | AWS全般read、個別安全確認 | Bitwardenの初期外部操作リスト空と矛盾しない |
| REQ-023 | 秘密値/データ本文原則禁止 | 054が外部返答の秘密保護を追加。例外緩和しない |
| REQ-024 | 安全なAWS公式MCP部分互換 | 外部Secret AdapterにAWS API任意実行を委譲しない |
| REQ-025 | Bitwarden Secrets Manager保管 | 050によりQ34/Q38で「連携機能必須/デフォルト無効」を追補。解釈の非退行は独立Review |
| REQ-026 | Broker内の登録・設定永続化 | Adapter独立設定をBroker可変に拡張しない |
| REQ-027 | Broker管理Webで設定操作 | Adapter/Token管理は独立境界でBroker画面から禁止 |
| REQ-028 | Git運用設定依存禁止 | 056のCI/CD経路列挙はGit運用必須化ではない |
| REQ-029 | タスク/Agent/全体のAWS利用上限 | 052/053のAdapter制限は追加、AWS制限を緩めない |
| REQ-030 | AWS上限後新規操作拒否 | B1原文維持。Adapterも独立上限 |
| REQ-031 | 安全readのみ障害後再開 | 057はAdapterの未確定処理自動再実行を認めない |
| REQ-032 | 終了・取消後新規AWS操作禁止 | 057のC/Sは外部Adapterへの追加制約、AWS禁止不変 |
| REQ-033 | AWS既受付処理の取消保証なし | 057の外部in-flight区別も同様に残存として記録 |
| REQ-034 | STS残存追跡 | BWS session残存は別管理、STS保証を代替しない |
| REQ-035 | 必要条件不明時Fail Closed | 全新規REQで証明/契約/監査欠落は拒否 |
| REQ-036 | AWS操作の構造化監査 | 外部操作/Token管理は独立監査を追加 |
| REQ-037 | 追記監査90日/秘密記録禁止 | 外部監査にも秘密を流さず独立改変防止を追加 |
| REQ-038 | Broker設定/承認/監査永続化 | 外部証明単回性/取消永続台帳は追加し、Broker設定を省略不可 |
| REQ-039 | 自動暗号化バックアップ | Adapter追加のため既存Brokerバックアップ要件を緩めない |
| REQ-040 | 復元後の承認再生禁止 | 外部証明/契約/Token更新でも古い状態の再生禁止 |
| REQ-041 | Deno/Workers/Docker Linux+mac | 059で対象構成を個別に証拠化 |
| REQ-042 | 機能と安全性の同等性 | 059で未実証をfull complianceと表示禁止。AWS-onlyを代替扱い禁止 |
| REQ-043 | Broker間独立/同一Broker多instance | 055はMachine AccountをBroker install別に独立、057が多Adapter競合を強化 |
| REQ-044 | AWS Lambda必須化禁止 | 新規要件でもLambda使用を前提にしない |
| REQ-045 | 既存IAM長期キー流入禁止 | 055/056とAC-036で未承認・正規二者承認双方のSecret内容混入/差替え経路を拒否 |
| REQ-046 | **Broker専用Machine Account**と最小Project権限 | **Owner承認待ち**：REQ-046の冒頭/第1〜6項/Password Manager段落/CLI段落の改訂後全文を`08`に収録。既存IAMキー取得禁止は不変 |
| REQ-047 | AWSキーfallback禁止 | 050/058はBitwarden障害時AWS長期キー代替を認めない |
| REQ-048 | フィッシング耐性と再認証 | B2-S1で8h/15m確定。053は独立認証を追加 |
| REQ-049 | 秘密の複製・STS実行利用最小化 | 054/055のAdapter秘密境界と両立。STS必要使用は維持 |

## AC-001〜024（24件）

| 原文ID | 原文要旨（照合用） | Rev4との関係/追加試験 |
|---|---|---|
| AC-001 | 3環境AWS認証 | 050/059によりBitwarden不要、環境別未実証を明示 |
| AC-002 | 登録済み複数アカウント切替 | 変更なし |
| AC-003 | 未許可アカウント拒否 | 変更なし |
| AC-004 | readonly credential write禁止 | 変更なし |
| AC-005 | read認証自動更新 | BWS tokenローテとは別 |
| AC-006 | Portal/直接接続本人性 | 034で独立発行者試験も追加 |
| AC-007 | AWS個別書込承認 | 外部サービスwrite禁止を維持 |
| AC-008 | AWS承認二重使用防止 | 035でAdapter証明単回性を追加 |
| AC-009 | 承認期限・取消時拒否 | 029/035のAdapter時系列を追加 |
| AC-010 | AWS高リスク禁止 | 外部二者承認によるAWS例外なし |
| AC-011 | AWS取消後新規拒否 | 029/035は外部Adapterでの追加試験 |
| AC-012 | AI/ログ/応答秘密非公開 | 025/032/033でAdapter漏洩経路も検証 |
| AC-013 | AWS書込outcome_unknown/再送禁止 | Adapter結果不明時の再送保証と区別 |
| AC-014 | 安全readのみ復旧 | 変更なし |
| AC-015 | AWS利用量上限 | 外部Adapterレート制限は追加 |
| AC-016 | AWS監査 | 独立Adapter監査は追加 |
| AC-017 | バックアップ承認復活不可 | 027/035でAdapter証明・Token承認の復活も拒否 |
| AC-018 | 3環境安全性試験 | 031を増補。Docker Linux/macを区別 |
| AC-019 | MCP実呼び出し強制認可 | 053/034でBroker自己申告による認可迂回を拒否 |
| AC-020 | 隔離実AWS非本番検証 | 032の外部模擬読み取り試験は追加、実AWS試験を省略しない |
| AC-021 | 長期キー不使用認証 | 030/031もBitwarden不使用の経路を確認 |
| AC-022 | **Broker専用Machine Account**によるテストSecret取得、別Project模擬IAMキー拒否 | **Owner承認待ち**：取得主体をAdapterへ変更する改訂全文を`08`に収録。二者承認済みの禁止内容混入もAC-036で拒否。取得前隔離未証明では肯定的取得試験BLOCKED |
| AC-023 | 失敗時fallbackなし | 030でもBitwarden AWS credential経路を認めない |
| AC-024 | 再認証・無人分離 | 034が独立主体確認を追加 |

## 追加のクロス参照

- REQ-025→REQ-050（初期無効）, REQ-042→REQ-059（3環境）, REQ-045/046→REQ-055/056（既存キー隔離）, REQ-014〜021→REQ-052（AWS vs 外部書込）, REQ-010〜013→REQ-053（独立本人性）。
- AC-021〜024→AC-025/028/030/031/033/034/036。既存ACの動的要求は新試験で置き換えられない。
- `RG-BRK-NR-001`: B1/B2本文はZIP内でSHA-256固定したが、外部に所有者が承認した署名付き原本があるかは不明。独立Reviewerは本会話の決定と本文を別途比較し、相違があれば`BASELINE_MISMATCH`を報告する。

**Static coverage:** 49 REQ / 24 AC / total 73 entries. **Dynamic proofs:** 0.

## Rev4重点非退行・衝突マトリクス（Owner未承認の採用禁止）

| 旧条項 | 新条項との衝突 | 修正条件 | 判断 |
|---|---|---|---|
| REQ-009 | Broker保護境界のみ vs 独立Adapter保護境界 | 種類別保護境界をOwnerが明示的に採用 | OWNER_PENDING |
| REQ-046 | Broker専用Machine Account vs Adapter保有Machine Account | インストール専用/Adapter保有/最小権限を明文化しOwner採用 | OWNER_PENDING |
| AC-022 | Broker専用Machine Accountの取得試験 vs BrokerによるToken/Secret取得禁止 | Adapterの取得限定とBrokerの拒否をOwner採用しAC-033と整合 | OWNER_PENDING |
| REQ-045 | **既存キーの取得自体を禁止** vs 許可Secret値だけ差替え | 取得前独立強制。事後検査では不合格。実証不能なら連携停止 | NOT_PROVEN/BLOCKING |
| REQ-032〜035 | AWS取消/失効保証 vs Adapter `S/D/C/R` | AWS側取消を緩和せず外部に追加。未送信キューを取消後送らない | NOT_PROVEN |
| REQ-042 | 3環境の完全同等性 vs Adapter連携の環境別無効化 | 不完全環境は非完全準拠。要件緩和する場合Owner判断必須 | NOT_PROVEN |

固定原文ファイルのDigestはRev2と同一。`SHA256SUMS`参照。全49 REQ/24 ACの行は維持。真正性・逐字の独立照合は未完了。

## Rev4の追補トレース — RG-BRK-NR-R3-001/002

| 既存条項 | 新規・改訂候補 | 対応AC | 状態 |
|---|---|---|---|
| REQ-009 | 本文全文改訂案（credential別実行境界、Broker/Adapterの明示分離） | AC-025/AC-022改訂候補 | OWNER_PENDING |
| REQ-046（冒頭/1〜6/末尾2段落） | 本文全文改訂案（Broker設置単位、Adapter専用主体、Password Manager及びCLIの全経路） | AC-022/025/026/028/033/036 | OWNER_PENDING |
| AC-022 | 全文改訂案（Adapter肯定的取得＋Broker拒否＋正規承認毒入れ否定） | AC-033/036補完 | OWNER_PENDING |
| REQ-045 | 取得禁止は承認の有無で解除できない | AC-028/033/036 | NOT_PROVEN |
| REQ-055 | 2名承認が成立してもSecret値取得前の独立内容保証が必須 | AC-028/033/036 | NOT_PROVEN / FEAS-007-C BLOCKED |
| REQ-056 | 2名承認は必要条件であり取得前禁止内容検査の代用不可 | AC-027/028/036 | NOT_PROVEN / INT-003 OPEN |
| REQ-057 | C/S/D/R、物理送信境界維持 | AC-029/035 | NOT_PROVEN |

**Fixed text / candidate text:** B1/B2原文を維持。正式採用後の改訂原文との73件の非退行判定は、採用Decision Recordと新しい版Digestに対して独立にやり直すこと。R4の文書ハッシュは採用の証明ではない。
