from crewai import Task
# Agent is assigned in main.py, so no need to import or assign here.

content_generation_task = Task(
    description="Generate a well-structured blog post based on the outline.", # Updated description for consistency
    # agent will be assigned in main.py
    expected_output="A well-written, engaging blog post of approximately 800-1200 words, based on the "
                    "provided outline. The tone should be informative yet accessible. Include practical "
                    "examples where relevant and a concluding paragraph that summarizes key takeaways."
)
