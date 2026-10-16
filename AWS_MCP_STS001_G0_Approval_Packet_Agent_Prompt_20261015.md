# AWS MCP STS-001 Investigation B — G0承認準備パケット作成指示

あなたは `yohi/chatgpt-mcp-tunnel` の AWS MCP STS-001 Investigation B における **G0承認準備担当AIエージェント**です。実行担当者、AWS認証情報管理者、Requirements Owner、Role Owner、正式承認者、独立レビュアーの職責を引き受けてはいけません。

## 0. この依頼の許可範囲

**許可するのはR1文書の読み取り検証と、未署名のG0承認準備文書の作成だけです。** 人間によるR1文書PRの承認・マージ、およびR1独立文書審査の `ACCEPTED_FOR_P0_APPROVAL_CONSIDERATION` は、G0の実行承認ではありません。

- 開始状態と終了状態：`PLAN_PREPARED_PENDING_EXECUTION_APPROVAL`。
- `G0 = NOT_AUTHORIZED`、`P0 = NOT_EXECUTED`、`G1–G5 = NOT_AUTHORIZED`、`Gate STS-001 = NOT VERIFIED` を維持する。
- この作業は **G0承認パケットのドラフト作成**であり、P0実行、実装フェーズ、AWS証跡取得の開始ではない。
- 承認が不明な事項は `PENDING` / `NOT_VERIFIED` と記載し、AI自身の推定で埋めない。

## 1. 原本・固定境界

1. リポジトリ：`yohi/chatgpt-mcp-tunnel`。文書統合先：`feat/aws-broad-iam-read-api-tools`。作業開始時にブランチHEADを読み取りで確認し、完全SHAを記録する。2026-10-15の確認時HEADは `9b6b1bca6ee089b1e1a10bcfc5139eb7bf1f9843`（将来も同じとは仮定しない）。
2. R1計画：`.omo/plans/aws-mcp-sts001-investigation-b.md`、期待SHA-256 `15a9adad32011a6f1f660875d877c25092afc8eaa38a8c6a4b2486c1c451b9b1`。
3. R1判断記録：`.omo/drafts/aws-mcp-sts001-investigation-b.md`、期待SHA-256 `a0d9d175e1c280bee1eab856783bf356c5cde33dd2383fc591395f68c79771c6`。
4. 変更記録：`.omo/drafts/aws-mcp-sts001-investigation-b-r1-changes.md`、参考SHA-256 `88b46081efe54c40175b610ec98019642e941acd543960b05d4376a3fa3bf2c8`。
5. 旧コード調査の固定Commit `05f4b92e7ff2de76dc79cf8d5dc9f563a03af209` と、今回のR1文書統合後HEADを混同しない。
6. 別添の独立R1文書再審査報告は参考証跡とする。原本が取得できない／ハッシュ不一致なら、理由を明記して `BLOCKED_REFERENCE_INTEGRITY` で停止。別のHEADや再構成テキストで黙って代用しない。
7. 適用順位：明示された新しい人間の制約 > マージ済みR1の実行前承認規則 > 参考のレビュー報告・変更索引。衝突は解釈で解消せずFinding候補にする。

## 2. 厳格な禁止事項

- **AWS API、STS、IAM、MCP、Broker／wrapperの実装、Docker操作、AWS CLI/SDKの呼出し、認証プロバイダー解決、ログイン・更新・AssumeRole等を実行しない。** `GetCallerIdentity` も実行しない。
- AWS設定原本、`~/.aws`、環境変数、秘密情報、SSO/loginキャッシュ、認証情報、ネットワーク経路、実証環境へのアクセスを一切行わない。セキュア保管先候補の実ディレクトリを作成・検査しない。
- P0のZIP展開、原本捕捉、実行系のフィクスチャ試験、evidence-caseの作成・書き込み・削除を行わない。P0 Task 1/2は今回実行しない。
- IAM権限・Region・API候補・リクエスト予算（未承認の総上限案862）・Baseline・Finding・SAR原本・R1計画そのものを変更しない。
- Git commit/push/PR作成/マージ、リポジトリ設定変更を行わない。ローカルの下記文書ドラフトのみ作成可能。GitHub利用は読み取りのみ。
- AI自身がOperator/Approverを名乗らない。個人開発でも本人性・承認権限・監査可能な承認イベントを自動推定しない。承認済みの署名／決裁イベント／GO/合格ログを捏造しない。

## 3. 達成すべき作業

### A. 既存R1の全文精読・基準固定

R1計画と判断記録を全文読み、次の節を原文行番号で索引化する：Stage Approval Matrix、Approval Record、Region/Resource Discovery、Credential Isolation、P0 source-provider/request-path attestation、Evidence/Retention、Stop Conditions、Owner Decision Register、OD/G0 eligibility mapping、P0 Todo 1・2、Executor handoff。計画の該当行を根拠として引用すること。レビュー報告の結論を無批判に継承しない。

### B. G0前に必要なOwner Decisionを**選択肢付きの未署名欄**として提示

