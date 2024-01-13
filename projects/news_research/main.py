from langchain.llms import GooglePalm
from langchain.vectorstores import FAISS

from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceInstructEmbeddings


import streamlit as st
import os

import time
from dotenv import load_dotenv

load_dotenv()   
local_store_path = 'faiss_index'
instructor_embeddings = HuggingFaceInstructEmbeddings()

llm = GooglePalm(google_api_key = os.environ["GOOGLE_API_KEY"], temperature = 0.7)

st.title('News Research Application 📰')

urls =[]

def load_vector_db():
    main_placeholder = st.empty()
    main_placeholder.text("Data Loading ....starting.... 💡⏱️⏱️")

    data = ""
    f1 = open('E:/mydocs/python/news_extract/files/news1.txt', "r")
    data = f1.read()

    f2 = open('E:/mydocs/python/news_extract/files/news2.txt', "r")
    data1 = f2.read()
    data = data + data1
        
    f3 = open('E:/mydocs/python/news_extract/files/news3.txt', "r")
    data2 = f2.read()
    data = data + data2

    main_placeholder.text("Data Loading ....Started.... 💡⏱️⏱️")

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    pages = text_splitter.split_text(data)

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)

    main_placeholder.text("Text Splitter ...Started.... ⏰⏰⏰⏰")
    docs = text_splitter.create_documents(pages)
    main_placeholder.text("Embedding Vector Started Building...✅✅✅")

    vectordb = FAISS.from_documents(documents=docs, embedding=instructor_embeddings)
    vectordb.save_local(local_store_path)

    time.sleep(2)
    main_placeholder.text("Embedding Completed ...✅✅✅")

def get_qa_chain():
    vector_db = FAISS.load_local(local_store_path, instructor_embeddings)
    retriever = vector_db.as_retriever(score_threshold = "0.7")
    prompt_template = """Given the following context and a question, generate an answer based on this context only.
    In the answer try to provide as much text as possible from "response" section in the source document context without making much changes.
    If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.

    CONTEXT: {context}

    QUESTION: {question}"""

    prompt = PromptTemplate(
        template = prompt_template,
        input_variables=["context", "question"]
    )
    chain = RetrievalQA.from_chain_type(
        llm =llm,
        chain_type="stuff",
        retriever=retriever,
        input_key="question",
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt}
    )
    return chain

if __name__ =='__main__':
    process_button_clicked = st.button('Load News article')
    if process_button_clicked:
        load_vector_db()
    question = st.text_input("Question: ")
    if question:
        chain= get_qa_chain()
        print("Chain recieved")
        response = chain({"question": question}, return_only_outputs=True)
        print(response)
        st.header("Answer")
        st.write(response["result"])
    

