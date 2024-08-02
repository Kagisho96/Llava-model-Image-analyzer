# """
# DevTechBytes
# https://www.youtube.com/@DevTechBytes
# """

# class Config:
#     PAGE_TITLE = "LLava Image Analyzer"

#     OLLAMA_MODELS = (
#         'llava:13b', 
#         'llava:34b', 
#         'bakllava',
#         'mistral:instruct'
#         )

#     SYSTEM_PROMPT = f"""You are a helpful chatbot that has access to the following 
#                     open-source vision models {OLLAMA_MODELS}.
#                     You can can answer questions about images."""
    
class Config:
    PAGE_TITLE = "LLava Image Analyzer"

    OLLAMA_MODELS = (
        'llava:13b', 
        'llava:34b', 
        'bakllava',
        'mistral:instruct'
    )

    SYSTEM_PROMPT = f"""You are a helpful chatbot that has access to the following 
                        open-source vision models {OLLAMA_MODELS}.
                        You can answer questions about images."""

# Assuming 'mistral:instruct' is the model to be used for answering the questions
prompt = Config.SYSTEM_PROMPT.replace('{OLLAMA_MODELS}', 'mistral:instruct')
prompt += f"\n\n{original_author_info}"