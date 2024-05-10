from jinja2 import Template
import json
import dotenv
import os
from openai import OpenAI

dotenv.load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


data = json.load(open('docs/683.json', 'r'))
prompt_template_text = """
tell me a joke about this date and number
{{ bulletin.date }} ({{ bulletin.id }})
"""

args = {
    "bulletin": data
}

prompt_template = Template(prompt_template_text)
prompt = prompt_template.render(**args)

print(prompt)


# send the prompt to OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)
messages = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": prompt},

        ]
    }
]
# print(messages)
response = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=messages,
    max_tokens=300,
)

response_data = response.choices[0]
response_text = response_data.message.content
print(response_text)
