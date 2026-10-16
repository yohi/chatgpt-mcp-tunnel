# AWS MCP Broker v1.1 — Phase N1-P
## Prospective Baseline Composition & Human Owner Adoption Preparation

作業区分：**新たな前向き採用（Case P）のための未署名決裁資料準備**。正式採用・署名・Owner本人性認証・AWS実行は含まない。

### 0. あなたの役割と作業目的

あなたは `yohi/chatgpt-mcp-tunnel` の新しい **Requirements / Architecture / Security Baseline Composition Investigator** です。N0/N1の記録、旧R4/Option A R1案、既存GitHubの事実を独立に照合してください。AIが正式Owner、Design/Security Approver、Custodian、INT-003の第2の人間承認者を兼ねることは禁止します。

目的は、N1で作成された未署名決裁パケットを**矛盾・曖昧な適用範囲・原本不足を明示した、人間が実際に決裁可能な新規Baseline候補**へ整理することです。N1の候補を無条件に正式採用してはなりません。

**Option A（REQ-009／REQ-046／AC-022）の採用意思は既に表明済みです。方針の再選択を要求しないでください。** ただし、その厳密な本文・SHA-256・法的/組織的な権限・実際の承認イベント・効力時点を新規に確定する必要があります。

### 1. 固定GitHub Baseline

- Repository: `yohi/chatgpt-mcp-tunnel`
- Branch (観測対象): `feat/aws-broad-iam-read-api-tools`
- Fixed commit: `ac462699e0b1988eda63ea3d6dacfc2a030bb822`
- PR #14/#15はマージ済み。I1-TEST-001とI1-API-002は別主体の限定再審査でCLOSEDとの報告がある。

Branchが進んでいても固定commitを勝手に更新しないこと。ドリフトを記録し、必要なら差分影響を隔離して報告すること。GitHubは読み取り専用。

### 2. 入力と検証順序

添付の `AWS_MCP_Broker_N1P_Handoff_20261016.zip` を受領する。必ず次の順に行う。

1. 外側のSHA-256、ZIP CRC、安全な相対パス・重複・リンク・暗号化・展開サイズの上限を検査する。
2. `00_READ_FIRST.md` と本 `01_N1P_AGENT_WORK_CONTRACT.md` を**全文**読む。
3. `MANIFEST.json` のサイズとSHA-256、および `SHA256SUMS` を独立再計算する。
4. `sources/01_N1_Deliverables_20261016.zip` を独立再検証する。期待SHA-256は `b26add50668cf2bdc7929513a7a8c1e3a2325b7c6d8e45e0ab9dd35ca67e0ef6`。外側CRC・内部MANIFEST・SHA256SUMSを再確認する。
5. N1の6文書、B1/B2/B3、R4、Option A R1、Owner意思表明、STS-001 Security Contract Draftを指定の入れ子アーカイブから取得し、必要な本文を全文精読する。R4・R1等の提出コピーは権威原本ではない。
6. 過去のReview Conclusion、主張されたハッシュ一致、N1のN2移行条件を検証し、独立確認できない権威/承認事実は `NOT_VERIFIED` とする。

**今回のZIPは信頼済みCustodianの証明書ではありません。** ZIP/JSONの自己記述や GitHub PRマージを正式採用イベントに昇格させないこと。

### 3. 固定候補本文（ハッシュを独立再計算）

B1/B2/B3の提出コピー全体：

- B1 `01-fixed-baseline-v1.0.md` : `39002fc2ce5f21e9e686a427c793a7fd42fc84e5bdb02684be9e1e3a4305f4bc`
- B2 `02-fixed-baseline-v1.1.md` : `3078acc5c31b5e900697dbb585e5ed604dfca89fe82b56cfc9528ac3c91350e2`
- B3 `03-fixed-decisions-Q33-Q40.md` : `f287966ac61f467704f99c545f2d7a9756b9f21a70a5f90a814367ab7a113aa4`

Option A R1全文置換の**本文**（ファイル全体のSHA-256とは混同しない）：

- REQ-009：1241 UTF-8 bytes, `f17db0565942501a39c3302912dcb161e2f3e38e168f29a51491a711e0851bb9`
- REQ-046：2939 UTF-8 bytes, `6362d06bfe5d1c1184057f84c42f2f6ed4c19d6dc47b8662cfe039105e21d931`
- AC-022：1213 UTF-8 bytes, `3a02643899b8d79683f6c13300e0ee655b4b00fe20d23f87a3c35efb4e521a39`

新本文の実体はN1内 `evidence/expanded/R1/adopted-text-{REQ-009,REQ-046,AC-022}.txt`。`adopted-text`という名前を承認証拠とみなさない。バイト列・改行・Unicode正規化の影響を明示し、本文を黙って校正しない。本文変更が必要な場合は**別Revisionの変更候補**としOption A R1を破壊しない。

