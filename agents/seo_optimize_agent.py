import logging # Standard logging import
from crewai import Agent
from utils import call_openai_api

logger = logging.getLogger(__name__) # Named logger

class SEOOptimizeAgent(Agent):
    def __init__(self):
        super().__init__(
            role="SEO Optimization Agent",
            goal="Optimize the blog post for SEO.",
            backstory="An AI SEO expert improving rankings.",
            verbose=True, # CrewAI's verbose
            allow_delegation=False
        )
        logger.info(f"{self.role} initialized.")

    def execute(self, blog_content: str):
        """Optimizes the blog post for SEO using the OpenAI utility function."""
        logger.info(f"Starting execution for {self.role}.")
        logger.debug(f"Received blog content of length: {len(blog_content)}")
        
        system_prompt = "Optimize this blog for SEO with keywords, meta descriptions, and readability improvements."
        user_prompt = blog_content
        
        optimized_content = call_openai_api(system_prompt=system_prompt, user_prompt=user_prompt)
        
        if "Error:" in optimized_content: # Check if the utility function returned an error
            logger.error(f"Execution failed for {self.role}: {optimized_content}")
        else:
            logger.info(f"Execution completed for {self.role}. Optimized content length: {len(optimized_content)}")
        return optimized_content

