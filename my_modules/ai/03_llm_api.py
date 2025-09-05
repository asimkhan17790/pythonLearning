# LLM API Integration
# This module provides functions to interact with a language model API.
from openai import OpenAI
import os
client = OpenAI()

response = client.responses.create(
    model="gpt-5",
    input="Write a one-sentence bedtime story about a horse."
)

print(response.output_text)

print(os.environ.get("OPENAI_API_KEY"))
