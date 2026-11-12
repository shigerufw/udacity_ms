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
