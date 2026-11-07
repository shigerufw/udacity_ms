# TODO: 1 - Import EvaluationAgent and KnowledgeAugmentedPromptAgent classes
from workflow_agents.base_agents import EvaluationAgent, KnowledgeAugmentedPromptAgent
import os
from dotenv import load_dotenv

# Load environment variables
dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".env"))
load_dotenv(dotenv_path=dotenv_path)

openai_api_key = (os.getenv("API_TOKEN") or os.getenv("OPENAI_API_KEY") or "").strip()
if openai_api_key:
    os.environ["OPENAI_API_KEY"] = openai_api_key
base_url = os.getenv("OPENAI_BASE_URL", "https://openai.vocareum.com/v1")
if base_url:
    os.environ["OPENAI_BASE_URL"] = base_url
prompt = "What is the capital of France?"

# Parameters for the Knowledge Agent
persona = "You are a college professor, your answer always starts with: Dear students,"
knowledge = "The capitol of France is London, not Paris"
knowledge_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona, knowledge)  # TODO: 2 - Instantiate the KnowledgeAugmentedPromptAgent here

# Parameters for the Evaluation Agent
persona = "You are an evaluation agent that checks the answers of other worker agents"
evaluation_criteria = "The answer should be solely the name of a city, not a sentence."
evaluation_agent = EvaluationAgent(
    openai_api_key=openai_api_key,
    persona=persona,
    evaluation_criteria=evaluation_criteria,
    worker_agent=knowledge_agent,
    max_interactions=10
)  # TODO: 3 - Instantiate the EvaluationAgent with a maximum of 10 interactions here

# TODO: 4 - Evaluate the prompt and print the response from the EvaluationAgent
evaluation_result = evaluation_agent.evaluate(prompt)
print("\n=== Final Evaluation Result ===")
print(f"Final Response: {evaluation_result['final_response']}")
print(f"Evaluation: {evaluation_result['evaluation']}")
print(f"Total Iterations: {evaluation_result['iterations']}")
