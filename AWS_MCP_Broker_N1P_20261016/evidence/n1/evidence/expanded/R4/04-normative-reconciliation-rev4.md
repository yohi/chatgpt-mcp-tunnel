# AWS MCP Broker v1.1 — Normative Reconciliation Revision 4

**Date:** 2026-10-13 (JST)  
**Status:** `REVISION_CANDIDATE / OWNER_DECISION_PENDING / INDEPENDENT_REVIEW_REQUIRED / FEASIBILITY_NOT_VERIFIED`  
**Trigger:** Independent Revision 3 Review: `REVISION_REQUIRED`.

## 1. Review finding closure map

| Finding | Severity | R4 candidate change | Disposition |
|---|---|---|---|
| RG-BRK-NR-R2-001 | Major | REQ-009 / REQ-046 / AC-022の改訂をOwner専用の判断として明示し、**各条項の原文全文・改訂後全文・逐行差分・本文SHA-256**を`08`に収録 | **OPEN / OWNER_DECISION_PENDING** |
| RG-BRK-NR-R3-001 | Moderate | REQ-046の旧項目6は「Broker専用」を含まないことを確認し、Rev3の誤った位置指定を撤回。末尾のPassword Manager・CLI境界を含む改訂全文を提案 | **NORMATIVE_REPAIR_CANDIDATE / OWNER_PENDING** |
| RG-BRK-NR-R3-002 | Moderate | REQ-055/056に「**正規二者承認が成立しても禁止Secret混入は禁止**」を明記。AC-028/033を拡張し**AC-036**を新設 | **NORMATIVE_REPAIR_CANDIDATE / NOT_PROVEN** |
| RG-BRK-NR-R2-002 | Major | 値のみ差替えの取得前独立強制が成立しなければ**BitwardenへSecret値取得要求を送信しない** | 文書案は維持 / `FEAS-007-C NOT_PROVEN` |
| RG-BRK-NR-R2-003 | Moderate | `S`/`D`/`C`/`R`を区別し、取消確定後に未送信キューを初回送信することを禁止 | 文書案は維持 / `FEAS-Authorization NOT_PROVEN` |
| INT-003 | **Critical** | Bitwarden Owner/Admin、クラウド特権、CI/CD、Secret Store、認可発行者、バックアップ復元の全管理経路を二者承認の実効強制対象 | **OPEN / BLOCKING** |

## 2. B1/B2/B3 fixed baseline and provenance

- `01-fixed-baseline-v1.0.md`: 既存REQ-001〜044 / AC-001〜020（B1）。
- `02-fixed-baseline-v1.1.md`: 既存REQ-045〜049 / AC-021〜024、REQ-048確定期限の追補（B2/B2-S1）。
- `03-fixed-decisions-Q33-Q40.md`: 質問33〜40の決定要約（B3）。

この3文書はR2/R3とバイト同一に維持する。SHA-256は`SHA256SUMS`で固定する。ただし、**過去に正式採用された外部原本との逐字一致は引き続き独立未照合**であり、同梱Digestを真正なOwner承認の証拠としてはならない。

`08-owner-decision-request.md`の全文改訂候補は、B1/B2とは別の未承認文書である。候補をベースラインと表示しない。Ownerが正式に採用した後で、採用版全文と承認日時、決定ID、個別本文Digestを新たに固定し、独立非退行審査を受ける。

## 3. Secretの正規変更と禁止内容検査の独立性

`REQ-045`は無条件の**既存IAM長期アクセスキーの取得禁止**である。組織管理者2名による変更承認やBitwarden API上の権限が正規であっても、この禁止を免除できない。

### 反例

1. 本番許可リストに登録されたSecret ID `X`があり、許可元の外部サービス用Secretとして認識されている。
2. 異なる2人の管理者が、誤認によって、値だけを既存IAMキー相当の内容へ差し替える変更を正規に承認した。
3. Secret ID、Project、参照先、取得前Version/metadata、署名付き変更承認がすべて正常に見える。
4. Adapterが「承認済み」を根拠としてSecret値を取得してしまう。

