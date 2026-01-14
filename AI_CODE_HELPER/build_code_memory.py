import json
import os
from sentence_transformers import SentenceTransformer
from langchain_community.vectorstores import FAISS

# Load code knowledge
with open("DATA/code_knowledge.json", "r", encoding="utf-8") as f:
    knowledge = json.load(f)

texts = []

# Convert functions to documents
for fn in knowledge.get("functions", {}).values():
    texts.append(
        f"""
FUNCTION: {fn.get('name','')}
FILE: {fn.get('file','')}
LINES: {fn.get('start_line','na')} - {fn.get('end_line','na')}
CODE:
{fn.get('code','')}
"""
    )

# Convert classes to documents
for cls in knowledge.get("classes", {}).values():
    texts.append(
        f"""
CLASS: {cls.get('name','')}
FILE: {cls.get('file','')}
LINES: {cls.get('start_line','na')} - {cls.get('end_line','na')}
CODE:
{cls.get('code','')}
"""
    )

print(f"loaded {len(texts)} code blocks")

# Load free local embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Wrap for LangChain
class LocalEmbeddings:
    def embed_documents(self, texts):
        return model.encode(texts).tolist()

    def embed_query(self, text):
        return model.encode([text])[0].tolist()

embeddings = LocalEmbeddings()

# Build FAISS
db = FAISS.from_texts(texts, embeddings)

# Save
os.makedirs("DATA/VECTOR_DB", exist_ok=True)
db.save_local("DATA/VECTOR_DB")

print("vector database built successfully")
