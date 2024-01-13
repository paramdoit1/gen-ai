
import os
from langchain.llms import HuggingFaceHub

api_key=os.environ['HUGGINGFACEHUB_API_TOKEN']
print(api_key)

llm_hf = HuggingFaceHub(
    repo_id = "google/flan-t5-xl",
    model_kwargs ={"temperature" : 0.9} 
)
text = "who is president of united states?"

print(llm_hf(text))