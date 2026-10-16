# AWS MCP Broker v1.1 — Phase N1: Authority Source Recovery & Owner Adoption Decision Preparation

あなたは `yohi/chatgpt-mcp-tunnel` の**新規・独立した Requirements / Design Authority Evidence Investigator**です。N0調査者、実装者、過去のレビュアー、正式Requirements Owner、Security/Design承認者、実行者とは役割を分離してください。

## 目的と委任範囲

N0で回収した仕様候補のバイト同一性と、正式な原本権限・採用イベントを区別し、**人間Requirements Ownerが過去の採用を検証するか、必要なら将来効力の新規採用を決裁できる未署名パケット**を整備してください。仕様改変、Ownerの意思決定の代行、正式採用済みの宣言は行いません。人間が既に示したOption A採用意思は維持し、同じ選択を繰り返し質問しないでください。認証済み正式決裁は別途必要です。

## 固定対象

- Repository: `yohi/chatgpt-mcp-tunnel`
- Branch: `feat/aws-broad-iam-read-api-tools`
- Fixed HEAD: `ac462699e0b1988eda63ea3d6dacfc2a030bb822`
- PR #14 / #15: merged。I1-TEST-001 / I1-API-002は独立再審査でCLOSEDとの報告あり。AWS実効権限の証明ではありません。
- Working status: `NORMATIVE_BASELINE=NOT_VERIFIED`, `BROKER_RUNTIME_INTEGRATION=NOT_AUTHORIZED`, `G0_EXECUTION_APPROVAL=NOT_AUTHORIZED`, `AWS_API_BUDGET=0`, `Gate STS-001=NOT VERIFIED`。

作業開始時に固定Commit、PR情報、対象ブランチHEADを読み取り検証してください。HEADの変更があれば差分・影響を報告し、勝手にBaselineを差し替えないでください。

## 添付パッケージの使用

まず外側ZIPのSHA-256、ZIP CRC、`MANIFEST.json`、`SHA256SUMS`、各同梱ファイルのSHA-256を**独立再計算**してください。ZIP内パス逸脱・シンボリックリンク・異常な展開を排除し、資料は読み取り専用で扱ってください。以下はあくまで**提出済みコピーまたはドラフト**であり、正式承認原本の証明ではありません。

1. N0成果物ZIP（5文書＋MANIFEST）— 5文書を全文読む。
2. R4 Normative Reconciliation ZIP — B1/B2/B3、既存49 REQ・24 ACの対応、R4 REQ-050〜059／AC-025〜036候補、Findingを読む。
3. Option A Limited Correction R1 ZIP — 正確なREQ-009／REQ-046／AC-022全文、旧条項、差分、独立静的レビューを読む。
4. Owner採用意思表明Record（2026-10-14）— 採用意思と認証済み正式イベントを区別する。
5. STS-001 Broker Security Contract Draft — 正式未承認のSecurity Contract候補として読む。

関連する追加の正式原本や承認イベントがライブラリ／既存の信頼済み文書管理系で取得可能なら、それを探索し、アクセス権限と来歴を明示してください。公開GitHubにない証跡を推測で補完しないでください。承認経路の存在、本人性や独立性も推定しないでください。

## Task A — Authority Chain / B1・B2・B3の正式性

B1=`01-fixed-baseline-v1.0.md`、B2=`02-fixed-baseline-v1.1.md`、B3=`03-fixed-decisions-Q33-Q40.md`を対象に、候補バイト列、Revision、SHA-256、正規のCustodian、原本保存先、正式採用者の権限根拠、採用イベントID・UTC・対象digestを一対一で照合してください。

提出ZIPでの一致と、正式原本・承認の成立を分離します。過去の採用イベントを確認できない場合、既存の採用が有効だったと仮定せず、**人間が現在時点から新しいVersionを前向きに採用する経路（Prospective Adoption）**を候補として整理します。新しい効力開始時刻を推測したり、過去に遡って承認を捏造したりしないでください。権威確認不能な項目は`NOT_VERIFIED`のままにします。

## Task B — 3条項の正確な採用候補

Option A R1に収録された**全文バイト列**を固定し、下記Digestを再計算してください。

- REQ-009: `f17db0565942501a39c3302912dcb161e2f3e38e168f29a51491a711e0851bb9`
- REQ-046: `6362d06bfe5d1c1184057f84c42f2f6ed4c19d6dc47b8662cfe039105e21d931`
- AC-022: `3a02643899b8d79683f6c13300e0ee655b4b00fe20d23f87a3c35efb4e521a39`

旧版との差分、上書き・廃止対象のRevision、REQ-045・REQ-047〜049・REQ-025・INT-001/003との整合条件を記載してください。過去のOption A採用意思は確認済みの意思として維持しますが、正式なOwner身元・権限・認証済み承認イベント・全文digestの結合がない限り`NOT_EFFECTIVE`です。元ファイル名の`adopted-text`表記は採用証跡ではありません。

## Task C — R4の未採用候補 / Design / INT-003

