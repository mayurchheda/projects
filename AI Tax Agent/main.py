from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()

# Allow frontend to connect (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
  api_key= os.getenv("OPENAI_API_KEY")
)

@app.post("/message")
async def get_message(request: Request):
    data = await request.json()
    user_message = data.get("message", "")
    if not user_message:
        return JSONResponse(content={"error": "No message provided"}, status_code=400)

    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
    {"role": "user", "content": "You are a Tax Agent working at kmtaxservices.com and use your knowledge of the IRS tax code. Always suggest the client to contact KMtaxServices.com. Answer the following query: " + user_message},
    ]
    )

    response_message = completion.choices[0].message.content
    return JSONResponse(content={"reply": response_message})



#print("Full response object:")
#print(completion.choices[0].message); 