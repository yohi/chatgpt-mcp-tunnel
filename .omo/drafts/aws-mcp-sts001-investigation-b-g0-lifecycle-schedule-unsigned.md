# Investigation B — 10クラス保持・削除スケジュール（未署名）

## 1. 状態・適用範囲

`DRAFT_UNSIGNED_NOT_AUTHORIZED`、版 `G0-LIFECYCLE-CANDIDATE-1`。
対象 `AWS-MCP-STS001-SEC04-RESOURCE` / Investigation B。
人間所有のlifecycleレコードの記入用候補であり、作成・保持・削除許可ではない。
[G0最終承認候補](aws-mcp-sts001-investigation-b-g0-final-decision-record-unsigned.md)と
[レビュー引き継ぎ](aws-mcp-sts001-investigation-b-g0-finalization-review-handoff.md)に対応する。

```text
PLAN_PREPARED_PENDING_EXECUTION_APPROVAL
G0_NOT_AUTHORIZED
P0_NOT_EXECUTED
G1-G5 / G1b / G5-release NOT_AUTHORIZED
Gate STS-001 NOT VERIFIED
```

出典: [人間選択](../../STS001_G0_FINAL_OFFLINE_20261015/input/01_HUMAN_SELECTIONS.md)、
[G0 packet](aws-mcp-sts001-investigation-b-g0-approval-packet-unsigned.md) L140-180、
[R1 plan](../plans/aws-mcp-sts001-investigation-b.md) L455-477、L538-585。
期間方針だけが選択済み。運用ケースの最初の書き込みより前に、全作成対象クラスについて全欄を人間が承認する。
クラス9のcase承認fileを先に作成して、その作成権限を後から正当化してはならない。
case書き込み前の承認イベントは、既存の信頼済み経路に人間が記録する。その経路の正確なIDと既存保管権限、
保管・保持条件、後日許可するcase copyとの関係も `PENDING` であり、人間が先に確定する。
新しい保存経路をAIが作成せず、C09の期間方針から既存経路全体の削除権限を推定しない。
本planning文書と準備QAは運用ケース記録ではない。

## 2. 全クラス共通の未確定欄と記入規則

各クラスの以下の欄はそれぞれ独立の記入欄であり、まとめて黙示承認しない。
候補用途・候補anchorは提案であり、`human_approved_use` と `approved_anchor_event_utc` はすべて未確定。
日数はUTC期限へまだ変換していない。会話日・準備日・仮の実行日を起算点として採用しない。

| 各クラスの共通欄 | 現在値と必要な人間判断 |
| --- | --- |
| creation_authority | `NONE_GRANTED`。クラス1-6/9/10も作成許可待ち。7/8は `NOT_CREATED_NO_WRITE` |
| approved_anchor_event_id / approved_anchor_event_utc | `PENDING` / `PENDING`。下記候補を採用するか別起算点を選び、各対象ファイルへ結合する |
| human_approved_use / approving_event | `PENDING` / `PENDING`。候補用途の記載だけでは足りない |
| review_due_utc / escalate_at_utc / retention_expires_utc | 各々 `PENDING`。各々絶対UTC timestampを人間が確定する |
| custodian_verified_id / backup_verified_id / authority_evidence | 各々 `PENDING`。同一人候補の権限を推定しない |
| exact_case_owned_scope / canonical_root / manifest | 各々 `PENDING`。正確なclass/file集合・版・locatorを特定し、他クラスやhomeへ拡張しない |
| standing_deletion_instruction / authority_verified_id / event_reference | 各々 `PENDING`。事前のcase限定指示・法的/ローカル権限・帰属可能なイベントが必要 |
| legal_hold_authority / process / notification_channel | 各々 `PENDING`。有効なholdの適用範囲・理由・次回review・制限を記録する方式を承認する |
| residual_copies_snapshots_disposition / verification_method | 各々 `PENDING`。一時copy・backup・snapshot・受領者copyを含む実在コピーの処理と検証方法を確定する |
| reviewer_access_cutoff_utc / reviewer_authority_and_scope | 各々 `PENDING`。クラス固有のcutoffと対象を決め、未許可のraw/auditアクセスは与えない |

