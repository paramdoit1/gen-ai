
import os

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

api_key=os.environ['OPENAI_API_KEY']
print(api_key)

llm = OpenAI(model_name = 'text-davinci-003',
              temperature = 0.9,    
              max_tokens = 256)
prompt_template_cuisine = PromptTemplate(
    input_variables =['cuisine'],
    template = "I want to open a restaurant for {cuisine} food. Suggest me a name"
)

name_chain =  LLMChain(llm=llm, prompt = prompt_template_cuisine, output_key="restaurant_name")

prompt_template_food_item = PromptTemplate(
    input_variables =['restaurant_name'],
    template = "Suggest some Vegetarian menu items for  {restaurant_name}. Suggest me as list"
)

food_item_chain =  LLMChain(llm=llm, prompt = prompt_template_food_item, output_key="menu_items")

chain = SequentialChain(chains=[name_chain,food_item_chain],
                        input_variables = ['cuisine'],
                        output_variables = ['restaurant_name','menu_items']
                        )

response = chain({'cuisine':"Arabian"})

print(response)