from crewai import Crew
from agents.research_agent import ResearchAgent
from agents.content_planning_agent import ContentPlanningAgent
from agents.content_generation_agent import ContentGenerationAgent
from agents.seo_optimize_agent import SEOOptimizeAgent
from agents.review_agent import ReviewAgent
from tasks.research_task import research_task
from tasks.content_planning_task import content_planning_task
from tasks.content_generation_task import content_generation_task
from tasks.seo_optimize_task import seo_optimize_task
from tasks.review_task import review_task

# Initialize all agents
research_agent = ResearchAgent()
content_planning_agent = ContentPlanningAgent()
content_generation_agent = ContentGenerationAgent()
seo_optimize_agent = SEOOptimizeAgent()
review_agent = ReviewAgent()

# Assign agents to tasks
research_task.agent = research_agent
content_planning_task.agent = content_planning_agent
content_generation_task.agent = content_generation_agent
seo_optimize_task.agent = seo_optimize_agent
review_task.agent = review_agent

# Create and execute CrewAI workflow
crew = Crew(tasks=[research_task, content_planning_task, content_generation_task, seo_optimize_task, review_task])

if __name__ == "__main__":
    print("🚀 Running Multi-Agent Blog System...")
    results = crew.kickoff()
    with open("crewai_blog2.txt", "w", encoding="utf-8") as file:
        file.write(str(results))
    print("✅ Blog Generated Successfully!")
