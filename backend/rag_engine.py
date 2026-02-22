import os
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama

vector_store = None


def process_pdf(file_path):
    global vector_store

    # Load PDF
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    # Split text
    text_splitter = CharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    texts = text_splitter.split_documents(documents)

    # Create embeddings
    embeddings = OllamaEmbeddings(model="mistral")

    # Create FAISS vector store
    vector_store = FAISS.from_documents(texts, embeddings)

    return "PDF processed successfully."


def ask_question(question):
    global vector_store

    if vector_store is None:
        return "Please upload a PDF first."

    # Create LLM
    llm = Ollama(model="mistral")

    # Create RetrievalQA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vector_store.as_retriever()
    )

    # IMPORTANT FIX HERE
    result = qa_chain.invoke({"query": question})

    # Return proper result
    return result["result"]