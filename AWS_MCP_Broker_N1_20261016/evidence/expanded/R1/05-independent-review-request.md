# Fresh Independent Normative Review — limited correction request

あなたはAWS MCP Broker v1.1の新規・独立したNormative Reviewerです。資料の読み取り専用で審査してください。先行Reviewerの結論を正解とみなさず、ファイルから再計算してください。

## 対象

- `01-owner-decision-record-option-a-limited-correction-r1.md`
- `02-independent-static-review-20261014.md`
- `03-limited-diff.patch`
- B1/B2/B3・`08-owner-decision-request.md`・3件の`adopted-text-*.txt`
- `04-owner-ratification-evidence-checklist.md`
- `SHA256SUMS`

## 実施事項

1. ZIP CRC、Manifest、元Decision Recordに対する変更範囲、原文と改訂候補のDigestを独立確認する。
2. `ODR-IR-001`に対し、「高リスク・権限拡大は二者承認」と「Q40/REQ-057の緊急停止・縮小・取消は認可された管理者1名」を同時に保持するか審査する。
3. `REQ-009`、`REQ-046`、`AC-022`の採用候補本文が**一文字も変更されていない**ことを確認する。
4. Owner ratification (`ODR-IR-002`)、外部権威baseline (`ODR-IR-003`)、INT-003、Gate S0/S1/Cは別途証拠がない限り未成立として保持する。
5. 静的文書修正の受容可否と、正式な規範採用可否を別々に判定する。

## 禁止事項

Owner採用・設計・実AWS/Bitwarden実験・実装・秘密情報取得・クラウド設定変更・Gate通過の宣言。
