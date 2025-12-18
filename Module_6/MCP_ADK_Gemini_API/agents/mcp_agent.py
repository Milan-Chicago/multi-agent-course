import asyncio
import logging
import uuid
from dotenv import load_dotenv
from google.genai import types
from google.adk.agents.llm_agent import LlmAgent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.artifacts.in_memory_artifact_service import InMemoryArtifactService
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
load_dotenv()

async def get_tools_async():
    """Connect to MCP Server and get tools."""
    logger.info("Connecting to MCP server...")
    tools, exit_stack = await MCPToolset.from_server(
        connection_params=StdioServerParameters(
            command='python',
            args=["./servers/server_mcp.py"],
            env={**os.environ}
        )
    )
    logger.info(f"Connected with {len(tools)} tools")
    return tools, exit_stack

async def run_mcp_agent(query):
    """Run the MCP agent with a query."""
    exit_stack = None
    
    try:
        # Get tools
        tools, exit_stack = await get_tools_async()
        
        # Create agent with better instructions
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
        
        # Create session
        session_service = InMemorySessionService()
        session = session_service.create_session(
            state={},
            app_name='sql_app',
            user_id='user_1',
            session_id=f"session_{uuid.uuid4()}"
        )
        
        # Run query
        runner = Runner(
            app_name='sql_app',
            agent=agent,
            artifact_service=InMemoryArtifactService(),
            session_service=session_service,
        )
        
        content = types.Content(role='user', parts=[types.Part(text=query)])
        result_text = ""
        
        async for event in runner.run_async(
            session_id=session.id,
            user_id=session.user_id,
            new_message=content
        ):
            # Log all events for debugging
            logger.info(f"Event type: {type(event).__name__}")
            
            if event.is_final_response() and event.content and event.content.parts:
                result_text = event.content.parts[0].text
                
        return result_text or "No response generated"
        
    except Exception as e:
        logger.error(f"Error: {e}", exc_info=True)
        return f"Error: {str(e)}"
        
    finally:
        if exit_stack:
            await exit_stack.aclose()

# Test
async def main():
    result = await run_mcp_agent("What is the average weekly sales for department 1 in store 1?")
    print(f"\nResult:\n{result}\n")

if __name__ == "__main__":
    asyncio.run(main())
