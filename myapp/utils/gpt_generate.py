import os
#import openai
import ollama
#from dotenv import load_dotenv
from ollama import Client

#load_dotenv()
#openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_development(user_message):
    conversation = build_conversation(user_message)
    assistant_message = generate_assistant_message(conversation)
    
#   try:
#       assistant_message = generate_assistant_message(conversation)
#   except openai.error.RateLimitError as e:
#       assistant_message = "Rate limit exceeded. Sleeping for a bit..."

    return assistant_message


def build_conversation(user_message):
    return [
        {"role": "system",
         "content": "You are an assistant that gives the idea for PowerPoint presentations. When answering, give the user the summarized content for each slide based on the number of slide. And the format of the answer must be Slide X(the number of the slide): title of the content \n Content: content that clearly shows relevant information with no more than 50 words"},
        {"role": "user", "content": user_message}
    ]


def generate_assistant_message(conversation):
    client = Client(host='http://192.168.3.91:11434')
    response = client.chat(
        model="llama2",
        messages=conversation
    )
    return response['message']['content']

#
#user_message =  f"I want you to come up with the idea for the PowerPoint. The number of slides is 5. " \
#               f"The content is: Spanish colonization.The title of content for each slide must be unique, " \
#               f"and extract the most important keyword within two words for each slide. Summarize the content for each slide. "
#                       
#print(chat_development(user_message))
def write_script(slideinfo,draft=''):
    conversation = [
        {"role": "system",
         "content": "You are an assistant that write presentation drafts for PowerPoint presentations. The user will give you the outline for a set of slides, write a presentation draft regarding what can be talked about the given outline with specific content focused on each slide, make sure you write at least 150 words per slide, make it sound informative and professional."},
        {"role": "user", "content": slideinfo+"\nKeep in mind that you have already wrote "+draft+"in other slides and should not repeat the same thing too many times"}
    ]
    if draft=='':
        conversation = [
        {"role": "system",
         "content": "You are an assistant that write presentation drafts for PowerPoint presentations. The user will give you the outline for a set of slides, write a presentation draft regarding what can be talked about the given outline with specific content focused on each slide, make sure you write at least 150 words per slide, make it sound informative and professional."},
        {"role": "user", "content": slideinfo}
    ]
    
    return generate_assistant_message(conversation)
