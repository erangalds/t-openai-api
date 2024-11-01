from openai import OpenAI
import base64
from PIL import Image

client = OpenAI()
# There we are using an Image hosted on a URL
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What’s in this image?"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

print(f'Image Hosted on a URL.\n\nDescription of the Image:\n{response.choices[0].message.content}\n')

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
image_path = '02-text-to-image/supporting-images/image_variation_original.png'
convert_webp_to_png(image_path, image_path)
# Getting the base64 string
base64_image = encode_image(image_path)

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What is in this image?",
        },
        {
          "type": "image_url",
          "image_url": {
            "url":  f"data:image/jpeg;base64,{base64_image}"
          },
        },
      ],
    }
  ],
)


print(f'Image Uploaded from our Computer.\n\nDescription of the Image:\n{response.choices[0].message.content}\n')