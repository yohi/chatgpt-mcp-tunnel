# Investigation B — G0最終候補の独立静的レビュー引き継ぎ

## 1. 依頼と現在状態

レビュー対象は[G0最終承認候補](aws-mcp-sts001-investigation-b-g0-final-decision-record-unsigned.md)と
[10クラスlifecycle候補](aws-mcp-sts001-investigation-b-g0-lifecycle-schedule-unsigned.md)、および本書。
レビューは別担当/別sessionの文書静的レビューのみ。作成AIは独立判定を先取りしない。
本候補の `independent_review_status=PENDING`、`reviewer_verdict=UNASSIGNED`。
既存G0 packetのacceptanceを今回の改訂候補へ転記しない。

```text
DRAFT_UNSIGNED_NOT_AUTHORIZED
PLAN_PREPARED_PENDING_EXECUTION_APPROVAL
G0_NOT_AUTHORIZED
P0_NOT_EXECUTED
G1-G5 / G1b / G5-release NOT_AUTHORIZED
Gate STS-001 NOT VERIFIED
```

AWS API/CLI/SDK/STS、認証情報/config/env/provider/cacheアクセス、Docker、P0、
運用保存先の調査/作成/削除、IAM変更、Broker実装、GitHub書き込みは禁止。
レビューは元資料とplanning成果物のoffline検査に限定する。

## 2. 原本と読み順

1. `OFFLINE_ONLY_REFERENCE` README_FIRST（元参照: `../../STS001_G0_FINAL_OFFLINE_20261015/input/README_FIRST.md`; ZIP: `AWS_MCP_STS001_G0_Final_Unsigned_Record_Handoff_20261015.zip` 内 `README_FIRST.md`; SHA-256: `d4cd8dcd9417e7449701acacf685f42b6669f15d91be6f85af1068c1ef8b64d0`; 取得管理経路: `PENDING` — 人間のData Custodianが許可されたreviewerへの既存経路を確認する。経路・受領権限は未検証）、
   `OFFLINE_ONLY_REFERENCE` 作業契約（元参照: `../../STS001_G0_FINAL_OFFLINE_20261015/input/00_AGENT_PROMPT.md`; ZIP: `AWS_MCP_STS001_G0_Final_Unsigned_Record_Handoff_20261015.zip` 内 `00_AGENT_PROMPT.md`; SHA-256: `a43ee92207633f8e79ec461fd33484aeb56b7739895864248492d02f695c44a6`; 取得管理経路: `PENDING` — 人間のData Custodianが許可されたreviewerへの既存経路を確認する。経路・受領権限は未検証）、
   `OFFLINE_ONLY_REFERENCE` 人間の選択（元参照: `../../STS001_G0_FINAL_OFFLINE_20261015/input/01_HUMAN_SELECTIONS.md`; ZIP: `AWS_MCP_STS001_G0_Final_Unsigned_Record_Handoff_20261015.zip` 内 `01_HUMAN_SELECTIONS.md`; SHA-256: `4b7e754594fbecc557c1240ac00c1d1132a3a71f3bb5ae348a40283bef5a0037`; 取得管理経路: `PENDING` — 人間のData Custodianが許可されたreviewerへの既存経路を確認する。経路・受領権限は未検証）を全文読む。
2. G0最終承認候補section 2のP/D/C/G/H/Rの6原本を全文読む。
   Pの実行境界が支配し、選択記録は本人/権限の証明ではない。
3. 受領ZIPのmember safety、重複/型/展開量、CRC、内部 `SHA256SUMS` と固定原本hashを再検査する。
   ZIP計算hashは `fc0dd28b9872ab8738f6b7790377a880168a7d5ad23643e1d2b1516079ac4cd1`。
   これは独立の発行者認証ではない。抽出参照とZIP内バイト列の一致も確認する。
4. `OFFLINE_ONLY_REFERENCE` 成果物SHA256SUMS（元参照: `aws-mcp-sts001-investigation-b-g0-final-SHA256SUMS`; ローカル原本: `.omo/drafts/aws-mcp-sts001-investigation-b-g0-final-SHA256SUMS`; SHA-256: `16322bcf2d835e02b6ddc90871f52a306a807e93876180c98ec7e5bd7ca06a87`; 原本版用であり現PR版の検証値ではない。ZIP内パス: `PENDING`; 取得管理経路: `PENDING` — 人間のData Custodianが許可されたreviewerへの既存経路を確認する。経路・受領権限は未検証） と
   `OFFLINE_ONLY_REFERENCE` 準備QA記録（元参照: `aws-mcp-sts001-investigation-b-g0-final-qa-receipt.md`; ローカル原本: `.omo/drafts/aws-mcp-sts001-investigation-b-g0-final-qa-receipt.md`; SHA-256: `ce97b60be56d39aef2f5f8dcf5bd9db825c0ff4fe163d287a73b7919cb0ffbed`; 原本作成時点の記録。ZIP内パス: `PENDING`; 取得管理経路: `PENDING` — 人間のData Custodianが許可されたreviewerへの既存経路を確認する。経路・受領権限は未検証）を確認し、納品バイト列を再hashする。

