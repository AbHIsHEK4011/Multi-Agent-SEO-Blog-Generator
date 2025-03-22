import requests
import openai
from crewai import Agent
from configs import BROWSERLESS_API_KEY, OPENAI_API_KEY


class ResearchAgent(Agent):
    def __init__(self):
        super().__init__(
            role="Research Agent",
            goal="Find trending HR topics and collect relevant information.",
            backstory="An AI-powered HR researcher extracting the latest industry insights.",
            verbose=True,
            allow_delegation=False
        )

    def fetch_trending_hr_articles(self):
        """Scrapes HR trend data using Browserless API"""
        search_url = "https://www.google.com/search?q=latest+HR+trends+2025"
        api_url = f"https://chrome.browserless.io/content?token={BROWSERLESS_API_KEY}"

        payload = {
            "url": search_url,
            "waitFor": "body",
            "gotoOptions": {"waitUntil": "networkidle2"},
        }

        response = requests.post(api_url, json=payload)

        if response.status_code == 200:
            return response.text
        else:
            return "Error fetching HR trends."

    def execute(self):
        raw_html = self.fetch_trending_hr_articles()

        # Summarize research using OpenAI
        openai.api_key = OPENAI_API_KEY
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Summarize key HR trends for 2025 from the given HTML content."},
                {"role": "user", "content": raw_html}
            ]
        )

        return response["choices"][0]["message"]["content"]