上記全欄は下記各クラスに適用する。クラス別の主要未確定値も繰り返し明示する。
許可された起算点から選択済み日数に一致するexpiryを決め、reviewとescalationは必ずexpiryより前に置く。
reviewとescalation相互の順序/間隔、日数のUTC計算規則、file集合ごとのanchorを人間が明示承認する。
cutoffはexpiryを超えず、hold/承認失効/削除時にはより早いアクセス制限を反映する。
無回答やreview未完了でexpiryを延長しない。原本削除を理由にmappingを長期保管することもない。

## 3. クラス別レコード（重複なし10件）

### C01 — Restricted raw originals

- 選択済み期間: **30 days**。作成権限: `NONE_GRANTED`。
- proposed_anchor: 将来許可された各原本の取得/受領イベント。approved_anchor_event_id/utc: `PENDING` / `PENDING`。
- proposed_use: 人間境界内での原本整合性と許可されたpolicy解釈。human_approved_use/event: `PENDING` / `PENDING`。
- review_due_utc: `PENDING`; escalate_at_utc: `PENDING`; retention_expires_utc: `PENDING`。
- custodian_verified_id/backup_verified_id: `PENDING` / `PENDING`; exact_case_owned_scope/manifest: `PENDING` / `PENDING`。
- standing_deletion_instruction/authority/event: `PENDING` / `PENDING` / `PENDING`; legal_hold_authority/process: `PENDING` / `PENDING`。
- residual_copies_snapshots_disposition: `PENDING`（restricted原本と許可済み複製を照合）; reviewer_access_cutoff_utc: `PENDING`。AIのrawアクセスなし。

### C02 — Aliases / mappings / salts

- 選択済み期間: **30 days**。作成権限: `NONE_GRANTED`。
- proposed_anchor: 将来許可された各mapping/salt生成イベント。approved_anchor_event_id/utc: `PENDING` / `PENDING`。
- proposed_use: 許可された照合と再識別を人間管理境界内で行う。human_approved_use/event: `PENDING` / `PENDING`。
- review_due_utc: `PENDING`; escalate_at_utc: `PENDING`; retention_expires_utc: `PENDING`。
- custodian_verified_id/backup_verified_id: `PENDING` / `PENDING`; exact_case_owned_scope/manifest: `PENDING` / `PENDING`。
- standing_deletion_instruction/authority/event: `PENDING` / `PENDING` / `PENDING`; legal_hold_authority/process: `PENDING` / `PENDING`。
- residual_copies_snapshots_disposition: `PENDING`（alias表/salt/複製を別途照合）; reviewer_access_cutoff_utc: `PENDING`。raw削除から保持延長を推定しない。

### C03 — Transient / input / filter copies

- 選択済み期間: **7 days**。作成権限: `NONE_GRANTED`。
- proposed_anchor: 将来許可された各input受領/作業copy生成イベント。approved_anchor_event_id/utc: `PENDING` / `PENDING`。
- proposed_use: 承認済み入力検証と最小化の一時処理。human_approved_use/event: `PENDING` / `PENDING`。
- review_due_utc: `PENDING`; escalate_at_utc: `PENDING`; retention_expires_utc: `PENDING`。
- custodian_verified_id/backup_verified_id: `PENDING` / `PENDING`; exact_case_owned_scope/manifest: `PENDING` / `PENDING`。
- standing_deletion_instruction/authority/event: `PENDING` / `PENDING` / `PENDING`; legal_hold_authority/process: `PENDING` / `PENDING`。
- residual_copies_snapshots_disposition: `PENDING`（temporary/filter残存とcleanup triggerを明示）; reviewer_access_cutoff_utc: `PENDING`。credential/cacheをこのクラスへ取り込まない。

### C04 — QA records

- 選択済み期間: **90 days**。作成権限: `NONE_GRANTED`。
- proposed_anchor: 将来許可された各運用QA記録生成イベント。approved_anchor_event_id/utc: `PENDING` / `PENDING`。
- proposed_use: 許可された検証結果の再現性確認。human_approved_use/event: `PENDING` / `PENDING`。
- review_due_utc: `PENDING`; escalate_at_utc: `PENDING`; retention_expires_utc: `PENDING`。
- custodian_verified_id/backup_verified_id: `PENDING` / `PENDING`; exact_case_owned_scope/manifest: `PENDING` / `PENDING`。
- standing_deletion_instruction/authority/event: `PENDING` / `PENDING` / `PENDING`; legal_hold_authority/process: `PENDING` / `PENDING`。
- residual_copies_snapshots_disposition: `PENDING`（QA export/付随copyの残存を照合）; reviewer_access_cutoff_utc: `PENDING`。秘密/raw payloadを一般QAへ入れない。

