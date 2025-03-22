import openai
from crewai import Agent
from configs import OPENAI_API_KEY


class ContentGenerationAgent(Agent):
    def __init__(self):
        super().__init__(
            role="Content Generation Agent",
            goal="Generate a well-structured blog post based on the outline.",
            backstory="A skilled AI HR content writer.",
            verbose=True,
            allow_delegation=False
        )

    def execute(self, outline):
        openai.api_key = OPENAI_API_KEY
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Write a 2000-word HR blog based on the outline."},
                {"role": "user", "content": outline}
            ]
        )
        return response["choices"][0]["message"]["content"]
