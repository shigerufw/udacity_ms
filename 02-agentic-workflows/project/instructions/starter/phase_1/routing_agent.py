# TODO: 1 - Import the KnowledgeAugmentedPromptAgent and RoutingAgent
from workflow_agents.base_agents import KnowledgeAugmentedPromptAgent, RoutingAgent
import os
from dotenv import load_dotenv

# Load environment variables from .env file
dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".env"))
load_dotenv(dotenv_path=dotenv_path)

openai_api_key = (os.getenv("API_TOKEN") or os.getenv("OPENAI_API_KEY") or "").strip()
if openai_api_key:
    os.environ["OPENAI_API_KEY"] = openai_api_key
base_url = os.getenv("OPENAI_BASE_URL", "https://openai.vocareum.com/v1")
if base_url:
    os.environ["OPENAI_BASE_URL"] = base_url

persona = "You are a college professor"

knowledge = "You know everything about Texas"
# TODO: 2 - Define the Texas Knowledge Augmented Prompt Agent
texas_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona, knowledge)

knowledge = "You know everything about Europe"
# TODO: 3 - Define the Europe Knowledge Augmented Prompt Agent
europe_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona, knowledge)

persona = "You are a college math professor"
knowledge = "You know everything about math, you take prompts with numbers, extract math formulas, and show the answer without explanation"
# TODO: 4 - Define the Math Knowledge Augmented Prompt Agent
math_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona, knowledge)

routing_agent = RoutingAgent(openai_api_key, [])
agents = [
    {
        "name": "texas agent",
        "description": "Answer a question about Texas",
        "func": lambda x: texas_agent.respond(x)  # TODO: 5 - Call the Texas Agent to respond to prompts
    },
    {
        "name": "europe agent",
        "description": "Answer a question about Europe",
        "func": lambda x: europe_agent.respond(x)  # TODO: 6 - Define a function to call the Europe Agent
    },
    {
        "name": "math agent",
        "description": "When a prompt contains numbers, respond with a math formula",
        "func": lambda x: math_agent.respond(x)  # TODO: 7 - Define a function to call the Math Agent
    }
]

routing_agent.agents = agents

# TODO: 8 - Print the RoutingAgent responses to the following prompts:
#           - "Tell me about the history of Rome, Texas"
#           - "Tell me about the history of Rome, Italy"
#           - "One story takes 2 days, and there are 20 stories"
test_prompts = [
    "Tell me about the history of Rome, Texas",
    "Tell me about the history of Rome, Italy",
    "One story takes 2 days, and there are 20 stories"
]

for test_prompt in test_prompts:
    print(f"\n==========================================")
    print(f"Testing Prompt: '{test_prompt}'")
    print(f"==========================================")
    response = routing_agent.route(test_prompt)
    print(f"Final Routed Response:\n{response}")
