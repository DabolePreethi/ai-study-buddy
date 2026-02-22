from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import shutil
import os

from rag_engine import process_pdf, ask_question
from summarizer import summarize_text
from quiz_generator import generate_quiz
from flashcards import generate_flashcards

app = FastAPI()

# ----------------------------
# CORS Middleware (IMPORTANT)
# ----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (development)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------------
# Request Models
# ----------------------------

class QuestionRequest(BaseModel):
    question: str

class TextRequest(BaseModel):
    text: str


# ----------------------------
# Routes
# ----------------------------

@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    try:
        # Save uploaded file to disk
        file_path = f"temp_{file.filename}"

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Process PDF (create embeddings + FAISS index)
        process_pdf(file_path)

        return {"message": "PDF processed successfully"}

    except Exception as e:
        return {"error": str(e)}


@app.post("/ask/")
def ask(req: QuestionRequest):
    try:
        answer = ask_question(req.question)
        return {"answer": answer}
    except Exception as e:
        return {"error": str(e)}


@app.post("/summarize/")
def summarize(req: TextRequest):
    try:
        summary = summarize_text(req.text)
        return {"summary": summary}
    except Exception as e:
        return {"error": str(e)}


@app.post("/quiz/")
def quiz(req: TextRequest):
    try:
        quiz_data = generate_quiz(req.text)
        return {"quiz": quiz_data}
    except Exception as e:
        return {"error": str(e)}


@app.post("/flashcards/")
def flashcards(req: TextRequest):
    try:
        cards = generate_flashcards(req.text)
        return {"flashcards": cards}
    except Exception as e:
        return {"error": str(e)}