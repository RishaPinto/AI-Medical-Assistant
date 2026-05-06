from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from groq import Groq

# SET API KEY
import os

api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)


# FASTAPI SETUP
app = FastAPI(title="AI Medical Assistant (Groq)")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MODEL
MODEL = "llama-3.1-8b-instant"

# REQUEST MODEL
class MedicalQuery(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "Groq AI Medical Assistant running"}

# MAIN ENDPOINT
@app.post("/ask")
def ask_medical(query: MedicalQuery):
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful medical assistant. Give safe, general advice. Always suggest consulting a doctor."
                },
                {
                    "role": "user",
                    "content": query.question
                }
            ],
            temperature=0.5
        )

        answer = response.choices[0].message.content

        return {
            "answer": answer,
            "disclaimer": "This is AI-generated information. Consult a doctor."
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))