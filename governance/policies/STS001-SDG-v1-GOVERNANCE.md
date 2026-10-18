# STS001-SDG-v1 — Solo Developer Governance（制定候補）

文書ID：`STS001-SDG-v1-GOVERNANCE`  
作成日：2026-10-18 JST  
**Status：`PROPOSED_NOT_ADOPTED`／Effective Date：未設定**  
承認ルート：当該個人プロジェクトのOwner Rootに基づく**将来効の新Baseline制定**。旧E0に対する例外や遡及承認ではない。

## 1. 効力の起点と対象範囲
1. 本文書は新しい`SDG-v1`名前空間にのみ適用する。旧E0、C0/C1、既存G1〜G5の過去の状態を変更せず、旧E0のSecurity Approval Authorityの要件を充足したとも主張しない。
2. 正式効力は、Ownerが**採用対象文書のRaw SHA-256、Version、適用スコープ、発効日時、明示的APPROVE**を含む独立した採用Decisionを記録した後に限る。採用記録は監査可能な別媒体にも保存する。現時点では未実施。
3. 当該プロジェクトを拘束する上位合意、共同所有者または外部承認義務が後日確認されれば、新Governanceの効力判断を中断し根拠を再評価する。
4. GithubのRepository管理権だけを規範制定権の唯一の証明としない。Owner申告と原本調査の証拠を併置する。

## 2. Ownerの兼務と責任分界
- 同一の**単独の自然人**が `Project Owner`、`Governance Authority`、`Security Accountable Owner`、`SDK Evidence Custodian`、`IAM/SEC-04 Evidence Custodian`を兼務できる**新設計候補**とする。
- これを「独立したSecurity承認」「別自然人による職務分離」と呼ばない。Owner兼務による利益相反・単一点故障・誤判断リスクは明示して受容または代替統制する。
- `Independent Technical Reviewer` は任意の証拠検証Role。AIの別セッションは別の人間・独立した正式承認者の代わりにならない。
- `Release Signer`、`Key Custodian`、`Trust Registry Operator`、`Epoch/Revocation Authority`は**技術的に別の責務**として設計できるが、同じ自然人による運用を人的分離と表示しない。これらの正式任命・鍵・登録は未実施。
- 人間によるOperation単位の承認は、エージェントが自分で承認したり同じ権限を使い回したりできない認証済み**独立Web UI**で行う。人的な別承認者の存在を意味しない。

## 3. 不可放棄の技術的セーフティ境界（設計要求）
1. **Fail Closed**：未署名、Authority不明、Validator不一致、Version/Epochの不整合、Ledger更新不能、Revocation未確認、Outcome Unknown、状態競合では Dispatch を拒否する。
2. **Credentials Isolation**：AWS資格情報・秘密鍵をAI Agentへ露出しない。長期AWS IAMアクセスキーへのFallbackを禁止。Bitwarden等の既存IAMキーとBroker専用認証情報を分離する。
3. **Operation Boundaries**：初期8 Operationは候補であって**承認0/8**。IAM書込み・権限付与・高リスクOperationは明示的な新決裁がなければDENY。除外Operationの自動復活は禁止。
4. **Write Control**：登録済みの低リスク書込み候補でも、本人認証・対象Principal/Account/Action/Parametersの完全Binding・1操作1承認・期限・Nonce・取消/Revocation・重複実行防止を必須とする。`OUTCOME_UNKNOWN`の自動再試行は禁止。
5. **Artifact Authority**：Catalog、Request Schema、Governed Manifest Schema、Envelope Schema、Validator設定、Grant、Response Projection、Ledger契約は型・Version・Raw Digest・Authority IDで識別し、Mix-and-MatchとRollbackを拒否する。提案中のTyped Registryは未採用。
6. **Trust Bootstrap**：署名検証用公開鍵／Trust Rootの初期値は、Ownerが決裁対象Fingerprintを**事前に**確認する別の記録によって固定。Envelopeの自己申告鍵やRegistryの自己署名をそのまま根源的Authorityにしない。鍵ローテーション・失効・高水位を別に規範化し実証する。
7. **Runtime Tests**：Ledgerの原子的・不可逆なGrant消費、強整合／アンチRollback、Principal/Task/Grant Binding、署名付きHTTP Wire、双Worker整合、Response Projection、実際のAWS最小権限は実装・オフライン統合・許可されたAWS試験で証拠が必要。候補設計をRuntime PROVENへ昇格させない。
8. **Audit**：Owner決裁、採用対象Digest、対話型再認証、承認対象差分、失効とEmergency Stop、Dispatch拒否・Outcome Unknownを監査可能な改変検知ログに残す。単独Ownerがログを管理する限界を説明し、補完のオフラインバックアップと必要に応じた外部Timestampを検討する。

