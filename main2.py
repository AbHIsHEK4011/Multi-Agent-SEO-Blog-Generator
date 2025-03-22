import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
import requests
import openai

load_dotenv()


# Load API Keys from Environment Variables
BROWSERLESS_API_KEY = os.getenv("BROWSERLESS_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# Research Agent - Fetches HR Trends Using Browserless API
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
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Summarize key HR trends for 2025 from the given HTML content."},
                {"role": "user", "content": raw_html}
            ]
        )

        return response["choices"][0]["message"]["content"]


# Content Planning Agent - Generates a Blog Outline
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
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Create a structured blog outline based on the research summary."},
                {"role": "user", "content": research_summary}
            ]
        )
        return response["choices"][0]["message"]["content"]


# Content Generation Agent - Writes the Blog
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
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Write a 2000-word HR blog based on the outline."},
                {"role": "user", "content": outline}
            ]
        )
        return response["choices"][0]["message"]["content"]


# SEO Optimization Agent - Enhances Content
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
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system",
                 "content": "Optimize this blog for SEO with keywords, meta descriptions, and readability improvements."},
                {"role": "user", "content": blog_content}
            ]
        )
        return response["choices"][0]["message"]["content"]


# Review Agent - Proofreads and Refines Content
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
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system",
                 "content": "Proofread this blog and refine it for readability, grammar, and coherence."},
                {"role": "user", "content": optimized_content}
            ]
        )
        return response["choices"][0]["message"]["content"]


research_agent = ResearchAgent()
content_planning_agent = ContentPlanningAgent()
content_generation_agent = ContentGenerationAgent()
seo_optimize_agent = SEOOptimizeAgent()
review_agent = ReviewAgent()

# Define Tasks
research_task = Task(
        description="Gather HR trends for 2025.",
        agent=research_agent,
        expected_output="A summary of trending HR topics."
    )

content_planning_task = Task(
        description="Create a blog outline based on research.",
        agent=content_planning_agent,
        expected_output="A detailed blog outline with headings and subheadings."
    )

content_generation_task = Task(
        description="Generate a 2000-word blog post.",
        agent=content_generation_agent,
        expected_output="A well-written HR blog article."
    )

seo_optimize_task = Task(
        description="Optimize the blog for SEO.",
        agent=seo_optimize_agent,
        expected_output="An SEO-optimized blog with proper keywords and meta descriptions."
    )

review_task = Task(
        description="Proofread and finalize the content.",
        agent=review_agent,
        expected_output="Final high-quality, proofread content ready for publishing."
    )

# Define Crew
crew = Crew(
    agents=[research_agent, content_planning_agent, content_generation_agent, seo_optimize_agent, review_agent],
    tasks=[research_task, content_planning_task, content_generation_task, seo_optimize_task, review_task]
)

# Execute CrewAI System
if __name__ == "__main__":
    print("Running CrewAI-based Blog Generation System")
    results = crew.kickoff()
    with open("crewai_blog.txt", "w", encoding="utf-8") as file:
        file.write(str(results))
    print("✅ Final Output:", results)