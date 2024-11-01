from openai import OpenAI
from pathlib import Path

client = OpenAI()

speech_file_path = Path(__file__).parent / "speech_translated_to_hindi.mp3"
audio_file= open(speech_file_path, "rb")
translation = client.audio.translations.create(
  model="whisper-1", 
  file=audio_file
)
print(translation.text)