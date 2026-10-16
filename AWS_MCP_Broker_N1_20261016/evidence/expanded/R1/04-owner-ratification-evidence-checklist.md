# Owner ratification — evidence checklist (NOT SIGNED / NOT EFFECTIVE)

**Working record ID:** `DRAFT-AWS-MCP-BROKER-V1.1-OWNER-OPTION-A-20261013`

このチェックリストは本人確認・正式決裁の代わりではありません。正式なOwner権限を持つ人間が、独立して監査可能な手段で原本を確定してください。2026-10-13の会話での意思表明を事後的に正式な承認日時として扱ってはいけません。

- [ ] 正式Decision IDを確定し、Decision Recordと紐付ける
- [ ] Owner本人性とRequirements Owner権限の検証可能な根拠を記録する
- [ ] 実際の承認日時（UTC/JST、時刻の証拠）を記録する
- [ ] 権威あるB1/B2原本の取得元、版、保有者、バイトSHA-256、承認由来を確定する
- [ ] B3のQ33〜Q40原決定と同梱要約の同一性／差分を照合する
- [ ] REQ-009・REQ-046・AC-022の採用候補全文と各本文SHA-256を個別に明示して承認する
- [ ] 承認証跡の改変耐性、署名者と承認対象Digestの結合、監査記録を確認する
- [ ] 承認された条項のみを採用baselineとして固定し、新しいDigestを記録する
- [ ] 別主体によるpost-ratification Normative Reviewを実施する

## 採用候補本文Digest（未承認）

| 条項 | SHA-256 |
|---|---|
| REQ-009 | `f17db0565942501a39c3302912dcb161e2f3e38e168f29a51491a711e0851bb9` |
| REQ-046 | `6362d06bfe5d1c1184057f84c42f2f6ed4c19d6dc47b8662cfe039105e21d931` |
| AC-022 | `3a02643899b8d79683f6c13300e0ee655b4b00fe20d23f87a3c35efb4e521a39` |

## 継続中のブロッカー

`OWNER_ATTESTATION_PENDING / NOT_EFFECTIVE`、`INT-003 CRITICAL OPEN / BLOCKING`、`Gate S0/S1/C NOT_PROVEN`。この文書はAWS・Bitwarden操作、Feasibility実験、設計、実装、本番運用を許可しません。
