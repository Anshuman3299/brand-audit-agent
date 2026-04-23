A multi-agent AI system that generates comprehensive brand audit reports using live web data.

## Live Demo
https://web-production-782e2.up.railway.app

## What It Does
Enter any brand name and get a complete AI-powered audit in under 60 seconds:
- Searches live web for customer reviews, news, and social mentions
- Analyzes public perception using 4 specialized AI agents
- Produces a structured brand audit report
- Independently scores the report quality using LLM-as-Judge

## Agent Pipeline

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

## Tech Stack
- LLM: Llama 3.3 70B via Groq LPU
- Search: Tavily Search API
- Frontend: Streamlit
- Deployment: Railway
- Language: Python 3.13

## Agents

| Agent | Role | Input | Output |
|-------|------|-------|--------|
| Perception Researcher | Extracts themes from web data | Tavily search results | Structured perception report |
| Sentiment Analyst | Scores emotional tone | Perception report | Sentiment scores 0-10 |
| Audit Report Writer | Writes professional audit | Perception + Sentiment | Full structured report |
| LLM-as-Judge | Evaluates report quality | Audit report | Quality scores out of 50 |

## LLM-as-Judge Rubric
- Objectivity: 0-10
- Insight Depth: 0-10
- Actionability: 0-10
- Evidence Quality: 0-10
- Structural Clarity: 0-10
- Total: 50 points

## Local Setup

### 1. Clone the repo
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

### 4. Add API keys
```bash
cp .env.example .env
# Edit .env and add your keys
```

Get free API keys:
- Groq: https://console.groq.com
- Tavily: https://tavily.com

### 5. Run
```bash
streamlit run app.py
```

## Project Context
Semester IV B.E. Electronics and Communication
Agentic AI Systems Project
