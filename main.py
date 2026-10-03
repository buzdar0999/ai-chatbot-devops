import logging
import os

import anthropic
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)
logger = logging.getLogger("chatbot")

MODEL = "claude-haiku-4-5-20251001"

app = FastAPI(title="AI Chatbot", version="1.1.0")
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=2000)


class ChatResponse(BaseModel):
    reply: str


@app.get("/")
def home():
    return {"status": "AI chatbot is running"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    logger.info("Chat request received (%d characters)", len(req.message))
    try:
        response = client.messages.create(
            model=MODEL,
            max_tokens=500,
            messages=[{"role": "user", "content": req.message}],
        )
    except anthropic.APIError as exc:
        logger.error("AI API error: %s", exc)
        raise HTTPException(status_code=502, detail="AI service error")
    return ChatResponse(reply=response.content[0].text)
