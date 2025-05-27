import os
from dotenv import load_dotenv
load_dotenv()

# Load API Keys from Environment Variables
BROWSERLESS_API_KEY = os.getenv("BROWSERLESS_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Default Configuration Parameters
DEFAULT_OPENAI_MODEL = "gpt-4o"
RESEARCH_AGENT_SEARCH_QUERY = "latest HR trends 2025"
DEFAULT_OPENAI_TEMPERATURE = 0.7
