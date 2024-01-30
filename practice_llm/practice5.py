from openai import OpenAI
from api_secrets import API_KEY
import time

client = OpenAI(api_key=API_KEY)



#create an assistant
assistant = client.beta.assistants.create(
    name="Math Tutor",
    instructions="You are a personal math tutor. Write and run code to answer math questions.",
    tools=[{"type": "code_interpreter"}],
    model="gpt-3.5-turbo-1106"
)

#create a thread
thread = client.beta.threads.create()

#put message on a thread
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
)

#send the thread to the assistant
run = client.beta.threads.runs.create(
  thread_id=thread.id,
  assistant_id=assistant.id,
  instructions="Please address the user as Jane Doe. The user has a premium account."
)

#retrieve the run
run = client.beta.threads.runs.retrieve(
  thread_id=thread.id,
  run_id=run.id
)

time.sleep(10)  # Adjust the sleep time as needed


#retrieve the messages
messages = client.beta.threads.messages.list(
  thread_id=thread.id
)

# Print the assistant's response
for message in messages.data:
    if message.role in ["system", "assistant"]:
        print(message.content)