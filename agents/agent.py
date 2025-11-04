import os
from google.adk.agents import Agent
from google.adk.tools.bigquery import BigQueryToolset
from google.adk.tools.bigquery import BigQueryCredentialsConfig
from google.adk.tools.bigquery.config import BigQueryToolConfig
from google.adk.tools.bigquery.config import WriteMode
import google.auth

DATASET = "bigquery-public-data.google_cloud_release_notes.release_notes"
PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT")
if not PROJECT_ID:
    raise ValueError(
        "GOOGLE_CLOUD_PROJECT 環境変数を設定してください。\n"
        "例: export GOOGLE_CLOUD_PROJECT=your-project-id"
    )

application_default_credentials, _ = google.auth.default()
bigquery_toolset = BigQueryToolset(
    credentials_config=BigQueryCredentialsConfig(
        credentials=application_default_credentials
    ),
    bigquery_tool_config=BigQueryToolConfig(write_mode=WriteMode.BLOCKED)
)

bigquery_tools = BigQueryToolset(
    project_id=PROJECT_ID,
    dataset_id=DATASET
)

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
