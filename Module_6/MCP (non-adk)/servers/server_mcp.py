from mcp.server.fastmcp import FastMCP
from langchain.tools import tool
import sqlite3
from loguru import logger
from typing import Any, Dict, List
import pandas as pd
import os

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
def setup_database(authenticator: DatabaseAuthenticator) -> sqlite3.Connection:
    """Set up the database connection with authentication."""
    username = "admin"
    password = "admin123"

    if not authenticator.verify_credentials(username, password):
        raise ValueError("Invalid credentials!")

    # Load dataset and create database
    df = pd.read_csv(r"/content/multi-agent-course/Module_6/MCP (non-adk)/data/walmart_sales.csv")
    connection = sqlite3.connect("walmart_sales.db")
    df.to_sql(name="walmart_sales", con=connection, if_exists='replace', index=False)

    return connection


# Initialize database with sample credentials
sample_credentials = {
    'admin': 'admin123',
    'analyst': 'data456',
    'reader': 'read789'
}
authenticator = DatabaseAuthenticator(sample_credentials)
db_connection = setup_database(authenticator)


@mcp.tool()
def execute_sql_query(sql: str) -> str:
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


@mcp.tool()
def get_table_info(table_name: str = "walmart_sales") -> str:
    """Get schema and sample data for specified table."""
    logger.info(f"Getting info for table: {table_name}")
    conn = sqlite3.connect("walmart_sales.db")
    try:
        cursor = conn.cursor()
        
        # Get table schema
        cursor.execute(f"PRAGMA table_info({table_name})")
        schema = cursor.fetchall()
        schema_str = "Table Schema:\n" + "\n".join(str(col) for col in schema)
        
        # Get sample data (first 5 rows)
        cursor.execute(f"SELECT * FROM {table_name} LIMIT 5")
        sample_data = cursor.fetchall()
        sample_str = "\n\nSample Data:\n" + "\n".join(str(row) for row in sample_data)
        
        return schema_str + sample_str
    except Exception as e:
        logger.error(f"Table Info Error: {str(e)}")
        return f"Error: {str(e)}"
    finally:
        conn.close()


@mcp.tool()
def list_database_tables() -> str:
    """List all tables in the database."""
    logger.info("Listing all database tables")
    conn = sqlite3.connect("walmart_sales.db")
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        return "\n".join(table[0] for table in tables)
    except Exception as e:
        logger.error(f"List Tables Error: {str(e)}")
        return f"Error: {str(e)}"
    finally:
        conn.close()


if __name__ == "__main__":
    with open("server_log.txt", "a") as f:
        f.write("Server started\n")
    # Start the server (this will block until the server is stopped)
    print("Starting MCP server...")
    mcp.run(transport="stdio")

