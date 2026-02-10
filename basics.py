from dotenv import load_dotenv
import os
from pathlib import Path
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
print("Loaded key:", api_key)

client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

response = client.chat.completions.create(
    model="google/gemma-3-4b-it",
    messages=[
        {"role": "user", "content": "tell me a joke "}
    ]
)

print(response.choices[0].message.content)
