"example of streaming a conversation with the model"

from openai import OpenAI

client = OpenAI(api_key="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")
for i in range(1000):
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[{"role": "user", "content": "Tell me a story"}],
        stream=True,
    )
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")