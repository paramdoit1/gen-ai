
import os
from langchain.llms import OpenAI

api_key=os.environ['OPENAI_API_KEY']
print(api_key)

llm = OpenAI(model_name = 'text-davinci-003',
              temperature = 0.9,
              max_tokens = 256)
text = "who is president of united states?"

print(llm(text))