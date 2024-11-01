from openai import OpenAI
from pathlib import Path

client = OpenAI()

# First Generating a MP3 file to use
speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy", # Available options: alloy, echo, fable, onyx, nova, and shimmer
  input="Today we are learning the OpenAI python APIs"
)

#response.stream_to_file(speech_file_path)
response.write_to_file(speech_file_path)

audio_file= open(speech_file_path, "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)
print(transcription.text)