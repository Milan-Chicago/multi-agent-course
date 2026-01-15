from google.genai import types
from google.adk.agents.llm_agent import LlmAgent, Agent
from google.adk.runners import Runner
from toolbox_core import ToolboxSyncClient
from google.adk.sessions import InMemorySessionService
import asyncio
from dotenv import load_dotenv
from memory import search_memory, save_memory
from prompts import PROMPT_INSTRUCTION

load_dotenv()

APP_NAME = "agents"
USER_ID = "demo_cli"

toolbox_client = ToolboxSyncClient(
    url="http://127.0.0.1:5000"
)

database_tools = toolbox_client.load_toolset("cs_agent_tools")

NEW_PROMPT_INSTRUCTION = PROMPT_INSTRUCTION.format(USER_ID=USER_ID)

root_agent = Agent(
    model='gemini-2.5-flash',
    name='customer_support_assistant',
    description=(
        'An expert customer support agent helping users with order-related questions and requests. '
        'Provides fast, clear, and friendly assistance with memory of past interactions.'
    ),
    instruction=NEW_PROMPT_INSTRUCTION,
    tools=[*database_tools, search_memory],
)

session_service = InMemorySessionService()
runner = Runner(agent=root_agent, app_name=APP_NAME, session_service=session_service)

async def main():

    messages = []
    # Create a new session
    await session_service.create_session(app_name=APP_NAME, user_id=USER_ID, session_id=f"session_{USER_ID}")

    while True:

        print("=" * 80)
        user_input = input("You: ")
        # print("User: ", user_input)
        if user_input.lower() in ['quit', 'exit', 'bye', 'q']:
            break
        messages.append({"role": "user", "content": user_input})
        content = types.Content(role='user', parts=[types.Part(text=user_input)])
        response = runner.run(user_id=USER_ID, session_id=f"session_{USER_ID}", new_message=content)
        
        for event in response:
            # Print final response
            if event.is_final_response() and event.content:
                print("Agent: ", event.content.parts[0].text)
                messages.append({"role": "assistant", "content": event.content.parts[0].text})
        
        # print(messages)
    save_memory(messages, USER_ID)


if __name__ == "__main__":
    asyncio.run(main())
