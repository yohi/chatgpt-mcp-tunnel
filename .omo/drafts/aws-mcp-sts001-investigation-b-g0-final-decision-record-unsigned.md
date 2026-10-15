# Investigation B — G0最終承認レコード（未署名候補）

## 1. 状態と対象

`DRAFT_UNSIGNED_NOT_AUTHORIZED`。文書版 `G0-FINAL-CANDIDATE-1`。
対象は `AWS-MCP-STS001-SEC04-RESOURCE`、Investigation B、G0のローカル準備範囲。
本書は人間の判断用の最終候補であり、確定済み承認レコードではない。
作成AIはHuman Operator、Approver、Custodian、独立レビュー担当者を代行しない。
未確定値はG0充足として数えない。今回の文書作成はP0実行でも運用ケースへの書き込みでもない。

[保持・削除スケジュール](aws-mcp-sts001-investigation-b-g0-lifecycle-schedule-unsigned.md)と
[独立静的レビュー引き継ぎ](aws-mcp-sts001-investigation-b-g0-finalization-review-handoff.md)を併読する。

```text
PLAN_PREPARED_PENDING_EXECUTION_APPROVAL
G0_NOT_AUTHORIZED
P0_NOT_EXECUTED
G1-G5 / G1b / G5-release NOT_AUTHORIZED
Gate STS-001 NOT VERIFIED
```

## 2. 不変参照と証明の限界

受領ZIPは `AWS_MCP_STS001_G0_Final_Unsigned_Record_Handoff_20261015.zip`。
計算SHA-256は `fc0dd28b9872ab8738f6b7790377a880168a7d5ad23643e1d2b1516079ac4cd1`。
内部CRC・ハッシュ一致は整合性を示すが、外部の信頼済み発行者署名や期待ZIPハッシュは未提供。
原本は受領ZIPのバイト列から検証した。GitHub原本の新規取得・ブランチ現況確認は行っていない。

Repository `yohi/chatgpt-mcp-tunnel`、integration branch `feat/aws-broad-iam-read-api-tools`。
引き継ぎ時の記録HEADは `2b10b5eab33cde6d4d7869473e5c9bee7583865c`。
履歴上の固定コード参照は `05f4b92e7ff2de76dc79cf8d5dc9f563a03af209`。両者を置換しない。
旧G0文書のHEAD `9b6b1bca6ee089b1e1a10bcfc5139eb7bf1f9843` は過去の準備時点の記録である。
後日ブランチ確認を行う場合、指定HEADからの移動を検出したら停止し、別HEADで補完しない。

| ID | 受領原本へのリンク | SHA-256 |
| --- | --- | --- |
| P | [R1 plan](../plans/aws-mcp-sts001-investigation-b.md) | `15a9adad32011a6f1f660875d877c25092afc8eaa38a8c6a4b2486c1c451b9b1` |
| D | [R1 decision](aws-mcp-sts001-investigation-b.md) | `a0d9d175e1c280bee1eab856783bf356c5cde33dd2383fc591395f68c79771c6` |
| C | [R1 changes](aws-mcp-sts001-investigation-b-r1-changes.md) | `88b46081efe54c40175b610ec98019642e941acd543960b05d4376a3fa3bf2c8` |
| G | [G0 packet](aws-mcp-sts001-investigation-b-g0-approval-packet-unsigned.md) | `7a47ddaa5c8d9109d65d3ef59e8090a7c2fc9428a646913cca819e4f50026d60` |
| H | [旧review handoff](aws-mcp-sts001-investigation-b-g0-independent-review-handoff.md) | `ee05fa9c9d2ac43506f6be266e2b18da82b2c2ffaff9e11baa0c84bf061643d7` |
| R | [既存static review](../../STS001_G0_FINAL_OFFLINE_20261015/input/reference/G0_INDEPENDENT_STATIC_REVIEW.md) | `2a1ce704f4e215c31dc437d38703d9ab5c4cf86d7062027edbe334f5b702279b` |

Pの実行境界が支配する。D/Cは計画の経緯、G/Hは未署名の人間判断候補、Rは旧G/Hの文書レビュー。
Rの `ACCEPTED_FOR_HUMAN_G0_DECISION_CONSIDERATION` は本書のレビュー判定でもG0承認でもない。
旧資料が参照するR1独立再確認の別原本は本ZIPに含まれず、今回再検証したとは主張しない。
[人間の選択記録](../../STS001_G0_FINAL_OFFLINE_20261015/input/01_HUMAN_SELECTIONS.md)は選好の出典であり、本人確認や権限証明ではない。

