import os
import sys

# Add the project root to the path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.modules.pop("servers", None)  # Clear any failed import attempts
    sys.path.insert(0, project_root)

from agents.mcp_agent import run_mcp_agent


# Then update the call_sql_agent function to use the MCP agent
async def call_sql_agent(query):
    print(f"\n>>> SQL Input: {query}")

    # Use the MCP agent instead of the existing implementation
    result_text = await run_mcp_agent(query)

    print(">>> SQL Result", result_text)
    return result_text


# Update your analyze_sale_data_async function
async def analyze_sale_data_async(query: str):
    # Use A2A to call the SQL agent
    try:
        sql_prompt = f"""
        You are a SQL expert analyzing the sales database.

        Task: Generate and execute a SQL query to answer this question: "{query}"

        First, understand the database schema.
        Then write a clear, efficient SQL query using UPPER CASE keywords.
        Finally, execute the query.
        Return the output of the query, nothing else
        """

        sql_result = await call_sql_agent(sql_prompt)
        return sql_result
    except Exception as e:
        return f"SQL execution error: {str(e)}"


# 7. Execute with asyncio

# "List the top 5 dates with the highest total weekly sales across all stores."
# "What is the average weekly sales for department 1 in store 1?"

def main():
    """Run the demo query when script is executed directly."""
    # Sample query for testing
    query = "What is the average weekly sales for department 1 in store 1?"

    import asyncio
    result = asyncio.run(analyze_sale_data_async(query))

    print(f"Result: {result}")

# This guard ensures the code only runs when the file is executed directly
# and not when it's imported by another module
if __name__ == "__main__":
    main()
