import os
from fastapi import FastAPI
from pydantic import BaseModel
import anthropic

app = FastAPI(title="AI Chatbot")
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"status": "AI chatbot is running"}

@app.post("/chat")
def chat(req: ChatRequest):
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=500,
        messages=[{"role": "user", "content": req.message}],
    )
    return {"reply": response.content[0].text}