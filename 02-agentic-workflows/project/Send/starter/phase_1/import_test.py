# Test script for DirectPromptAgent class

# TODO: 1 - Import the DirectPromptAgent class from BaseAgents
from workflow_agents.base_agents import DirectPromptAgent
import os
from dotenv import load_dotenv

# Load environment variables from .env file
dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../test/", ".env"))
print(dotenv_path)
load_dotenv(dotenv_path=dotenv_path)

openai_api_key = os.getenv("API_TOKEN")
print(openai_api_key)


from openai import OpenAI

client = OpenAI(
    base_url="https://openai.vocareum.com/v1",
    api_key=openai_api_key,
)

# Fetch and print all model IDs
#model_list = client.models.list()

# Print the model IDs
#for model in model_list.data:
 #   print(model.id)