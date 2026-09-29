package com.trader.api.service;

import com.trader.api.model.AiResponse;
import com.trader.api.model.TraderQueryRequest;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestClient;

@Service
public class AiService {

    private final RestClient restClient;

    // Spring injects ai.service.base-url from application.yml.
    public AiService(
            RestClient.Builder builder,
            @Value("${ai.service.base-url}") String aiServiceBaseUrl
    ) {
        // RestClient is the HTTP client used by Spring Boot to call Python.
        this.restClient = builder
                .baseUrl(aiServiceBaseUrl)
                .build();
    }

    public AiResponse analyze(TraderQueryRequest request) {
        // POST the trader JSON to the Python AI Orchestrator.
        return restClient
                .post()
                .uri("/ai/analyze")
                .body(request)
                .retrieve()
                .body(AiResponse.class);
    }
}
