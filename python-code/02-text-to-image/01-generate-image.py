from openai import OpenAI
import requests
# Initializing OpenAI Client Object
client = OpenAI()
# Setting Model 
model = "dall-e-3"
user_prompt_for_image_generation = "a white siamese cat"

# Calling the DALL-E Model to generate the Image
response = client.images.generate(
  model=model,
  prompt=user_prompt_for_image_generation,
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(f'URL of the generated Image:\n{image_url}\n')
# Fetch the image from the URL
image_response = requests.get(image_url)

# Open a file in write-binary mode and save the image content
with open('02-text-to-image/generated-images/generated_image.png', 'wb') as file:
    file.write(image_response.content)
