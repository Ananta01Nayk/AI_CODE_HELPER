# AI Code Helper

AI Code Helper is an **AI-powered developer assistant** that analyzes Python codebases to help developers **find syntax errors, detect logical issues, understand code structure, and improve code quality**.

The system combines **static code analysis (AST)** with **LLM-based reasoning (RAG)** to provide accurate, explainable, and developer-friendly insights.

---

##  Features

-  **Code Structure Analysis**
  - Extracts functions, classes, and their source code
  - Builds function call and dependency relationships

-  **Syntax Error Detection**
  - Detects Python syntax errors with exact file and line number
  - Prevents invalid code from being analyzed further

-  **Logical Bug Detection (Static)**
  - Unused variables
  - Empty `except` blocks
  - Potential logical issues (non-hallucinated)

-  **AI-Powered Explanations (RAG)**
  - LLM explains detected issues using real code context
  - No guessing or hallucination
  - Suggests safe improvements

-  **Semantic Search with Vector DB**
  - Code, syntax errors, and logical issues are embedded together
  - Enables intelligent retrieval using FAISS

- **Streamlit UI**
  - Browse functions and classes
  - View syntax errors and potential issues
  - Ask AI questions about code and bugs

---

##  Project Architecture

```
Codebase
  ↓
Static Analysis (AST)
  ↓
code_knowledge.json   ← Source of Truth
  ↓
Vector Database (FAISS)
  ↓
RAG + LLM (Gemini)
  ↓
Developer Assistance (UI / IDE-ready)
```

---

## Project Structure

```
AI_CODE_HELPER/
│
├── SAMPLES/                  # Python files to analyze
│
├── DATA/
│   ├── code_knowledge.json   # Extracted code & issues (truth)
│   └── VECTOR_DB/            # FAISS vector index
│
├── extract_code_knowledge.py # Static analysis (AST + bugs)
├── build_code_memory.py      # Vector DB builder (code + issues)
├── ai_code_brain.py          # RAG + LLM logic
├── app.py                    # Streamlit UI
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

```bash
pip install -r requirements.txt
```

(Optional but recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

---

##  How to Run

###  Extract Code Knowledge
```bash
python extract_code_knowledge.py
```

### Build Vector Database
```bash
python build_code_memory.py
```

### Start the UI
```bash
streamlit run app.py
```

---

## How This Helps Developers

- Detects **real issues using deterministic logic**
- Uses AI to **explain**, not invent problems
- Helps understand **impact of changes**
- Improves productivity and code quality

---

## Design Philosophy

- **Static analysis detects issues**
- **JSON stores the truth**
- **Vector DB enables search**
- **LLM reasons over verified context**

This avoids hallucination and builds developer trust.

---

## Future Improvements

- VS Code Extension
- Auto-fix suggestions
- Severity scoring
- Test case generation
- CI/CD integration

---

##  Author

Ananta Nayak

---

##  Summary

> AI Code Helper is not just a chatbot — it is a **code-aware AI system** designed to help developers **find errors, understand code, and improve software quality**.
