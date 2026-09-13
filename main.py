from fastapi import FastAPI
from pydantic import BaseModel

from app.agent import ask_agent

app = FastAPI(
    title="Grmini-AI-Agent-API",
    version = "0.1"
)

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

@app.get("/")
def root():
    return{
        "message": "Gemini Agent API is running!"
    }

@app.post("/api/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    answer = ask_agent(request.message)

    return {
        "response": answer
    }
    