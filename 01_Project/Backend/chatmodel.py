import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask(query,model='llama-3.1-8b-instant',temperature=0.2):
   sysPrompt='You are friendly AI expert solve the user query in a concise way'
   chat_completion = client.chat.completions.create(
    messages=[
       {"role": "system","content": sysPrompt},
       {"role": "user","content": query}
       ],
    max_tokens=100,
    model=model,
    temperature=temperature,      # (0-0.3 makes model more deterministic) & (0.7 to 1 model more random and creative)
    )
   response=chat_completion.choices[0].message.content

   return response