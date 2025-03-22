from crewai import Task
from agents.content_planning_agent import ContentPlanningAgent

content_planning_task = Task(
        description="Create a blog outline based on research.",
        agent=ContentPlanningAgent(),
        expected_output="A detailed blog outline with headings and subheadings."
    )
