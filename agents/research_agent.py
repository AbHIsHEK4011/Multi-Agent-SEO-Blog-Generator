import requests
# import openai # No longer directly needed here
from bs4 import BeautifulSoup
import logging # Standard logging import
from crewai import Agent
from configs import BROWSERLESS_API_KEY, RESEARCH_AGENT_SEARCH_QUERY 
from utils import call_openai_api

logger = logging.getLogger(__name__) # Named logger

class ResearchAgent(Agent):
    def __init__(self, search_query: str = RESEARCH_AGENT_SEARCH_QUERY):
        super().__init__(
            role="Research Agent",
            goal="Find trending HR topics and collect relevant information.",
            backstory="An AI-powered HR researcher extracting the latest industry insights.",
            verbose=True, # CrewAI's verbose, not directly related to standard logging
            allow_delegation=False
        )
        self.search_query = search_query
        logger.info(f"{self.role} initialized with search query: '{self.search_query}'.")

    def fetch_trending_hr_articles(self):
        """Scrapes HR trend data using Browserless API and parses with BeautifulSoup."""
        logger.info(f"Fetching trending HR articles for query: '{self.search_query}'")
        search_url = f"https://www.google.com/search?q={self.search_query}" # Use self.search_query
        api_url = f"https://chrome.browserless.io/content?token={BROWSERLESS_API_KEY}"

        payload = {
            "url": search_url,
            "waitFor": "body",
            "gotoOptions": {"waitUntil": "networkidle2"},
        }

        try:
            response = requests.post(api_url, json=payload)
            response.raise_for_status()  # Raise an exception for bad status codes

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Try to extract specific content
                extracted_texts = []
                # General selectors for common content holding tags
                # This can be refined if the structure of target pages is known
                for element in soup.find_all(['p', 'h1', 'h2', 'h3', 'article', 'div']):
                    # Avoid overly broad divs by checking for some text content and maybe class names if needed
                    if element.name == 'div' and not element.find_all(['p', 'h1', 'h2', 'h3', 'article']):
                        # If a div doesn't contain other relevant tags, take its direct text if it's meaningful
                         if len(element.get_text(separator=' ', strip=True)) > 50: # Arbitrary length to consider it meaningful
                            extracted_texts.append(element.get_text(separator=' ', strip=True))
                    elif element.name != 'div': # For p, h1, h2, h3, article
                        extracted_texts.append(element.get_text(separator=' ', strip=True))

                content = "\n".join(extracted_texts)

                if len(content) < 200: # If very little content extracted, fall back to full text
                    logger.warning("Falling back to full text extraction as specific content selectors yielded minimal results.")
                    content = soup.get_text(separator=' ', strip=True)
                logger.info(f"Successfully fetched and parsed content for query: '{self.search_query}'. Content length: {len(content)}")
                return content
            else:
                # This case might be redundant due to raise_for_status(), but kept for clarity
                logger.error(f"Error fetching HR trends. Status code: {response.status_code} for query: '{self.search_query}'")
                return f"Error fetching HR trends. Status code: {response.status_code}"

        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching content via Browserless for query '{self.search_query}': {e}", exc_info=True)
            return f"Error fetching content: {e}"
        except Exception as e: # Catch any other unexpected errors during parsing
            logger.error(f"An unexpected error occurred during content fetching/parsing for query '{self.search_query}': {e}", exc_info=True)
            return f"An unexpected error occurred: {e}"


    def execute(self):
        logger.info(f"Starting execution for {self.role} with query: '{self.search_query}'.")
        
        processed_text = self.fetch_trending_hr_articles()
        logger.debug(f"Received processed text of length: {len(processed_text)} for query: '{self.search_query}'.")


        if "Error fetching content" in processed_text or \
           "An unexpected error occurred" in processed_text or \
           "Error fetching HR trends" in processed_text:
            logger.error(f"Execution failed for {self.role} due to error in fetching/processing: {processed_text}")
            return processed_text # Return error message from fetching step

        # Summarize research using the utility function
        system_prompt = f"Summarize key insights for the query '{self.search_query}' from the given text content."
        summary = call_openai_api(system_prompt=system_prompt, user_prompt=processed_text)
        
        if "Error:" in summary: # Check if the utility function returned an error
            logger.error(f"Execution failed for {self.role} due to OpenAI API error: {summary}")
        else:
            logger.info(f"Execution completed for {self.role}. Summary length: {len(summary)}")
        return summary