## 3. 人間が選択済みの方針と残る判断

| selected human policy | still requires evidence/formal human decision |
| --- | --- |
| OD-01: ユーザー本人がHuman Operatorを担う | 氏名・verified ID・確認方法/参照・連絡経路・正確なローカル範囲と同意は `IDENTITY_PENDING`。アカウント名から推定しない |
| OD-02: 同一人がG0 ApproverとData Custodian。Retention/Deletion Ownerも同一人を候補とする | G0ローカル権限の根拠と検証、custodian権限、候補の削除権限、別個に帰属可能な承認行為、scope/digest/expiryは `PENDING`。AWS権限は推定しない |
| OD-08: 人間が用意し独立承認した最小化候補メタデータをAIへ供給 | 文書ID/版/実バイトSHA-256、正確な入力・出力・受領者・来歴・安全境界証明・承認イベントは `PENDING`。未提供のため `P0_CONFIG_DISCOVERY_BLOCKED` |
| OD-09: `$HOME/local-restricted-evidence/AWS-MCP-STS001-SEC04-RESOURCE/<approved-run-id>/` を候補として採用 | canonical root、所有者/custodian、mount、親経路、ACL/default ACL、暗号化/アクセス方式、Git/sync/backup除外の人間による証明は `PENDING`。保存先は未調査・未作成 |
| OD-10: 10クラスの期間方針を採用。30/30/7/90/180/30日、クラス7/8は `NOT_CREATED_NO_WRITE`、クラス9/10は180日 | 起算点・用途・scope・reviewer cutoff・絶対UTC三期限・custodian/backup・事前のcase限定standing deletion instruction・hold/残存コピー処理は `PENDING`。期間合意を削除許可に変換しない |

出典: P L173、L185-217、L225-249、L455-477、L538-585、L652-661、L668-675。
G L140-180とR section 4の補完注意に従い、日付欄だけの記入でOD-10を完了としない。

## 4. JSON承認レコード案

`null` と `PENDING` は未確定を表す。以下は実際の承認記録ではない。
scopeの識別子、版・digest、実入力/出力、実行tool/runtime/configの各結合は人間が確定する。

```json
{
  "document_status": "DRAFT_UNSIGNED_NOT_AUTHORIZED",
  "document_revision": "G0-FINAL-CANDIDATE-1",
  "decision": "UNDECIDED",
  "approval_state": "APPROVAL_PENDING",
  "case_id": "AWS-MCP-STS001-SEC04-RESOURCE",
  "investigation": "B",
  "stage": "G0",
  "scope_id": "PENDING",
  "scope_revision": "PENDING",
  "scope_digest": "PENDING",
  "plan_sha256": "15a9adad32011a6f1f660875d877c25092afc8eaa38a8c6a4b2486c1c451b9b1",
  "handoff_recorded_head": "2b10b5eab33cde6d4d7869473e5c9bee7583865c",
  "branch_current_state": "NOT_CHECKED_OFFLINE",
  "fixed_code_reference_commit": "05f4b92e7ff2de76dc79cf8d5dc9f563a03af209",
  "operator_verified_id": "IDENTITY_PENDING",
  "operator_identity_method_contact_and_reference": "PENDING",
  "approver_verified_id": "PENDING",
  "local_authority_basis_and_verification_reference": "PENDING",
  "data_custodian_verified_id_and_authority": "PENDING",
  "retention_deletion_owner_candidate": "SAME_HUMAN_AUTHORITY_PENDING",
  "retention_deletion_owner_verified_id_and_authority": "PENDING",
  "trusted_channel": "PENDING",
  "independently_attributable_approval_event": "PENDING",
  "approved_at_utc": null,
  "approval_expires_utc": null,
  "selected_initial_metadata_policy": "HUMAN_SUPPLIED_INDEPENDENTLY_APPROVED_MINIMIZED_CANDIDATE_METADATA",
  "sanitized_input_id_version_sha256_and_provenance": "PENDING",
  "sanitized_input_boundary_approval_reference": "PENDING",
  "exact_input_paths_and_digests": "PENDING",
  "exact_output_paths_fields_and_recipients": "PENDING",
  "executor_verified_id": "PENDING",
  "tool_runtime_config_ids_versions_digests_and_invocations": "PENDING",
  "approved_local_operation_subset": "PENDING_NONE_GRANTED",
  "execution_mode": "PENDING_NO_MODE_ATTESTED",
  "canonical_case_root_and_storage_attestation": "PENDING",
  "final_lifecycle_revision_digest_and_authority_event": "PENDING",
  "final_immutable_record_digest_binding": "PENDING_EXTERNAL_TRUSTED_APPROVAL_RECORD",
  "final_artifact_manifest_digest_binding": "PENDING",
  "human_risk_acceptance": "PENDING_NONE_GRANTED",
  "aws_api_count": 0,
  "aws_request_budget": 0,
  "aws_api_allowlist": [],
  "aws_region_endpoint_grants": [],
  "credential_provider_resolution": "PROHIBITED",
  "source_profile_fallback": "PROHIBITED",
  "deletion_grant": "NONE_GRANTED",
  "source_principal_baseline": "SOURCE_PRINCIPAL_BASELINE_PENDING",
  "actual_mode_source_request_path_go": "PRE_G1_PENDING",
  "operational_validation": "NOT_PERFORMED_NOT_VERIFIED",
  "g0": "G0_NOT_AUTHORIZED",
  "p0": "P0_NOT_EXECUTED",
  "later_gates": "G1-G5 / G1b / G5-release NOT_AUTHORIZED",
  "gate_sts001": "Gate STS-001 NOT VERIFIED",
  "signature": ""
}
```

