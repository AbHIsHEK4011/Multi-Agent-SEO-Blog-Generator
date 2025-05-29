import logging # Standard logging import
from crewai import Agent
from utils import call_openai_api 

logger = logging.getLogger(__name__) # Named logger

class ContentPlanningAgent(Agent):
    def __init__(self):
        super().__init__(
            role="Content Planning Agent",
            goal="Create a structured blog outline based on research findings.",
            backstory="An expert content strategist.",
            verbose=True, # CrewAI's verbose
            allow_delegation=False
        )
        logger.info(f"{self.role} initialized.")

    def execute(self, research_summary: str):
        """Generates a blog outline from research data using the OpenAI utility function."""
        logger.info(f"Starting execution for {self.role}.")
        logger.debug(f"Received research summary of length: {len(research_summary)}")
        
        system_prompt = "Create a structured blog outline based on the research summary."
        user_prompt = research_summary
        
        outline = call_openai_api(system_prompt=system_prompt, user_prompt=user_prompt)
        
        if "Error:" in outline: # Check if the utility function returned an error
            logger.error(f"Execution failed for {self.role}: {outline}")
        else:
            logger.info(f"Execution completed for {self.role}. Outline length: {len(outline)}")
        return outline
