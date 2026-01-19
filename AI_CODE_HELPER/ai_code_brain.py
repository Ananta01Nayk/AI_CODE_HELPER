import os
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = SentenceTransformer("all-MiniLM-L6-v2")

class LocalEmbeddings:
    def embed_documents(self, texts):
        return model.encode(texts).tolist()

    def embed_query(self, text):
        return model.encode([text])[0].tolist()

    def __call__(self, text):
        return self.embed_query(text)

embeddings = LocalEmbeddings()

db = FAISS.load_local(
    folder_path="DATA/VECTOR_DB",
    embeddings=embeddings,
    allow_dangerous_deserialization=True
)

llm = ChatGoogleGenerativeAI(
    model="models/gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0
)

def ask_ai(question: str) -> str:
    docs = db.similarity_search(question, k=4)
    context = "\n\n".join(d.page_content for d in docs)

    prompt = f"""
You are a senior Python engineer.

Rules:
- Use ONLY provided context
- Mention function names
- Mention file names
- Mention line numbers
- Explain dependencies
- Mention syntax errors or bugs if present
- Explain whether issues are definite or potential
- Suggest safe improvements
- Never invent code

CODE CONTEXT:
{context}

QUESTION:
{question}
"""

    return llm.invoke(prompt).content
