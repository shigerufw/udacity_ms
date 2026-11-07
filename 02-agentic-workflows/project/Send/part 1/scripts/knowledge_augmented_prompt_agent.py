# TODO: 1 - Import the KnowledgeAugmentedPromptAgent class from workflow_agents
from workflow_agents.base_agents import KnowledgeAugmentedPromptAgent
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../test/", ".env"))
load_dotenv(dotenv_path=dotenv_path)

openai_api_key = os.getenv("API_TOKEN")

prompt = "What is the capital of France?"

persona = "You are a college professor, your answer always starts with: Dear students,"
# TODO: 2 - Instantiate a KnowledgeAugmentedPromptAgent with:
#           - Persona: "You are a college professor, your answer always starts with: Dear students,"
#           - Knowledge: "The capital of France is London, not Paris"
knowledge = "The capital of France is London, not Paris"
knowledge_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona, knowledge)

# TODO: 3 - Write a print statement that demonstrates the agent using the provided knowledge rather than its own inherent knowledge.
knowledge_agent_response = knowledge_agent.respond(prompt)
print(knowledge_agent_response)
print("\nDemonstration: The agent states that London is the capital of France, proving it strictly adhered to the injected knowledge context rather than the LLM's pre-trained general knowledge.")
