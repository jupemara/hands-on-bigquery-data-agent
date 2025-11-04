import os
from google.adk.agents import Agent
from google.adk.tools.bigquery import BigQueryToolSet

# BigQuery の public dataset を指定
DATASET = "bigquery-public-data.google_cloud_release_notes.release_notes"

# プロジェクト ID を環境変数から取得
project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")
if not project_id:
    raise ValueError(
        "GOOGLE_CLOUD_PROJECT 環境変数を設定してください。\n"
        "例: export GOOGLE_CLOUD_PROJECT=your-project-id"
    )

# BigQueryToolSet を初期化
bigquery_tools = BigQueryToolSet(
    project_id=project_id,
    dataset_id=DATASET
)

# エージェントを作成
root_agent = Agent(
    model="gemini-2.5-flash",
    tools=bigquery_tools.get_tools(),
    system_instruction=f"""
あなたは BigQuery データ分析のエキスパートです。
{DATASET} データセットに対して、ユーザーの質問に基づいてデータ分析を行います。

このデータセットには Google Cloud のリリースノート情報が含まれています。

以下のガイドラインに従ってください:
- 自然言語の質問を適切な SQL クエリに変換して実行してください
- クエリ結果をわかりやすく説明してください
- 必要に応じて複数のクエリを実行して詳細な分析を提供してください
- データの傾向やパターンを見つけて洞察を提供してください
- 日本語で応答してください
"""
)
