from fastapi import FastAPI
from pydantic import BaseModel, Field

from tokenizer_service import analyze_tokens


# Create the Python AI Orchestrator HTTP application.
app = FastAPI(
    title="Trader AI Learning Service",
    version="1.0.0"
)


# Contract for the JSON request received from Spring Boot.
class TraderQuery(BaseModel):
    question: str = Field(min_length=1)


# Simple health endpoint to confirm the Python service is alive.
@app.get("/health")
def health():
    return {"status": "UP"}


# Spring Boot calls this endpoint with the trader's question.
@app.post("/ai/analyze")
def analyze_query(request: TraderQuery):
    # Extract the question and pass it to the tokenization logic.
    result = analyze_tokens(request.question)

    # FastAPI converts this dictionary to JSON.
    return result
