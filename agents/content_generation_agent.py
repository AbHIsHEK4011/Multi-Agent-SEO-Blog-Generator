import logging # Standard logging import
from crewai import Agent
from utils import call_openai_api

logger = logging.getLogger(__name__) # Named logger

class ContentGenerationAgent(Agent):
    def __init__(self):
        super().__init__(
            role="Content Generation Agent",
            goal="Generate a well-structured blog post based on the outline.",
            backstory="A skilled AI HR content writer.",
            verbose=True, # CrewAI's verbose
            allow_delegation=False
        )
        logger.info(f"{self.role} initialized.")

    def execute(self, outline: str):
        """Generates a blog post from an outline using the OpenAI utility function."""
        logger.info(f"Starting execution for {self.role}.")
        logger.debug(f"Received outline of length: {len(outline)}")
        
        system_prompt = "Write a 2000-word HR blog based on the outline."
        user_prompt = outline
        
        blog_post = call_openai_api(system_prompt=system_prompt, user_prompt=user_prompt)
        
        if "Error:" in blog_post: # Check if the utility function returned an error
            logger.error(f"Execution failed for {self.role}: {blog_post}")
        else:
            logger.info(f"Execution completed for {self.role}. Blog post length: {len(blog_post)}")
        return blog_post