integration HEADの引き継ぎ記録 `2b10b5eab33cde6d4d7869473e5c9bee7583865c` と
固定コード参照 `05f4b92e7ff2de76dc79cf8d5dc9f563a03af209` を混同しない。
旧G/Hの `9b6b1bca6ee089b1e1a10bcfc5139eb7bf1f9843` は過去時点の記録。
今回の準備はGitHub現況を確認していない。将来確認する場合もSHAへ固定し、drift時は停止する。
別原本R1 independent recheckやR0比較は今回の再検証対象に含まれず、過去reviewの引用を再実行の証拠としない。

## 3. 独立レビューの検査表

| 検査 | 期待する境界 | 原本の行参照 |
| --- | --- | --- |
| 原本整合性 | 不足/hash不一致なら `BLOCKED_REFERENCE_INTEGRITY`、別HEADへの置換なし | P L59-105、作業契約section 1-2 |
| OD-01 | 本人担当の選択だけ反映、名前/verified ID/確認手段は未確定 | P L173、L652、L672 |
| OD-02 | 同一人兼務可、G0ローカル権限実証と別の帰属可能な承認行為が必要。削除ownerは候補のまま | P L185-217、L653 |
| OD-08 | 人間供給の独立承認済み最小化候補metadataを選択。未提供の入力ID/hash/境界はblock | P L225-253、L659 |
| OD-09 | symbolic rootは候補のみ。canonical/mount/ACL/owner/暗号化/除外を実証済みとしない | P L455-477、L660 |
| OD-10 coverage | C01-C10が一度ずつ存在し、30/30/7/90/180/30/禁止/禁止/180/180の方針を保持 | G L140-180、人間選択の10行 |
| OD-10 completeness | 各クラスにanchor、用途、三つの絶対UTC、custodian/backup、exact scope、standing deletion権限/event、hold、残存copy、reviewer cutoff | P L538-585、R section 4 |
| 期限と権限 | reviewer沈黙で延長せず、valid holdと `RETENTION_BREACH` を区別。AI監査削除不可、authority/receiptの独立lifecycle | P L564-585 |
| G0 JSON | `UNDECIDED` / `APPROVAL_PENDING` / `signature=""`、exact scope/paths/runtime/digest/event/time/expiryすべて未確定 | P L192-217 |
| G0 budget | AWS要求/実行0、API/Region/endpoint grants空、provider解決・fallback・削除grantなし | P L290、L319 |
| ゲート順序 | pre-G0、別承認P0、pre-G1実モードGO/endpoint/P1 limits、post-P1 G1b、G2-G5/G5-release独立 | P L668-675 |
| mode証明 | A/Bとも実際の選択Modeにfull proof、発行/refresh遮断、物理attempt計数、offline fixtureと実境界同等性。live probeなし | P L412-449 |
| 真正性 | 最終不変版digest/scope/expiryを既存trusted channelのエージェント外の人間承認へ結合。自己hashなし | P L192-217、G L255-258 |
| scope fidelity | Gate/Finding閉鎖、role reuse、Broker実装、配布、862予算採用を推論しない | P L98-128、L315-363 |

## 4. 未解決項目レジスター

以下は人間による補完/後続実証項目であり、文書に未確定と明記されていること自体は文書欠陥ではない。