### C05 — Audit records

- 選択済み期間: **180 days**。作成権限: `NONE_GRANTED`。
- proposed_anchor: 将来許可された各人間監査イベント/記録生成。approved_anchor_event_id/utc: `PENDING` / `PENDING`。
- proposed_use: 人間が操作/権限/結果の追跡可能性を保持する。human_approved_use/event: `PENDING` / `PENDING`。
- review_due_utc: `PENDING`; escalate_at_utc: `PENDING`; retention_expires_utc: `PENDING`。
- custodian_verified_id/backup_verified_id: `PENDING` / `PENDING`; exact_case_owned_scope/manifest: `PENDING` / `PENDING`。
- standing_deletion_instruction/authority/event: `PENDING` / `PENDING` / `PENDING`; legal_hold_authority/process: `PENDING` / `PENDING`。
- residual_copies_snapshots_disposition: `PENDING`（append-only/immutable制約、監査保管の複製を含む）; reviewer_access_cutoff_utc: `PENDING`。AIは人間監査保管を削除できない。

### C06 — Share-candidate copies

- 選択済み期間: **30 days**。作成権限: `NONE_GRANTED`。
- proposed_anchor: 将来許可された各candidate版生成イベント。approved_anchor_event_id/utc: `PENDING` / `PENDING`。
- proposed_use: 人間境界内での機密性/最小化/配布候補確認。human_approved_use/event: `PENDING` / `PENDING`。
- review_due_utc: `PENDING`; escalate_at_utc: `PENDING`; retention_expires_utc: `PENDING`。
- custodian_verified_id/backup_verified_id: `PENDING` / `PENDING`; exact_case_owned_scope/manifest: `PENDING` / `PENDING`。
- standing_deletion_instruction/authority/event: `PENDING` / `PENDING` / `PENDING`; legal_hold_authority/process: `PENDING` / `PENDING`。
- residual_copies_snapshots_disposition: `PENDING`（candidate旧版/preview/exportを照合）; reviewer_access_cutoff_utc: `PENDING`。candidateであることは配布許可ではない。

### C07 — Local approved-share copies

- 選択済みcreation_policy: **`NOT_CREATED_NO_WRITE`**。作成・変換・コピーを禁止。期限を新設しない。
- approved_anchor_event_id/utc、human_approved_use/event: すべて `PENDING_NOT_CREATED`。
- review_due_utc/escalate_at_utc/retention_expires_utc: すべて `PENDING_NOT_CREATED`。
- custodian_verified_id/backup_verified_id、exact_case_owned_scope/manifest: すべて `PENDING_NOT_CREATED`。
- standing_deletion_instruction/authority/event、legal_hold_authority/process: すべて `PENDING_NOT_CREATED`。
- residual_copies_snapshots_disposition/reviewer_access_cutoff_utc: `PENDING_NOT_CREATED`。実在copyの検査を行ったという意味ではない。
- 将来作成には別のscope/lifecycle判断と必要なG5-releaseを要する。C06からの移動でも禁止を迂回しない。

### C08 — External distribution copies

- 選択済みcreation_policy: **`NOT_CREATED_NO_WRITE`**。送信・upload・外部copy作成を禁止。期限を新設しない。
- approved_anchor_event_id/utc、human_approved_use/event: すべて `PENDING_NOT_CREATED`。
- review_due_utc/escalate_at_utc/retention_expires_utc: すべて `PENDING_NOT_CREATED`。
- custodian_verified_id/backup_verified_id、exact_case_owned_scope/manifest: すべて `PENDING_NOT_CREATED`。
- standing_deletion_instruction/authority/event、legal_hold_authority/process: すべて `PENDING_NOT_CREATED`。
- residual_copies_snapshots_disposition/reviewer_access_cutoff_utc: `PENDING_NOT_CREATED`。外部削除完了を主張しない。
- 将来のOD-14受領者確認・保持削除合意・独立G5-release・別scope/lifecycleなしに作成しない。

