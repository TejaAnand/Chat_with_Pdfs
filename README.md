<p align="center">
  <img src="" alt="Chat with PDF Workflow" width="80%">
</p>

# ✨ Chat with Your PDFs - AI-Powered Document Question Answering System

The **Chat with Your PDFs** project is an intelligent Colab-based tool that lets you interact with the contents of multiple PDFs using AI. Powered by **Google Gemini** and **LangChain**, this tool allows you to ask natural language questions about your uploaded files and receive relevant, AI-generated answers instantly!

---

It uses:
- ✂️ Smart text splitting for large PDF content
- 🧠 Semantic embedding with Google Gemini Embeddings
- 🔍 ChromaDB for vector-based similarity search
- 💬 Natural language understanding with Gemini (free tier)
- ⚙️ Simple Python code in a Google Colab notebook

---

## ⚡ Features

- Upload and process **multiple PDFs**  
- Ask questions like:  
  - "What is the summary of this file?"  
  - "List the main points in this document"  
  - "What does the second chapter talk about?"  
- AI pulls the most relevant chunks from your content  
- Answers delivered in real-time using Gemini AI  
- No installation needed — just run in Google Colab!

---

## 🧰 Hardware Requirements

- ✅ Google Colab or any browser  
- ✅ Gemini API key (free from [Google AI Studio](https://aistudio.google.com/app/apikey))

---

## 💻 Software Requirements

- Python 3  
- Required libraries listed in `requirements.txt`:
  - PyPDF2  
  - langchain  
  - chromadb  
  - google-generativeai  
  - langchain-google-genai

---

## 🔧 How to Run (Google Colab)

1. Open `app.py` in Google Colab  
2. Install dependencies with:  
   ```python
   !pip install -r requirements.txt

