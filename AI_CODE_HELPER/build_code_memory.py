import json
import os
from sentence_transformers import SentenceTransformer
from langchain_community.vectorstores import FAISS

# LOAD CODE KNOWLEDGE

with open("DATA/code_knowledge.json", encoding="utf8") as f:
    knowledge = json.load(f)

texts = []

# CODE DOCUMENTS

for fn in knowledge.get("functions", {}).values():
    texts.append(
        f"""
TYPE: FUNCTION
NAME: {fn['name']}
FILE: {fn['file']}
LINES: {fn['start']} - {fn['end']}

CODE:
{fn['code']}
"""
    )

# CODE DOCUMENTS

for cls in knowledge.get("classes", {}).values():
    texts.append(
        f"""
TYPE: CLASS
NAME: {cls['name']}
FILE: {cls['file']}
LINES: {cls['start']} - {cls['end']}

CODE:
{cls['code']}
"""
    )

# SYNTAX ERROR DOCUMENTS

for err in knowledge.get("syntax_errors", []):
    texts.append(
        f"""
TYPE: SYNTAX_ERROR
FILE: {err['file']}
LINE: {err['line']}
MESSAGE: {err['message']}

IMPACT:
This syntax error prevents Python from parsing this file.
"""
    )

# LOGICAL BUG DOCUMENTS

for bug in knowledge.get("logical_bugs", []):
    texts.append(
        f"""
TYPE: LOGICAL_BUG
BUG: {bug['type']}
NAME: {bug.get('name', 'N/A')}
FILE: {bug['file']}

NOTE:
This is a statically detected potential issue.
It may or may not be an actual bug depending on intent.
"""
    )

# SAFETY CHECK

if not texts:
    raise RuntimeError("No documents found to embed. Run extract_code_knowledge.py first.")

print(f"Loaded {len(texts)} total documents (code + issues)")

# EMBEDDING MODEL

model = SentenceTransformer("all-MiniLM-L6-v2")

class LocalEmbeddings:
    def embed_documents(self, texts):
        return model.encode(texts).tolist()

    def embed_query(self, text):
        return model.encode([text])[0].tolist()

    # REQUIRED BY FAISS
    def __call__(self, text):
        return self.embed_query(text)

embeddings = LocalEmbeddings()

# BUILD FAISS VECTOR DB

db = FAISS.from_texts(
    texts=texts,
    embedding=embeddings
)

# SAVE VECTOR DB

os.makedirs("DATA/VECTOR_DB", exist_ok=True)
db.save_local("DATA/VECTOR_DB")

print(" Code memory vector DB built successfully")
