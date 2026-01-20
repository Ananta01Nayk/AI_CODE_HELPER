# AI Code Helper (VS Code + RAG)

A **developer-focused AI Code Helper** that integrates a **RAG-powered Python engine** with a **VS Code extension** to answer questions about your own codebase — **without guessing or hallucination**.

---

## 📂 Project Structure

```
Day3/
├── AI_CODE_HELPER        # Python AI + RAG Engine (Brain)
└── ai-code-helper        # VS Code Extension (UI)
```

---

## 🧠 AI_CODE_HELPER (Python – RAG Brain)

- AST-based code analysis
- Extracts functions, classes, call graph, errors, bugs
- Builds FAISS vector database
- Uses RAG with Gemini (temperature = 0)

Key files:
```
extractor.py
rag_index.py
ai_code_brain.py
ask_cli.py
DATA/
venv/
```

---

## 🧩 ai-code-helper (VS Code Extension)

- Chat-style UI
- Multiple questions supported
- Calls Python RAG using venv Python
- Shows answers inside VS Code

Key files:
```
src/extension.ts
package.json
esbuild.js
```

---

## 🔁 End-to-End Flow

```
VS Code
 → Ask Question
 → Extension (TypeScript)
 → rag_query.py
 → ask_ai() [RAG]
 → FAISS Search
 → Gemini LLM
 → Answer in VS Code
```

---

## ▶️ How to Run

```bash
python extractor.py
python rag_index.py
npm run watch
```

Press **F5** → Open Chat → Ask questions

---

## 📌 Status

- Code Analyzer: ✅
- Vector DB: ✅
- RAG Pipeline: ✅
- VS Code Chat UI: ✅

---
