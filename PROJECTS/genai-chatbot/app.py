"""Minimal placeholder for the GenAI chatbot service.

Run with: `uvicorn app:app --reload` (after installing dependencies)
"""
from fastapi import FastAPI

app = FastAPI(title="GenAI Chatbot (placeholder)")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat")
def chat(message: dict):
    # Placeholder: replace with RAG + generator pipeline
    prompt = message.get("text", "")
    return {"reply": f"(stub) Echo: {prompt}"}