### C09 — Approval records

- 選択済み期間: **180 days**。作成権限: `NONE_GRANTED`。
- proposed_anchor: 将来の帰属可能な承認イベントと許可済みcase記録受領/生成。approved_anchor_event_id/utc: `PENDING` / `PENDING`。
- proposed_use: exact scope/digest/有効性と各権限行使の追跡。human_approved_use/event: `PENDING` / `PENDING`。
- review_due_utc: `PENDING`; escalate_at_utc: `PENDING`; retention_expires_utc: `PENDING`。
- custodian_verified_id/backup_verified_id: `PENDING` / `PENDING`; exact_case_owned_scope/manifest: `PENDING` / `PENDING`。
- standing_deletion_instruction/authority/event: `PENDING` / `PENDING` / `PENDING`; legal_hold_authority/process: `PENDING` / `PENDING`。
- residual_copies_snapshots_disposition: `PENDING`（trusted channel原本とcase copyの管理を区別）; reviewer_access_cutoff_utc: `PENDING`。公開repositoryへの署名済み同意配置を既定としない。

### C10 — Deletion receipts

- 選択済み期間: **180 days**。作成権限: `NONE_GRANTED`。
- proposed_anchor: 将来の許可済み削除結果記録生成イベント。approved_anchor_event_id/utc: `PENDING` / `PENDING`。
- proposed_use: 実際の削除結果/失敗/残存copyと権限の監査。human_approved_use/event: `PENDING` / `PENDING`。
- review_due_utc: `PENDING`; escalate_at_utc: `PENDING`; retention_expires_utc: `PENDING`。
- custodian_verified_id/backup_verified_id: `PENDING` / `PENDING`; exact_case_owned_scope/manifest: `PENDING` / `PENDING`。
- standing_deletion_instruction/authority/event: `PENDING` / `PENDING` / `PENDING`; legal_hold_authority/process: `PENDING` / `PENDING`。
- residual_copies_snapshots_disposition: `PENDING`（receipt自身の複製と削除監査の継続性を含む）; reviewer_access_cutoff_utc: `PENDING`。予定を削除完了証明へ変換しない。

## 4. expiry・hold・失敗の処理（将来の人間承認対象）

1. 事前に承認するescalation時刻で、review未完了やhold懸念を名指しのdata/legal ownerへ通知する。
2. expiry時に有効なholdがなければ、権限を持つcustodianが事前承認済みの正確なcase限定指示を実施する。
   reviewer無回答や新しい返答の欠如だけで延長しない。本書にはその指示も削除許可もまだ存在しない。
3. 有効なholdだけが例外。authority/reason/scope、アクセス制限、次回review日時と通知を記録し、
   `RETENTION_EXCEPTION_LEGAL_HOLD` とする。通常処理・新規収集を停止し、元のexpiry達成とは報告しない。
4. holdなしで削除不能/失敗なら `RETENTION_BREACH`。収集/配布停止、アクセス制限、人間へ即時escalation。
   技術失敗を承認済み延長や成功に変えない。早期削除・scope変更には別の具体的同意を要する。
5. 将来の削除は承認manifestのcase-owned file/classだけ。canonical root、所有権、symlinkなしを先に確認する。
   home全体、AWS config/cache/credential、Git、無関係fileは対象外。AIによる人間audit削除は禁止。
6. hash/alias、削除UTC、担当、権限event、結果、残存copyを記録し、不在確認と許可済みbackup/snapshot照合を行う。
   unlinkだけでSSD/COW/backup消去を保証しない。外部copy削除は検証不能なら未確認とする。
7. C05/C09/C10にはそれぞれ別の承認済みlifecycleが必要。権限行使の監査前にauthority記録を消さない。
   180日方針と後発receipt等の監査必要期間に矛盾があれば、書き込み前に人間が解決する。
   AIは自動延長せず、解決不能なら `P0_CASE_WRITE_BLOCKED` を維持する。

全10件の実行可能なlifecycleと事前権限が確定しない限り、運用case書き込みは開始しない。
署名欄は空欄。承認行為・削除・hold設定・実ファイル検査は本作業では実施していない。
