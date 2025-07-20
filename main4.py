import os
from dotenv import load_dotenv
from agents import AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
from agents.tools import Tool

import math
import datetime

# Load .env for GEMINI_API_KEY
load_dotenv()

# External Gemini-compatible OpenAI client
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("Missing GEMINI_API_KEY in .env")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

run_config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

def get_config():
    return run_config

# ----------- 🛠️ Tool Definitions -----------

# 🧮 Calculator
def calculate(expression: str) -> str:
    try:
        result = eval(expression, {"__builtins__": {}}, math.__dict__)
        return f"The result is: {result}"
    except Exception as e:
        return f"Calculation error: {str(e)}"

# 🌦️ Weather
def get_weather(city: str) -> str:
    return f"The current weather in {city} is sunny and 30°C."  # Replace with real API later

# 📰 News
def get_news(topic: str) -> str:
    return f"Here are the latest headlines about {topic}:\n- Headline 1\n- Headline 2\n- Headline 3"  # Replace with real API later

# Register tools
tools = [
    Tool(name="Calculator", description="Solve math expressions", func=calculate),
    Tool(name="Weather", description="Get weather for a city", func=get_weather),
    Tool(name="News", description="Get latest news headlines", func=get_news),
]

def get_tools():
    return tools
