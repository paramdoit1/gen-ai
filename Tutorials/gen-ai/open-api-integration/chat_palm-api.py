
import google.generativeai as palm
import os

palm.configure(api_key=os.environ['PALM_API_KEY'])

model_id="models/text-bison-001"

response = palm.chat(messages='hi')
print(response.last)

userInput = ""

while True:
  userInput = input("reply: ")
  if userInput.upper() == 'Q':
    break
  response = response.reply(userInput)  
  print(response.last)