from crewai import Task
from agents.review_agent import ReviewAgent
review_task = Task(
        description="Proofread and finalize the content.",
        agent=ReviewAgent(),
        expected_output="Final high-quality, proofread content ready for publishing."
    )
