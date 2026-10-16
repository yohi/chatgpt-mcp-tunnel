# AWS MCP Broker v1.1 — Normative Reconciliation Revision 4

**Date:** 2026-10-13 (JST)  
**Status:** `REVISION_CANDIDATE / OWNER_DECISION_PENDING / FRESH_INDEPENDENT_REVIEW_REQUIRED / FEASIBILITY_NOT_VERIFIED`  
**Trigger:** Independent Revision 3 normative verdict `REVISION_REQUIRED`.

## Document manifest

| File | Contents | Authority |
|---|---|---|
| `00-README.md` | 本README、文書状態・制約 | PACKAGE SUMMARY |
| `01-fixed-baseline-v1.0.md` | B1: REQ-001〜044 / AC-001〜020 | FROZEN REFERENCE, provenance not independently proven |
| `02-fixed-baseline-v1.1.md` | B2: REQ-045〜049 / AC-021〜024 / B2-S1 session expiry | FROZEN REFERENCE, provenance not independently proven |
| `03-fixed-decisions-Q33-Q40.md` | B3: 確定質問33〜40要約 | FROZEN REFERENCE |
| `04-normative-reconciliation-rev4.md` | R3 Findings処置、INT-001〜006、保証境界 | CANDIDATE |
| `05-nonregression-matrix-rev4.md` | 既存REQ49/AC24の73件、重点競合と追加AC-036の追跡 | CANDIDATE |
| `06-security-requirements-rev4.md` | REQ-050〜059（取得前隔離、正規承認毒入れ、取消モデル） | CANDIDATE |
| `07-acceptance-rev4.md` | AC-025〜036（AC-036追加） | CANDIDATE, NOT_EXECUTED |
| `08-owner-decision-request.md` | REQ-009/046/AC-022の原文・改訂後**全文**・差分・本文SHA-256 | **OWNER APPROVAL REQUIRED** |
| `09-fresh-independent-review-request.md` | 新規独立Normative Reviewer用指示 | REVIEW REQUEST |
| `10-feasibility-handoff-rev4.md` | 今後の独立Feasibility検査項目・制限 | NOT_AUTHORIZED |
| `11-r2-review-findings.md` | 独立R2レビューの作者要約 | REFERENCE DIGEST |
| `12-r3-review-findings.md` | 独立R3レビューの作者要約 | REFERENCE DIGEST |
| `13-owner-decision-record-template.md` | **未記入**のOwner決裁記録テンプレート | NOT AN APPROVAL |
| `SHA256SUMS` | 上記14文書のファイルハッシュ | ZIP INTEGRITY ONLY |

## R4's three priorities

1. **RG-BRK-NR-R2-001 / RG-BRK-NR-R3-001:** B1/B2原文を変更せず、REQ-009/046・AC-022の**全条項改訂後全文**を`08`で提示。Rev3のREQ-046「第6項にBroker専用」の誤特定を訂正。Ownerによる正式採用・決定日時・確定条項Digestは**未取得**。過去の原文との独立逐字比較も未完了。
2. **RG-BRK-NR-R3-002:** **2名が正当に承認しても禁止されたIAMキーのSecret混入は拒否**。REQ-055/056とAC-028/033を強化し、AC-036を追加。取得後Digest/正規表現/承認の有無を取得前隔離保証の代用にしない。安全な取得前検証不能ならBitwarden Secret値の読み取りを禁止し、連携BLOCKED。
3. **Critical INT-003:** Bitwarden Org Owner/Admin、クラウド基盤、CI/CD、Secret Store、独立認可発行者、復元の迂回経路を実際に二者承認で強制できるかは**未実証**。引き続き`OPEN / BLOCKING`。

## Strict non-claims

- REQ-009/046・AC-022の改訂案を正式採用済みと宣言しない。
- B1/B2/B3が別途存在するOwner署名済み原本と一致すると断言しない。
- 本ZIPに実AWS/Bitwarden/Cloudflare/Deno/Docker実験・Secret読み取り・動的試験結果は含まない。
- Bitwarden無効でのAWS-only動作を、Bitwarden有効のfull-v1.1準拠と表示しない。
- AC-025〜036の実行・合格、Gate S0/S1/C、FEAS-001/007/011をPROVENとしない。
- 独立Normative ReviewがあってもFeasibility実験、Design、Implementation、本番への権限を付与しない。

**Next:** Requirements OwnerのREQ-009/046・AC-022全文改訂についての判断を取得し、正式に採用された原文・Decision Record・Digestを固定。その後、別の独立Normative Reviewを実施する。Owner承認がないまま提出するレビューは候補の静的評価に限り、`NORMATIVE_PASS`にはできない。
