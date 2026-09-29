# Lab 01 — Tokenization & Token Counting for Trader AI

## Overview

This lab implements the first AI preprocessing layer of an enterprise financial trading assistant.

A trader submits a natural-language market or portfolio-risk question through a Spring Boot REST API. The request is forwarded to a Python FastAPI service, where the text is tokenized and analyzed.

This lab focuses on understanding how raw financial-domain text is transformed into tokens and token IDs before downstream AI processing.

---

## Financial Trading Use Case

Example trader question:

> What are today's major portfolio risks?

The system analyzes the question and returns:

- Character count
- Word count
- Token count
- Token pieces
- Token IDs

### Request Flow

```text
Trader
   ↓
Spring Boot REST API
   ↓
Python FastAPI Service
   ↓
Hugging Face Tokenizer
   ↓
Tokenization Analysis
   ↓
Spring Boot
   ↓
Trader
```

---

## Concepts Implemented

- Tokenization
- Tokens
- Token IDs
- Token counting
- Character counting
- Word counting
- Subword tokenization
- Tokenizer vocabulary lookup
- Java-to-Python REST integration

> **Lab 01 Scope:** This lab implements preprocessing and tokenization only.  
> No LLM inference or generative model is executed in Lab 01.

---

## Technology Stack

| Layer | Technology |
|---|---|
| Client / Trader | PowerShell REST Client |
| Enterprise API | Java 17 + Spring Boot |
| AI Service | Python + FastAPI |
| Tokenization | Hugging Face Transformers |
| Service Integration | REST / JSON |
| Java Build | Maven |
| Python Server | Uvicorn |

---

## Technical Flow

```text
Trader
   │
   │ POST /api/trader/query
   ▼
Spring Boot API :8080
   │
   │ REST / JSON
   ▼
Python FastAPI :8000
   │
   ▼
Hugging Face Tokenizer
   │
   ├── Character Count
   ├── Word Count
   ├── Tokenization
   ├── Token IDs
   └── Token Count
   │
   ▼
JSON Response
   │
   ▼
Spring Boot API
   │
   ▼
Trader
```

---

## Project Structure

```text
lab-01-tokenization/
│
├── README.md
│
├── ai-service/
│   ├── app.py
│   ├── tokenizer_service.py
│   └── requirements.txt
│
├── spring-api/
│   ├── pom.xml
│   └── src/
│       └── main/
│           ├── java/
│           │   └── com/trader/api/
│           │       ├── controller/
│           │       ├── model/
│           │       ├── service/
│           │       └── TraderApiApplication.java
│           │
│           └── resources/
│               └── application.yml
│
└── docs/
    └── Lab01_Architecture_Diagrams.pdf
```

---

## Spring Boot ↔ Python Integration

Spring Boot provides the enterprise-facing REST API, while Python handles the AI/NLP preprocessing.

```text
Spring Boot :8080
       │
       │ HTTP / JSON
       ▼
FastAPI :8000
```

Spring Boot locates the Python service through configuration in `application.yml`:

```yaml
ai:
  service:
    base-url: http://localhost:8000
```

The Spring Boot service sends the trader's question to FastAPI over HTTP/JSON. FastAPI executes the tokenizer logic and returns the analysis as JSON.

This separation allows the Java API/business layer and Python AI layer to evolve independently.

---

## Running Lab 01

### Prerequisites

- Java 17
- Maven
- Python 3.x

Three terminal windows are used to run and test the complete end-to-end flow.

### Terminal 1 — Start Python AI Service

From the repository root:

```powershell
cd lab-01-tokenization\ai-service

python -m venv venv

.\venv\Scripts\Activate.ps1

pip install -r requirements.txt

uvicorn app:app --reload --port 8000
```

Python AI service:

```text
http://localhost:8000
```

### Terminal 2 — Start Spring Boot API

From the repository root:

```powershell
cd lab-01-tokenization\spring-api

mvn spring-boot:run
```

Spring Boot API:

```text
http://localhost:8080
```

### Terminal 3 — Submit Trader Question

From another PowerShell window:

```powershell
$body = @{
    question = "What are today's major portfolio risks?"
} | ConvertTo-Json

Invoke-RestMethod `
    -Uri "http://localhost:8080/api/trader/query" `
    -Method Post `
    -ContentType "application/json" `
    -Body $body
```

---

## Example Output

```text
original_text   : What are today's major portfolio risks?
character_count : 39
word_count      : 6
token_count     : 9
tokens          : [...]
```

---

## What Produces These Values?

```text
Python
├── len(text)             → Character Count
├── len(text.split())     → Word Count
└── len(token_ids)        → Token Count

Hugging Face Tokenizer
├── Text                   → Tokenization
├── Token Pieces           → Token IDs
└── Token IDs              → Readable Token Pieces
```

The number of words and tokens can differ because an AI tokenizer may split words, punctuation, or subwords into separate token units.

---

## Why Token Awareness Matters

Token awareness becomes important in later AI stages for:

- Context-window management
- Prompt-size optimization
- Retrieval-context optimization
- Latency management
- AI inference cost optimization

Lab 01 establishes this foundation before introducing embeddings, vector similarity, semantic retrieval, RAG, and generative LLM inference.

---

## Architecture Documentation

The `docs/` directory contains the Lab 01 architecture documentation:

- Functional high-level architecture
- Low-level technical architecture

---

## Key Learning

Lab 01 demonstrates the boundary between traditional application processing and AI preprocessing:

```text
Trader Request
      ↓
Java / Spring Boot
Enterprise API Layer
      ↓
REST / JSON
      ↓
Python / FastAPI
AI Service Layer
      ↓
Tokenizer
      ↓
Tokens + Token IDs
```

At this stage, the system performs **tokenization only**. The tokenizer converts text into model-understandable token representations, but no LLM generates an answer.

---

## Next Lab

### Lab 02 — Embeddings & Vector Similarity

Lab 02 extends the implementation from discrete token representations to numerical vector representations and introduces:

- Embeddings
- Vectors
- Vector similarity
- Cosine similarity

These concepts establish the foundation for semantic search and retrieval in later labs.
