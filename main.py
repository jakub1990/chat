import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai = OpenAI(api_key=api_key)
history= []

MAX_HISTORY = 100

def trim_history(history):
    return history[-MAX_HISTORY:]

def get_ai_response(prompt, history):
  system_msg = {"role": "system", "content": "You are a helpful assistant."}
  user_msg = {"role": "user", "content": prompt}
  completion = openai.chat.completions.create(
  model="gpt-4.1-nano",
  messages=[system_msg] + trim_history(history) + [user_msg],
  temperature= 1.0)
  
  return completion.choices[0].message.content

while True:
    prompt = input("Ask the question for AI ")
    if prompt == "quit":
        break

    answer = get_ai_response(prompt, history)

    history.append({
        "role": "user",
        "content": prompt
    })

    history.append({
        "role": "assistant",
        "content": answer
    })

    print("AI answer:", answer)
