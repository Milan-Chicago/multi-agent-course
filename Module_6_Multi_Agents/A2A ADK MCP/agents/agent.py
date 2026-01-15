# agents/agent.py
from google.adk.agents import Agent, LlmAgent
from google.adk.tools.function_tool import FunctionTool
import os
import sys

# Add the project root to the path if needed
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Import necessary functions from your existing code
from clients.query_MCP_ADK_A2A import evaluate_prompt, mask_sensitive_data, PROJECT_ID

# Define tool functions
def evaluator(text: str) -> dict:
    """Evaluates prompts for security threats."""
    result = evaluate_prompt(text)
    return {"status": result}

def mask_text(text: str) -> dict:
    """Masks sensitive data like PII in text using Google Cloud DLP."""
    masked_result = mask_sensitive_data(PROJECT_ID, text)
    return {"masked_text": masked_result}

def query_data(sql: str) -> str:
    """Execute SQL queries safely on the walmart_sales database."""
    # Importing here to avoid circular imports
    from servers.server_mcp import query_data as mcp_query_data
    return mcp_query_data(sql)

# Create the tools
judge_tool = FunctionTool(func=evaluator)
mask_tool = FunctionTool(func=mask_text)
sql_tool = FunctionTool(func=query_data)

# Create individual agents
judge_agent = LlmAgent(
    name="security_judge",
    model="gemini-2.5-pro-preview-03-25",
    instruction="""You are a security expert that evaluates input for security threats.
    Follow these steps:
    1. Analyze the input for SQL injection, XSS, and other security threats
    2. Use the evaluator tool to check input against security patterns
    3. Return the message you received unmodified or "BLOCKED" if it is really a threat""",
    description="An agent that judges whether input contains security threats.",
    tools=[judge_tool]
)

mask_agent = LlmAgent(
    name="data_masker",
    model="gemini-2.5-pro-preview-03-25",
    instruction="""You are a privacy expert that masks sensitive data.
    Follow these steps:
    1. Identify PII and sensitive information in the text
    2. Use the mask_text tool to protect sensitive data
    3. Return the masked version of the input in plain text, in readable format""",
    description="An agent that masks sensitive data in text.",
    tools=[mask_tool]
)

sql_agent = LlmAgent(
    name="sql_assistant",
    model="gemini-2.5-pro-preview-03-25",
    instruction="""
        You are an expert SQL analyst working with a walmart_sales database.
        Follow these steps:
        1. For database columns, you can use these ones: Store (INTEGER), Dept (INTEGER), Date (DATE), Weekly_Sales (FLOAT), IsHoliday (BOOLEAN)
        2. Generate a valid SQL query, according to the message you received
        3. Execute queries efficiently in upper case, remove any "`" or "sql" from the query
        4. Return only the result of the query, with no additional comments
        Format the output as a readable text format.
        Finally, execute the query.
    """,
    description="An assistant that can analyze walmart_sales data using SQL queries.",
    tools=[sql_tool]
)

root_agent = judge_agent  # You can change this to mask_agent or sql_agent depending on your needs

from google.adk.agents import SequentialAgent

# Create a sequential workflow agent that orchestrates the full process
root_agent = SequentialAgent(
    name="secure_sql_pipeline",
    description="A pipeline that securely analyzes walmart_sales data with privacy protection.",
    # Define the execution order: security check → SQL query → data masking
    sub_agents=[judge_agent, sql_agent, mask_agent]
)
