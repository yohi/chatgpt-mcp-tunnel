# AWS MCP Broker v1.1 — Fresh Independent Normative Review R4

あなたはR4改訂作成者、Requirements Owner、過去レビュアー、Feasibility/実装担当とは独立した**Normative Review Gate**担当である。**読み取り専用**に限定し、AWS/Bitwarden/Cloudflare/Deno/Docker操作、Secret取得、実験、承認、設計・コード変更、Push、本番運用をしてはならない。

## 審査入力と固定資料

- Review ZIP: `aws-mcp-broker-v1.1-normative-reconciliation-rev4.zip`。ZIP CRC / 各SHA256SUMS検証。
- B1 `01-fixed-baseline-v1.0.md`: REQ-001〜044, AC-001〜020。
- B2 `02-fixed-baseline-v1.1.md`: REQ-045〜049, AC-021〜024, REQ-048の8時間/15分追補。
- B3 `03-fixed-decisions-Q33-Q40.md`: 8件のユーザー決定。
- `04-normative-reconciliation-rev4.md`: R3 Findingsの処置案。
- `05-nonregression-matrix-rev4.md`: 73条項非退行対応。
- `06-security-requirements-rev4.md`: REQ-050〜059候補。
- `07-acceptance-rev4.md`: AC-025〜036候補。
- `08-owner-decision-request.md`: **REQ-009/046/AC-022の全文原文・全文改訂候補・逐行差分・本文Digest**。現時点では正式な改訂ではない。
- `10-feasibility-handoff-rev4.md`: 実証条件・制限。
- `11-r2-review-findings.md` / `12-r3-review-findings.md`: 過去Finding要約（作者記録であり署名付きReview Reportではない）。
- `13-owner-decision-record-template.md`: Ownerが別途決定するための未記入テンプレート。**承認証拠ではない。**

## 最優先審査

1. **R2-001 / R3-001 (OWNER_PENDING):** B1/B2原文と`08`の原文抜粋が逐字一致するか。特にREQ-046の冒頭、6箇条、Password Manager段落、Bitwarden CLI段落を**すべて**確認。Rev3で誤った「項目6のBroker専用」位置指定が解消したか。改訂後全文に主体混同・意図しない権限緩和がないか。**Owner採用記録が存在しなければ正式統合PASSとしない。**
2. **R3-002 (APPROVED POISON):** 異なる2名が正式承認していても既存IAM長期キー相当のSecret値が許可済みSecretへ混入し得る。REQ-045/055/056とAC-028/033/**036**が、実際のBWSからの値取得前の拒否を要求しているか。変更承認、用途ラベル、Secret署名、値取得後のDigestで取得前保証と誤認しないか。取得前保証が技術的に不成立なら連携BLOCKEDと規定しているか。
3. **R2-002 (VALUE-ONLY POISON):** Secret ID/Project/見かけのVersion/取得前metadata/Operation Contract Digestが同じで、値だけ違う反例を評価。独立した変更阻止・取得時内容固定を証明できなければSecret取得APIを呼ばない契約か。
4. **R2-003 (C/S/D/R):** S→停止→C→復旧の未送信操作の初回送信を禁止しているか。Dが実transport送信境界とCを直列化できる根拠が文書中で必要とされているか。文書上の要件と技術的なPROVENを混同しないか。
5. **B1/B2真性:** ZIP内の固定原文と過去の会話上の原文・権威ある原本を独立に比較し、照合できないときは限界を明記。内部ハッシュを外部原本の真正性の証拠にしてはいけない。
6. **回帰・網羅性:** 既存REQ49/AC24、REQ-050〜059の10件、AC-025〜036の12件の採番・参照・試験粒度。INT-001〜006、Q33〜40、独立認可発行/Operation Contract Digest、肯定的E2E、Token変更単位2名承認、初期許可リスト空、3実行環境+Docker Linux/macOS別試験、N/Aの規範根拠。
7. **INT-003:** BWS Owner/Admin、CI/CD、クラウド基盤特権、Secret Store、認可基盤、復元経路を含む二者承認迂回が未実証である。**CRITICAL OPEN/BLOCKING**を維持するか確認。

## Verdict と出力

`NORMATIVE_PASS / REVISION_REQUIRED / BASELINE_INCOMPLETE / BASELINE_MISMATCH`から判定し、Severity・具体的反例・条項・修正条件を提示。**REQ-009/046/AC-022の正式改訂にOwner承認が必要で未取得なら`NORMATIVE_PASS`を出してはならない。** Rev4候補そのものの文書改善と、要件採用の手続き不足を分けて報告する。

Gate S0/S1/Cは`NOT_PROVEN`、INT-003は`CRITICAL OPEN/BLOCKING`。文書審査によってFeasibility、実AWS/Bitwarden実験、設計、実装、本番の許可が生じることはない。
