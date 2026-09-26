---
title: "Project: AgentsVille Trip Planner: A Multi-Agent Travel Assistant System"
source: "https://learn.udacity.com/nd900?version=1.3.57&partKey=cd14526&lessonKey=17acdfc4-8a19-4448-8235-4beee6d4fc64&conceptKey=255c9670-c988-4f98-821c-05ca518315e4"
author:
published:
created: 2026-09-26
description:
tags:
  - "clippings"
---
## Environment Setup

## Project Environment

### Provided Resources

- **I** n the Udacity workspace on the following pages, you'll find a **starter Jupyter Notebook (project\_starter.ipynb):** This will contain the project structure, some helper functions, and clearly marked TODO sections for you to complete.
- **project\_lib.py:** A Python file containing:
	- Pydantic models (e.g., VacationInfo, TravelItinerary, Activity, DayPlan, ToolCall) for data structure and validation.
		- Mock Python functions for the simulated tools (e.g., get\_weather\_forecast, search\_activities\_tool - the solution actually has search\_flights\_tool, find\_hotels\_tool, get\_weather\_tool, get\_activities\_tool).
		- The available\_tools dictionary, which maps tool names to their Python functions and their JSON schemas (for prompting the LLM).
		- Other utility functions like print\_in\_box.

## Local Machine Instructions

If you prefer to work on this project on your local machine, please follow these steps to set up your environment. Note that using your personal OpenAI API key will incur costs based on your usage with OpenAI.

1. Install Python:
	1. Ensure you have Python installed on your computer. We recommend Python version 3.8 or newer.
		2. You can download Python from the official website: [(opens in a new tab)](https://www.python.org/downloads/) [https://www.python.org/downloads/(opens in a new tab)](https://www.python.org/downloads/)
		3. During installation, make sure to check the box that says "Add Python to PATH" (or similar wording) if you are on Windows.
2. Create a Project Directory and Virtual Environment (Recommended):
3. Create a new folder for your project on your computer (e.g., agentsville\_planner).
4. It's highly recommended to use a virtual environment to manage project dependencies and avoid conflicts with other Python projects.
	- Open your terminal or command prompt.
		- Navigate into your new project directory: cd path/to/agentsville\_planner
		- Create a virtual environment. A common name for it is.venv:
		- On macOS/Linux: python3 -m venv.venv
				- On Windows: python -m venv.venv
		- Activate the virtual environment:
		- On macOS/Linux: source.venv/bin/activate
				- On Windows:.venv\\Scripts\\activate
		- You should see the name of your virtual environment (e.g., (.venv)) appear at the beginning of your terminal prompt.
5. Install Jupyter Notebook or JupyterLab
6. Install Required Python Libraries:
7. The project uses several Python libraries. Install them using pip: `pip install json-repair==0.47.1 numexpr==2.11.0 openai==1.74.0 pandas==2.3.0 pydantic==2.11.7 python-dotenv==1.1.0`
	- openai: The official OpenAI Python client library (version 1.x or later is needed).
		- numexpr: Useful for evaluating arithmetic in strings
		- pydantic: Used for data validation and modeling.
		- python-dotenv: Useful for managing your API key in a.env file (optional but good practice).
		- pandas: For any data manipulation or display tasks (often useful in data-centric projects).
		- json-repair: Useful for fixing JSON output of LLMs that sometimes omit, e.g. ending braces.

**5\. Obtain Project Files:**

- Download or copy the project\_starter.ipynb notebook file and the project\_lib.py Python library file into your project directory (agentsville\_planner) from the Udacity workspace by right-clicking on them and choosing "download".

## Workspace Instructions

A workspace is provided on the following pages for you to complete the project in the Udacity Classroom.