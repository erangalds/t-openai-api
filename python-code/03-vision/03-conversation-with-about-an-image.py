from openai import OpenAI
import base64
from PIL import Image

# Initializing a OpenAI client object
client = OpenAI()
## When we have an image with us, without hosted on a URL

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')
# convert and image to png
def convert_webp_to_png(input_image_path, output_image_path):
  with Image.open(input_image_path) as img:
    img.save(output_image_path, 'PNG')

# Path to your image
image_path = '02-text-to-image/supporting-images/sales-data-bsllabs-pvt-ltd.png'
convert_webp_to_png(image_path, image_path)
# Getting the base64 string
base64_image = encode_image(image_path)

model = 'gpt-4o-mini'
messages = [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What is in this image about?",
        },
        {
          "type": "image_url",
          "image_url": {
            "url":  f"data:image/jpeg;base64,{base64_image}",
            "detail": 'high'
          },
        },
      ],
    }
]
response = client.chat.completions.create(
  model=model,
  messages=messages,
)


print(f'Image About BSL Labs Sales Data was uploaded from our Computer.\n\nDescription of the Image:\n{response.choices[0].message.content}\n')
# Append the LLM Response to the messages list
messages.append(
  {
    'role': 'assistant',
    'content': response.choices[0].message.content
  }
)

while True:
  query = input(f'Do you want to know ask more question about this image? or Press quit() to stop\n\nUser:\n')
  if query != 'quit()':
    user_content = {
    'role':'user',
    'content': query
    }
    # Append the new user query
    messages.append(user_content)
    # Invoke LLM 
    response = client.chat.completions.create(
        model=model,
        messages=messages,
    )
    print(f'\nLLM: \n{response.choices[0].message.content}')
  else:
    break



