from transformers import AutoTokenizer

# Lab tokenizer used only to make tokenization visible.
# Claude/Bedrock models can use a different tokenizer, so exact token counts
# for production model billing/context should come from the model/provider.
MODEL_NAME = "bert-base-uncased"

# Download/load the tokenizer once when the AI service starts.
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)


def analyze_tokens(text: str):
    """Convert trader text into token IDs/tokens and return learning metrics."""

    # Convert the input string into integer token IDs.
    # Special model tokens are disabled so the lab output is easier to inspect.
    token_ids = tokenizer.encode(
        text,
        add_special_tokens=False
    )

    # Convert numeric token IDs into readable token pieces.
    tokens = tokenizer.convert_ids_to_tokens(token_ids)

    # Build an easy-to-read list pairing every token with its ID.
    token_details = []

    # zip() walks through token_ids and tokens together.
    for token_id, token in zip(token_ids, tokens):
        token_details.append({
            "token": token,
            "token_id": token_id
        })

    # Return everything as a Python dictionary; FastAPI serializes it as JSON.
    return {
        "original_text": text,
        "character_count": len(text),
        "word_count": len(text.split()),
        "token_count": len(token_ids),
        "tokens": token_details
    }
