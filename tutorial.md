# ADK BigQueryToolSet で自然言語データ分析

## はじめに

このハンズオンでは, ADK の Built-in tools である `BigQueryToolSet` を使用して, 自然言語でデータ分析を行うエージェントを構築します.

## Google Cloud への認証確認

まず、Google Cloud への認証が正しく設定されているか確認します。

以下のコマンドを実行して、認証状態を確認してください。

```bash
gcloud auth list
```

認証されていない場合は、以下のコマンドで認証を行います。

```bash
gcloud auth application-default login
```

ブラウザが開くので、Google アカウントでログインしてください。

## プロジェクトとリージョンの設定

次に、使用する Google Cloud プロジェクトとリージョンを設定します。

プロジェクト ID を環境変数に設定します。

```bash
export PROJECT_ID=<your-project-id>
gcloud config set project $PROJECT_ID
```

リージョンも設定します（例: us-central1）。

```bash
export REGION=us-central1
```

## 必要な API の有効化

BigQuery API を有効化します。

```bash
gcloud services enable bigquery.googleapis.com
```

API の有効化には数分かかる場合があります。

## agents ディレクトリと agent.py の作成

agents ディレクトリを作成し、agent.py ファイルを作成します。

```bash
mkdir -p agents
```

agents/agent.py を以下の内容で作成します。

```python
from google.adk.agents import Agent
from google.adk.tools.bigquery import BigQueryToolSet

# BigQuery の public dataset を指定
DATASET = "bigquery-public-data.google_cloud_release_notes.release_notes"

# BigQueryToolSet を初期化
bigquery_tools = BigQueryToolSet(
    project_id="<your-project-id>",  # プロジェクト ID を指定
    dataset_id=DATASET
)

# エージェントを作成
root_agent = Agent(
    model="gemini-2.0-flash-exp",
    tools=bigquery_tools.get_tools(),
    system_instruction=f"""
    あなたは BigQuery データ分析のエキスパートです。
    {DATASET} データセットに対して、ユーザーの質問に基づいてデータ分析を行います。

    - 自然言語の質問を SQL クエリに変換して実行してください
    - 結果をわかりやすく説明してください
    - 必要に応じて複数のクエリを実行して詳細な分析を提供してください
    """
)
```

上記のファイルで、`<your-project-id>` を実際のプロジェクト ID に置き換えてください。

## 依存関係のインストール

ADK をインストールします。

```bash
pip install google-adk
```

## エージェントの起動

作成したエージェントを起動します。

```bash
adk run agents/agent.py
```

エージェントが起動すると、対話型のプロンプトが表示されます。

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

## クリーンアップ

ハンズオンが完了したら、エージェントを終了します。

プロンプトで `exit` または `quit` と入力するか、Ctrl+C を押してください。

## まとめ

おめでとうございます！

このハンズオンでは、以下のことを学びました。

- ADK の BigQueryToolSet の基本的な使い方
- 自然言語でデータ分析を行うエージェントの構築
- BigQuery public dataset を活用したデータ分析

### 次のステップ

- 他の BigQuery public datasets を試してみる
- カスタムデータセットでエージェントを構築する
- 複数のツールを組み合わせたより高度なエージェントを作成する

### 参考リンク

- [ADK BigQueryToolSet ドキュメント](https://google.github.io/adk-docs/tools/built-in-tools/#bigquery)
- [BigQuery public datasets](https://cloud.google.com/bigquery/public-data)
- [ADK 公式ドキュメント](https://google.github.io/adk-docs/)
