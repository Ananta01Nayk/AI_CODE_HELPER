import os
from dotenv import load_dotenv
load_dotenv()

from sentence_transformers import SentenceTransformer
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI

# -----------------------------
# Local embedding model (NO API)
# -----------------------------
model = SentenceTransformer("all-MiniLM-L6-v2")

class LocalEmbeddings:
    def embed_documents(self, texts):
        return model.encode(texts).tolist()

    def embed_query(self, text):
        return model.encode([text])[0].tolist()

    def __call__(self, text):
        return self.embed_query(text)

embeddings = LocalEmbeddings()

# -----------------------------
# Load vector database
# -----------------------------
DB_PATH = "DATA/VECTOR_DB"

if not os.path.exists(DB_PATH):
    raise RuntimeError("VECTOR_DB not found. Run build_code_memory.py first.")

db = FAISS.load_local(DB_PATH, embeddings, allow_dangerous_deserialization=True)

# -----------------------------
# Gemini LLM 
llm = ChatGoogleGenerativeAI(
    model="models/gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0
)
# -----------------------------
# RAG System
# -----------------------------
def ask_ai(question):
    # Perform similarity search
    docs = db.similarity_search(question, k=4)
    
    # Combine context from retrieved documents
    context = "\n\n".join([d.page_content for d in docs])

    prompt = f"""
You are a senior software engineer.

Rules:
• Always mention function names
• Always mention file names
• Always mention line numbers
• Explain dependencies
• Explain impact of changes
• Never invent code

CODE CONTEXT:
{context}

QUESTION:
{question}

Answer in a clear structured way.
"""
    try:
        response = llm.invoke(prompt)
        return response.content
    except Exception as e:
        return f"Error: {str(e)}"