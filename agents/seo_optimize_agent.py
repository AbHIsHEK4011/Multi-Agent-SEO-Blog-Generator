import openai
from crewai import Agent
from configs import OPENAI_API_KEY


class SEOOptimizeAgent(Agent):
    def __init__(self):
        super().__init__(
            role="SEO Optimization Agent",
            goal="Optimize the blog post for SEO.",
            backstory="An AI SEO expert improving rankings.",
            verbose=True,
            allow_delegation=False
        )

    def execute(self, blog_content):
        openai.api_key = OPENAI_API_KEY
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system",
                 "content": "Optimize this blog for SEO with keywords, meta descriptions, and readability improvements."},
                {"role": "user", "content": blog_content}
            ]
        )
        return response["choices"][0]["message"]["content"]

