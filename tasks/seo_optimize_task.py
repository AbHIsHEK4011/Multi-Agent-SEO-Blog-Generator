from crewai import Task
# Agent is assigned in main.py, so no need to import or assign here.

seo_optimize_task = Task(
    description="Optimize the blog post for SEO.", # Consistent description
    # agent will be assigned in main.py
    expected_output="The original blog post content, enhanced with relevant keywords (if a list is "
                    "provided or derivable), an optimized title, and a meta description (150-160 characters). "
                    "Keywords should be naturally integrated."
)
