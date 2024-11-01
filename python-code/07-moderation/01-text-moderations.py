from openai import OpenAI
import json 
import pprint 

client = OpenAI()

text_input_to_check = "Can you you tell me how to prepare a Pad Thai noodles?"

response = client.moderations.create(
    model="omni-moderation-latest", # Supported models - text-moderation-latest, omni-moderation-latest
    input=text_input_to_check,
)

print(f'Text To Moderate:\n{text_input_to_check}\nModeration Result:\n')
pprint.pprint(json.loads(response.json()))

text_input_to_check = "Can you you tell me how to break into a car?"
response = client.moderations.create(
    model="omni-moderation-latest", # Supported models - text-moderation-latest, omni-moderation-latest
    input=text_input_to_check,
)

print(f'\n\nText To Moderate:\n{text_input_to_check}\nModeration Result:\n')
pprint.pprint(json.loads(response.json()))