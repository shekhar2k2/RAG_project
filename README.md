# Document Question-Answering System (RAG)

> An intelligent Flask-based application that lets you upload documents and ask questions about their content using AI-powered natural language processing.

## What Is This?

This is a **Retrieval-Augmented Generation (RAG)** system that allows you to:
- Upload your documents (PDFs, Word files, text files)
- Ask questions about the content in plain English
- Get accurate, AI-generated answers based on your documents

Think of it as having a smart assistant that reads your documents and answers questions about them instantly!

## Key Features

- ** Easy Document Upload**: Support for multiple document formats
- ** AI-Powered Answers**: Uses advanced language models (Google Gemini)
- ** Smart Search**: Finds relevant information from your documents automatically
- ** Natural Language**: Ask questions like you're talking to a person
- ** Fast Responses**: Quick processing and answer generation
- ** Web Interface**: User-friendly web application

## System Architecture

![Alt text](https://github.com/shekhar2k2/RAG_project/blob/main/image.png)

### How It Works:

1. **Upload Phase** (`/upload` endpoint)
   - User uploads a document through the web interface
   - System extracts text from the document
   - Text is broken into smaller, manageable chunks

2. **Question Phase** (`/ask` endpoint)
   - User asks a question
   - System searches through document chunks
   - Relevant information is retrieved

3. **Answer Phase**
   - AI Generator creates a comprehensive answer
   - Response is sent back to the user in JSON format

## Project Structure

```
project/
│
├── app.py                    # Main Flask application (Web server)
├── ingest.py                 # Document processing (Extract & chunk text)
├── retriever.py              # Search engine (Index & retrieve context)
├── generator_gemini.py       # AI answer generator (Google Gemini)
│
├── requirements.txt          # Python dependencies
├── README.md                 # This file
│
└── uploads/                  # Uploaded documents storage (auto-created)
```

## Technology

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Web Framework** | Flask | Handles HTTP requests and responses |
| **Document Processing** | PyMuPDF, python-docx | Extracts text from various formats |
| **Text Chunking** | LangChain | Splits documents into searchable pieces |
| **Search Engine** | FAISS / ChromaDB | Vector-based document retrieval |
| **AI Model** | Google Gemini | Generates natural language answers |
| **Embeddings** | Sentence Transformers | Converts text to searchable vectors |


