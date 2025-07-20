from agents import Agent, Runner
from tool import get_config

# Initialize chat history
chat_history = []

def add_to_history(role, content):
    chat_history.append({"role": role, "content": content})

def build_prompt_from_history(history):
    """Create a context string for the agent from prior messages."""
    return "\n".join([f"{msg['role'].capitalize()}: {msg['content']}" for msg in history])

# Initialize agent
agent = Agent(name="Assistant", instructions="You are a helpful assistant")

# Function to handle a new user query
def handle_query(user_input):
    add_to_history("user", user_input)

    # Combine chat history into one prompt
    full_prompt = build_prompt_from_history(chat_history)

    result = Runner.run_sync(agent, full_prompt, run_config=get_config())

    add_to_history("assistant", result.final_output)
    print(result.final_output)
    print("-" * 40)

# Interactions
handle_query("Which is the largest city in Pakistan?")
handle_query("Who is the current President of Pakistan?")
handle_query("What is the population of that city?")  # Context-aware follow-up

# Print full chat history
print("\n--- Full Chat History ---")
for message in chat_history:
    print(f"{message['role'].capitalize()}: {message['content']}")
