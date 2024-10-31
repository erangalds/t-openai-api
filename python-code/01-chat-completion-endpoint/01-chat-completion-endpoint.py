import os
from openai import OpenAI 

# Creating a OpenAI Instance
client = OpenAI()

# If Environment Variables are not set on OS
# if the ENV variables are in .env file then uncomment below two lines
# If the environment variables are set then no need
#from dotenv import load_dotenv
#load_dotenv()
#client.openai_apikey = os.getenv('OPENAI_API_KEY')

# Setting a model
model = 'gpt-4o-mini'

completion_response = client.chat.completions.create(
    model=model, # Setting the model
    messages=[
        {
            'role':'system',
            'content':'You are a helpful assistant'
        },
        {
            'role':'user',
            'content':'Write a poem about python programming'
        }
    ]
)
# Printing the response from LLM
print(f'Response from the OpenAI LLM:\n\n{completion_response.choices[0].message.content}')



