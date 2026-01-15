# from google.genai import types
# from google.adk.agents.llm_agent import LlmAgent, Agent
# from google.adk.runners import Runner
# from toolbox_core import ToolboxSyncClient
# from google.adk.sessions import InMemorySessionService
# import asyncio
# from dotenv import load_dotenv

# from cs_agent.memory import search_memory
# from cs_agent.prompts import NEW_PROMPT_INSTRUCTION
# load_dotenv()

# APP_NAME = "agents"
# USER_ID = "1234"

# toolbox_client = ToolboxSyncClient(
#     url="http://127.0.0.1:5000"
# )

# database_tools = toolbox_client.load_toolset("cs_agent_tools")

# root_agent = Agent(
#     model='gemini-2.5-flash',
#     name='customer_support_assistant',
#     description=(
#         'An expert customer support agent helping users with order-related questions and requests. '
#         'Provides fast, clear, and friendly assistance with memory of past interactions.'
#     ),
#     instruction=NEW_PROMPT_INSTRUCTION,
#     tools=[*database_tools, search_memory],
# )

# # # Session and Runner
# # session_service = InMemorySessionService()
# # # Create the session before using it
# # session = await session_service.create_session(app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID)
# # runner = Runner(agent=root_agent, app_name=APP_NAME, session_service=session_service)

# # # Agent Interaction
# # def call_agent(query):
# #     content = types.Content(role='user', parts=[types.Part(text=query)])
# #     events = runner.run(user_id=USER_ID, session_id=SESSION_ID, new_message=content)

# #     for event in events:
# #         print(f"\nDEBUG EVENT: {event}\n")
# #         if event.is_final_response() and event.content:
# #             final_answer = event.content.parts[0].text.strip()
# #             print("\n🟢 FINAL ANSWER\n", final_answer, "\n")
# # # 1. Define the user's input (prompt)
# # call_agent("Hello, what is the status of my order with ID 102?")

# async def chat_with_agent(user_input: str, user_id: str) -> str:
#     """
#     Handle user input with automatic memory integration.

#     Args:
#         user_input: The user's message
#         user_id: Unique identifier for the user

#     Returns:
#         The agent's response
#     """
#     # Set up session and runner
#     session_service = InMemorySessionService()
#     session = await session_service.create_session(
#         app_name=APP_NAME,
#         user_id=user_id,
#         session_id=f"session_{user_id}"
#     )
#     runner = Runner(agent=root_agent, app_name=APP_NAME, session_service=session_service)

#     # Create content and run agent
#     content = types.Content(role='user', parts=[types.Part(text=user_input)])
#     events = runner.run(user_id=user_id, session_id=session.id, new_message=content)

#     # Extract final response
#     for event in events:
#         if event.is_final_response():
#             response = event.content.parts[0].text

#             return response

#     return "No response generated"

# if __name__ == "__main__":
#     response = asyncio.run(chat_with_agent(
#         "what is the status of my order with ID 102?",
#         user_id="1234"
#     ))
#     print(response)

from google.genai import types
from google.adk.agents.llm_agent import LlmAgent, Agent
from google.adk.runners import Runner
from toolbox_core import ToolboxSyncClient
from google.adk.sessions import InMemorySessionService
import asyncio
from dotenv import load_dotenv
from cs_agent.memory import search_memory, save_memory
from cs_agent.prompts import PROMPT_INSTRUCTION

load_dotenv()

APP_NAME = "agents"
USER_ID = "demo"

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
        
    save_memory(messages, USER_ID)


if __name__ == "__main__":
    asyncio.run(main())