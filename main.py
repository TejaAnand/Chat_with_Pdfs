# 📄 Chat with Multiple PDFs using Gemini AI and LangChain (Colab-Compatible Version)

# Install dependencies in Google Colab:
# !pip install PyPDF2 langchain chromadb google-generativeai langchain-google-genai

# Install the version compatible with your requirements
!pip install "protobuf==5.29.4"

!pip install langchain-community

# 📦 Imports
import os
import PyPDF2
import google.generativeai as genai
from langchain.text_splitter import CharacterTextSplitter
from langchain.schema import Document
# Import Chroma from the correct location:
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain

# 🔑 Enter your API key here (Paste your free Gemini API key)
GEMINI_API_KEY = "PASTE_YOUR_API_KEY_HERE"
os.environ["GOOGLE_API_KEY"] = GEMINI_API_KEY
genai.configure(api_key=GEMINI_API_KEY)

# 📄 Read PDF and extract text
def read_pdf_text(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text

# 📤 Upload your PDFs
from google.colab import files
uploaded_files = files.upload()

raw_text = ""
for filename in uploaded_files.keys():
    with open(filename, 'rb') as file:
        raw_text += read_pdf_text(file)

# ✂️ Split text into chunks
text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=200)
texts = text_splitter.split_text(raw_text)

# 📚 Convert to Document objects
documents = [Document(page_content=text) for text in texts]

# 📊 Create Embeddings and Vector Store
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
vectorstore = Chroma.from_documents(documents, embedding=embeddings)

# 🧠 Ask a question
query = input("Ask a question based on your PDFs: ")

# 🔍 Search for similar documents
docs = vectorstore.similarity_search(query)

# 🤖 Set up Gemini LLM and QA Chain
llm = ChatGoogleGenerativeAI(model="gemini-pro")  # Gemini free tier is fine here
chain = load_qa_chain(llm, chain_type="stuff")

# 📝 Get the answer
response = chain.run(input_documents=docs, question=query)

# 📢 Print result
print("\n📘 Answer:")
print(response)