import os
from openai import OpenAI
from dotenv import load_dotenv

import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

openai = OpenAI()

def get_ai_response(prompt: str) -> str:
  completion = openai.chat.completions.create(
  model="gpt-4.1-nano",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": prompt}],
   temperature= 1.0)
  
  return completion.choices[0].message.content

#fun_fact = get_ai_response("Give me funny fact about Poland")

#print(fun_fact)

while True:
  prompt = input("Ask the question for AI ")
  if input == "quit":
    break
  answer = get_ai_response(prompt)
  print("AI answer: ", answer)
  