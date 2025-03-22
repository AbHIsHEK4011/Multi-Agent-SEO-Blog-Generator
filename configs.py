import os
from dotenv import load_dotenv
load_dotenv()

# Load API Keys from Environment Variables
BROWSERLESS_API_KEY = os.getenv("BROWSERLESS_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
