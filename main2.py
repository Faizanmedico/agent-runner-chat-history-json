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
    save_history()  # Save after every message

def build_prompt_from_history(history):
    return "\n".join([f"{msg['role'].capitalize()}: {msg['content']}" for msg in history])

agent = Agent(name="Assistant", instructions="You are a helpful assistant")

def handle_query(user_input):
    add_to_history("user", user_input)

    full_prompt = build_prompt_from_history(chat_history)

    result = Runner.run_sync(agent, full_prompt, run_config=get_config())

    add_to_history("assistant", result.final_output)
    print(result.final_output)
    print("-" * 40)

# Start asking questions
handle_query("Which is the largest city in Pakistan?")
handle_query("Who is the current President of Pakistan?")
handle_query("What is the population of that city?")
