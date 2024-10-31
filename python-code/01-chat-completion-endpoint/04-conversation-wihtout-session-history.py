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

# Looping for conversation
while True:
    # Defining a list to hold the questions
    messages = [
        {
                'role':'system',
                'content':'You are a helpful assistant'
        },
    ]
    # Getting the question from the user
    query = input('Enter quit() to exit\n\nUser:\n')

    if query != 'quit()':
        user_query = {
            'role': 'user',
            'content': query
        }
        # Add the User Query
        messages.append(user_query)
        # Invoking the LLM
        completion_response = client.chat.completions.create(
            model=model, # Setting the model
            messages=messages
        )
        # Printing the response from LLM
        print(f'\nLLM :\n{completion_response.choices[0].message.content}')

    else:
        break # Breaking the Loop

