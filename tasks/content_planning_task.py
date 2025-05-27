from crewai import Task
# Agent is assigned in main.py, so no need to import or assign here.

content_planning_task = Task(
    description="Create a blog outline based on research findings.", # Updated description for consistency
    # agent will be assigned in main.py
    expected_output="A structured blog post outline with a clear title, an introduction, "
                    "3-5 main sections with descriptive headings (H2), and 2-3 sub-points "
                    "(H3 or bullet points) under each main section. Conclude with a summary section."
)
