# Project Structure

```text
udacity_ms/
├── 01-agentic-basics/
│   ├── agent/
│   │   └── agent-basic-knowledge.md
│   ├── project/
│   │   ├── done/
│   │   │   ├── project_lib (1).py
│   │   │   └── project_starter (2).ipynb
│   │   └── instructions/
│   │       ├── Project AgentsVille Trip Planner A Multi-Agent Travel Assistant System.md
│   │       ├── project_lib (1).py
│   │       └── project_starter (2).ipynb
│   ├── study_files/
│   │   ├── deep-dive-1-role-based-prompting.ipynb
│   │   ├── deep-dive-2-chain-of-thought-and-react.ipynb
│   │   ├── deep-dive-3-prompt-instruction-refinement.ipynb
│   │   ├── deep-dive-4-chaining-prompts.ipynb
│   │   └── deep-dive-5-llm-feedback-loops.ipynb
│   ├── udacity_files/
│   │   ├── lesson-1-role-based-prompting.ipynb
│   │   ├── lesson-2-chain-of-thought-and-react-prompting-part-i.ipynb
│   │   ├── lesson-2-chain-of-thought-and-react-prompting-part-ii.ipynb
│   │   ├── lesson-3-prompt-instruction-refinement.ipynb
│   │   ├── lesson-4-chaining-prompts-for-agentic-reasoning.ipynb
│   │   └── lesson-5-implementing-llm-feedback-loops.ipynb
│   └── README.md
├── 01-ai_engineering/
│   └── cd14715-claude-code-classroom/
│       ├── lesson-00-warm-up/
│       │   └── exercise/
│       │       └── starter/
│       │           ├── src/
│       │           │   └── hello-agent.ts
│       │           ├── package.json
│       │           └── README.md
│       ├── lesson-01-model-selection/
│       │   ├── demo/
│       │   │   ├── src/
│       │   │   │   ├── helpers.ts
│       │   │   │   ├── index.ts
│       │   │   │   ├── models.ts
│       │   │   │   └── sample-alerts.ts
│       │   │   ├── package.json
│       │   │   ├── README.md
│       │   │   └── tsconfig.json
│       │   └── exercise/
│       │       ├── solution/
│       │       │   ├── src/
│       │       │   │   ├── classifier.ts
│       │       │   │   ├── helpers.ts
│       │       │   │   ├── models.ts
│       │       │   │   └── sample-tickets.ts
│       │       │   ├── package.json
│       │       │   ├── README.md
│       │       │   └── tsconfig.json
│       │       └── starter/
│       │           ├── src/
│       │           │   ├── classifier.ts
│       │           │   ├── helpers.ts
│       │           │   ├── models.ts
│       │           │   └── sample-tickets.ts
│       │           ├── package.json
│       │           ├── README.md
│       │           └── tsconfig.json
│       ├── lesson-02-extended-thinking/
│       │   ├── demo/
│       │   │   ├── src/
│       │   │   │   ├── incident-analyzer.ts
│       │   │   │   ├── index.ts
│       │   │   │   └── sample-incidents.ts
│       │   │   ├── package.json
│       │   │   ├── README.md
│       │   │   └── tsconfig.json
│       │   └── exercise/
│       │       ├── solution/
│       │       │   ├── src/
│       │       │   │   ├── fraud-analyzer.ts
│       │       │   │   ├── index.ts
│       │       │   │   └── sample-transactions.ts
│       │       │   ├── package.json
│       │       │   ├── README.md
│       │       │   └── tsconfig.json
│       │       └── starter/
│       │           ├── src/
│       │           │   ├── fraud-analyzer.ts
│       │           │   ├── index.ts
│       │           │   └── sample-transactions.ts
│       │           ├── package.json
│       │           ├── README.md
│       │           └── tsconfig.json
│       ├── lesson-03-agentic-architecture/
│       │   ├── demo/
│       │   │   ├── diagrams/
│       │   │   │   ├── multi-agent.mmd
│       │   │   │   ├── multi-agent.svg
│       │   │   │   ├── sequence.mmd
│       │   │   │   ├── sequence.svg
│       │   │   │   ├── single-agent.mmd
│       │   │   │   ├── single-agent.svg
│       │   │   │   ├── workflow.mmd
│       │   │   │   └── workflow.svg
│       │   │   ├── ARCHITECTURE.md
│       │   │   └── README.md
│       │   └── exercise/
│       │       ├── solution/
│       │       │   ├── diagrams/
│       │       │   │   ├── multi-agent.mmd
│       │       │   │   ├── multi-agent.svg
│       │       │   │   ├── sequence.mmd
│       │       │   │   ├── sequence.svg
│       │       │   │   ├── single-agent.mmd
│       │       │   │   ├── single-agent.svg
│       │       │   │   ├── sla-monitoring.mmd
│       │       │   │   ├── sla-monitoring.svg
│       │       │   │   ├── workflow.mmd
│       │       │   │   └── workflow.svg
│       │       │   ├── ARCHITECTURE.md
│       │       │   └── README.md
│       │       └── starter/
│       │           ├── diagrams/
│       │           │   ├── multi-agent.mmd
│       │           │   ├── sequence.mmd
│       │           │   ├── single-agent.mmd
│       │           │   ├── single-agent.svg
│       │           │   ├── sla-monitoring.mmd
│       │           │   └── workflow.mmd
│       │           ├── ARCHITECTURE.md
│       │           └── README.md
│       ├── lesson-04-claude-code-config/
│       │   ├── demo/
│       │   │   ├── src/
│       │   │   │   └── example.ts
│       │   │   └── README.md
│       │   └── exercise/
│       │       ├── solution/
│       │       │   └── README.md
│       │       ├── starter/
│       │       │   ├── sample-tickets/
│       │       │   │   ├── billing.txt
│       │       │   │   ├── general.txt
│       │       │   │   └── technical.txt
│       │       │   └── README.md
│       │       └── README.md
│       ├── lesson-05-agent-sdk/
│       │   ├── demo/
│       │   │   ├── src/
│       │   │   │   ├── document-summarizer.ts
│       │   │   │   ├── index.ts
│       │   │   │   └── sample-api-guide.md
│       │   │   ├── package.json
│       │   │   ├── README.md
│       │   │   └── tsconfig.json
│       │   ├── exercise/
│       │   │   ├── solution/
│       │   │   │   ├── src/
│       │   │   │   │   ├── contracts/
│       │   │   │   │   │   ├── consulting.txt
│       │   │   │   │   │   ├── email.txt
│       │   │   │   │   │   ├── saas.txt
│       │   │   │   │   │   └── vendor.txt
│       │   │   │   │   ├── standardized/
│       │   │   │   │   │   ├── standardized-email.md
│       │   │   │   │   │   └── standardized-saas.md
│       │   │   │   │   ├── contract-standardizer.ts
│       │   │   │   │   ├── index.ts
│       │   │   │   │   └── sample-contracts.ts
│       │   │   │   ├── package.json
│       │   │   │   └── README.md
│       │   │   └── starter/
│       │   │       ├── src/
│       │   │       │   ├── contracts/
│       │   │       │   │   ├── consulting.txt
│       │   │       │   │   ├── email.txt
│       │   │       │   │   ├── saas.txt
│       │   │       │   │   └── vendor.txt
│       │   │       │   ├── standardized/
│       │   │       │   ├── contract-standardizer.ts
│       │   │       │   ├── index.ts
│       │   │       │   └── sample-contracts.ts
│       │   │       ├── package.json
│       │   │       └── README.md
│       │   └── Python /
│       │       ├── 01-Agentic_Loop/
│       │       │   ├── claims_intake/
│       │       │   │   ├── __init__.py
│       │       │   │   ├── __main__.py
│       │       │   │   ├── budget.py
│       │       │   │   ├── client.py
│       │       │   │   ├── loop.py
│       │       │   │   ├── pricing.py
│       │       │   │   ├── run.py
│       │       │   │   ├── session.py
│       │       │   │   ├── system_prompt.py
│       │       │   │   ├── tools.py
│       │       │   │   └── tracer.py
│       │       │   ├── fixtures/
│       │       │   │   └── claims/
│       │       │   │       ├── claim_01_kitchen_fire.json
│       │       │   │       ├── claim_02_stolen_bike.json
│       │       │   │       ├── claim_03_water_damage.json
│       │       │   │       ├── claim_04_neighbor_injury.json
│       │       │   │       ├── claim_05_auto_collision.json
│       │       │   │       ├── claim_06_low_confidence_escalation.json
│       │       │   │       ├── claim_07_tree_falls_on_car.json
│       │       │   │       └── claim_08_minor_porch_damage.json
│       │       │   ├── tests/
│       │       │   │   ├── __init__.py
│       │       │   │   ├── fakes.py
│       │       │   │   ├── test_antipatterns.py
│       │       │   │   ├── test_fixtures.py
│       │       │   │   ├── test_loop.py
│       │       │   │   └── test_tools.py
│       │       │   └── pyproject.toml
│       │       ├── 02-tools-and-audit/
│       │       │   ├── claims_intake/
│       │       │   │   ├── __init__.py
│       │       │   │   ├── __main__.py
│       │       │   │   ├── budget.py
│       │       │   │   ├── client.py
│       │       │   │   ├── loop.py
│       │       │   │   ├── pricing.py
│       │       │   │   ├── run.py
│       │       │   │   ├── session.py
│       │       │   │   ├── system_prompt.py
│       │       │   │   ├── tools.py
│       │       │   │   └── tracer.py
│       │       │   ├── fixtures/
│       │       │   │   └── claims/
│       │       │   │       ├── claim_01_kitchen_fire.json
│       │       │   │       ├── claim_02_stolen_bike.json
│       │       │   │       ├── claim_03_water_damage.json
│       │       │   │       ├── claim_04_neighbor_injury.json
│       │       │   │       ├── claim_05_auto_collision.json
│       │       │   │       ├── claim_06_low_confidence_escalation.json
│       │       │   │       ├── claim_07_tree_falls_on_car.json
│       │       │   │       └── claim_08_minor_porch_damage.json
│       │       │   ├── tests/
│       │       │   │   ├── __init__.py
│       │       │   │   ├── fakes.py
│       │       │   │   ├── test_antipatterns.py
│       │       │   │   ├── test_fixtures.py
│       │       │   │   ├── test_loop.py
│       │       │   │   └── test_tools.py
│       │       │   └── pyproject.toml
│       │       └── 03-dynamic-decomposition/
│       │           ├── claims_intake/
│       │           │   ├── __init__.py
│       │           │   ├── __main__.py
│       │           │   ├── budget.py
│       │           │   ├── client.py
│       │           │   ├── loop.py
│       │           │   ├── pricing.py
│       │           │   ├── run.py
│       │           │   ├── session.py
│       │           │   ├── system_prompt.py
│       │           │   ├── tools.py
│       │           │   └── tracer.py
│       │           ├── fixtures/
│       │           │   └── claims/
│       │           │       ├── claim_01_kitchen_fire.json
│       │           │       ├── claim_02_stolen_bike.json
│       │           │       ├── claim_03_water_damage.json
│       │           │       ├── claim_04_neighbor_injury.json
│       │           │       ├── claim_05_auto_collision.json
│       │           │       ├── claim_06_low_confidence_escalation.json
│       │           │       ├── claim_07_tree_falls_on_car.json
│       │           │       └── claim_08_minor_porch_damage.json
│       │           ├── tests/
│       │           │   ├── __init__.py
│       │           │   ├── fakes.py
│       │           │   ├── test_antipatterns.py
│       │           │   ├── test_fixtures.py
│       │           │   ├── test_loop.py
│       │           │   ├── test_run_backstop.py
│       │           │   └── test_tools.py
│       │           └── pyproject.toml
│       ├── lesson-06-custom-tools/
│       │   ├── demo/
│       │   │   ├── src/
│       │   │   │   ├── index.ts
│       │   │   │   ├── tax-calculator.test.ts
│       │   │   │   ├── tax-calculator.ts
│       │   │   │   └── thinking-with-tools.ts
│       │   │   ├── package.json
│       │   │   └── README.md
│       │   └── exercise/
│       │       ├── solution/
│       │       │   ├── src/
│       │       │   │   ├── api-validator.test.ts
│       │       │   │   ├── api-validator.ts
│       │       │   │   └── index.ts
│       │       │   ├── package.json
│       │       │   └── README.md
│       │       └── starter/
│       │           ├── src/
│       │           │   ├── api-validator.ts
│       │           │   └── index.ts
│       │           ├── package.json
│       │           └── README.md
│       ├── lesson-07-structured-outputs/
│       │   ├── demo/
│       │   │   ├── src/
│       │   │   │   ├── index.ts
│       │   │   │   ├── product-review-analyzer.ts
│       │   │   │   └── sample-reviews.ts
│       │   │   ├── package.json
│       │   │   └── README.md
│       │   ├── exercise/
│       │   │   ├── solution/
│       │   │   │   ├── src/
│       │   │   │   │   ├── index.ts
│       │   │   │   │   ├── meeting-analyzer.ts
│       │   │   │   │   └── sample-transcripts.ts
│       │   │   │   ├── package.json
│       │   │   │   └── README.md
│       │   │   └── starter/
│       │   │       ├── src/
│       │   │       │   ├── index.ts
│       │   │       │   ├── meeting-analyzer.ts
│       │   │       │   └── sample-transcripts.ts
│       │   │       ├── package.json
│       │   │       └── README.md
│       │   └── Python/
│       │       ├── 01-prune-tool-output/
│       │       │   ├── retail_context/
│       │       │   │   ├── prompts/
│       │       │   │   │   └── compression_prompt.md
│       │       │   │   ├── __init__.py
│       │       │   │   ├── __main__.py
│       │       │   │   ├── assemble.py
│       │       │   │   ├── case_facts.py
│       │       │   │   ├── client.py
│       │       │   │   ├── compressor.py
│       │       │   │   ├── evaluate.py
│       │       │   │   ├── pruner.py
│       │       │   │   ├── run.py
│       │       │   │   ├── tokens.py
│       │       │   │   └── transcript.py
│       │       │   ├── scripts/
│       │       │   │   └── generate_transcript.py
│       │       │   ├── tests/
│       │       │   │   ├── __init__.py
│       │       │   │   ├── test_antipatterns.py
│       │       │   │   ├── test_assemble.py
│       │       │   │   ├── test_case_facts.py
│       │       │   │   ├── test_compressor.py
│       │       │   │   ├── test_pruner.py
│       │       │   │   ├── test_tokens.py
│       │       │   │   └── test_transcript.py
│       │       │   ├── pyproject.toml
│       │       │   └── README.md
│       │       ├── 02-case-facts-block/
│       │       │   ├── retail_context/
│       │       │   │   ├── prompts/
│       │       │   │   │   └── compression_prompt.md
│       │       │   │   ├── __init__.py
│       │       │   │   ├── __main__.py
│       │       │   │   ├── assemble.py
│       │       │   │   ├── case_facts.py
│       │       │   │   ├── client.py
│       │       │   │   ├── compressor.py
│       │       │   │   ├── evaluate.py
│       │       │   │   ├── pruner.py
│       │       │   │   ├── run.py
│       │       │   │   ├── tokens.py
│       │       │   │   └── transcript.py
│       │       │   ├── scripts/
│       │       │   │   └── generate_transcript.py
│       │       │   ├── tests/
│       │       │   │   ├── __init__.py
│       │       │   │   ├── test_antipatterns.py
│       │       │   │   ├── test_assemble.py
│       │       │   │   ├── test_case_facts.py
│       │       │   │   ├── test_compressor.py
│       │       │   │   ├── test_pruner.py
│       │       │   │   ├── test_tokens.py
│       │       │   │   └── test_transcript.py
│       │       │   ├── pyproject.toml
│       │       │   └── README.md
│       │       ├── 03-compress-with-budget/
│       │       │   ├── retail_context/
│       │       │   │   ├── prompts/
│       │       │   │   │   └── compression_prompt.md
│       │       │   │   ├── __init__.py
│       │       │   │   ├── __main__.py
│       │       │   │   ├── assemble.py
│       │       │   │   ├── case_facts.py
│       │       │   │   ├── client.py
│       │       │   │   ├── compressor.py
│       │       │   │   ├── evaluate.py
│       │       │   │   ├── pruner.py
│       │       │   │   ├── run.py
│       │       │   │   ├── tokens.py
│       │       │   │   └── transcript.py
│       │       │   ├── scripts/
│       │       │   │   └── generate_transcript.py
│       │       │   ├── tests/
│       │       │   │   ├── __init__.py
│       │       │   │   ├── test_antipatterns.py
│       │       │   │   ├── test_assemble.py
│       │       │   │   ├── test_case_facts.py
│       │       │   │   ├── test_compressor.py
│       │       │   │   ├── test_pruner.py
│       │       │   │   ├── test_tokens.py
│       │       │   │   └── test_transcript.py
│       │       │   ├── pyproject.toml
│       │       │   └── README.md
│       │       └── 04-assemble-and-locate/
│       │           ├── retail_context/
│       │           │   ├── prompts/
│       │           │   │   └── compression_prompt.md
│       │           │   ├── __init__.py
│       │           │   ├── __main__.py
│       │           │   ├── assemble.py
│       │           │   ├── case_facts.py
│       │           │   ├── client.py
│       │           │   ├── compressor.py
│       │           │   ├── evaluate.py
│       │           │   ├── pruner.py
│       │           │   ├── run.py
│       │           │   ├── tokens.py
│       │           │   └── transcript.py
│       │           ├── scripts/
│       │           │   └── generate_transcript.py
│       │           ├── tests/
│       │           │   ├── __init__.py
│       │           │   ├── test_antipatterns.py
│       │           │   ├── test_assemble.py
│       │           │   ├── test_case_facts.py
│       │           │   ├── test_compressor.py
│       │           │   ├── test_pruner.py
│       │           │   ├── test_tokens.py
│       │           │   └── test_transcript.py
│       │           ├── pyproject.toml
│       │           └── README.md
│       ├── lesson-08-claude-skills/
│       │   ├── demo/
│       │   │   ├── src/
│       │   │   │   ├── email-reviewer.ts
│       │   │   │   ├── index.ts
│       │   │   │   └── sample-emails.ts
│       │   │   ├── package.json
│       │   │   └── README.md
│       │   └── exercise/
│       │       ├── solution/
│       │       │   ├── src/
│       │       │   │   ├── sample-code/
│       │       │   │   │   ├── clean.js
│       │       │   │   │   └── issues.js
│       │       │   │   ├── index.ts
│       │       │   │   └── js-reviewer.ts
│       │       │   ├── package.json
│       │       │   └── README.md
│       │       └── starter/
│       │           ├── src/
│       │           │   ├── sample-code/
│       │           │   │   ├── clean.js
│       │           │   │   └── issues.js
│       │           │   ├── index.ts
│       │           │   └── js-reviewer.ts
│       │           ├── package.json
│       │           └── README.md
│       ├── lesson-09-mcp-integration/
│       │   ├── demo/
│       │   │   ├── src/
│       │   │   │   ├── github-summarizer.ts
│       │   │   │   └── index.ts
│       │   │   ├── package.json
│       │   │   └── README.md
│       │   └── exercise/
│       │       ├── solution/
│       │       │   ├── src/
│       │       │   │   ├── config/
│       │       │   │   │   └── mcp.config.ts
│       │       │   │   ├── sample-code/
│       │       │   │   │   ├── clean.js
│       │       │   │   │   ├── errors.js
│       │       │   │   │   └── issues.js
│       │       │   │   ├── code-reviewer.ts
│       │       │   │   ├── index.ts
│       │       │   │   └── sample-code.ts
│       │       │   ├── package.json
│       │       │   └── README.md
│       │       └── starter/
│       │           ├── src/
│       │           │   ├── config/
│       │           │   │   └── mcp.config.ts
│       │           │   ├── sample-code/
│       │           │   │   ├── clean.js
│       │           │   │   ├── errors.js
│       │           │   │   └── issues.js
│       │           │   ├── code-reviewer.ts
│       │           │   ├── index.ts
│       │           │   └── sample-code.ts
│       │           ├── package.json
│       │           └── README.md
│       ├── lesson-10-multi-agent-orchestration/
│       │   ├── demo/
│       │   │   ├── src/
│       │   │   │   ├── index.ts
│       │   │   │   └── research-orchestrator.ts
│       │   │   ├── package.json
│       │   │   └── README.md
│       │   └── exercise/
│       │       ├── solution/
│       │       │   ├── src/
│       │       │   │   ├── index.ts
│       │       │   │   ├── sales-qualifier.ts
│       │       │   │   └── sample-prospects.ts
│       │       │   ├── package.json
│       │       │   └── README.md
│       │       └── starter/
│       │           ├── src/
│       │           │   ├── index.ts
│       │           │   ├── sales-qualifier.ts
│       │           │   └── sample-prospects.ts
│       │           ├── package.json
│       │           └── README.md
│       ├── lesson-11-tdd-with-ai/
│       │   ├── demo/
│       │   │   ├── src/
│       │   │   │   ├── auth.test.ts
│       │   │   │   ├── auth.ts
│       │   │   │   └── index.ts
│       │   │   ├── package.json
│       │   │   ├── README.md
│       │   │   └── tsconfig.json
│       │   └── exercise/
│       │       ├── solution/
│       │       │   ├── src/
│       │       │   │   ├── index.ts
│       │       │   │   ├── shopping-cart.test.ts
│       │       │   │   └── shopping-cart.ts
│       │       │   ├── package.json
│       │       │   ├── README.md
│       │       │   ├── tdd-strategy.md
│       │       │   └── tsconfig.json
│       │       └── starter/
│       │           ├── src/
│       │           │   ├── index.ts
│       │           │   ├── shopping-cart.test.ts
│       │           │   └── shopping-cart.ts
│       │           ├── package.json
│       │           ├── README.md
│       │           ├── tdd-strategy.md
│       │           └── tsconfig.json
│       ├── lesson-12-evaluating-agents/
│       │   ├── demo/
│       │   │   ├── src/
│       │   │   │   ├── evaluators/
│       │   │   │   │   └── index.ts
│       │   │   │   ├── index.ts
│       │   │   │   ├── tip-agent.ts
│       │   │   │   ├── tip-calculator.ts
│       │   │   │   └── types.ts
│       │   │   ├── package.json
│       │   │   └── README.md
│       │   └── exercise/
│       │       ├── solution/
│       │       │   ├── src/
│       │       │   │   ├── evaluators/
│       │       │   │   │   └── index.ts
│       │       │   │   ├── index.ts
│       │       │   │   ├── sentiment-agent.ts
│       │       │   │   ├── sentiment-tool.ts
│       │       │   │   └── types.ts
│       │       │   ├── package.json
│       │       │   └── README.md
│       │       └── starter/
│       │           ├── src/
│       │           │   ├── evaluators/
│       │           │   │   └── index.ts
│       │           │   ├── index.ts
│       │           │   ├── sentiment-agent.ts
│       │           │   ├── sentiment-tool.ts
│       │           │   └── types.ts
│       │           ├── package.json
│       │           └── README.md
│       ├── lesson-13-computer-use/
│       │   ├── demo/
│       │   │   ├── src/
│       │   │   │   ├── action-handlers.ts
│       │   │   │   ├── computer-use-client.ts
│       │   │   │   ├── index.ts
│       │   │   │   └── types.ts
│       │   │   ├── package.json
│       │   │   └── README.md
│       │   ├── exercise/
│       │   │   ├── solution/
│       │   │   │   ├── src/
│       │   │   │   │   ├── action-handlers.ts
│       │   │   │   │   ├── form-agent.ts
│       │   │   │   │   ├── index.ts
│       │   │   │   │   └── types.ts
│       │   │   │   ├── package.json
│       │   │   │   └── README.md
│       │   │   └── starter/
│       │   │       ├── src/
│       │   │       │   ├── action-handlers.ts
│       │   │       │   ├── form-agent.ts
│       │   │       │   ├── index.ts
│       │   │       │   └── types.ts
│       │   │       ├── package.json
│       │   │       └── README.md
│       │   └── README.md
│       ├── project/
│       │   ├── starter/
│       │   │   ├── src/
│       │   │   │   ├── agents/
│       │   │   │   │   └── index.ts
│       │   │   │   ├── config/
│       │   │   │   │   └── mcp.config.ts
│       │   │   │   ├── prompts/
│       │   │   │   │   └── index.ts
│       │   │   │   ├── types/
│       │   │   │   │   ├── analysis-results.ts
│       │   │   │   │   ├── index.ts
│       │   │   │   │   └── report-types.ts
│       │   │   │   ├── utils/
│       │   │   │   │   ├── error-handler.ts
│       │   │   │   │   ├── index.ts
│       │   │   │   │   ├── logger.ts
│       │   │   │   │   ├── rate-limiter.ts
│       │   │   │   │   └── report-generator.ts
│       │   │   │   ├── main.ts
│       │   │   │   └── orchestrator.ts
│       │   │   ├── tests/
│       │   │   │   └── orchestrator.test.ts
│       │   │   ├── package-lock.json
│       │   │   ├── package.json
│       │   │   ├── README.md
│       │   │   └── tsconfig.json
│       │   └── README.md
│       ├── CODEOWNERS
│       ├── LICENSE.md
│       ├── package-lock.json
│       ├── package.json
│       └── README.md
├── 02-agentic-workflows/
│   ├── agent/
│   │   └── agent-basic-knowledge.md
│   ├── project/
│   │   ├── done/
│   │   ├── instructions/
│   │   │   ├── starter/
│   │   │   │   ├── phase_1/
│   │   │   │   │   ├── workflow_agents/
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   └── base_agents.py
│   │   │   │   │   ├── action_planning_agent.py
│   │   │   │   │   ├── augmented_prompt_agent.py
│   │   │   │   │   ├── direct_prompt_agent.py
│   │   │   │   │   ├── evaluation_agent.py
│   │   │   │   │   ├── knowledge_augmented_prompt_agent.py
│   │   │   │   │   ├── rag_knowledge_prompt_agent.py
│   │   │   │   │   ├── README.md
│   │   │   │   │   └── routing_agent.py
│   │   │   │   ├── phase_2/
│   │   │   │   │   ├── workflow_agents/
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   └── base_agents.py
│   │   │   │   │   ├── agentic_workflow.py
│   │   │   │   │   ├── Product-Spec-Email-Router.txt
│   │   │   │   │   └── README.md
│   │   │   │   └── README.md
│   │   │   ├── Agentic AI - points.md
│   │   │   ├── AI-Powered Agentic Workflow for Project Management - Phase 1 - Building your Agent Library.md
│   │   │   ├── AI-Powered Agentic Workflow for Project Management - Phase 2 - Implementing your Agentic Workflow.md
│   │   │   ├── project_overview.md
│   │   │   ├── README.md
│   │   │   └── requirements.txt
│   │   └── Send/
│   │       └── starter/
│   │           ├── phase_1/
│   │           │   ├── output_txt/
│   │           │   │   ├── output_action_planning_agent.txt
│   │           │   │   ├── output_augmented_prompt_agent.txt
│   │           │   │   ├── output_direct_prompt_agent.txt
│   │           │   │   ├── output_evaluation_agent.txt
│   │           │   │   ├── output_knowledge_augmented_prompt__agent.txt
│   │           │   │   ├── output_rag_knowledge_prompt_agent.txt
│   │           │   │   └── output_routing_agent.txt
│   │           │   ├── prints/
│   │           │   │   ├── action_planning_agent copy.png
│   │           │   │   ├── augmented_prompt_agent.png
│   │           │   │   ├── direct_prompt_agent.png
│   │           │   │   ├── evaluation_agent_pt1.png
│   │           │   │   ├── evaluation_agent_pt2.png
│   │           │   │   ├── knowledge_augmented_prompt_agent.png
│   │           │   │   ├── rag_knowlegde_prompt_agent.png
│   │           │   │   └── routing_agent.png
│   │           │   ├── workflow_agents/
│   │           │   │   ├── __init__.py
│   │           │   │   └── base_agents.py
│   │           │   ├── action_planning_agent.py
│   │           │   ├── augmented_prompt_agent.py
│   │           │   ├── direct_prompt_agent.py
│   │           │   ├── evaluation_agent.py
│   │           │   ├── import_test.py
│   │           │   ├── knowledge_augmented_prompt_agent.py
│   │           │   ├── rag_knowledge_prompt_agent.py
│   │           │   ├── README.md
│   │           │   └── routing_agent.py
│   │           ├── phase_2/
│   │           │   ├── output_txt/
│   │           │   │   └── output_agentic_workflow.txt
│   │           │   ├── print/
│   │           │   │   ├── agentic_workflow_example_print_1.png
│   │           │   │   └── agentic_workflow_example_print_2.png
│   │           │   ├── workflow_agents/
│   │           │   │   ├── __init__.py
│   │           │   │   └── base_agents.py
│   │           │   ├── agentic_workflow.py
│   │           │   ├── generate_map.py
│   │           │   ├── Product-Spec-Email-Router.txt
│   │           │   └── README.md
│   │           ├── test/
│   │           │   └── test
│   │           └── README.md
│   ├── study_files/
│   │   ├── deep-dive-1-agentic-workflow-fundamentals.ipynb
│   │   ├── deep-dive-2-prompt-chaining-with-agents.ipynb
│   │   ├── deep-dive-3-routing.ipynb
│   │   ├── deep-dive-4-parallelization.ipynb
│   │   ├── deep-dive-5-evaluator-optimizer.ipynb
│   │   └── deep-dive-6-orchestrator-workers.ipynb
│   ├── udacity_files/
│   │   ├── class_01-agentic.py
│   │   ├── class_02-chaining-prompt.py
│   │   ├── class_03-example_chaining.py
│   │   ├── class_04-routing.py
│   │   ├── class_05-example_routing.py
│   │   ├── class_06-evaluator optimizer.py
│   │   ├── class_06-Parallelization.py
│   │   └── class_07-orchestrator.py
│   └── README.md
├── 03-agentic-building-agents/
│   ├── agent/
│   ├── project/
│   │   ├── done/
│   │   └── instructions/
│   ├── study_files/
│   ├── udacity_files/
│   └── README.md
├── CLAUDE.md
├── generate_map.py
└── README.md
```

<!--
Copy and paste the code block above directly into your README.md under the "## Structure" section.
-->
