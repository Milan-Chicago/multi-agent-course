# Agent Engineering Bootcamp: Developers Edition

Welcome to the official course repository for **Agent Engineering Bootcamp: Developers Edition**.

This repo is for **anyone** and contains all code, exercises, templates, and project materials used throughout the course.

**What makes this different?**
Move beyond theory and build production-ready AI systems. From Agentic RAG and Knowledge Graphs to Multi-Agent Workflows and LLM Guardrails — learn to architect, evaluate, and deploy AI applications that work in the real world.

🔗 [Visit course page](https://maven.com/boring-bot/advanced-llm) • 💾 [Save $200 with code 200OFF](https://maven.com/boring-bot/advanced-llm?promoCode=200OFF)

---
<img width="2752" height="1536" alt="unnamed-3" src="https://github.com/user-attachments/assets/a206c511-5e8b-42ce-abc2-f8e36f87861d" />


## Quick Links

- [Week 2: LLM Optimization & Deployment](#week-2-optimizing-and-deploying-large-language-models)
- [Week 3: Agentic RAG & Semantic Cache](#week-3-agentic-rag-rag-memory--semantic-cache)
- [Week 4: Knowledge Graphs (NEW!)](#week-4-knowledge-graphs-and-multi-agent-workflows)
- [Week 5: AI Agents](#week-5-agents)
- [Week 6: Responsible AI](#week-6-responsible-ai)
- [Technology Stack](#technology-stack)
- [What You'll Build](#what-youll-build)

---

## Recommended Resource

If you'd like to deepen your understanding of building LLM applications, refer to this book:

[**Build LLM Applications from Scratch**](https://www.manning.com/books/build-llm-applications-from-scratch)

---

## How to Use This Repo

- This repo contains supplemental content for the course. Content is organized **week by week**, aligned with live sessions and project milestones.
- **Google Colab Pro** is the preferred environment for running notebooks.
- You may also **clone the repo locally** and run notebooks using Jupyter or your IDE.
- Each notebook includes its own dependencies via `!pip install` — there is **no global `requirements.txt`**.

---

## Cloning the Repository (Optional)

```bash
git clone https://github.com/yourusername/enterprise-rag-agents.git
cd enterprise-rag-agents
python3 -m venv venv
source venv/bin/activate
```

## Weekly Breakdown

### Week 2: Optimizing and Deploying Large Language Models

- LLM Deployment and Hosting
- Mixture of Experts
- Quantization methods

TextSTreamer: [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hamzafarooq/multi-agent-course/blob/main/Module_2/Quantization/TextStreamer_Meta_Llama_3_1_8B_Instruct.ipynb)

Bitsnbytes Quantization: [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hamzafarooq/multi-agent-course/blob/main/Module_2/Quantization/Bitsnbytes_4bit_Quantization.ipynb)

---

### Week 3: Agentic RAG, RAG Memory & Semantic Cache

- Naive RAG vs Agentic RAG
- Agentic RAG Components
- Advanced Agents
- RAG Memory
- Semantic Cache

Upload Data to Qdrant: [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hamzafarooq/multi-agent-course/blob/main/Module_1/Agentic_RAG/Upload_data_to_Qdrant_Notebook.ipynb)

Agentic RAG: [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hamzafarooq/multi-agent-course/blob/main/Module_1/Agentic_RAG/Agentic_RAG_Notebook.ipynb)

Semantic Cache: [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hamzafarooq/multi-agent-course/blob/main/Module_3/Semantic_Cache/Semantic_cache_from_scratch.ipynb)

---

### Week 4: Knowledge Graphs and Multi-Agent Workflows

- Using knowledge graphs in RAG
- Principles of KG Standardization
- GraphRAG at scale
- **RAG vs Knowledge Graph Evaluation** (NEW!)
- Text-to-Cypher conversion with LLMs
- Interactive graph visualizations

**📊 Featured Project: RAG vs Knowledge Graph Comparison Framework**

A production-ready Streamlit application that objectively compares RAG and Knowledge Graph approaches using LLM-based evaluation. Includes interactive graph visualizations showing the exact data path used for each answer.

[View Full Documentation →](Module_4_Knowledge_Graphs/)

**Notebooks:**

Knowledge Graphs Basic Version: [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hamzafarooq/multi-agent-course/blob/main/Module_4/Knowledge_Graphs/Knowledge_Graphs_Basic_Version.ipynb)

Knowledge Graphs Advanced Version: [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hamzafarooq/multi-agent-course/blob/main/Module_4/Knowledge_Graphs/Knowledge_Graphs_Advanced_Version.ipynb)

**Interactive Demo:**

```bash
cd Module_4_Knowledge_Graphs
python setup.py  # One-time setup
streamlit run app.py
```

---

### Week 5: Agents

- Building LLM Agents from scratch
- AI Agents Frameworks - smolagents, AutoGen, etc.

AgentPro Starter Code: [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hamzafarooq/multi-agent-course/blob/main/Module_5/Agents/AgentPro%20Starter%20Code.ipynb)

Agent Pro from Scratch [old version]: [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hamzafarooq/multi-agent-course/blob/main/Module_5/Agents/Agent%20Pro%20from%20Scratch%20%5Bold%20version%5D.ipynb)

Agent Pro ReAct: [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hamzafarooq/multi-agent-course/blob/main/Module_5/Agents/Agent%20Pro%20ReAct.ipynb)

Smol Agents: [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hamzafarooq/multi-agent-course/blob/main/Module_5/Agents/Smol%20Agents.ipynb)

---

### Week 6: Responsible AI

- Guardrails and their impact on production systems

ADK A2A MCP: [![GitHub Folder](https://img.shields.io/badge/View%20on-GitHub-blue?logo=github)](https://github.com/hamzafarooq/multi-agent-course/tree/main/Module_6/A2A%20ADK%20MCP)

MCP (non-adk): [![GitHub Folder](https://img.shields.io/badge/View%20on-GitHub-blue?logo=github)](https://github.com/hamzafarooq/multi-agent-course/tree/main/Module_6/MCP%20(non-adk))

Ollama jailbreak: [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hamzafarooq/multi-agent-course/blob/main/Module_6/Ollama/Mistral%20Llama%203.1%20and%20Llama%203.2%20jailbreak.ipynb)

Llama Guard: [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hamzafarooq/multi-agent-course/blob/main/Module_6/Guardrails/Llama%20Guard.ipynb)

---

## Technology Stack

This course uses the following tools and services:

| Area                  | Tools / Frameworks                                   |
|-----------------------|------------------------------------------------------|
| **LLM Access**        | Ares API (via Traversaal.ai), OpenAI GPT-4o-mini     |
| **Agent Frameworks**  | ADK, A2A, CrewAI                                     |
| **Vector Search**     | FAISS (Colab), OpenSearch (optional)                 |
| **Graph Databases**   | Neo4j Aura, NetworkX                                 |
| **Memory & Caching**  | Redis Cloud (recommended setup)                      |
| **Web Interfaces**    | Streamlit, FastAPI                                   |
| **Visualizations**    | Pyvis, Plotly, Interactive Graph Rendering           |
| **Notebooks**         | Google Colab Pro (preferred), Jupyter (optional)     |
| **Deployments (Optional)** | AWS Lambda, Step Functions, FastAPI             |
| **Language**          | Python 3.10+                                         |

> You don't need to pre-install anything locally.
> All key dependencies are included in each notebook.
g
---

## What You'll Build

This course goes beyond theory. You'll build production-ready systems including:

- **Agentic RAG Systems** with advanced retrieval and semantic caching
- **Knowledge Graph Applications** with RAG vs KG evaluation framework
- **Interactive Dashboards** using Streamlit for real-time demos
- **Multi-Agent Workflows** with ADK and A2A and CrewAI
- **LLM-based Evaluators** for objective system comparison
- **Production Guardrails** for responsible AI deployment

Each module includes hands-on projects you can showcase in your portfolio.

---

## Student Feedback (Beta Cohort)

> "Finally a course that moves past theory and teaches **how to build AI systems that work**."
> "Everything was practical — I now know how to apply RAG and agents in real products."

---

## Ready to Master Multi-Agent Systems?

<a href="https://maven.com/boring-bot/advanced-llm?promoCode=200OFF">
  <img src="Module_4_Knowledge_Graphs/course_img.png" alt="Agent Engineering Bootcamp" width="600">
</a>

### Agent Engineering Bootcamp: Developers Edition

**Rating:** ⭐⭐⭐⭐⭐ 4.8/5 (96 reviews)

**Your Instructor:** Hamza Farooq
*Founder | Ex-Google | Professor at UCLA & UMN*

**What You'll Learn:**
- 🚀 Build production-ready multi-agent systems from scratch
- 🔍 Master RAG, Knowledge Graphs, and hybrid approaches
- 🛠️ Deploy AI systems that survive real-world conditions
- 📊 Implement LLM evaluation frameworks and guardrails
- 💼 Create portfolio-worthy projects with modern AI stacks

**Course Highlights:**
- 6 weeks of intensive, hands-on learning
- Live sessions with industry expert
- Production-ready code and templates
- Real-world case studies and architectures
- Certificate of completion

### [🎓 Enroll Now - Save $200 with code 200OFF →](https://maven.com/boring-bot/advanced-llm?promoCode=200OFF)

---

## Let's Build AI Systems That Survive the Real World

This repository is for enrolled students only and contains all code, exercises, and project materials.

**Your instructor**: [Hamza Farooq](https://www.linkedin.com/in/hamzafarooq/)
**Created by** [boring-bot](https://maven.com/boring-bot)

*Building the future of AI, one agent at a time.*
