from crewai import Task
# Agent is assigned in main.py, so no need to import or assign here.

research_task = Task(
    description="Research the latest trends in HR for 2025 and create a summary.", # Updated description for consistency
    # agent will be assigned in main.py
    expected_output="A concise summary of 3-5 key trending topics related to the search query, "
                    "including brief explanations for each. The summary should be suitable for "
                    "informing a blog post."
)