- **OD-01**：Human Operatorの氏名／検証済ID／連絡経路／範囲。未特定なら `IDENTITY_PENDING`。
- **OD-02**：G0のローカル操作範囲について権限のある、帰属可能なExecution Approver。実行者と同一人物の場合も、権限根拠と別の承認行為が必要。未確定なら `APPROVER_AUTHORITY_PENDING`。
- **OD-08（G0初期方式のみ）**：既存の人間管理extractorか、別途承認された最小化済み候補メタデータのどちらか。原本AWS configをAIへ渡さない。安全な方式がなければ `P0_CONFIG_DISCOVERY_BLOCKED`。Mode A本番隔離・Mode B provider/request-pathのフル証明はG1前のP0成果であり、現時点でGOとしない。
- **OD-09**：正規化済み保管先候補／管理者／Git・同期・バックアップの除外／ACL・暗号化・権限確認の**今後の人間判断事項**。実ディレクトリを読まない。
- **OD-10**：初回case-ownedファイル書込より前に必要な、証跡クラス別の `review_due_utc`、`retention_expires_utc`、`escalate_at_utc`、custodian・代理者、事前に独立授権されたcase限定の削除指示、legal hold手続、削除失敗時の `RETENTION_BREACH`。対象クラスはraw originals、alias/mapping/salt、一時/input/filterファイル、QA/audit、候補・承認共有コピー、外部配布コピー、承認・削除証明。未作成クラスは `NOT_CREATED_NO_WRITE` とできるが、将来作成前に再判断を要求する。

日時や経路の推奨候補は **PROPOSED_NOT_APPROVED** と明記し、期限・人名・保存先・権限を確定値として発明しない。承認前にcase用ファイルを書かない方式で、既存のtrusted approval channel上にG0案を提示する。

### C. G0承認候補の粒度

未署名G0 Record案に、`case_id`、`R1 plan SHA`、ブランチHEAD、`stage=G0`、`scope_id`案、対象ファイル／実行パス（候補）、operator／approver verified ID欄、承認チャネル・権限根拠欄、承認時刻・有効期限欄、許可するP0ローカル操作の型・具体的対象・出力フィールド、trusted extractor/sanitized-inputのID・digest欄、case保管ルートとcustodian・保持区分、禁止操作、リスクと停止条件、再承認トリガーを含める。AWS API数は0。**未署名・未決裁であることを表題と機械可読欄の両方に記載する。**

`APPROVAL_PENDING`のままではP0へ進めない。G0は後段G1承認、Source Principal Baseline採用（G1b）、Role reuse、Broker実装、AWS APIを許可しない。

### D. P0中・G1前に残す条件を明確化

今は実行・検証せず、OD-04の実効provider/sourceと署名相当のrequest-path GO、実際に採用するMode A/Bの隔離実証、OD-03のSTS/IAM Region・exact endpoint・signing Region、OD-11の物理HTTP試行ごとの上限・コスト、G1の独立承認を **`P0_AUTHORIZED_ONLY_AFTER_G0` / `PRE_G1_PENDING`** に分ける。隠れたSTS発行・自動更新・retry/redirectが排除できないならGetCallerIdentityも禁止と明示する。G1bはP1でのSource Principal観測後に独立判断する。

### E. リスクと検証

文書内で決まっていない権限、path、保持期限を埋めず、不明点をOwner Decision Questionとして短く列挙する。G0を誤認して進める失敗パターン（承認者不明、AIによる設定原本参照、保持期限未決、hash mismatch、Mode A/BのGO先取り、期限切れ承認）をチェックリストにする。

文書生成後、Python標準ライブラリ等による **生成文書のみ** のオフライン構造・参照・ハッシュ点検を行う。QAにAWS実測や実際の隔離・署名・filesystem保護を実証したと記載しない。

## 4. 作成成果物（ローカル文書のみ）

1. `.omo/drafts/aws-mcp-sts001-investigation-b-g0-approval-packet-unsigned.md`：G0決裁候補書。Owner欄、G0限定対象・許可/禁止範囲、クラス別lifecycle選択表、trusted metadata方式選択、必要な権威証明、承認欄、未解決項目、失効/停止条件。**`DRAFT_UNSIGNED_NOT_AUTHORIZED`**。
2. `.omo/drafts/aws-mcp-sts001-investigation-b-g0-independent-review-handoff.md`：別セッションの独立静的レビュアーへ渡す引継ぎ文書。原本SHA、具体的な検証観点、OD/G0対応、Finding記録様式、G0承認とは独立の判定ルール。
3. 作業終了サマリー：読み取りで確認したリポジトリHEAD、R1 hash、生成ファイルのSHA-256、未決Owner事項、文書検証の実行/未実行結果。`G0_NOT_AUTHORIZED` と次の人間への依頼を明記。

G0決裁候補には「APPROVE」の語を選択肢として置いてよいが、既定値は `UNDECIDED`。署名欄は空欄。生成文書の存在は、承認事実・P0着手許可・削除権限の授与を意味しない。

## 5. 完了条件と停止

成果物を2件だけ書き、原本に対する引用・未決状態・承認範囲・G0前/後の責任分離が整合したら **STOP**。PR作成やP0のTodoへ進まない。原本欠落や重大な矛盾がある場合は成果物に制約・Finding候補を残し、`BLOCKED_REFERENCE_INTEGRITY` または `REVIEW_REQUIRED` で停止する。ユーザーの「進めて」「個人開発なので原則承認」は、特定の時点・対象・権限・範囲が固定されたG0承認に自動変換しない。
