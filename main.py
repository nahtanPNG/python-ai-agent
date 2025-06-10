import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

user_prompt = sys.argv[1]
verbose_flag = None

if len(sys.argv) >= 3 and sys.argv[2] == "--verbose":
    verbose_flag = sys.argv[2]

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

response = client.models.generate_content(model="gemini-2.0-flash-001", contents= messages)
prompt_tokens = client.models.generate_content(model="gemini-2.0-flash-001", contents= messages).usage_metadata.prompt_token_count
response_tokens = client.models.generate_content(model="gemini-2.0-flash-001", contents= messages).usage_metadata.candidates_token_count

if verbose_flag is not None:
    print("User prompt: ", user_prompt)
    print("Prompt tokens: ", prompt_tokens)
    print("Response tokens: ", response_tokens)
else:
    print(response.text)