## 5. G0ローカル操作allowlist候補

すべて `PROPOSED_NOT_APPROVED`。正確なpath/tool/runtime/config/hash/実行呼出しと範囲は未結合。
汎用shell許可ではなく、人間が個別に選択した部分集合のみ将来承認の対象になる。
AWS API予算は **0**、Region/endpointの許可は空、provider解決・source-profile fallback・削除許可はない。
将来P0の選択済みローカル部分集合を許可し得る行為は、全前提充足後に完成版のdigestへ結合された、
帰属可能な人間のG0ローカル承認イベントである。「別途承認されたP0」はこの有効なG0許可の範囲内を指す。
本draftや今回の作成依頼はそのイベントではない。G0に含まれない操作は新しい正確な許可を要する。

| 候補操作 | 将来の対象・出力と制限 | 未確定の結合 |
| --- | --- | --- |
| 運用入力ZIPの整合性と安全な展開 | 取得用別ZIPのCRC/member/hash。期待regular memberのみ、埋め込み実行なし | 入力原本/実バイトdigest、外部input宛先、tool呼出し、クラス3 lifecycleすべて `PENDING` |
| 固定参照のinventory | 指定参照の有無とdigest。欠落は `REFERENCE_NOT_AVAILABLE`、HEAD置換なし | 参照path/tool/digestは `PENDING` |
| 最小化候補メタデータ受領 | 承認済み人間供給文書のみ。原config、env、provider、cache、raw extractor入力にAIアクセスなし。extractor実装なし | 入力ID/版/hash/来歴、output/recipient、承認は `PENDING` |
| 保存先準備 | 人間所有のroot/ACL/除外証明。運用ファイル作成は全前提と別のP0許可の後のみ | 実path/owner/mount/権限と各クラス作成範囲は `PENDING` |
| offline readiness/実モードattestation | 既存承認verifierまたは人間harness、synthetic fixture、network-disabled評価と実境界同等性の人間証明 | tool/fixture/呼出し/config digestと実行者は `PENDING`。新Broker実装やlive probeは含まない |

候補メタデータの出力fieldは `source`（承認済み非秘密の来歴のみ）、`candidate_region`、
`candidate_sts_mode`、`conflict`、`observed_local_utc`、`authorization_state=NOT_AUTHORIZED`。
該当時のoverrideはboolean `OVERRIDE_PRESENT_REQUIRES_HUMAN_REVIEW` のみ。
未提供値・競合・default由来の値は候補または `UNKNOWN`。timestampは観測を捏造しない。
config section、provider command、URL/userinfo/query、認証情報、cacheを出力しない。
フィルタ試験の成功は実環境の隔離証明ではない。

