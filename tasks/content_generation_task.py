from crewai import Task
from agents.content_generation_agent import ContentGenerationAgent
content_generation_task = Task(
        description="Generate a 2000-word blog post.",
        agent=ContentGenerationAgent(),
        expected_output="A well-written HR blog article."
    )
