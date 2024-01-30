from openai import OpenAI
from api_secrets import API_KEY
client = OpenAI(api_key=API_KEY)

request = "Can you give me 3 recipies for dinner that are easy to make and are healthy, about 10 min long and no preferences just suporise me?"

#read in txt file and store in variable
with open('chef.txt', 'r') as file:
    kitchen_aid = file.read()

while True:
  completion = client.chat.completions.create(
    model="gpt-3",
    messages=[
      {"role": "system", "content": "You are a kitchen aid. Your role is to take the users request and analize it with the perspective of how you can help them choose a meal that is correct. If they dont provide the following info, ask for it for a better analysis: time to make the meal, who are they making it for, is it breakfast, lunch, or dinner. Are they trying to avoid any foods"},
      {"role": "system", "content": kitchen_aid},
      {"role": "user", "content": request}
    ]
  )

  print(completion.choices[0].message.content)