### 4. 作業 Task A：Case P採用範囲の明確化

- N1 `04_N1_Owner_Adoption_Record_UNSIGNED.md` §4のCase Pをベースに、**Case Pは採用提案であって、ユーザーが今回承認した事実ではない**と明記する。
- 新しい**候補**Revision識別子を提案してよいが、その採用状態は `PROPOSED / UNSIGNED / NOT_EFFECTIVE`。承認時刻、正式署名ID、実際の効力時刻を創作しない。
- B1/B2の維持部分、B2-S1、B3のQ33〜Q40の正確な適用を**成分単位**で明記する。B3は原発言ではなく要約の提出コピーである。過去の承認復元を主張せず、新規現行テキストとしての扱いはOwner未決定とする。
- Option Aの3条項の置換対象は**全本文**であり、適用時点は将来の承認イベント以降とする。旧本文・証拠を削除しない。
- もし全部を一回で決裁できないなら、独立した**部分採用イベント候補**に分け、そのイベントが全体Baseline・N2開始を認可しないことを明記する。
- 最終のCanonical Source URI、Custodian、Owner権限の証拠参照、UTC時刻、Composition Digestおよび署名欄は未確認の場合空欄/`PENDING`にする。

### 5. Task B：優先関係・衝突を「推奨案」と「人間の決定」に分離

以下を**個別のDecision Item**として扱う。推奨が可能でも、それを採用済み規範として本文に上書きしない。

1. **REQ-025 / INT-001**：提出B1にはSecrets Managerがストレージとして読める記述、B3/R4には外部サービス連携でAWSとは独立・当初無効とする整理がある。競合範囲、提案できる選択肢、本文改訂が必要な箇所、依存REQ/ACを完全に照合する。
2. **REQ-042 / INT-002**：Deno／Cloudflare／Dockerの同等性、Docker Linux/macOS、Adapter無効時／有効時を混同しない。部分機能を全環境同等と呼ばない。
3. **B3 Q33〜Q40**：全8項目を個別照合し、曖昧な「B3が上書き」を禁止。正式採用する対象は受領した要約の正確なバイト列か、別に起案され審査される明示的Revisionのどちらかとする。
4. **INT-003**：2つのアカウント・同一人のロール兼務・2署名では独立した二者承認にならない。一人による**停止・取消・縮小**と、拡張・解除・再有効化を明確に区別し、実際の全管理権限経路を跨ぐ二者強制の可能性は `CRITICAL_OPEN` のままとする。
5. **FEAS-007-C / 取得前内容保証**：承認済みであってもSecretの値差替え・復元・Version alias変更によって既存IAM長期キーを取得する可能性が残る。取得した後の検査では禁止値の不取得を証明できない。未実証ならAdapter/Token/取得経路は無効。
6. **STS-001 Draft**：旧Broker特権境界/認証情報設計と新v1.1境界の不整合を列挙し、Draftを正式なSecurity Contractとして昇格させない。

### 6. Task C：R4追加22条項の個別処遇マトリクス

- REQ-050〜REQ-059（10件）、AC-025〜AC-036（12件）を**省略せず1行ずつ**列挙する。
- 列：ID、原本パス、条項SHA/原文の取得方法、適用対象、既存条項依存、相互依存、リスク、候補Disposition（ADOPT / DEFER / REJECT / REVISEから人間に提示可能）、人間の決定（初期値PENDING）、効果・未解決事項。
- **全22条項は未採用**。過去資料に実装必要性があるだけで採用済みとしない。初期値を `REJECTED` にもしない。
- 他の49 REQ / 24 ACおよびB2-S1を、適用漏れ・黙示改訂のない形式で参照する。
- 条項の一部採用に必要な依存閉包と、採用せず無効のまま保持できる機能を区別する。

### 7. Task D：正式Design／統合AC／Security Contractの完成条件

- 既存の正式版が外部の権威管理経路から見つかった場合のみ、認証済みRevision・Digest・承認証跡を示す。
- 見つからない場合、**執筆・修正が必要な具体的節、責務、承認者とAccept Criteriaの範囲**を列挙する。提案ドラフトを起案してもよいが、既存規範原本の復元や採用済みDesignとは表示しない。
- 実装対象として、AWS読み取り、操作ごとの書き込み承認、独立Authorizer/Issuer、STS Explicit-Denyとresource-policy/role-policy drift、認証情報隔離、Bitwarden Secret Adapter、3実行環境、取消・replay・state/audit・障害復旧の各責務を**正式仕様が足りる／不足／矛盾／実装実証なし**に仕分ける。
- `INT-003: CRITICAL_OPEN` とFEAS-007-Cがある状態で、Adapterを利用する機能や高リスクの権限拡張を有効化する設計を承認可能として扱わない。

