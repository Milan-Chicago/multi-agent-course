from mcp.server.fastmcp import FastMCP
from langchain.tools import tool
import sqlite3
from loguru import logger
from typing import Any, Dict, List
from langchain_community.utilities import SQLDatabase
import pandas as pd
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    HarmBlockThreshold,
    HarmCategory,
)
import os

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", max_tokens=2048, temperature=0.1, top_p=1.0,
                             frequency_penalty=0.0, presence_penalty=0.0,
                             safety_settings={
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_VIOLENCE: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_CIVIC_INTEGRITY: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE})

mcp = FastMCP("security-hub")


# Database Authentication
class DatabaseAuthenticator:
    def __init__(self, credentials: Dict[str, str]):
        self.credentials = {
            username: self._hash_password(password)
            for username, password in credentials.items()
        }

    def _hash_password(self, password: str) -> str:
        """Hash a password using SHA-256."""
        import hashlib
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_credentials(self, username: str, password: str) -> bool:
        """Verify if the provided credentials are valid."""
        if username not in self.credentials:
            return False
        return self.credentials[username] == self._hash_password(password)

# Database setup and connection
def setup_database(authenticator: DatabaseAuthenticator) -> SQLDatabase:
    """Set up the database connection with authentication."""
    import getpass

    username = "admin"#input('\033[1;91mEnter username: \033[0m')
    password = "admin123" #getpass.getpass('\033[1;91mEnter password: \033[0m')

    if not authenticator.verify_credentials(username, password):
        raise ValueError("Invalid credentials!")

    # Load dataset and create database
    df = pd.read_csv(r"C:\Users\alish\Documents\google_adk\A2A_ADK_MCP_Walmart_Sales\data\walmart_sales.csv")
    connection = sqlite3.connect("walmart_sales.db")
    df.to_sql(name="walmart_sales", con=connection, if_exists='replace', index=False)

    return SQLDatabase.from_uri("sqlite:///walmart_sales.db")

# Initialize database with sample credentials
sample_credentials = {
    'admin': 'admin123',
    'analyst': 'data456',
    'reader': 'read789'
}
authenticator = DatabaseAuthenticator(sample_credentials)

db=setup_database(authenticator)

toolkit = SQLDatabaseToolkit(
db=db,
llm=llm
)

mcp = FastMCP("security-hub")

# Extract the individual tools from your toolkit
query_tool = toolkit.get_tools()[0]  # QuerySQLDatabaseTool
info_tool = toolkit.get_tools()[1]   # InfoSQLDatabaseTool
list_tool = toolkit.get_tools()[2]   # ListSQLDatabaseTool
checker_tool = toolkit.get_tools()[3]  # QuerySQLCheckerTool

# Create wrapper functions for each tool
@mcp.tool()
def execute_sql_query(sql: str) -> str:
    """Execute SQL queries safely on the walmart_sales database."""
    logger.info(f"Executing SQL query: {sql}")
    try:
        # First check the query using the checker tool
        checked_sql = checker_tool.run(sql)
        # Then execute the query
        result = query_tool.run(checked_sql)
        return result
    except Exception as e:
        logger.error(f"SQL Error: {str(e)}")
        return f"Error: {str(e)}"

@mcp.tool()
def get_table_info(tables: str) -> str:
    """Get schema and sample data for specified tables (comma-separated)."""
    logger.info(f"Getting info for tables: {tables}")
    try:
        result = info_tool.run(tables)
        return result
    except Exception as e:
        logger.error(f"Table Info Error: {str(e)}")
        return f"Error: {str(e)}"

@mcp.tool()
def list_database_tables() -> str:
    """List all tables in the database."""
    logger.info("Listing all database tables")
    try:
        result = list_tool.run("")
        return result
    except Exception as e:
        logger.error(f"List Tables Error: {str(e)}")
        return f"Error: {str(e)}"

@mcp.tool()
def query_data(sql: str) -> str:
    """Execute SQL queries safely on the walmart_sales database."""
    logger.info(f"Executing SQL query: {sql}")
    conn = sqlite3.connect("walmart_sales.db")
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        conn.commit()
        return "\n".join(str(row) for row in result)
    except Exception as e:
        logger.error(f"SQL Error: {str(e)}")
        return f"Error: {str(e)}"
    finally:
        conn.close()


if __name__ == "__main__":
    # Start the server (this will block until the server is stopped)
    print("Starting MCP server...")
    mcp.run(transport="stdio")  # You may want to change this to TCP for network access