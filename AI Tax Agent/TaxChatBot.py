from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
  api_key= os.getenv("OPENAI_API_KEY")
)
query = input("Enter your tax query: ")
completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "You are a tax agent working at KMTaxService.com. Answer the following query: " + query},
  ]
)
response = completion.choices[0].message.content
print("Response from the AI Tax Agent:")
print(response)
#print("Full response object:")
#print(completion.choices[0].message); 

