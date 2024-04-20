#!/usr/bin/env python3

from gpt_generate import *
from text_pp import *
number_of_slide=5
user_text="British colonization"
user_message = f"I want you to come up with the idea for the PowerPoint. The number of slides is {number_of_slide}. " \
f"The content is: {user_text}.The title of content for each slide must be unique, " \

assistant_response = chat_development(user_message)
print(assistant_response)
slides_content = parse_response(assistant_response)
create_ppt(slides_content, 'bright_modern', user_text, 'Ray', 1)
draft=''
for slide in slides_content:
	draft+=write_script(str(slide),draft)


print('='*40)
print(draft)
#print(write_script('Slide 1: Introduction to Spanish Colonization \n Content: Brief overview of Spanish colonization, including its beginnings, key events, and impact on the Americas. '))