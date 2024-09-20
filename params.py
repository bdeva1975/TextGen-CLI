import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_text_response(model, input_content):
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )
    
    chat_completion = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": input_content,
            }
        ],
        max_tokens=2000,
        temperature=0,
        top_p=0.9,
    )
    
    return chat_completion.choices[0].message.content

# Use command-line arguments for model and input content
model = sys.argv[1]
input_content = sys.argv[2]

response = get_text_response(model, input_content)
print(response)