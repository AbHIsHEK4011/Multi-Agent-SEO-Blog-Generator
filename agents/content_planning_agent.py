import openai
from crewai import Agent
from configs import OPENAI_API_KEY

class ContentPlanningAgent(Agent):
    def __init__(self):
        super().__init__(
            role="Content Planning Agent",
            goal="Create a structured blog outline based on research findings.",
            backstory="An expert content strategist.",
            verbose=True,
            allow_delegation=False
        )

    def execute(self, research_summary):
        """Generates a blog outline from research data."""
        openai.api_key = OPENAI_API_KEY
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Create a structured blog outline based on the research summary."},
                {"role": "user", "content": research_summary}
            ]
        )
        return response["choices"][0]["message"]["content"]
