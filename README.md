
# 🔍 Brand Audit AI Agent

> A multi-agent AI system that generates comprehensive brand audit reports using live web data — powered by Groq LPU + Tavily Search + Streamlit.

![Python](https://img.shields.io/badge/Python-3.13-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35-red?style=flat-square&logo=streamlit)
![Groq](https://img.shields.io/badge/Groq-LPU-orange?style=flat-square)
![Tavily](https://img.shields.io/badge/Tavily-Search-green?style=flat-square)
![Railway](https://img.shields.io/badge/Deployed-Railway-purple?style=flat-square)

---

## 🌐 Live Demo

**https://web-production-782e2.up.railway.app**

---

## 📌 What It Does

Enter any brand name and get a complete AI-powered audit in under 60 seconds.

The system searches the live web for customer reviews, news coverage, and social media mentions — then passes that data through 4 specialized AI agents to produce a structured, scored brand audit report.

---

## 🤖 Agent Pipeline

| Stage | Agent | Role | Input | Output |
|-------|-------|------|-------|--------|
| 1 | Perception Researcher | Extracts key themes from web data | Tavily search results | Structured perception report |
| 2 | Sentiment Analyst | Scores emotional tone across 5 dimensions | Perception report | Sentiment scores 0–10 |
| 3 | Audit Report Writer | Writes professional brand audit | Perception + Sentiment | Full structured report |
| 4 | LLM-as-Judge | Evaluates report quality | Audit report | Quality scores out of 50 |

## Agent Pipeline
```
User Input (Brand Name)
          ↓
Tavily Search (Live Web Data)
          ↓
Agent 1: Perception Researcher
          ↓
Agent 2: Sentiment Analyst
          ↓
Agent 3: Audit Report Writer
          ↓
Agent 4: LLM-as-Judge (Quality Scoring)
          ↓
Final Scored Brand Audit Report
```
---

## 🧠 LLM-as-Judge Rubric

Agent 4 independently evaluates the audit report using this rubric:

| Criterion | Max Score | What it checks |
|-----------|-----------|----------------|
| Objectivity | 10 | Is it balanced and evidence-based? |
| Insight Depth | 10 | Are there non-obvious useful insights? |
| Actionability | 10 | Are recommendations specific and clear? |
| Evidence Quality | 10 | Are claims backed by data? |
| Structural Clarity | 10 | Is it well organized? |
| **Total** | **50** | |

---

## ⚙️ Tech Stack

| Component | Technology |
|-----------|-----------|
| LLM | Llama 3.3 70B via Groq LPU API |
| Search Tool | Tavily Search API |
| Frontend | Streamlit |
| Deployment | Railway |
| Language | Python 3.13 |

---

## 🗂️ Project Layout

## Project layout
```
.
├── app.py                 # Streamlit UI
├── config.py              # Env loading, API key helpers, model defaults
├── gemini_agents.py       # Multi-step campaign pipeline
├── tools                  # Function-calling tools (catalog, Tavily search)
├── architecture.png       # Architecture Diagram
├── problem_statement.txt  # Generated images + Markdown (gitignored except .gitkeep)
├── requirements.txt
├── .env.example.pages     # Template only — copy to `.env` locally
└── README.md
```
---

## 🚀 Local Setup

### 1. Clone the repository
```bash
git clone https://github.com/Anshuman3299/brand-audit-agent
cd brand-audit-agent
```

### 2. Create virtual environment
```bash
python3.13 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure API keys
```bash
cp .env.example .env
```

Edit `.env` and add your keys:

Get your free API keys:
- Groq: [console.groq.com](https://console.groq.com)
- Tavily: [tavily.com](https://tavily.com)

### 5. Run the app
```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🔧 Configuration Reference

| Variable | Required | Description |
|----------|----------|-------------|
| `GROQ_API_KEY` | Yes | Groq API key for Llama 3.3 70B |
| `TAVILY_API_KEY` | Yes | Tavily Search API key for live web search |

---

## 📊 Why Multi-Agent?

A single LLM prompt cannot reliably search the web, analyze sentiment, write a structured report, AND evaluate its own quality simultaneously.

By splitting into 4 specialized agents:
- Each agent has a focused system prompt for its specific task
- Output quality improves significantly at each stage
- The pipeline mirrors how real brand consultancies work
- LLM-as-Judge provides independent quality assurance

## 🎥 Demo Video

Brand Audit AI Agent Demo
**https://www.loom.com/share/e0a569b075874227aca0bdb6a3f57cc0**


## 📁 Related Links

| Resource | Link |
|----------|------|
| Live App | [web-production-782e2.up.railway.app](https://web-production-782e2.up.railway.app) |
| GitHub | [github.com/Anshuman3299/brand-audit-agent](https://github.com/Anshuman3299/brand-audit-agent) |
| Groq API | [console.groq.com](https://console.groq.com) |
| Tavily API | [tavily.com](https://tavily.com) |

---

## 👨‍💻 Built By
**Anshuman Deshmukh**

B.Tech. Electronics and Communication — Semester IV
Agentic AI Systems Project
