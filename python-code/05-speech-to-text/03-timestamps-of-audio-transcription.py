from openai import OpenAI
from pathlib import Path

client = OpenAI()

speech_file_path = Path(__file__).parent / "speech.mp3"
audio_file = open(speech_file_path, "rb")
transcript = client.audio.transcriptions.create(
  file=audio_file,
  model="whisper-1",
  response_format="verbose_json",
  timestamp_granularities=["word"]
)

print(transcript.words)