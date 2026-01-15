from google.genai import types
from google.adk.agents.llm_agent import LlmAgent
from google.adk.runners import Runner
from toolbox_core import ToolboxSyncClient
from google.adk.sessions import InMemorySessionService
import asyncio
import os
from dotenv import load_dotenv
from memory import search_memory, save_memory
from prompts import SQL_PROMPT_INSTRUCTION, GUARDRAIL_PROMPT_INSTRUCTION
from greet import display_users, greet_user

load_dotenv()

toolbox_client = ToolboxSyncClient(
    url="http://127.0.0.1:5000"
)

database_tools = toolbox_client.load_toolset("cs_agent_tools")

judge_agent = LlmAgent(
    name="security_judge",
    model="gemini-2.5-flash",
    instruction=GUARDRAIL_PROMPT_INSTRUCTION,
    description="An agent that judges whether input contains security threats.",
)
judge_session_service = InMemorySessionService()
judge_runner = Runner(agent=judge_agent, app_name="security_app", session_service=judge_session_service)


async def validate_input(user_input: str, user_id: str) -> bool:
    """
    Validate user input using LLM-based guardrails.
    
    Args:
        user_input: The user's input to validate
        user_id: The user ID for session management
        
    Returns:
        True if input is safe, False if blocked
    """
    try:
        # Create or get judge session
        judge_session_id = f"judge_session_{user_id}"
        try:
            await judge_session_service.create_session(
                app_name="security_app", 
                user_id=user_id, 
                session_id=judge_session_id
            )
        except:
            # Session might already exist, continue
            pass
        
        # Run judge agent to evaluate input
        judge_content = types.Content(role='user', parts=[types.Part(text=user_input)])
        judge_response = judge_runner.run(
            user_id=user_id, 
            session_id=judge_session_id, 
            new_message=judge_content
        )
        
        # Extract the judge's response
        judge_result = None
        for event in judge_response:
            if event.is_final_response() and event.content:
                judge_result = event.content.parts[0].text.strip().upper()
                break
        
        # Check if input was unsafe
        if judge_result and "unsafe" in judge_result:
            print("\n⚠️  Security Alert: Your input contains potential security threats and has been blocked.")
            print("Please rephrase your question in a safe manner.\n")
            return False
        
        return True
    except Exception as e:
        print(f"\n⚠️  Warning: Input validation encountered an error: {e}")
        print("Proceeding with caution...\n")
        return True


async def main():
    print("=" * 80)

    print("Welcome to the Customer Support Assistant")

    print("=" * 80)
    print("Select your id from the following list:")

    display_users()

    print("=" * 80)
    user_id = input("Enter your id: ")
    USER_ID = user_id
    print(greet_user(USER_ID))


    IMPROVED_SQL_PROMPT_INSTRUCTION = SQL_PROMPT_INSTRUCTION.format(USER_ID=USER_ID)
    
    root_agent = LlmAgent(
        model='gemini-2.5-flash',
        name='customer_support_assistant',
        description=(
            'An expert customer support agent helping users with order-related questions and requests. '
            'Provides fast, clear, and friendly assistance with memory of past interactions.'
        ),
        instruction=IMPROVED_SQL_PROMPT_INSTRUCTION,
        tools=[*database_tools, search_memory],
    )
    
    session_service = InMemorySessionService()
    runner = Runner(agent=root_agent, app_name="agents", session_service=session_service)
    
    # Create a new session
    await session_service.create_session(app_name="agents", user_id=USER_ID, session_id=f"session_{USER_ID}")
    
    messages = []

    while True:
        print("=" * 80)
        user_input = input("You: ")
        # print("User: ", user_input)
        if user_input.lower() in ['quit', 'exit', 'bye', 'q']:
            break
        
        # Validate input with LLM guardrails
        if not await validate_input(user_input, USER_ID):
            continue  # Skip processing if input is Unsafe
        
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
