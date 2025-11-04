# ADK BigQueryToolSet で自然言語データ分析

## はじめに

このハンズオンでは, ADK の Built-in tools である `BigQueryToolSet` を使用して, 自然言語でデータ分析を行うエージェントを構築します.

## Step 1-1. Google Cloud への認証確認

Google Cloud への認証状況を確認します.

```bash
gcloud auth list
```

```bash
gcloud config get-value account
```

もし期待したユーザが認証されていない場合は, 以下のコマンドで認証を行います.

```bash
gcloud auth application-default login --no-launch-browser
```

を実行してログインを行います (ログイン URL が出てくるので, URL をクリック, verification code を入力しましょう)

## Step 1-2. プロジェクト ID の設定

次に, 使用する Google Cloud プロジェクト ID を設定します.

```bash
gcloud config set project PLEASE_SPECIFY_YOUR_PROJECT_ID
```

`PLEASE_SPECIFY_YOUR_PROJECT_ID` の部分は, ご自身のプロジェクト ID に置き換えてください.
念の為, 正しく設定されているか確認しましょう.

```bash
gcloud config get-value project
```

設定したプロジェクト ID は, 後ほど使用するため環境変数に設定しておきます.

```bash
export GOOGLE_CLOUD_PROJECT=$(gcloud config get-value project)
```

## Step 1-3. 必要な API の有効化

BigQuery API を有効化します.
```bash
gcloud services enable bigquery.googleapis.com
```
新規のプロジェクトの場合, このコマンドは数分程度かかる可能性があります.

## Set Up BigQuery Data Agent

### Python 環境のセットアップ

```bash
python -m venv .venv
```

```bash
source .venv/bin/activate
```

```bash
pip install google-adk
```

## BigQuery Data Agent

ADK の Built-in tools なので, 実はこちらもかなり簡単に Agent 作成ができちゃいます
まずは対象のファイルを眺めましょう

```bash
cloudshell edit agents/agent.py
```

### エージェントの起動

作成したエージェントを起動します。

```bash
adk web --port 8080
```

右上の `Web Preview` から Cloud Shell 上の 8080 を見に行きましょう

## エージェントに質問する

エージェントが起動したら、以下のような質問を試してみましょう。

### 質問例 1: データ概要の確認

```
このデータセットにはどのようなデータが含まれていますか？
```

### 質問例 2: 最新のリリースノート

```
最新の10件のリリースノートを教えてください
```

### 質問例 3: 特定プロダクトの分析

```
Compute Engine に関連するリリースノートは何件ありますか？
```

### 質問例 4: 時系列分析

```
2024年に公開されたリリースノートの数を月別に集計してください
```

### 質問例 5: カテゴリ分析

```
最も多くのリリースノートがあるプロダクトカテゴリトップ5を教えてください
```

エージェントは自動的に適切な SQL クエリを生成し、BigQuery に対して実行し、結果を返します。

## 参考リンク

- [ADK BigQueryToolSet ドキュメント](https://google.github.io/adk-docs/tools/built-in-tools/#bigquery)
- [ADK 公式ドキュメント](https://google.github.io/adk-docs/)
