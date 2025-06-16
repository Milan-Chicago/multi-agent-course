# Enterprise RAG & Multi-Agent Applications

Welcome to the official course repository for **Enterprise RAG & Multi-Agent Applications**.

This repo is for **enrolled students only** and contains all code, exercises, templates, and project materials used throughout the course.

🔗 [Visit course page for more information](https://maven.com/boring-bot/advanced-llm)

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

### Week 1: Agentic RAG

- Naive RAG vs Agentic RAG
- Agentic RAG Components
- Advanced Agents

Upload Data to Qdrant: [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hamzafarooq/multi-agent-course/blob/main/Module_1/Agentic_RAG/Upload_data_to_Qdrant_Notebook.ipynb)

Agentic RAG: [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hamzafarooq/multi-agent-course/blob/main/Module_1/Agentic_RAG/Agentic_RAG_Notebook.ipynb)

---

### Week 2: Optimizing and Deploying Large Language Models

- LLM Deployment and Hosting
- Mixture of Experts
- Quantization methods

TextSTreamer: [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hamzafarooq/multi-agent-course/blob/main/Module_2/Quantization/TextStreamer_Meta_Llama_3_1_8B_Instruct.ipynb)

Bitsnbytes Quantization: [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hamzafarooq/multi-agent-course/blob/main/Module_2/Quantization/Bitsnbytes_4bit_Quantization.ipynb)

---

### Week 3: RAG Memory & Semantic Cache

- RAG Memory
- Semantic Cache

Semantic Cache: [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hamzafarooq/multi-agent-course/blob/main/Module_3/Semantic_Cache/Semantic_cache_from_scratch.ipynb)

---

### Week 4: Knowledge Graphs and Multi-Agent Workflows

- Using knowledge graphs in RAG
- Principles of KG Standardization
- GraphRAG at scale

Knowledge Graphs Basic Version: [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hamzafarooq/multi-agent-course/blob/main/Module_4/Knowledge_Graphs/Knowledge_Graphs_Basic_Version.ipynb)

Knowledge Graphs Advanced Version: [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hamzafarooq/multi-agent-course/blob/main/Module_4/Knowledge_Graphs/Knowledge_Graphs_Advanced_Version.ipynb)

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

MCP (non-adk): [![GitHub Folder](https://img.shields.io/badge/View%20on-GitHub-blue?logo=github)](https://github.com/hamzafarooq/multi-agent-course/tree/main/Module_6/MCP)

Ollama jailbreak: [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hamzafarooq/multi-agent-course/blob/main/Module_6/Ollama/Mistral%20Llama%203.1%20and%20Llama%203.2%20jailbreak.ipynb)

Llama Guard: [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hamzafarooq/multi-agent-course/blob/main/Module_6/Guardrails/Llama%20Guard.ipynb)

---

## Technology Stack

This course uses the following tools and services:

| Area                  | Tools / Frameworks                                  |
|-----------------------|------------------------------------------------------|
| **LLM Access**        | Ares API (via Traversaal.ai)                         |
| **Agent Frameworks**  | LangGraph, AutoGen, SmolAgents                       |
| **Vector Search**     | FAISS (Colab), OpenSearch (optional)                |
| **Memory & Caching**  | Redis Cloud (recommended setup)                      |
| **Notebooks**         | Google Colab Pro (preferred), Jupyter (optional)     |
| **Deployments (Optional)** | AWS Lambda, Step Functions, FastAPI            |
| **Graph Systems**     | NetworkX, LangGraph                                  |
| **Language**          | Python 3.10+                                         |

> You don’t need to pre-install anything locally.  
> All key dependencies are included in each notebook.

---

## Student Feedback (Beta Cohort)

> “Finally a course that moves past theory and teaches **how to build AI systems that work**.”  
> “Everything was practical — I now know how to apply RAG and agents in real products.”

---

## Let’s Build AI Systems That Survive the Real World

**Your instructor**: [Hamza Farooq](https://www.linkedin.com/in/hamzafarooq/)  
**Created by** [boring-bot](https://maven.com/boring-bot)
