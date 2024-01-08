from langchain.embeddings import GooglePalmEmbeddings
from langchain.llms import GooglePalm
from langchain.utilities import  SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain_core.utils import get_from_env
from  langchain.embeddings import HuggingFaceEmbeddings    
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain.prompts import FewShotPromptTemplate
from langchain.vectorstores import Chroma
from langchain.chains.sql_database.prompt import   PROMPT_SUFFIX, _mysql_prompt
from langchain.prompts.prompt import PromptTemplate

import os
import few_shorts
def get_few_short_db_chain():
    google_api_key=os.getenv('PALM_API_KEY')

    db_user = "root"
    db_password = 'root'
    db_host = "localhost"
    db_name = "atliq_tshirts"

    db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}",
                                sample_rows_in_table_info=3)

    llm = GooglePalm(google_api_key=google_api_key)
    llm.temperature = 0.1

    embeddings = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')

    to_vectorize = [" ".join(example.values()) for example in few_shorts.few_shots]
    vectorstore = Chroma.from_texts(to_vectorize, embeddings, metadatas=few_shorts.few_shots)
    example_selector = SemanticSimilarityExampleSelector(
            vectorstore=vectorstore,
            k=2,
    )

    example_prompt = PromptTemplate(
            input_variables=["Question", "SQLQuery", "SQLResult","Answer",],
            template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}",
        )

    few_shot_prompt = FewShotPromptTemplate(
            example_selector=example_selector,
            example_prompt=example_prompt,
            prefix=_mysql_prompt,
            suffix=PROMPT_SUFFIX,
            input_variables=["input", "table_info", "top_k"], #These variables are used in the prefix and suffix
        )
    chain = SQLDatabaseChain.from_llm(llm, db, verbose=True, prompt=few_shot_prompt)
    return chain
    
if __name__ =='__main__':
    chain= get_few_short_db_chain()
    print(chain.run("How many white color Levi\'s  small shirt I have?"))