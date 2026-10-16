# AWS MCP Broker v1.1 — Independent Feasibility Handoff (R4)

**Status:** `NOT_AUTHORIZED_PENDING_NORMATIVE_REVIEW_AND_OWNER_DECISION`。規範レビューPASSも実験・実装許可を意味しない。

## 事前ブロッカー

**OWNER_DECISION_PENDING:** REQ-009/046・AC-022の保護境界改訂は未承認。Owner決裁と独立規範レビューが整うまで本工程開始の認可なし。

**INFORMATION-THEORETIC LIMIT:** ID/Project/メタデータに変化がなく値だけ差し替えられるなら、取得前情報だけで改ざんを識別不能。秘密内容を**取得して初めて検出する方式ではREQ-045違反**。独立した取得前書換え阻止とバージョン拘束が現実に成立するかを重点検証し、不能ならAdapter連携BLOCKED。

## 優先調査トラック

1. **FEAS-001（AWS鍵なし認証）:** Deno Deploy、Cloudflare Workers、Docker/Linux、Docker/macOSで、長期AWS IAMキーの取得・フォールバックを禁止しながら独立に認証・STS更新・Role切替が成立するか。OIDCとIAM Roles Anywhereの証明書秘密鍵依存を区別。AWS SDK implicit credential fallbackを否定テスト。
2. **FEAS-007-A（既存IAMキー隔離）:** Password Manager/Secrets Manager双方、Machine Account、Secret ID・内容・所属Project・参照/バックアップ、Org Owner/Adminによる**値だけ差替え・取得前の独立強制・取得競合**を攻撃経路に含める。**既存IAMキー実値は一切使わずダミーのみ**。
3. **FEAS-007-B（Adapter独立性）:** Brokerの実行ID・管理UIが完全侵害されても、Adapter環境・Secret Store・独立認可発行鍵、信頼先、契約Digest、S/D/C/R台帳、監査を変更できないか。
4. **FEAS-007-C（実効二者承認）:** Bitwarden Org Owner/Admin、Cloudflare/Deno/ホスト管理者、Secret Store、CI/CD、バックアップ、rollback、Token発行/配置、Secret内容更新の全変更経路を列挙。独立2名の承認を破る経路はCritical BLOCKED。自動Token更新が具体的1変更の承認を再利用/包括承認に変えないこと。
5. **FEAS-011（3環境同等性）:** AWS-only初期状態とBitwarden有効化能力を各環境別に実証。Docker/LinuxとmacOSを別に扱う。未実証の連携能力を「N/Aだから合格」としない。
6. **FEAS-Authorization（独立認可/送信）:** `S`送信解放と`D`実transport送信開始を分離し、`S<C`未送信の停止→取消→再起動では絶対に初回送信しないことを最終通信境界で検証する。 本人/サービス主体の独立認証、元要求完全性、発行者の独立ポリシー、契約Digest、送信主体束縛、S/D/C/R競合、複数Adapterの単回台帳・監査障害を検証。
7. **FEAS-E2E（非本番read）:** Ownerが別途許可したテスト用read/status operation、使い捨て模擬Secret、模擬外部接続で肯定的E2Eと拒否/出力秘匿化の両方を検証。本番操作の初期許可リスト空を維持。

## 必須アウトプット

- 環境別Actor×Operation×Resource×Authorityの**実効権限**マトリクス。
- 全変更経路（Bitwarden Secret**内容**、Org管理、クラウド特権、CI/CD、ロールバック等）の列挙と単独迂回可否。
- Broker侵害/Adapter侵害/単独特権管理者侵害/認可発行者の誤発行の別々の脅威モデル。
- 操作契約固定、証明発行の根拠、C/Sの意味と競合で破綻しない証拠。
- ACごとの証拠ID・反例・環境・判定。実証できなければ`NOT_PROVEN`、要件不成立なら`BLOCKED/NO_CREDIBLE_DESIGN`。
- 実験計画は実行許可ではない。実験に必要な別承認（使用アカウント・模擬Secret・予算・安全な破棄）を提出。

**固定禁止:** 実IAM長期キーの読取り/移動/利用、AWS長期キーへのfallback、BrokerへのBWS Token返却、外部write、任意HTTP/Secret取得、二者承認回避、独断での要件緩和。安全性保証が成立しないプラットフォームでBitwardenを有効化しない。

**現時点:** INT-003 Critical OPEN/BLOCKING; Gate S0/S1/C NOT_PROVEN; FEAS-001/007/011 NOT_PROVEN; Design/Implementation NOT_AUTHORIZED。

## R4専用判定

- 既存REQ-009/046・AC-022のOwner決裁なしに境界改訂を事実上採用することを禁止。
- 実験でSecret実値/既存IAMキーを使用することを禁止。模擬キーでもBitwardenからの値取得前に拒否できる否定試験の構築自体、別の実験許可が必要。
- Adapterを無効化できることと、安全にBitwarden有効運用できることを混同しない。
- 分散台帳だけで実送信順序が強制できるとの推測を禁ずる。`D`/`C`の最終送信経路での強制根拠が必要。

## Rev4 additional blockers

- **RG-BRK-NR-R3-001:** REQ-009/046・AC-022の全文改訂がRequirements Ownerに正式採用されていない。文書候補では実効認証境界を変更できない。
- **RG-BRK-NR-R3-002:** 2名の正規承認を経て禁止IAM長期キー相当のSecretが混入するケースも含む。二者承認の正常実行と、取得前内容安全性は独立した保証。**AC-036**の実施・可否が未確定。
- FEAS-007-Cでは承認を受けたSecret値自体に対する内容由来の独立強制を検証する。汎用Bitwarden Secret値が内容を書き換え得る環境で取得前完全性を保証できない場合、Adapterの当該Secret取得を禁止し、連携は`BLOCKED`。
- INT-003/二者承認迂回を対象とする動的技術調査は、独立した実験許可を得るまで開始しない。
