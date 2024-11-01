from openai import OpenAI
import requests
from PIL import Image 
import os 

# Initializing OpenAI Client Object
client = OpenAI()

# As of date writing this code DALL-E 2 Only supports Editing
model = "dall-e-2"
user_prompt_for_image_edit = "A sunlit indoor lounge area with a pool containing a flamingo"

# As of the date writing this code, DALL-E 2 ONLY SUPPORTS PNG FILES OF LESS THAN 4MB
# Checking the current size of images
# Open Images
def check_image_details(image_file):
  with Image.open("02-text-to-image/supporting-images/image_edit_original.png") as img:
      # Get image size
      width, height = img.size
      # Get image resolution (DPI)
      dpi = img.info.get('dpi')
      # Get file size in MB
      file_size_in_bytes = os.path.getsize(image_file)
      file_size_in_mb = file_size_in_bytes / (1024*1024)
      
      print(f'Image width : {width} and Image heigth : {height}')
      print(f'Image Resolution : {dpi}')
      print(f'File Size: {file_size_in_mb}\n')

from PIL import Image

def is_png(file_path):
  try:
    with Image.open(file_path) as img:
      if img.format == 'PNG':
        # Usage
        print("The file is in PNG format.\n")
      else:
        print("The file is not in PNG format.\n")
        print(f'Format : {img.format}')
  except IOError:
    print('Could not open the File.\n')

def convert_webp_to_png(input_image_path, output_image_path):
  with Image.open(input_image_path) as img:
    img.save(output_image_path, 'PNG')

def convert_rgb_to_rgba(input_image_path, output_image_path):
  with Image.open(input_image_path) as img:
    # Convert image to RGBA
    rgba_img = img.convert("RGBA")
    
    # Optionally, you can add transparency by setting alpha to 0 for a specific color
    datas = rgba_img.getdata()
    new_data = []
    for item in datas:
      # Change all white (also consider black or any other color)
      if item[:3] == (255, 255, 255):
          new_data.append((255, 255, 255, 0))
      else:
          new_data.append(item)
  
    rgba_img.putdata(new_data)
    
    # Save the new image
    rgba_img.save(output_image_path)

# Usage

image_edit_original = "02-text-to-image/supporting-images/image_edit_original.png"
image_edit_mask = "02-text-to-image/supporting-images/image_edit_mask.png"


check_image_details(image_edit_original)
check_image_details(image_edit_mask)
is_png(image_edit_original)
is_png(image_edit_mask)
convert_webp_to_png(image_edit_original,image_edit_original)
convert_webp_to_png(image_edit_mask,image_edit_mask)
is_png(image_edit_original)
is_png(image_edit_mask)
convert_rgb_to_rgba(image_edit_original, image_edit_original)
convert_rgb_to_rgba(image_edit_mask,image_edit_mask)

response = client.images.edit(
  model=model,
  image=open(image_edit_original, "rb"),
  mask=open(image_edit_mask, "rb"),
  prompt=user_prompt_for_image_edit,
  n=1,
  size="1024x1024"
)

image_url = response.data[0].url
# Fetch the image from the URL
image_response = requests.get(image_url)
# Open a file in write-binary mode and save the image content
with open('02-text-to-image/generated-images/generated_image.png', 'wb') as file:
    file.write(image_response.content)
