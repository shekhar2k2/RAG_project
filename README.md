# 📚 Document Question-Answering System (RAG)

> An intelligent Flask-based application that lets you upload documents and ask questions about their content using AI-powered natural language processing.

## 🌟 What Is This?

This is a **Retrieval-Augmented Generation (RAG)** system that allows you to:
- Upload your documents (PDFs, Word files, text files)
- Ask questions about the content in plain English
- Get accurate, AI-generated answers based on your documents

Think of it as having a smart assistant that reads your documents and answers questions about them instantly!

## 🎯 Key Features

- **📤 Easy Document Upload**: Support for multiple document formats
- **🤖 AI-Powered Answers**: Uses advanced language models (Google Gemini)
- **🔍 Smart Search**: Finds relevant information from your documents automatically
- **💬 Natural Language**: Ask questions like you're talking to a person
- **⚡ Fast Responses**: Quick processing and answer generation
- **🌐 Web Interface**: User-friendly web application

## 🏗️ System Architecture

<img src="adv_rag_git/image.png" width="820" height="166" alt="image" />

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

## 📁 Project Structure

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

## 🔧 Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Web Framework** | Flask | Handles HTTP requests and responses |
| **Document Processing** | PyPDF2, python-docx | Extracts text from various formats |
| **Text Chunking** | LangChain | Splits documents into searchable pieces |
| **Search Engine** | FAISS / ChromaDB | Vector-based document retrieval |
| **AI Model** | Google Gemini | Generates natural language answers |
| **Embeddings** | Sentence Transformers | Converts text to searchable vectors |

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Google Gemini API key

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd <project-folder>
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   # Create a .env file and add:
   GEMINI_API_KEY=your_api_key_here
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open in browser**
   ```
   http://localhost:5000
   ```

## 📖 Usage Guide

### Uploading Documents

1. Navigate to the home page
2. Click the "Upload" button
3. Select your document (PDF, DOCX, TXT)
4. Wait for processing confirmation

### Asking Questions

1. Type your question in the input box
2. Click "Ask" or press Enter
3. View the AI-generated answer
4. The system shows which parts of your document were used

## 🔑 API Endpoints

### 1. Upload Document
```http
POST /upload
Content-Type: multipart/form-data

Response: {
  "status": "success",
  "message": "Document processed successfully"
}
```

### 2. Ask Question
```http
POST /ask
Content-Type: application/json

Body: {
  "query": "What is the main topic of the document?"
}

Response: {
  "answer": "The main topic is...",
  "query": "What is the main topic of the document?"
}
```

## 🧩 Component Details

### **app.py** - Flask Web Application
The main server that handles user interactions, file uploads, and coordinates between different components.

### **ingest.py** - Document Ingestion
Responsible for:
- Reading uploaded files
- Extracting text content
- Breaking text into smaller chunks for better searchability

### **retriever.py** - Context Retrieval
Handles:
- Creating searchable indexes from document chunks
- Finding relevant sections based on user questions
- Returning context to the answer generator

### **generator_gemini.py** - Answer Generation
Uses Google's Gemini AI to:
- Analyze the retrieved context
- Generate accurate, human-like answers
- Format responses appropriately

## 🛠️ Configuration

Key settings you can adjust:

- **Chunk Size**: Modify text splitting in `ingest.py`
- **Model Selection**: Change AI model in `generator_gemini.py`
- **Upload Limits**: Adjust file size limits in `app.py`
- **Port**: Change Flask port in `app.py`

## 🔒 Security Considerations

- Store API keys in environment variables (never in code)
- Validate uploaded file types and sizes
- Implement user authentication for production use
- Use HTTPS in production environments
- Sanitize user inputs to prevent injection attacks

## 🐛 Troubleshooting

**Problem**: Upload fails
- **Solution**: Check file format and size limits

**Problem**: No answer generated
- **Solution**: Verify API key is correctly set

**Problem**: Slow responses
- **Solution**: Reduce chunk size or optimize retrieval settings

**Problem**: Installation errors
- **Solution**: Ensure Python version is 3.8+ and all dependencies are installed

## 📊 Performance Tips

1. **Optimize chunk size** for your document type
2. **Use GPU acceleration** if available
3. **Cache frequently asked questions**
4. **Implement pagination** for large documents
5. **Monitor API usage** to stay within limits

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Google Gemini for AI capabilities
- Flask community for excellent documentation
- LangChain for document processing tools
- Open-source contributors

## 📧 Contact & Support

For questions, issues, or suggestions:
- Open an issue on GitHub
- Email: your-email@example.com
- Documentation: [Link to detailed docs]

## 🗺️ Roadmap

- [ ] Support for more document formats (Excel, PPT)
- [ ] Multi-language support
- [ ] Conversation history
- [ ] Document comparison features
- [ ] Export answers to PDF
- [ ] Mobile application

---

**Made with ❤️ using AI and Python**

*Last Updated: October 2025*