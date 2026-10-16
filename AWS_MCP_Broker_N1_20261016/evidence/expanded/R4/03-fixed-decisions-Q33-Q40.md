# Fixed baseline B3 — User decisions Q33–Q40

**Status:** USER-CONFIRMED DECISION REGISTER（原文そのものではなく、ユーザー決定内容の確認用要約）  
**Baseline ID:** B3。原文はこの会話の各確定メッセージに帰属する。Q32は保管先未確認でありD相当を暫定的な安全側の前提としたもので、実際の所在の確定ではない。

| 決定 | ユーザー確定内容 | 不変条件 |
|---|---|---|
| Q33 | AdapterをBrokerと別の実効的な実行・認証・認可・管理境界に分離。専用Machine Account/Project。既存IAMキー不可 | 同一プロセス/権限共有は独立とみなさない。成立は未実証 |
| Q34 A | Bitwardenの使用は外部サービス連携のSecretのみ | AWS認証・STS発行/更新・Role切替・Broker内部認証/暗号化はBitwarden非依存 |
| Q35 A | Secret Adapter内で許可された認証付き外部操作を完結 | Broker/AIへの秘密値返却なし。任意Secret取得APIなし |
| Q36 A | 初期外部操作は登録済み読み取り・状態確認のみ | 外部書き込みと任意HTTPは禁止、HTTP GETだけで読み取り認定しない。初期許可リスト空 |
| Q37 A | 独立主体認証＋操作ごとの証明 | Brokerだけで発行/改変不可、主体・インスタンス・操作・対象・パラメータ・期限・失効/再利用束縛 |
| Q38 A | Bitwarden連携は初期無効・必要時だけ管理者が有効化 | 初期Adapter起動/BWS Token配置不要。未検証の環境は連携不可。AWS機能は非依存 |
| Q39 A | Adapter専用の独立Secret Store | BrokerにはBWS Token取得・更新・配置・Store改変権限なし。環境別に検証 |
| Q40 A | Adapter独立管理＋高リスク変更は独立した2名の人間の承認 | 同一人物二重承認禁止。Bitwarden Owner/Admin、クラウド/CI/CD/Store管理経路も迂回不可。緊急縮小は認可済み1名。独立監査 |

**User-held safety floor:** 既存IAM長期アクセスキーはPassword Manager/Secrets Manager双方にある可能性を想定し、Broker/Executor/Adapterによる取得・復号・使用を禁止。実際の保管先は未確認。REQ-045はどちらにあっても緩和されない。REQ-048は絶対8時間・無操作15分。

**Decision status:** これらは要件意思決定として確定。ただしFEAS-001/007/011、Gate S0/S1/Cは未実証。要求が成立する実装の存在は保証しない。
