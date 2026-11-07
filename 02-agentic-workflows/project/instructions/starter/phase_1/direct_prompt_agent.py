# Test script for DirectPromptAgent class

# TODO: 1 - Import the DirectPromptAgent class from BaseAgents
from workflow_agents.base_agents import DirectPromptAgent
import os
from dotenv import load_dotenv

# Load environment variables from .env file
dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".env"))
load_dotenv(dotenv_path=dotenv_path)

# TODO: 2 - Load the OpenAI API key from the environment variables
openai_api_key = (os.getenv("API_TOKEN") or os.getenv("OPENAI_API_KEY") or "").strip()
if openai_api_key:
    os.environ["OPENAI_API_KEY"] = openai_api_key
base_url = os.getenv("OPENAI_BASE_URL", "https://openai.vocareum.com/v1")
if base_url:
    os.environ["OPENAI_BASE_URL"] = base_url

prompt = "What is the Capital of France?"

# TODO: 3 - Instantiate the DirectPromptAgent as direct_agent
direct_agent = DirectPromptAgent(openai_api_key)

# TODO: 4 - Use direct_agent to send the prompt defined above and store the response
direct_agent_response = direct_agent.respond(prompt)

# Print the response from the agent
print(direct_agent_response)

# TODO: 5 - Print an explanatory message describing the knowledge source used by the agent to generate the response
print("\nKnowledge Source: The DirectPromptAgent used the general pre-trained knowledge inherent in the underlying LLM (gpt-3.5-turbo), without any persona or domain-specific context provided.")
