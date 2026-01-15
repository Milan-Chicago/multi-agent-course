from agents import judge_agent, mask_agent, sql_agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.artifacts.in_memory_artifact_service import InMemoryArtifactService
import asyncio
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Define constants
USER_ID = "user_1"

def create_runner(agent, app_name):
    """Create a runner for an agent."""
    session_service = InMemorySessionService()
    artifact_service = InMemoryArtifactService()

    # Create a session for the agent
    session_id = f"{app_name}_{agent.name}"
    session_service.create_session(
        app_name=app_name,
        user_id=USER_ID,
        session_id=session_id
    )

    # Create and return the runner
    return Runner(
        agent=agent,
        app_name=app_name,
        artifact_service=artifact_service,
        session_service=session_service,
    ), session_id

# You can choose which agent to run based on command line args or environment variables
def main():
    # For example, run the SQL agent
    runner, session_id = create_runner(sql_agent, "sql_analysis_app")

    # You could set up CLI argument parsing here to choose which agent to run
    # For now, we'll just run the SQL agent as an example

    # Import and use the ADK CLI to run the agent
    from google.adk.cli import app
    app.run()

if __name__ == "__main__":
    main()