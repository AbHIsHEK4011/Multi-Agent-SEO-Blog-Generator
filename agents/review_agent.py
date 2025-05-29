import logging # Standard logging import
from crewai import Agent
from utils import call_openai_api

logger = logging.getLogger(__name__) # Named logger

class ReviewAgent(Agent):
    def __init__(self):
        super().__init__(
            role="Review Agent",
            goal="Proofread and refine the final content for quality.",
            backstory="An AI professional editor ensuring high-quality writing.",
            verbose=True, # CrewAI's verbose
            allow_delegation=False
        )
        logger.info(f"{self.role} initialized.")

    def execute(self, optimized_content: str):
        """Proofreads and refines the blog content using the OpenAI utility function."""
        logger.info(f"Starting execution for {self.role}.")
        logger.debug(f"Received optimized content of length: {len(optimized_content)}")
        
        system_prompt = "Proofread this blog and refine it for readability, grammar, and coherence."
        user_prompt = optimized_content
        
        reviewed_content = call_openai_api(system_prompt=system_prompt, user_prompt=user_prompt)
        
        if "Error:" in reviewed_content: # Check if the utility function returned an error
            logger.error(f"Execution failed for {self.role}: {reviewed_content}")
        else:
            logger.info(f"Execution completed for {self.role}. Reviewed content length: {len(reviewed_content)}")
        return reviewed_content
