"""
DevTechBytes
https://www.youtube.com/@DevTechBytes
"""

class Config:
    PAGE_TITLE = "Image and Text Analyzer"

    OLLAMA_MODELS = (
        'llava:13b', 
        'llava:34b', 
        'bakllava',
        'mistral:instruct'
        )

    SYSTEM_PROMPT = f"""You are a helpful chatbot that has access to the following 
                    open-source vision models {OLLAMA_MODELS}.
                    You can can answer questions about images."""
    