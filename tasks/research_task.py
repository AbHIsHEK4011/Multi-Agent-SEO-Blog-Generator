from crewai import Task
from agents.research_agent import ResearchAgent

research_task = Task(
        description="Gather HR trends for 2025.",
        agent=ResearchAgent(),
        expected_output="A summary of trending HR topics."
    )
