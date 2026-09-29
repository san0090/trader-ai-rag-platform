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
Tokenizer
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
Spring Boot
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
│           └── resources/
│
└── docs/
    └── Lab01-Architecture-Diagrams.pdf
```

---

## Spring Boot ↔ Python Integration

Spring Boot provides the enterprise-facing REST API while Python handles
the AI/NLP preprocessing.

```text
Spring Boot :8080
       │
       │ HTTP / JSON
       ▼
FastAPI :8000
```

Spring Boot uses the following configuration to locate the Python service:

```yaml
ai:
  service:
    base-url: http://localhost:8000
```

This separation allows the Java API/business layer and Python AI layer
to evolve independently.

---

## Running Lab 01

### Prerequisites

- Java 17
- Maven
- Python 3.x

Three terminal windows are used to run and test the complete flow.

### Terminal 1 — Start Python AI Service

```powershell
cd lab-01-tokenization\ai-service

python -m venv venv

.\venv\Scripts\Activate.ps1

pip install -r requirements.txt

uvicorn app:app --reload --port 8000
```

Python AI service runs on:

```text
http://localhost:8000
```

### Terminal 2 — Start Spring Boot API

```powershell
cd lab-01-tokenization\spring-api

mvn spring-boot:run
```

Spring Boot runs on:

```text
http://localhost:8080
```

### Terminal 3 — Submit Trader Question

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

### What Produced These Values?

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

The number of words and number of tokens can differ because an AI
tokenizer may split a word, punctuation, or subword into separate
token units.

---

## Why Token Awareness Matters

Token awareness becomes important in later stages for:

- Context-window management
- Prompt-size optimization
- Retrieval-context optimization
- Latency management
- AI inference cost optimization

Lab 01 establishes this foundation before introducing embeddings,
vector similarity, semantic retrieval, RAG, and generative LLM inference.

---

## Architecture Documentation

The `docs/` directory contains the Lab 01 architecture documentation:

- Functional high-level architecture
- Low-level technical architecture

---

## Next Lab

### Lab 02 — Embeddings & Vector Similarity

Lab 02 extends the implementation from discrete token representation
to numerical vector representations and introduces:

- Embeddings
- Vectors
- Vector similarity
- Cosine similarity

These concepts establish the foundation for semantic search and
retrieval in later labs.