| ID | 未解決項目・責任主体 | 阻止する時点 | 状態 |
| --- | --- | --- | --- |
| OI-01 | 人間組織/本人: operatorのverified ID、確認方法、連絡経路、ローカルscope/同意 | G0 | `IDENTITY_PENDING` |
| OI-02 | ローカル権限主体: 同一人approver/custodianの権限証拠、候補deletion ownerのscope権限 | G0 | `APPROVER_AUTHORITY_PENDING` |
| OI-03 | 人間供給者/独立承認者: 最小化metadataの正確なID/版/hash/来歴/受領者/境界/event | G0初期境界、P0 discovery | `P0_CONFIG_DISCOVERY_BLOCKED` |
| OI-04 | Data Custodian: canonical root/mount/owner/親経路/ACL/default ACL/暗号化/Git-sync-backup除外の証明 | G0 / 最初のcase write前 | `STORAGE_AUTHORITY_PENDING` |
| OI-05 | Data Owner/監査custodian: 8作成候補クラスの用途・anchor・全絶対UTC・backup・case scope・reviewer cutoff | 最初のcase write前 | `P0_CASE_WRITE_BLOCKED` |
| OI-06 | 権限主体: class別事前standing deletion指示/event、legal hold authority/process、残存copy処理、audit/authority/receipt整合 | 最初のcase write前 | `OWNER_DECISION_PENDING` |
| OI-07 | 人間approver: tool/runtime/config/入力/出力/部分集合、最終版digest/scope/expiry、既存trusted channelでの別承認event | G0有効化前 | `APPROVAL_PENDING` |
| OI-08 | 独立文書reviewer: この候補版の実バイト列を検査し判定 | 人間の最終判断の参考 | `PENDING` |
| OI-09 | credential/execution custodian: 実モードsource/provider/request-path GO、既存source有効性、実境界同等性 | 承認P0中 / G1前 | `SOURCE_REQUEST_PATH_NOT_ATTESTED` |
| OI-10 | AWS execution approver: STS/IAM endpoint/Region/signing Region、P1物理attempt/API/page/resource/rate/cost上限と新G1 | G1 | `PRE_G1_PENDING` |
| OI-11 | 人間baseline主体: 許可P1の実観測principal採用と別G1b | P2-P4前 | `SOURCE_PRINCIPAL_BASELINE_PENDING` |
| OI-12 | 各stage/data owner: G2-G5、OD-14 raw-review/受領者とG5-release、クラス7/8変更時の別lifecycle | 各後続stage/配布 | `NOT_AUTHORIZED` |

既に選んだ方針を再選択させず、選択と証明/正式行為を区別して未解決欄を人間へ提示する。
必要な原本が揃う前にG0を有効としない。未確認の本人性/保存先を静的QAで合格へ変えない。

## 5. negative readingと判定手順

次の解釈が文書から成立しないことを独立に確認する。

- 同一人兼務/チャット選択/PR mergeを帰属可能なG0承認とみなす。
- metadata不足を理由に原configやproviderをAIが開く。
- 日数を会話日から絶対期限へ変換し、期限/権限不備のまま最初のcase QAを書く。
- C07/C08をcandidate移動や新しい別名で作成する。
- 旧reviewのacceptanceを今回の独立判定またはhuman grantへ昇格する。
- synthetic passを本番隔離証明とし、GetCallerIdentityでGO前提をbootstrapする。
- G0からG1/G1b/後続stageへ承認を伝播し、862を承認予算とする。
- reviewer無回答で保持を延長し、holdなしの削除失敗を成功と報告する。
- audit/approval/deletion proofを監査前に消し、unlinkでbackup完全消去を保証する。
- 変更後のfileに旧draft hashへの署名を流用する。

Reviewerは入力/成果物のSHA-256、JSON parse、全10クラス・全欄、source行の内容と範囲、
相対リンク、機密/個人名/実home pathの混入、UTC未確定値、独立ゲートを実際に検査する。
static scanは機密性証明ではなく、最後に人間の機密性確認も必要。
レビュー記録はreviewer/session、対象hash、実行済み/未実行の検査、findingと根拠のfile/行/digestを明記する。
formal findingは `IB-G0-FINAL-DOC-NNN`、severity、引用、矛盾/欠落、影響OD/gate、修正要件、状態を持つ。

判定候補は次の三つ。**本書では選択しない。**

| 判定候補 | 意味 |
| --- | --- |
| `ACCEPTED_FOR_HUMAN_G0_DECISION_CONSIDERATION` | 未署名の判断候補として文書受理可能。人間の未解決判断は残る |
| `REVIEW_REQUIRED` | 重大な欠落/矛盾/曖昧さがあり文書修正を要する |
| `BLOCKED_REFERENCE_INTEGRITY` | 必須原本欠落/hash不一致。停止し代替しない |

`DOCUMENT_ACCEPTANCE`、人間のG0決定、P0実行は三つの別イベントである。
いかなる文書判定も本人性/権限/保存先実証/削除権限/AWS実証を作らない。
今回の準備QAは著者による検査であり独立レビューではない。判定後も自動実行せず、指定の未許可状態で停止する。
