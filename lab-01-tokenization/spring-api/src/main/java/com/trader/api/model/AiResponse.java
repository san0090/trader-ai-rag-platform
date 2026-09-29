package com.trader.api.model;

import java.util.List;

// Mirrors the JSON returned by the Python AI service.
public record AiResponse(
        String original_text,
        int character_count,
        int word_count,
        int token_count,
        List<TokenDetail> tokens
) {
}
