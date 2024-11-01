from pathlib import Path
from openai import OpenAI

client = OpenAI()

# Setting a model
model = 'gpt-4o-mini'

completion_response = client.chat.completions.create(
    model=model, # Setting the model
    messages=[
        {
            'role':'system',
            'content':'You are a helpful language translater'
        },
        {
            'role':'user',
            'content':'Can you translate  "I want to learn AI and Python so badly" into Hindi. Please give the translated sentence as the answer.'
        }
    ]
)
# Printing the response from LLM
translated_answer = completion_response.choices[0].message.content
print(f'Response from the OpenAI LLM:\n\n{translated_answer}')

speech_file_path = Path(__file__).parent / "speech_translated_to_hindi.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy", # Available options: alloy, echo, fable, onyx, nova, and shimmer
  input=translated_answer
)

#response.stream_to_file(speech_file_path)
response.write_to_file(speech_file_path)