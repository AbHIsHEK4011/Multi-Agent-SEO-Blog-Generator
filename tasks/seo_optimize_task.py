from crewai import Task
from agents.seo_optimize_agent import SEOOptimizeAgent
seo_optimize_task = Task(
        description="Optimize the blog for SEO.",
        agent=SEOOptimizeAgent(),
        expected_output="An SEO-optimized blog with proper keywords and meta descriptions."
    )
