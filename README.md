# 🧠 AI in Healthcare Research Project

This project demonstrates the use of **CrewAI**, a multi-agent orchestration framework, to simulate collaboration between two AI agents working on the topic **"AI in Healthcare"**. The agents autonomously research, analyze, and generate content using the Gemini LLM and Serper search tool.

---

## 🔍 Project Overview

### 👤 Agents
- **Senior Research Analyst**
  - Conducts in-depth web research on AI in healthcare.
  - Uses Serper (Google Search API) to gather credible data.
  - Outputs a structured research brief with analysis, trends, and statistics.

- **Content Writer**
  - Converts the research brief into a well-formatted, engaging blog post.
  - Focuses on clarity, readability, and markdown formatting with citations.

---

## 🛠️ Tech Stack

- **Python**
- **CrewAI** (Multi-agent task management)
- **Serper API** (Web search tool)
- **Gemini LLM** (for content generation)
- **AgentOps** (Agent behavior monitoring)

---

## 📁 Project Structure

```bash
crewaidemo/
├── app.py                # Main script to define agents, tasks, and run the crew
├── .env                  # API keys and environment variables
├── requirements.txt      # Required packages
└── venv/                 # Virtual environment
