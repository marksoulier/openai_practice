from openai import OpenAI
from pathlib import Path
from api_secrets import API_KEY
import time

client = OpenAI(api_key=API_KEY)

speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="I love Utah State University!"
)

response.stream_to_file(speech_file_path)