## 4. DecisionとReviewの区別
- すべてのDecisionにはID、Policy Version、EvidenceのRaw SHA、Scope、Decision Authority、具体的Choice（APPROVE/REJECT/DEFER）、日時、本人性・認証方式、COIの申告、残余リスク、Expiry/Revocationを束縛する。
- `null` / `PENDING` は**未決裁**であり、権限者が実際に`DEFER`を決裁した場合と区別する。
- OwnerによるGovernance制定と、本人による後続セキュリティ責任の受諾は分離したDecisionとする。元のE0独立承認での合格とは表現しない。
- Reviewを新たに発注する条件は、再現可能なBlocking反例、変更されたThreat Model、具体的なRuntime証拠欠落に限定する。形式的な軽微修正で無期限に審査を循環させない。

## 5. SDG-v1採用後でも別途必要なGate
- `SDG-G0`：Root／新Governance正式発効・版固定。**現在PENDING**。
- `SDG-G1`：技術Baseline、Typed Pin、Artifact署名・Trust Root、Epoch/Revocation、証拠受領、Scopeの採用。**現在OPEN**。
- `SDG-G2`：実装・Broker Runtimeとセキュリティ不変条件、オフライン統合。**現在OPEN**。
- `SDG-G3`：Host／複数Worker、Legacy Path、Egress、State、Recoveryの独立した検証。**現在OPEN**。
- `SDG-G4`：AWS接続・STS・IAM・高リスク禁止・環境別検証の明示的許可。**現在NOT AUTHORIZED**。
- `SDG-G5`：運用リスク受容／Release／Maintenance／インシデント対応／停止。**現在PENDING**。
- 旧E0のGate状態は過去のまま継続。新SDGの決裁が旧E0のFinding Closureとみなされることもない。

## 6. 既存証拠の再利用
- C0でバイト固定済みの4 Artifact、EA-01 Wheel／RECORD／SDK Model、EA-02 SAR8 Operation比較、R2.1 Patch等は**新NamespaceでDigestとScopeを明示して再利用候補**とする。
- 既存証拠の技術的正当性と新SDGでの正式Evidence Acceptanceは分離する。後者は新Policyで定めるAuthority Decisionが必要。
- CloudWatch Raw差分・過去HTTP取得経緯の限界・Runtime SDK Pinning未実証、SAR/FAS/実効IAMの証明不足を継承する。
- 旧OD-09/10を承認済みに変えず、必要なら別IDの`SDG-OD09/10`として新規決裁する。

## 7. 改訂、失効、撤回
- 新Policyの改訂はOwner Rootが、改訂前後SHA、理由、リスク影響、影響Gate、Effective Date、新Versionを記録する**将来効Decision**によってのみ行う。
- 緊急停止は即時DENY、資格取り消し、署名鍵失効等の設計された経路で優先させる。未実装なら運用許可なし。
- 不明な権限委任、未確認の共同権利、失効したOwner資格、ソース証拠の改竄が判明すれば正式採用や運用の継続を停止して判定をやり直す。

## 8. 初期正式状態（採用候補として）
`adopted=false`、`effective_at=null`、`production_root_approved=false`、`trust_registry_approved=false`、`signature_issued=false`、`owner_decisions_approved=0`、`operations_authorized=0`、`implementation_approved=false`、`aws_connectivity_authorized=false`、`dispatch=ALL_DENY`。
