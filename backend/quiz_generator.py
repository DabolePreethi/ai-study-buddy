from langchain_community.llms import Ollama

def generate_quiz(text):
    llm = Ollama(model="mistral")

    prompt = f"""
Generate 5 multiple choice questions from the following text.
Each question should have 4 options and indicate the correct answer.

{text}
"""

    response = llm.invoke(prompt)
    return response