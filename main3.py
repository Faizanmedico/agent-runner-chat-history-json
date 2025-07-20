import os
import json
from agents import Agent, Runner
from tool import get_config

HISTORY_FILE = "chat_history.json"

# Load history if it exists
if os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, "r") as f:
        chat_history = json.load(f)
else:
    chat_history = []

def save_history():
    with open(HISTORY_FILE, "w") as f:
        json.dump(chat_history, f, indent=2)

def add_to_history(role, content):
    chat_history.append({"role": role, "content": content})
    save_history()

def build_prompt_from_history(history):
    return "\n".join([f"{msg['role'].capitalize()}: {msg['content']}" for msg in history])

agent = Agent(name="Assistant", instructions="You are a helpful assistant")

def handle_query(user_input):
    add_to_history("user", user_input)
    full_prompt = build_prompt_from_history(chat_history)
    result = Runner.run_sync(agent, full_prompt, run_config=get_config())

    # Clean up any repeating 'Assistant:' prefix if present
    response = result.final_output.replace("Assistant: ", "").strip()
    add_to_history("assistant", response)
    print(f"\nAssistant: {response}\n")

# ----------- 💬 Start CLI Loop -----------

print("🧠 Ask me something. Type 'exit' to stop.\n")

while True:
    user_input = input("👤 You: ")
    if user_input.strip().lower() in ["exit", "quit"]:
        print("👋 Goodbye!")
        break
    handle_query(user_input)
