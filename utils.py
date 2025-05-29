import openai
import logging
from configs import OPENAI_API_KEY, DEFAULT_OPENAI_MODEL, DEFAULT_OPENAI_TEMPERATURE

# Get a logger instance for this module
logger = logging.getLogger(__name__)

# Note: BasicConfig should ideally be in main.py or the entry point of the application.
# If it's here and also in main.py, the first one called takes precedence.
# For this task, we'll assume main.py's config is the primary one.

def call_openai_api(system_prompt: str, user_prompt: str, model: str = DEFAULT_OPENAI_MODEL, temperature: float = DEFAULT_OPENAI_TEMPERATURE) -> str:
    """
    Calls the OpenAI ChatCompletion API with specified parameters (defaulting to values from configs.py) and robust error handling.

    Args:
        system_prompt: The system message to set the context for the AI.
        user_prompt: The user's message or query.
        model: The OpenAI model to use (e.g., "gpt-4o", "gpt-3.5-turbo").
        temperature: The sampling temperature for generation (0.0 to 2.0).

    Returns:
        The content of the AI's response message, or an error message string if an API call fails.
    """
    try:
        openai.api_key = OPENAI_API_KEY
        
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=temperature
        )
        
        if response and response.choices and len(response.choices) > 0:
            return response.choices[0].message.content.strip()
        else:
            logger.error("OpenAI API call returned an unexpected response structure.")
            return "Error: OpenAI API call returned an unexpected response structure."

    except openai.APIError as e:
        logger.error(f"OpenAI API Error: {e}. Status: {e.http_status}. Code: {e.code}", exc_info=True)
        return f"Error: OpenAI API call failed. Details: {e}"
    except openai.Timeout as e:
        logger.error(f"OpenAI Timeout Error: {e}", exc_info=True)
        return f"Error: OpenAI request timed out. Details: {e}"
    except openai.RateLimitError as e:
        logger.error(f"OpenAI Rate Limit Error: {e}", exc_info=True)
        return f"Error: OpenAI rate limit exceeded. Details: {e}"
    except openai.APIConnectionError as e:
        logger.error(f"OpenAI API Connection Error: {e}", exc_info=True)
        return f"Error: Failed to connect to OpenAI API. Details: {e}"
    except openai.InvalidRequestError as e: # Specific error for invalid requests (e.g. bad parameters)
        logger.error(f"OpenAI Invalid Request Error: {e}. Param: {e.param}", exc_info=True)
        return f"Error: Invalid request to OpenAI API. Details: {e}"
    except openai.AuthenticationError as e: # Specific error for authentication issues
        logger.error(f"OpenAI Authentication Error: {e}", exc_info=True)
        return f"Error: OpenAI authentication failed. Check API key. Details: {e}"
    except openai.PermissionDeniedError as e: # Specific error for permission issues
        logger.error(f"OpenAI Permission Denied Error: {e}", exc_info=True)
        return f"Error: Permission denied for OpenAI API. Details: {e}"
    except openai.NotFoundError as e: # Specific error for not found issues (e.g. model not found)
        logger.error(f"OpenAI Not Found Error: {e}", exc_info=True)
        return f"Error: OpenAI resource not found. Details: {e}"
    except Exception as e:
        logger.error(f"An unexpected error occurred during OpenAI API call: {e}", exc_info=True)
        return f"Error: An unexpected error occurred. Details: {e}"