## 6. 時点別の独立ゲート

| 時点 | 人間判断・実証 | 現在 |
| --- | --- | --- |
| pre-G0 | OD-01本人性、OD-02ローカル権限/別承認行為、OD-08初期メタデータ境界、OD-09保存先、OD-10 lifecycle、正確なscope/digest/expiry | `G0_NOT_AUTHORIZED`、`P0_CASE_WRITE_BLOCKED` |
| 別途承認されたP0中 | 承認部分集合のローカル準備。実際に選ぶMode AまたはBの完全な証明、source/provider/request-pathの人間attestationを準備 | `P0_NOT_EXECUTED`。今回実行しない |
| pre-G1 | OD-04有効な既存source、OD-08実モードGO、OD-03 STS Region/endpointとIAM endpoint/signing Region、OD-11 P1物理attempt/page/resource/rate/cost上限、別のG1 | `SOURCE_REQUEST_PATH_NOT_ATTESTED`。GetCallerIdentityも不可 |
| post-P1 / pre-G1b | 別G1で実観測したsource principalを人間が別途baseline採用。G1のbootstrap例外はprincipal baselineだけであり本人性/権限にはない | `SOURCE_PRINCIPAL_BASELINE_PENDING`。P2-P4不可 |
| G2/G3/G4 | 個別stage・service・Region・resource・予算の新規許可と先行stageのdisposition受理 | `NOT_AUTHORIZED`。G0/G1bから伝播しない |
| G5とG5-release | ローカル最小化処理と、OD-14受領者/機密性/独立raw-review権限・配布許可は別判断 | `NOT_AUTHORIZED`。share-candidateは配布不可、クラス7/8作成不可 |

出典: P L169-217、L412-449、L668-675。
両Modeに同じ要件が適用されるが、完全な実証は実際に選ぶModeについて行う。
自動発行/refresh/auto-assume、未承認egress/redirect/proxy/TLS例外を遮断し、1物理attemptと独立計数を実証する。
synthetic failure試験だけでproduction GOとせず、実設定同等性の帰属可能な人間証明を要する。
未知・不可観測・失効はNO_GO。live identity probeで前提を作らない。
862はR1の未承認提案上限であり、本G0の予算ではない。role reuse・IAM変更・Broker実装・Finding/Gate閉鎖は含まれない。

## 7. 承認の真正性と停止

人間は既存の信頼済み経路で全未確定項目を完成させ、署名対象の不変版を固定する。
その最終レコード、lifecycle、正確な入力/出力manifestのdigest、scope、失効UTCを
エージェント外の別途帰属可能な人間承認記録へ結合する。AIは署名・承認イベントを作成しない。
文書自身のdigestを本文へ自己埋込みせず、今回の候補hashは別SHA256SUMS/QA記録で識別する。
編集後は再hashし、新バイト列に承認を結合する。旧draftへの承認を流用しない。
署名済み同意は既定で公開repositoryへ置かず、未承認caseへの承認file書き込みで権限を自己生成しない。
チャットの選択・PR review/merge・文書受領・チェック合格はいずれもG0承認ではない。

次の場合は停止して人間判断を求める。

- 必須原本欠落/hash不一致: `BLOCKED_REFERENCE_INTEGRITY`。代替HEADや再構成で補わない。
- 身元・権限・scope・署名経路・有効期限が不明: `BLOCKED_APPROVAL`。
- 安全な候補メタデータ未提供: `P0_CONFIG_DISCOVERY_BLOCKED`。原configを開かない。
- 保存先/クラス別期限/standing deletion authority不備: `P0_CASE_WRITE_BLOCKED`。
- 隔離/監査/出力/実request-path証明不備: `BLOCKED_ISOLATION` / `SOURCE_REQUEST_PATH_NOT_ATTESTED`。
- scope/input/tool/config/source/request-path/lifecycle/digest変更、失効・撤回: 停止し再評価・別許可を要する。
- 意図しない操作・秘密露出・保存/整合性不良・重大な文書矛盾: 停止。自動fallbackや自己修復をしない。
- 正当なholdなしの削除不能: `RETENTION_BREACH`、収集/配布停止・アクセス制限・人間へ即時escalation。

本書の完成は未署名判断候補の提供まで。実条件の検証、G0決定、P0実行は未実施のまま停止する。
