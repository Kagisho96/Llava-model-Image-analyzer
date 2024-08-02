"""
Orignal Author: DevTechBytes
https://www.youtube.com/@DevTechBytes
"""
from ollama import generate
from config import Config
from helpers.image_helper import get_image_bytes

system_prompt = Config.SYSTEM_PROMPT

def analyze_image_file( model, user_prompt):
    # gets image bytes using helper function
    image_bytes = get_image_bytes(image_file)

    # calls the llava model using Ollama SDK
    stream = generate(model=model, 
            prompt=user_prompt, 
            images=[image_bytes], 
            stream=True)

    return stream

# handles stream response back from LLM
def stream_parser(stream):
    for chunk in stream:
        yield chunk['response']

# """
# Orignal Author: DevTechBytes
# https://www.youtube.com/@DevTechBytes
# """
# from ollama import generate
# from config import Config

# system_prompt = Config.SYSTEM_PROMPT

# def ask_mistral(question, model):
#     # calls the Mistral model using Ollama SDK
#     stream = generate(model=model, 
#                       prompt=question, 
#                       stream=True)

#     return stream

# # handles stream response back from LLM
# def stream_parser(stream):
#     for chunk in stream:
#         yield chunk['response']

# def get_answer(question, model):
#     stream = ask_mistral(question, model)
#     answers = [answer for answer in stream_parser(stream)]
#     return answers[0]  # return the first answer