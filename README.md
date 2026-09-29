# trader-ai-rag-platform
Hands-on enterprise GenAI/RAG implementation for financial trading workflows using Java, Python, tokenization, embeddings, vector search, RAG and AWS AI services.

# Trader AI Learning Project — Lab 01

## Concepts
1. Tokens
2. Token counting

## Flow
Trader/Postman -> Spring Boot :8080 -> Python FastAPI :8000 -> Tokenizer -> Token Count -> Spring Boot -> Trader

## Prerequisites
- Java 21
- Maven 3.9+
- Python 3.10–3.12 recommended
- Internet access on the first Python run so Hugging Face can download the lab tokenizer
- Postman or curl

> Note: Lab 01 uses `bert-base-uncased` only to make tokenization visible. Claude/Bedrock can use a different tokenizer. Do not use this lab count as the authoritative Claude billing/context count.

## 1. Start the Python AI service

### macOS/Linux
```bash
cd trader-ai-learning/ai-service
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload --port 8000
```

### Windows PowerShell
```powershell
cd trader-ai-learning\ai-service
py -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app:app --reload --port 8000
```

Verify:
```bash
curl http://localhost:8000/health
```

Expected:
```json
{"status":"UP"}
```

## 2. Start Spring Boot

Open a second terminal:

```bash
cd trader-ai-learning/spring-api
mvn spring-boot:run
```

Spring Boot runs on port 8080.

## 3. Act as the trader

### curl
```bash
curl -X POST http://localhost:8080/api/trader/query \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"What are today's major portfolio risks?\"}"
```

Or use Postman:
- Method: POST
- URL: `http://localhost:8080/api/trader/query`
- Header: `Content-Type: application/json`
- Body/raw/JSON:
```json
{
  "question": "What are today's major portfolio risks?"
}
```

## 4. Observe
The response includes:
- original text
- character count
- word count
- token count
- each token and its token ID

Exact token values/count depend on the selected tokenizer.

## 5. Experiments
Run the same endpoint with:
1. `Risk`
2. `What is portfolio risk?`
3. `Explain credit risk, liquidity risk and interest-rate risk across today's portfolio.`

Compare `word_count` and `token_count`. They are not necessarily equal.

## Troubleshooting
- Python import error: confirm the virtual environment is active and rerun `pip install -r requirements.txt`.
- Tokenizer download error: verify internet access on the first run.
- Spring connection refused to port 8000: start FastAPI first.
- Port already in use: stop the existing process or change the configured port.
- Java/Maven issue: run `java -version` and `mvn -version`; Java 21 is expected.
