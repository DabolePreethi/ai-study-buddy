# ai-study-buddy
AI Study Buddy is an AI-powered learning assistant that turns study materials into an interactive experience. Upload PDFs to get instant doubt solving, smart summaries, quizzes, and flashcards. Using advanced AI with Retrieval-Augmented Generation, it provides accurate, context-aware answers and adapts to your learning pace for personalized study.

🚀 Features
    📂 Upload and process PDFs
    💬 Ask questions from document content
    📑 Automatic summarization
    📝 AI-generated quizzes
    🗂 Flashcard generation
    ⚡ FastAPI backend with LangChain & FAISS

🧠 How It Works
  Extracts text from uploaded PDFs
  Splits content into chunks
  Generates embeddings and stores them in FAISS
  Retrieves relevant context for user queries
  Uses LLM to generate accurate, contextual responses

🛠 Tech Stack
  Python, FastAPI
  LangChain
  FAISS (Vector Database)
  OpenAI / GPT Models
  HTML, CSS, JavaScript

⚙️ Installation
git clone https://github.com/your-username/ai-study-buddy.git
cd ai-study-buddy
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
uvicorn main:app --reload

Add your OpenAI API key in a .env file:
OPENAI_API_KEY=your_api_key

🎯 Use Cases
Exam preparation
Concept revision
Research paper understanding
Self-paced learning
