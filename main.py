!pip install "protobuf==5.29.4"

!pip install langchain-community

import os
import PyPDF2
import google.generativeai as genai
from langchain.text_splitter import CharacterTextSplitter
from langchain.schema import Document
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain

GEMINI_API_KEY = "PASTE_YOUR_API_KEY_HERE"
os.environ["GOOGLE_API_KEY"] = GEMINI_API_KEY
genai.configure(api_key=GEMINI_API_KEY)

def read_pdf_text(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text

from google.colab import files
uploaded_files = files.upload()

raw_text = ""
for filename in uploaded_files.keys():
    with open(filename, 'rb') as file:
        raw_text += read_pdf_text(file)

text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=200)
texts = text_splitter.split_text(raw_text)

documents = [Document(page_content=text) for text in texts]

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
vectorstore = Chroma.from_documents(documents, embedding=embeddings)

query = input("Ask a question based on your PDFs: ")

docs = vectorstore.similarity_search(query)

llm = ChatGoogleGenerativeAI(model="gemini-pro")
chain = load_qa_chain(llm, chain_type="stuff")

response = chain.run(input_documents=docs, question=query)

print("\n📘 Answer:")
print(response)