### 8. Task E：人間による正式採用の実務と監査境界

AIが署名・正式承認を代行しない。人間が信頼する**私的な本人認証済みの経路**において、以下を人間が確定するまで決裁記録は `UNSIGNED / NOT_EFFECTIVE` とする。

- Requirements Owner、原本管理者、Design/Security承認者の実際の権限・本人性と必要な独立性。個人開発で役割兼務が可能でも、INT-003が要求する独立した2名の実効強制は別問題。
- 正式の保管システム、原本URI、Immutable Revision、全構成成分Digest、各条項の採否・上書き/優先関係。
- 本人の**実際の**採用操作と署名・承認イベントID、UTC日時、発効時刻（承認前に効力が発生したとしない）、対象範囲、将来の取消・失効・後続変更条件。
- 権限と採用イベントを、GitHubへの署名なしコミット、文書ファイルの署名欄記入、チャット上の承認文字列、AI生成時刻だけで証明したことにしない。
- 公開GitHubやチャットへ機密の本人確認ファイル、秘密鍵、AWSキー、Bitwarden Token、非承認私的証跡を転送しない。非機密の参照ID・検証Receiptのみを人間許可範囲で記録する。

**まだ承認操作が行われていない場合、N1-Pの作業者は未署名パケット完成で停止。** 人間が後から正式決裁しても、その時点で新しいDigestと実際のイベント証拠で別途検証する。

### 9. 必須成果物（オフライン、未署名）

次の8文書およびMANIFEST/SHA256SUMSを作成し、ZIP化して検証する。

1. `01_N1P_Candidate_Composition_Manifest_UNSIGNED.md` — 成分、Revision候補、全Digest、効力未発生と優先関係。
2. `02_N1P_Priority_and_Conflict_Decision_Worksheet.md` — REQ-025/INT-001、REQ-042/INT-002、B3、INT-003、取得前内容保証の競合とOwner未決事項。
3. `03_N1P_R4_22_Clause_Disposition_Matrix.md` — 10 REQ + 12 ACを個別に扱う。
4. `04_N1P_Design_AC_Security_Completion_Gaps.md` — 原本が無い領域と正式Design/AC/Security完成条件。
5. `05_N1P_Governance_Custody_and_Approval_Evidence_Checklist.md` — 人間Owner/Custodian/Design/Security権威・保管・署名実務の準備。
6. `06_N1P_Prospective_Owner_Decision_Record_UNSIGNED.md` — 完全な候補本文への参照、未決裁欄、実際の承認イベントの空欄。Option Aは再選択させない。
7. `07_N1P_N2_Entry_and_Partial_Adoption_Gate_Matrix.md` — 部分採用可能性と完全BaselineのN2開始条件、INT-003等の継続Gate。
8. `08_N1P_Readiness_Findings_and_Next_Actors.md` — Owner残作業、未確定事項、次担当、処理済み/未処理を明示。

各文書には `UNSIGNED / PROPOSED / NOT_EFFECTIVE` を冒頭で明示する。成果物ごとにSHA-256を固定する。元資料は改変・上書きせず、証拠元ZIPと生本文の出典・ハッシュを再現可能にする。

### 10. 作業禁止・停止条件

禁止：AWS API、STS、IAM、実認証情報、AWS設定/provider/cache、Bitwarden/Secret Store取得、Docker/本番Broker実行、実クラウド操作、GitHub書き込み/PR/マージ、署名捏造、本人性や組織権限の自己承認、R4追加22条項の自動採用、正式Gate Closure、N2の先行実行。

正式元資料を取得できない・私的経路にアクセスできない場合は `NOT_RECOVERED` を記載し、それだけの理由で作業を止めず、未署名候補と人間の最小残作業を完成させる。出所不明な内容を正式原本として補完しない。

最終状態：

```text
PHASE_N1P: PREPARED_UNSIGNED_ONLY
CASE_P: PROPOSED_NOT_YET_SELECTED_BY_OWNER
NORMATIVE_BASELINE: NOT_VERIFIED
OPTION_A_3_CLAUSES: INTENT_PRESERVED / NOT_EFFECTIVE
R4_22_CANDIDATES: UNADOPTED
INT-003: CRITICAL_OPEN
FEAS-007-C: NOT_PROVEN
PHASE_N2: NOT_STARTED
PHASE_I2_PRODUCT_INTEGRATION: BLOCKED
BROKER_RUNTIME_INTEGRATION: NOT_AUTHORIZED
G0_EXECUTION_APPROVAL: NOT_AUTHORIZED
AWS_API_BUDGET: 0
Gate STS-001: NOT VERIFIED
```

**Owner本人による私的経路での正式採用を伴わずに、AIは`FORMALLY_APPROVED`または`N2_READY`と表示してはいけません。**
