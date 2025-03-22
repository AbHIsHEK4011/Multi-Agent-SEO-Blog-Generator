import openai
from crewai import Agent
from configs import OPENAI_API_KEY


class ReviewAgent(Agent):
    def __init__(self):
        super().__init__(
            role="Review Agent",
            goal="Proofread and refine the final content for quality.",
            backstory="An AI professional editor ensuring high-quality writing.",
            verbose=True,
            allow_delegation=False
        )

    def execute(self, optimized_content):
        openai.api_key = OPENAI_API_KEY
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system",
                 "content": "Proofread this blog and refine it for readability, grammar, and coherence."},
                {"role": "user", "content": optimized_content}
            ]
        )
        return response["choices"][0]["message"]["content"]
