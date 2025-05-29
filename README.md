# AI-Powered Multi-Agent Blog Generation System

## Overview

This project automates the creation of high-quality, SEO-optimized blog posts using a collaborative team of AI agents. It leverages the CrewAI framework to orchestrate the workflow between different specialized agents, each contributing to a stage of the content creation process, from research to final review.

## Features

*   **Automated Content Pipeline:** End-to-end automation of blog post creation, including research, planning, drafting, SEO, and review.
*   **Specialized AI Agents:** Utilizes a team of distinct AI agents, each with a specific role and expertise.
*   **CrewAI Framework:** Built on CrewAI for robust multi-agent task management and orchestration.
*   **Configurable Parameters:**
    *   OpenAI models (e.g., "gpt-4o", "gpt-3.5-turbo") can be set in `configs.py`.
    *   OpenAI API temperature is configurable for content generation.
    *   Default search query for the ResearchAgent can be modified.
*   **Web Research:** The ResearchAgent uses Browserless API for scraping web content for up-to-date information.
*   **HTML Parsing:** Uses BeautifulSoup for parsing HTML content during research.
*   **Error Handling:** Includes try-except blocks for API calls and other operations.
*   **Logging:** Comprehensive logging is implemented throughout the application, providing insights into the execution flow and aiding in debugging. Log messages are printed to the console.

## Workflow / Agents

The system employs a series of AI agents that work sequentially:

1.  **Research Agent:**
    *   **Goal:** Find trending topics (e.g., HR trends) and collect relevant information.
    *   **Tools:** Uses Browserless API for web scraping and BeautifulSoup for HTML parsing.
    *   **Output:** A summary of key findings based on the configured search query.

2.  **Content Planning Agent:**
    *   **Goal:** Create a structured blog post outline based on the research findings.
    *   **Output:** A detailed outline with headings, subheadings, and key points.

3.  **Content Generation Agent:**
    *   **Goal:** Generate a well-structured and engaging blog post based on the provided outline.
    *   **Output:** A draft of the blog post.

4.  **SEO Optimization Agent:**
    *   **Goal:** Optimize the blog post for search engines.
    *   **Output:** The blog post enhanced with relevant keywords, an optimized title, and a meta description.

5.  **Review Agent:**
    *   **Goal:** Proofread and refine the final content for quality, grammar, coherence, and factual accuracy.
    *   **Output:** The final, polished blog post ready for publishing.

## Setup and Installation

### Prerequisites

*   Python 3.8 or higher
*   pip (Python package installer)

### Steps

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/AbHIsHEK4011/Multi-Agent-SEO-Blog-Generator.git
    ```

2.  **Navigate to the project directory:**
    ```bash
    cd Multi-Agent-SEO-Blog-Generator
    ```

3.  **Install dependencies:**
    Ensure your `requirements.txt` file is up-to-date (it should include `crewai`, `openai`, `python-dotenv`, `requests`, and `beautifulsoup4`). Then run:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Environment Variables:**
    This project requires API keys for OpenAI and Browserless.
    *   Create a file named `.env` in the root of the project directory.
    *   Add your API keys to the `.env` file. Use the following template:

        ```env
        OPENAI_API_KEY="your_openai_api_key_here"
        BROWSERLESS_API_KEY="your_browserless_api_key_here"
        ```

    *   **Where to get the keys:**
        *   **OpenAI API Key:** Visit [platform.openai.com/api-keys](https://platform.openai.com/api-keys).
        *   **Browserless API Key:** Visit [www.browserless.io](https://www.browserless.io/) and sign up for an API key.

## Configuration

Key operational parameters can be configured by directly editing the `configs.py` file:

*   `DEFAULT_OPENAI_MODEL` (string): Sets the default OpenAI model to be used by the agents (e.g., `"gpt-4o"`, `"gpt-3.5-turbo"`).
*   `DEFAULT_OPENAI_TEMPERATURE` (float): Controls the creativity of the AI's responses. A value between 0.0 (more deterministic) and 1.0 (more creative, up to 2.0 for some models). Default is `0.7`.
*   `RESEARCH_AGENT_SEARCH_QUERY` (string): Defines the default search query that the ResearchAgent will use if not overridden. Default is `"latest HR trends 2025"`.

To change these, open `configs.py` and modify the variable values directly.

## Running the Project

1.  Ensure all setup and configuration steps are completed.
2.  Run the main script from the project root directory:
    ```bash
    python main.py
    ```
3.  **Output:**
    *   The generated blog post will be saved to a file named `crewai_blog_output.txt` in the project's root directory.
    *   Execution logs, including agent activities and potential errors, will be printed to the console.

## Project Structure

```
.
├── agents/                     # Contains individual agent definitions
│   ├── research_agent.py
│   ├── content_planning_agent.py
│   ├── content_generation_agent.py
│   ├── seo_optimize_agent.py
│   └── review_agent.py
├── tasks/                      # Contains task definitions for CrewAI
│   ├── research_task.py
│   ├── content_planning_task.py
│   ├── content_generation_task.py
│   ├── seo_optimize_task.py
│   └── review_task.py
├── configs.py                  # Project-wide configurations (API keys loaded via dotenv, model params)
├── utils.py                    # Utility functions (e.g., call_openai_api)
├── main.py                     # Main script to initialize and run the CrewAI crew
├── requirements.txt            # Python dependencies for the project
├── .env                        # For storing API keys (not version controlled)
└── README.md                   # This file
```

## To Do / Potential Improvements

*   **More Sophisticated Content Extraction:** Improve the HTML parsing in `ResearchAgent` to more accurately extract main content from diverse web page structures.
*   **Keyword Input for SEO Agent:** Allow dynamic input of keywords for the `SEOOptimizeAgent`, perhaps from user input or an earlier analysis step.
*   **Fact Verification Agent:** Introduce an agent specifically for verifying facts and statistics mentioned in the generated content.
*   **Image Suggestion/Generation Agent:** Add an agent to suggest relevant images or even generate them using models like DALL-E.
*   **Plagiarism Check:** Integrate a plagiarism checker.
*   **Customizable Output Formats:** Allow output in different formats (e.g., Markdown, HTML directly).
*   **Interactive Mode:** Allow users to provide input/feedback at different stages of the workflow.
*   **File-based Logging:** Extend current logging to also write to a dedicated log file (e.g., `app.log`) in addition to console output for easier post-run analysis.

## Contributions

Contributions are welcome! If you have suggestions for improvements or find any bugs, please feel free to open an issue or submit a pull request.

---

🚀 Happy Automating!
