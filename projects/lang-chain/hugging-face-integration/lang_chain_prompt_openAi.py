
import os
from re import template
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

api_key=os.environ['OPENAI_API_KEY']
print(api_key)

llm = OpenAI(model_name = 'text-davinci-003',
              temperature = 0.9,    
              max_tokens = 256)
prompt_template = PromptTemplate(
    input_variables =['cuisine'],
    template = "I want to open a restaurant for {cuisine} food. Suggest me a name"
)

chain =  LLMChain(llm=llm, prompt = prompt_template)
chain.run("Indian")

