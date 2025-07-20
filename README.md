💻 Example Interaction
bash
Copy
Edit
$ python main.py
🧠 Ask me something. Type 'exit' to stop.

👤 You: What is the capital of Japan?

Assistant: The capital of Japan is Tokyo.

👤 You: What is it famous for?

Assistant: Tokyo is famous for its technology, anime culture, and cherry blossoms.

👤 You: exit
👋 Goodbye!




.

💬 Example:
python
Copy
Edit
handle_query("What is the capital of France?")
handle_query("How old is that city?")
handle_query("What is it famous for?")
Even though the second and third questions don’t mention "Paris", the AI knows you’re still talking about Paris, because it's looking at the full conversation history like this:

✅ Loads your saved chat_history.json
✅ Lets you chat with the AI agent
✅ Keeps history across questions
✅ Ends only when you type exit




✅ Step-by-Step Plan
We’ll update:

1. tool.py – Define tool functions
2. main.py – Register tools with your agent




mkdir myproject && cd myproject

uv init . 

uv venv 

source .venv/bin/activate

uv add openai-agents

uv add python-dotenv

uv run main.py

uv run app.py

# agent-runner-chat-history-json
