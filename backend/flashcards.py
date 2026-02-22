from langchain_community.llms import Ollama

def generate_flashcards(text):
    llm = Ollama(model="mistral")

    prompt = f"""
Generate flashcards (Question and Answer format) from the following text:

{text}
"""

    response = llm.invoke(prompt)
    return response