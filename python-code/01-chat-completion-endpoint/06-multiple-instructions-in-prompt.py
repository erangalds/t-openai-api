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
# Defining a list to hold the questions
system_prompt_instructions = [
    'You are an experienced data scientist',
    'You need to clearly look at the requirements given by the user',
    'You need to give the output in markdown format',    
]

user_prompt_instructions = [
   'You are working on a project to improve image search capabilities for an e-commerce platform.',
   'We are expecting to use Python for backend development.',
   'We need to evaluate Postgresql, and Mongodb as two options for the backend database.'
   'Your task is to explore how vector databases each can enhance the accuracy and speed of similarity searches.'
   'Give your recommendations about each one separately.'
   'Finally provide our final recommendation.'
]

print(f'System Instructions:\n{system_prompt_instructions}\nNumber of Instructions: {len(system_prompt_instructions)}')
print(f'User Instructions:\n{user_prompt_instructions}\nNumber of Instructions: {len(user_prompt_instructions)}')
# We need to convert the multiple instructions into LLM acceptable format. 
# For format is shown below. 
# message = [
#     {
#       "role": "system",
#       "content": [
#         {
#           "type": "text",
#           "text": `
#             You are a helpful assistant that answers programming questions 
#             in the style of a southern belle from the southeast United States.
#           `
#         }
#       ]
#     },
#     {
#       "role": "user",
#       "content": [
#         {
#           "type": "text",
#           "text": "Are semicolons optional in JavaScript?"
#         }
#       ]
#     }
# ]

def convert_multiple_instructions_to_content_list(multiple_instructions):
    """
    This Function converts the multiple instructions in the list to 
    LLM Acceptable list format
    """
    content = list() # Define Empty list 
    for instruction in multiple_instructions:
        content.append(
            {
                'type': 'text',
                'text': instruction
            }
        )
    return content

system_content = convert_multiple_instructions_to_content_list(system_prompt_instructions)
user_content = convert_multiple_instructions_to_content_list(user_prompt_instructions)

print(f'Generated System Content:\n{system_content}\n')
print(f'Generated User Content:\n{user_content}')
# Adding the system content and user content to the final messages list
messages = [
    {
        'role':'system',
        'content': system_content
    },
    {
        'role': 'user',
        'content': user_content
    }
]
# Invoking the LLM
completion_response = client.chat.completions.create(
    model=model, # Setting the model
    messages=messages
)
#Adding the LLM Answer as well. 
assistant_resoponse = completion_response.choices[0].message.content
print(f'\nFinal Analysis Report from LLM:\n{assistant_resoponse}')
