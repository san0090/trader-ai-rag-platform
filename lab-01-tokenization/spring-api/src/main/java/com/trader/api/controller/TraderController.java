package com.trader.api.controller;

import com.trader.api.model.AiResponse;
import com.trader.api.model.TraderQueryRequest;
import com.trader.api.service.AiService;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/trader")
public class TraderController {

    private final AiService aiService;

    // Constructor injection gives the controller access to the integration service.
    public TraderController(AiService aiService) {
        this.aiService = aiService;
    }

    // Trader entry point:
    // POST http://localhost:8080/api/trader/query
    @PostMapping("/query")
    public AiResponse query(@RequestBody TraderQueryRequest request) {
        return aiService.analyze(request);
    }
}
