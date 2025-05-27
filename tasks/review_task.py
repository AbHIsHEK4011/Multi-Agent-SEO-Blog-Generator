from crewai import Task
# Agent is assigned in main.py, so no need to import or assign here.

review_task = Task(
    description="Proofread and refine the final content for quality.", # Consistent description
    # agent will be assigned in main.py
    expected_output="A reviewed version of the blog post, corrected for grammar, spelling, clarity, "
                    "and factual accuracy. Feedback should also include suggestions for improving flow, "
                    "engagement, and ensuring the content aligns with the original plan and research. "
                    "Output should be the final, polished blog post."
)
