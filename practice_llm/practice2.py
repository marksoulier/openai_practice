"example of streaming a conversation with the model"

from openai import OpenAI
from api_secrets import API_KEY
client = OpenAI(api_key=API_KEY)

for i in range(1000):
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[{"role": "user", "content": "Tell me a story"}],
        stream=True,
    )
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")