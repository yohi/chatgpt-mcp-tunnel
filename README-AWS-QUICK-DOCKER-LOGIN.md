# AWS MCP quick-STS — Docker内ログインから起動する（暫定）

この追加パッチは、**元の `aws-mcp-quick-sts.patch` 適用済み**の作業ツリーにのみ適用します。以前のパッチは再適用しません。`.env.aws` に以下を設定します。

```dotenv
AWS_MCP_STS_ROLE_ARN=arn:aws:iam::456720798575:role/aws-security-audit-readonly
```

対話ターミナルから次の1コマンドで起動します。

```bash
bash scripts/aws-mcp-quick-start.sh
```

スクリプトは、設定/マウントの事前検査 → 必要ならイメージビルド → 旧MCP停止 → STS専用Volume初期化・旧認証情報消去 → **Docker内 `default` で `aws login --remote`** → AWSアカウント確認 → `ReadOnlyAccess` セッションポリシー付き `AssumeRole` → MCPコンテナ再作成 → 実効STSロール確認、の順に実行します。`aws login --remote` のURLにアクセスし、ブラウザに表示された認証コードを**ターミナルへ入力**します。

ホスト `~/.aws` の `default` とDocker `aws-sso-data` 内の `default` は別です。前回のDockerでの `profile default could not be found` は未ログインが原因であり、Docker `aws-auth` を初回ログインすればプロファイルが作成されます。ログインキャッシュは `aws-sso-data` に保持されますが、この起動スクリプトは毎回対話ログインを要求します。`docker compose up -d` だけでAWS CLIの完全無人ログインはできません。

STS認証情報は1時間、バックグラウンド更新はありません。継続するなら期限前に再実行します。停止・STSファイル削除:

```bash
docker compose --env-file .env.aws -f compose.aws.yaml -f compose.aws.quick-sts.yaml stop aws-tunnel
docker compose --env-file .env.aws -f compose.aws.yaml -f compose.aws.quick-sts.yaml run --rm --no-deps aws-quick-sts-clear
```

`--remove-orphans` と `down -v` は使用しないでください。既存Atlassian MCPやログインVolumeを消さないためです。

前提: Docker Compose 2.24.4+ (`!override`)、元のquick-STSパッチ適用済み、AWS CLI `aws login` 利用権限、元の主体から当該ロールへの `sts:AssumeRole` と信頼ポリシー。`ReadOnlyAccess` は広範な読み取り権限を持ち、`run_script` 自体は書込み可能なツールです。今回の起動確認は実効権限全体の監査、STS-001/G1正式承認を意味しません。

## Docker ログインVolumeの初期化

Docker側の `aws-sso-data` が初回作成時にroot所有である場合、起動スクリプトは
`aws-auth` コンテナの書込み可否を確認してから、必要なときだけ既存の
`aws-sso-init`（Volumeのトップディレクトリのみ所有者変更）を実行します。
ログインキャッシュの削除や `down -v` は行いません。

この手順はオンライン実行を未検証です。AWS認証、ロールTrust、
`sts:AssumeRole` 権限が不足していれば起動は失敗します。
