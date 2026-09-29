package com.trader.api.model;

// JSON sent by the trader: {"question":"..."}
public record TraderQueryRequest(String question) {
}
