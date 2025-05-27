import logging # Import logging

# Configure basic logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.StreamHandler()])
                    # For file logging, add: logging.FileHandler("app.log")

                    # For file logging, add: logging.FileHandler("app.log")

from crewai import Crew
from agents.research_agent import ResearchAgent
from configs import RESEARCH_AGENT_SEARCH_QUERY # Add this import
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
research_agent = ResearchAgent(search_query=RESEARCH_AGENT_SEARCH_QUERY) # Explicitly use imported config
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
    logging.info("🚀 Running Multi-Agent Blog System...")
    try:
        results = crew.kickoff()
        # It's good practice to log the nature of the results if possible, or at least their existence.
        # For now, we'll assume `results` can be converted to a string for logging/saving.
        logging.info(f"Crew kickoff completed. Results type: {type(results)}") 
        
        output_file = "crewai_blog_output.txt" # Changed filename slightly for clarity
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(str(results))
        logging.info(f"Results written to {output_file}")
        logging.info("✅ Blog Generated Successfully!")
    except Exception as e:
        logging.error(f"An error occurred during the crew kickoff: {e}", exc_info=True)
