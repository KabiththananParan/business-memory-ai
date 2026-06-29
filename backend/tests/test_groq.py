import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env
load_dotenv()

# Create Groq client
client = Groq(
    api_key=os.getenv("LLM_API_KEY")
)

# Send a simple prompt
response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "user",
            "content": "Say hello in one short sentence."
        }
    ],
)

# Print the response
print("Groq response:")
print(response.choices[0].message.content)