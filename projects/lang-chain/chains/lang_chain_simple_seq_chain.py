
import os
from re import template
import re
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain

api_key=os.environ['OPENAI_API_KEY']
print(api_key)

llm = OpenAI(model_name = 'text-davinci-003',
              temperature = 0.9,    
              max_tokens = 256)
prompt_template_cuisine = PromptTemplate(
    input_variables =['cuisine'],
    template = "I want to open a restaurant for {cuisine} food. Suggest me a name"
)

#prompt_template.format(cuisine = "Indian")

name_chain =  LLMChain(llm=llm, prompt = prompt_template_cuisine)

prompt_template_food_item = PromptTemplate(
    input_variables =['restaurant_name'],
    template = "Suggest some Vegetarian menu items for  {restaurant_name}. Suggest me as list"
)

#prompt_template.format(cuisine = "Indian")

food_item_chain =  LLMChain(llm=llm, prompt = prompt_template_food_item)

chain = SimpleSequentialChain(chains=[name_chain,food_item_chain ])

response = chain.run("Mexican")

print(response)