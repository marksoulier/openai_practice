from openai import OpenAI
from api_secrets import API_KEY
import time

client = OpenAI(api_key=API_KEY)

assistant_id = "asst_LCnRgE22XeXUFS7jxTioHVl9"

#create a thread
thread = client.beta.threads.create()

#put message on a thread
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="Who are you?"
)

#send the thread to the assistant
# Send the thread to the assistant
run = client.beta.threads.runs.create(
  thread_id=thread.id,
  assistant_id=assistant_id,
)

# Retrieve the run
run = client.beta.threads.runs.retrieve(
  thread_id=thread.id,
  run_id=run.id
)

# Wait for the response in a loop
response_received = False
while not response_received:
    time.sleep(2)  # Check every 5 seconds

    # Retrieve the messages
    messages = client.beta.threads.messages.list(
      thread_id=thread.id
    )

    if len(messages.data) > 1:  # Assuming the first message is the user's
        response_received = True

# Print the assistant's response
for msg in messages.data:
    # Check if the message content is of type 'text' and then print the value
    print(msg.content[0].text.value)