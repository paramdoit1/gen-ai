from langchain.llms import GooglePalm
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

import os
from dotenv import load_dotenv

load_dotenv()

local_store_path = 'faiss_index'
instructor_embeddings = HuggingFaceInstructEmbeddings()

llm = GooglePalm(google_api_key = os.environ["GOOGLE_API_KEY"], temperature = 0.7)

response = llm('How are you today?')
print(response)

def create_vector_db():
    loader = CSVLoader(file_path="codebasics_faqs.csv", source_column="prompt")
    data = loader.load()

    vectordb = FAISS.from_documents(documents=data, embedding=instructor_embeddings)
    vectordb.save_local(local_store_path)

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
        input_key="query",
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt}
    )
    return chain

if __name__ =='__main__':
    chain = get_qa_chain()
    print(chain("do you have course on botany?"))