この場合、秘密をBrokerへ返さなくても**取得禁止に違反**する。したがって、規範上は次を区別する。

- **変更認可:** 誰が、どの変更を二者承認したか。
- **内容安全性:** 変更後の取得対象に既存IAM長期キーが混入しないことを、取得前かつ承認と独立に強制できるか。

内容安全性は、単なる正規表現、二者承認、目的ラベル、保存済みDigest、変更履歴だけでは成立しない。値を取得する前に真の内容由来を確実に制限し、全投入経路を制御し、取得時と証明した値のすり替えを防げない限り、**AdapterがBitwardenの当該Secret値を取得すること自体を禁止**する。成立しない場合は連携`BLOCKED`。Adapter無効だけで「有効モードの安全性がPROVEN」と主張してはならない。

`AC-036`は、未承認だけでなく**正規二者承認された禁止値混入**を検証する。これは禁止値を実際にBitwardenへ保存する実験をこの文書で許可するものではない。

## 4. 取消・送信競合と認可証明（R3の保証を維持）

- `S`: 認可証明の単回消費と送信解放（ネットワーク送信開始ではない）。
- `D`: `C`と順序付け可能な実際のtransport送信開始。
- `C`: 全Adapterが共有する取消確定。
- `R`: 外部受理・結果観測。

`S < C`かつ`D`未開始なら、取消後の初回送信は禁止。停止・キュー・復元を経由しても同様。`D < C`の送信済み操作は残存と記録し再送しない。`D`をDBフラグに書くだけでは実送信開始の安全性は証明されない。

独立認可証明は、Brokerの自己申告だけで発行してはならず、独立本人性、サービス主体、元操作要求の完全性、認可ポリシー、操作契約Version/Digest、期限、取消、単回使用に束縛する。両保証の実効強制は未証明。

## 5. INT-001〜006の区別

| INT | R4文書候補 | 実証 |
|---|---|---|
| INT-001 | Bitwarden連携は機能として必須、初期状態は無効。旧REQ-025原文との正式整合性は独立レビュー対象 | NOT_PROVEN |
| INT-002 | 未検証環境はAWS-only/非完全準拠と区別。REQ-042の緩和はしていない | NOT_PROVEN |
| INT-003 | **Critical OPEN/BLOCKING**。すべての実効特権変更経路で二者承認が強制できるまで未解消 | NOT_PROVEN |
| INT-004 | Tokenの発行・配置・権限変更は特定の1変更に二者承認。包括事前承認禁止 | NOT_PROVEN |
| INT-005 | 独立認可発行・要求完全性・操作契約Digest・C/S/D/R・単回性を維持 | NOT_PROVEN |
| INT-006 | AWS書き込みの1操作承認と、外部連携の全書き込み禁止を区別 | NOT_PROVEN |

## 6. Approval and release boundaries

- **Existing baseline:** B1/B2/B3は既存の参照テキストとして固定（外部原本との照合は未完了）。
- **Owner amendment:** REQ-009/046・AC-022の改訂は`PENDING`。Owner承認記録を捏造しない。
- **Candidate requirements:** REQ-050〜059。候補の本文の修正は`06`。
- **Candidate acceptance:** AC-025〜036。全件`NOT_EXECUTED`、本文は`07`。
- **S0/S1/C:** `NOT_PROVEN`。INT-003: `CRITICAL OPEN / BLOCKING`。
- **Prohibited now:** 本番・非本番AWS/BWS/Cloudflare/Deno/Dockerへの変更、IAMキー取得、Secret読込、試験、設計承認、実装認可、Feasibility実験の開始。

**Next:** Requirements Ownerの明示的な3条項全文改訂判断 → 採用版のDigest付き固定 → 別の独立Normative Review → Feasibility開始の可否を別途決定。技術的な可否や試験許可を先取りしない。
