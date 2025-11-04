import os
from google.adk.agents import LlmAgent
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

root_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="bigquery_data_agent",
    instruction=f"""
あなたは BigQuery データ分析のエキスパートです。
{DATASET} データセットに対して、ユーザーの質問に基づいてデータ分析を行います。
BigQuery ジョブは必ずプロジェクト ID `{PROJECT_ID}` で実行します。


このデータセットには Google Cloud のリリースノート情報が含まれています。

以下のガイドラインに従ってください:
- 自然言語の質問を適切な SQL クエリに変換して実行してください
- クエリ結果をわかりやすく説明してください
- 必要に応じて複数のクエリを実行して詳細な分析を提供してください
- データの傾向やパターンを見つけて洞察を提供してください
- 日本語で応答してください
""",
    tools=[bigquery_toolset],
)
