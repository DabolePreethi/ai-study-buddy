from langchain_community.llms import Ollama

def summarize_text(text):
    llm = Ollama(model="mistral")

    prompt = f"""
Summarize the following text clearly and concisely:

{text}
"""

    response = llm.invoke(prompt)
    return response