
import google.generativeai as palm
import os

palm.configure(api_key=os.environ['PALM_API_KEY'])

models = [model for model in palm.list_models()]

for model in models:
  print(model.name)

model_id="models/text-bison-001"
prompt='''write a cover letter for a data science job applicaton. 
Summarize it to two paragraphs of 50 words each. '''

completion=palm.generate_text(
    model=model_id,
    prompt=prompt,
    temperature=0.99,
    max_output_tokens=800,
)

print(completion.result)