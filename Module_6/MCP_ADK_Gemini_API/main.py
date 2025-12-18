import os
import sys
import asyncio
from google.genai import types
from google.adk.agents.llm_agent import LlmAgent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.artifacts.in_memory_artifact_service import InMemoryArtifactService
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = ""
os.environ["GOOGLE_API_KEY"] = ""

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root) if project_root not in sys.path else None

async def run_mcp_agent(query):
    tools, exit_stack = await MCPToolset.from_server(
        connection_params=StdioServerParameters(
            command='python',
            args=["./servers/server_mcp.py"],
            env={**os.environ}
        )
    )
    
    try:
        agent = LlmAgent(
            model='gemini-2.0-flash-exp',
            name='sql_assistant',
            instruction="""You are a SQL database assistant with access to the walmart_sales database.
            
            IMPORTANT: You MUST use the tools to interact with the database:
            1. Use list_database_tables() to see available tables
            2. Use get_table_info(table_name="walmart_sales") to see the schema
            3. Use execute_sql_query(sql="YOUR_SQL_HERE") to run queries

            Always EXECUTE the query using execute_sql_query tool - don't just show the SQL code.
            Return only the query results, not the SQL itself.""",
            tools=tools,
        )
        
        runner = Runner(
            app_name='sql_app',
            agent=agent,
            artifact_service=InMemoryArtifactService(),
            session_service=InMemorySessionService(),
        )
        
        session = runner.session_service.create_session(
            state={}, app_name='sql_app', user_id='user_1'
        )
        
        result_text = ""
        async for event in runner.run_async(
            session_id=session.id,
            user_id=session.user_id,
            new_message=types.Content(role='user', parts=[types.Part(text=query)])
        ):
            if event.is_final_response() and event.content and event.content.parts:
                result_text = event.content.parts[0].text
                
        return result_text.strip()
        
    finally:
        await exit_stack.aclose()

def main():
    query = "What is the average weekly sales for department 1 in store 1?"
    result = asyncio.run(run_mcp_agent(query))
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
