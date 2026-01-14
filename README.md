# AI Code Helper (AST + RAG)

AI Code Helper is an AI-powered system that helps developers understand, explore, and modify large Python codebases.
It combines AST-based static analysis with RAG (Retrieval Augmented Generation) to provide both structural and semantic understanding of code.

## What this project does

### This system:

Scans a Python codebase

Extracts:

Functions

Classes

Variables

File names

Line numbers

Source code

Stores everything in a structured JSON knowledge file

Converts the extracted code into embeddings

Builds a vector database for semantic search

## Allows developers to:

Search for any function, class, or variable

See its file, line numbers, and full code

Ask AI questions about what a function does

Ask what to change when adding or modifying a feature

See which functions depend on each other

This helps developers work faster in unfamiliar or legacy codebases.

System Architecture

### The system has four main parts:

## Code Extractor (AST)

Parses Python source files

Builds code_knowledge.json with structured code data

Vector Memory Builder

Converts extracted code into text blocks

Creates embeddings

Stores them in a FAISS vector database

### AI Brain (RAG)

Searches relevant code from the vector database

Sends context to the LLM

Generates accurate, code-aware answers

Streamlit UI

Code explorer for functions, classes, and variables

Search by name

AI assistant for “how does this work?” and “what should I change?”

Folder structure


AI_CODE_HELPER/
│
├── SAMPLES/                     # Python code to analyze
├── DATA/
│   ├── code_knowledge.json      # Extracted AST data
│   └── VECTOR_DB/               # FAISS vector database (generated locally)
│
├── extract_code_knowledge.py
├── build_code_memory.py
├── ai_code_brain.py
└── app.py

Important note about VECTOR_DB

The DATA/VECTOR_DB folder is not included in this GitHub repository.

### It was intentionally deleted because:

It is a large binary file

GitHub blocks large files and repositories

It must be generated locally

You must run the build script to recreate it.

How to run the project

## Extract code:

python extract_code_knowledge.py


## Build vector database:

python build_code_memory.py


## Launch the UI:

streamlit run app.py


Open the browser URL shown by Streamlit.

Why this is useful

Most tools only show code.
## This system shows:

What code exists

Where it lives

What depends on what

What will break if you change something

What logic to modify when adding a new feature

It turns a large codebase into something you can talk to.
