from itertools import chain
from webbrowser import get
from langchain_helper import get_few_short_db_chain
import streamlit as st

st.title('Charm T Shirts: Q and A   ')

question = st.text_input("Question: ")

if question:
    chain = get_few_short_db_chain()
    answer =chain.run(question)
    st.header("Answer: ")
    st.write(answer)