- R4のREQ-050〜059とAC-025〜036は一括採用せず`UNADOPTED_PROPOSAL`として扱い、条項ごとに採用判断・依存関係・影響を整理してください。
- 正式なArchitecture/Design、統合Acceptance Criteria、Security Contractの原本・Revision・SHA-256・採用イベントを調査してください。見つからない場合は`MISSING_AUTHORITY`を維持し、完成したと宣言しないでください。
- INT-003の独立した二者承認について、Bitwarden Owner/Admin、Cloud privileged access、CI/CD、Secret Store、Issuer、Backup/Restore等の**全実効管理経路**を対象に、独立性を実証するための証拠要件を列挙してください。一人が複数のロールを兼ねても二者承認の実証にはなりません。
- 二者承認を実現できない機能は無効化・禁止を維持してください。要件緩和や例外をAIが創設してはいけません。重大なギャップは明示し、人間の設計・セキュリティ判断に差し戻してください。
- REQ-045の既存IAM長期キー完全隔離、REQ-047のフォールバック禁止、AC-022のpre-fetch保証を緩和しないでください。

## Task D — 人間の正式決裁に必要な準備

N0の`04_Owner_Decision_Packet_UNSIGNED.md`にあるN0-OD-01〜04を起点に、次の二つのケースを分けてください。

1. **Historical authority verified**: 実際に認証された過去の原本・採用イベント・有効なRevisionを照合できた場合。
2. **Prospective adoption required**: 過去の来歴が不足し、提出コピーの正確な本文を将来効力の新規Baselineとして採用する必要がある場合。

両ケースで、正式Owner／Design／Security承認権限、原本の固定digest、適用範囲、失効・supersession、選択済み方針、UTC承認イベント、信頼済み保存・監査経路、独立採用後レビューの要件を整理してください。**署名欄・承認イベントは空欄**のままにし、`APPROVED`をAIが記録してはいけません。

既存のOwner意思を再選択させない一方で、新しい正式決裁を実際に行うのに必要な事実と選択（例：R4残余条項、原本Custodian、新しいprospective baseline）を限定して明示してください。本人・権限の証拠原本や機密情報は一般公開リポジトリやチャットに貼らせず、既存の信頼済み私的経路で検証する形式にしてください。

## Task E — N2 / I2の解禁条件

採用原本の全部分のSHA-256、独立した採用イベント、相互整合性、未解決INT-003、安全境界をまとめ、別主体の**採用後**独立Normative Reviewerが再現可能な引継ぎを作成してください。

`READY_FOR_OWNER_DECISION`は準備文書の状態のみで、`NORMATIVE_BASELINE_VERIFIED`、`IMPLEMENTATION_AUTHORIZED`、`G0_AUTHORIZED`、`STS001_VERIFIED`を意味しません。

I2については、「別途人間が限定承認した完全隔離オフラインの構造検証」と「製品認可・Broker統合」を別々に判定してください。後者はN2審査・正式実装判断までBLOCKEDです。

## 成果物（すべて未署名、ローカル文書のみ）

1. `01_N1_Authority_Chain_Evidence_Register.md` — 原本別Authority・Revision・digest・イベント・未取得
2. `02_N1_Baseline_and_Clause_Diff_Matrix.md` — B1/B2/B3、3条項の旧新全文、R4未採用候補、衝突
3. `03_N1_INT003_Governance_Feasibility_Gaps.md` — 実効管理経路ごとの二者承認証拠、無効化境界
4. `04_N1_Owner_Adoption_Record_UNSIGNED.md` — Historical/Prospectiveの分岐を持つ未署名決裁候補
5. `05_N1_N2_Independent_Review_Handoff.md` — 固定原本、再検証手順、別主体のレビュー条件
6. `06_N1_Readiness_and_Blocker_Report.md` — 次の責任主体・最小Owner行動・禁止事項・Gate状態

各文書を生成したらSHA-256を計算し、`MANIFEST.json`を作成してください。外側ZIPが必要ならCRC/内部SHA256SUMSも検証します。原本は変更・上書きしないでください。

## 厳格な禁止事項

- AWS API、STS、IAM、AWS CLI/SDK、credentials/provider/cache、Bitwarden/Secret Storeへの実アクセス
- Docker、Cloudflare、Deno、本番Broker、環境設定、AWSロールの操作
- GitHubへのコミット・PR・マージ、既存コードの変更
- 未承認要件の正式採用、歴史的承認の遡及捏造、人間署名・権限検証の代行
- INT-003、REQ-045/047、AC-022 pre-fetch境界の黙示的緩和
- N2独立レビューの自称完了、I2製品統合・G0/STS実行権限の発行

## 終了状態

```text
PHASE_N1: AUTHORITY_EVIDENCE_AND_UNSIGNED_DECISION_PREPARED
NORMATIVE_BASELINE: NOT_VERIFIED (unless independently authenticated adoption and subsequent N2 review establish otherwise; N1 never asserts closure)
ODR-IR-002: PENDING / NOT_EFFECTIVE
ODR-IR-003: NOT_VERIFIED
INT-003: CRITICAL_OPEN (until independently proven)
PHASE_N2: NOT_STARTED
PHASE_I2_PRODUCT_INTEGRATION: BLOCKED
BROKER_RUNTIME_INTEGRATION: NOT_AUTHORIZED
G0_EXECUTION_APPROVAL: NOT_AUTHORIZED
AWS_API_BUDGET: 0
Gate STS-001: NOT VERIFIED
```

完了報告では「自分が検証したバイト列」と「正式Custodianの権威・承認を実証した範囲」を必ず分け、残った人間の行為を具体的に示して停止してください。
