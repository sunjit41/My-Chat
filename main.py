import os
from datetime import datetime
from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.genai.errors import ServerError, ClientError

load_dotenv()
client = genai.Client()

# 1. Define Python functions the AI Agent can choose to call
def get_current_time() -> str:
    """Returns the current local date and time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def analyze_project_directory(folder_path: str = ".") -> list[str]:
    """Lists files in a directory so the AI can inspect the workspace."""
    try:
        return [f for f in os.listdir(folder_path) if not f.startswith(".")]
    except Exception as e:
        return [f"Error reading directory: {e}"]

# 2. Configure the agent with tools and system instructions
agent_config = types.GenerateContentConfig(
    system_instruction=(
        "You are a helpful Python developer assistant. "
        "Use your available tools whenever the user asks about the time or files in their project."
    ),
    tools=[get_current_time, analyze_project_directory],
)

def run_chat():
    model_name = "gemini-3.5-flash-lite"
    chat = client.chats.create(model=model_name, config=agent_config)
    print(f"=== MyChat Agent Ready ({model_name}) | Type 'exit' to quit ===\n")

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        try:
            response = chat.send_message(user_input)
            print(f"\nAI: {response.text}\n")
        except (ServerError, ClientError) as e:
            print(f"\n[API Notice]: Temporary error ({e.code}). Please try again.\n")

if __name__ == "__main__":
    run_chat()
