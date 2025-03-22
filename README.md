# Multi-Agent Blog Generation System

## 📌 System Architecture
This project is a **multi-agent system** that automates the creation of high-quality, SEO-optimized blog posts on **trending HR topics**. The system follows a structured workflow where multiple AI-powered agents collaborate to research, plan, generate, optimize, and review blog content.

### **🔹 Components**
1. **Research Agent** - Gathers trending HR topics and relevant data from the web.
2. **Content Planning Agent** - Structures the research into a detailed blog outline.
3. **Content Generation Agent** - Writes the blog based on the structured outline.
4. **SEO Optimization Agent** - Ensures the blog follows SEO best practices.
5. **Review Agent** - Proofreads and improves content quality before finalization.

---

## 📌 Agent Workflow
Each agent performs a specific task in the **content creation pipeline**:

1️⃣ **Research Agent** scrapes trending HR topics using **Browserless API** and summarizes key insights using **OpenAI GPT-4o**.

2️⃣ **Content Planning Agent** generates a structured blog outline based on research findings.

3️⃣ **Content Generation Agent** writes a well-structured blog post using OpenAI's GPT model.

4️⃣ **SEO Optimization Agent** enhances the blog's SEO by adding keywords, meta descriptions, and readability improvements.

5️⃣ **Review Agent** proofreads the content, ensuring grammar accuracy, coherence, and final touch-ups.

✅ **Final Output:** A **~2000-word SEO-optimized blog post** ready for publishing.

---

## 📌 Tools and Frameworks Used
- **Python** - Programming language for the entire system.
- **CrewAI** - Multi-agent task orchestration.
- **OpenAI GPT-4o** - AI-based content generation.
- **Browserless API** - Web scraping for research.
- **Pydantic** - Data validation for task execution.
- **Requests** - API communication.
- **GitHub** - Version control and code management.

---

## 📌 Installation and Execution Steps
Follow these steps to **set up and run** the multi-agent blog generation system.

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/your-username/blog-automation.git
cd blog-automation
```

### **2️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **3️⃣ Configure API Keys**
Create a `config.py` file and add your API keys:
```python
# config.py
OPENAI_API_KEY = "your-openai-api-key"
BROWSERLESS_API_KEY = "your-browserless-api-key"
```

### **4️⃣ Run the System**
```sh
python main.py
```

### **5️⃣ View the Output**
After execution, the **generated blog post** will be displayed in the terminal or saved in the `output/` folder.

---

## 📌 Project Structure
```sh
blog-automation/
│── main.py                   # Entry point for execution
│── agents/
│   ├── research_agent.py     # Research agent
│   ├── content_planning_agent.py  # Planning agent
│   ├── content_generation_agent.py # Generation agent
│   ├── seo_agent.py          # SEO optimization agent
│   ├── review_agent.py       # Review agent
│── tasks/
│   ├── research_task.py      # Research task
│   ├── planning_task.py      # Planning task
│   ├── generation_task.py    # Content generation task
│   ├── seo_task.py           # SEO task
│   ├── review_task.py        # Review task
│── config.py                 # API keys and settings
│── requirements.txt           # Python dependencies
│── README.md                  # Documentation
│── .gitignore                 # Ignore unnecessary files

```

---

## 📌 Contributions
Feel free to **fork this repository** and improve the system! If you find bugs or have feature requests, create an issue or submit a pull request.

🚀 **Happy Coding!** 🎯
