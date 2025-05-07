<p align="center">
  <img src="https://your-banner-url.com/banner.png" alt="Chat with Your PDFs - Banner" style="width:80%;"/>
</p>

<h1 align="center">🤖 Chat with Your PDFs</h1>

<p align="center">
  AI-Powered PDF Question Answering System using Google Gemini + LangChain
</p>

<p align="center">
  <a href="https://colab.research.google.com/">
    <img alt="Colab Ready" src="https://img.shields.io/badge/Open%20in-Google%20Colab-orange?logo=googlecolab">
  </a>
  <a href="https://github.com/TejaAnand/pdf-chat-gemini/blob/main/LICENSE">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-blue.svg" />
  </a>
  <img alt="Repo Size" src="https://img.shields.io/github/repo-size/TejaAnand/pdf-chat-gemini" />
  <img alt="Last Commit" src="https://img.shields.io/github/last-commit/TejaAnand/pdf-chat-gemini" />
  <img alt="Stars" src="https://img.shields.io/github/stars/TejaAnand/pdf-chat-gemini?style=social" />
</p>

---
# 🤖 Chat with Your PDFs - AI-Powered Document Question Answering System

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

