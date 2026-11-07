# TODO: 1 - Import the AugmentedPromptAgent class
from workflow_agents.base_agents import AugmentedPromptAgent
import os
from dotenv import load_dotenv

# Load environment variables from .env file
dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".env"))
load_dotenv(dotenv_path=dotenv_path)

# Retrieve OpenAI API key from environment variables
openai_api_key = (os.getenv("API_TOKEN") or os.getenv("OPENAI_API_KEY") or "").strip()
if openai_api_key:
    os.environ["OPENAI_API_KEY"] = openai_api_key
base_url = os.getenv("OPENAI_BASE_URL", "https://openai.vocareum.com/v1")
if base_url:
    os.environ["OPENAI_BASE_URL"] = base_url

prompt = "What is the capital of France?"
persona = "You are a college professor; your answers always start with: 'Dear students,'"

# TODO: 2 - Instantiate an object of AugmentedPromptAgent with the required parameters
augmented_agent = AugmentedPromptAgent(openai_api_key, persona)

# TODO: 3 - Send the 'prompt' to the agent and store the response in a variable named 'augmented_agent_response'
augmented_agent_response = augmented_agent.respond(prompt)

# Print the agent's response
print(augmented_agent_response)

# TODO: 4 - Add a comment explaining:
# - What knowledge the agent likely used to answer the prompt.
# - How the system prompt specifying the persona affected the agent's response.
#
# Explanatory comment:
# 1. Knowledge source: The agent used the LLM's inherent pre-trained knowledge base to identify Paris as the capital of France.
# 2. Persona effect: The system prompt conditioned the model to adopt the persona of a college professor and prepend the exact required greeting ("Dear students,"), thereby shaping the tone and style of the output while preserving factual accuracy.
