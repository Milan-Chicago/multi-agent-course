# RAG vs Knowledge Graph Evaluation Framework

A comprehensive, production-ready system for comparing **Retrieval-Augmented Generation (RAG)** and **Knowledge Graph (KG)** approaches for question-answering systems.

Built with **Neo4j Aura** and **OpenAI GPT-4o-mini**, this framework provides objective, LLM-based evaluation to determine which approach works best for different types of questions.

<div align="center">

### 🎨 Modern Streamlit Web Interface

**Beautiful, minimal UI for comparing RAG and Knowledge Graph approaches side-by-side**

[Try it Now](#-streamlit-web-app-recommended) • [View Examples](#-code-examples) • [Join Course](https://maven.com/boring-bot/advanced-llm?promoCode=200OFF)

</div>

---

## 🎯 What This Does

This implementation provides **three distinct query methods**:

### 1. **RAG (Retrieval-Augmented Generation)**
- Uses semantic search (embeddings) or keyword matching to find relevant documents
- Passes retrieved context to an LLM for answer generation
- **Best for:** Natural language understanding, semantic queries, summarization

### 2. **Knowledge Graph with Text-to-Cypher**
- Converts natural language questions into Cypher queries using GPT-4o-mini
- Executes structured queries directly on Neo4j
- Returns exact, verifiable data
- **Best for:** Precise counts, relationship queries, aggregations, filtering

### 3. **LLM Judge Evaluation**
- Uses GPT-4o-mini as an impartial evaluator
- Scores each method on accuracy, completeness, precision, and verifiability
- Produces detailed reasoning and recommendations

## ✨ Key Features

- ✅ **No Hardcoded Queries** — Cypher is generated dynamically from natural language
- ✅ **Objective Evaluation** — Unbiased LLM-based scoring system
- ✅ **Production Ready** — Graceful error handling, retry logic, logging
- ✅ **Flexible Data Loading** — CSV support (URL or local files)
- ✅ **Vector Search Optional** — Embedding-based semantic RAG
- ✅ **Batch Evaluation** — Evaluate many questions together
- ✅ **Interactive Mode** — Ask questions in real-time

## 🏗️ Architecture

```
Question
    ↓
    ├── [RAG Path] ─────────────→ Answer A (Interpretive)
    │
    ├── [Knowledge Graph Path] → Answer B (Exact)
    │
    └── [LLM Judge] ───────────→ Winner + Analysis
```

### RAG Path
1. Convert question to embedding or keywords
2. Retrieve relevant articles from Neo4j
3. Pass context to GPT-4o-mini for answer generation

### Knowledge Graph Path
1. Convert question to Cypher using GPT-4o-mini
2. Execute structured query on Neo4j
3. Format results + natural-language explanation

### Judge Path
- Compares both answers
- Scores accuracy, precision, completeness
- Determines winner with detailed reasoning

## 📊 When to Use Which Method

### Knowledge Graph Excels At:
- *"Who are the collaborators of Emily Chen?"*
- *"How many articles has each researcher published?"*
- *"Which researchers work on AI Ethics?"*
- *"Find all papers published in 2024."*

### RAG Excels At:
- *"What are the main challenges in AI safety?"*
- *"Explain innovations in transformer architectures."*
- *"Summarize ethical concerns in AI research."*

### Both Are Useful:
- *"What topics does Emily Chen research?"*
- *"Compare research focus of two researchers."*

## 🚀 Quick Start

### Prerequisites

1. **Neo4j Aura Account** (free tier available)
   - Sign up at [neo4j.com/cloud/aura](https://neo4j.com/cloud/aura/)
   - Create a new database instance
   - Save your credentials

2. **OpenAI API Key**
   - Get one at [platform.openai.com/api-keys](https://platform.openai.com/api-keys)

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/multi-agent-course.git
cd multi-agent-course/Module_4_Knowledge_Graphs

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
# Edit .env file with your credentials
```

### Configuration

Create or update your `.env` file:

```env
NEO4J_URI=neo4j+s://your-instance.databases.neo4j.io
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your-password-here
NEO4J_DATABASE=neo4j
OPENAI_API_KEY=your-openai-api-key-here
```

### Usage

#### 🎨 Streamlit Web App (Recommended)

The easiest way to interact with the system is through our modern, minimal web interface.

**⚠️ IMPORTANT: Run Setup First (Only Once)**

Before using the app for the first time, run the setup script to load data and create embeddings:

```bash
python setup.py
```

This will:
- ✅ Check your environment variables
- ✅ Test Neo4j connection
- ✅ Load the dataset into Neo4j
- ✅ Create embeddings for semantic search
- ✅ Verify everything works

**Then Launch the App:**

```bash
# Option 1: Quick Launch
./run_app.sh         # macOS/Linux
run_app.bat          # Windows

# Option 2: Direct Launch
streamlit run app.py
```

Then open your browser to `http://localhost:8501`

**Features:**
- 🎯 Beautiful, minimal UI with modern design
- 📊 Side-by-side comparison of RAG vs KG
- 📈 Visual score charts and metrics
- ⚖️ Real-time LLM judge evaluation
- 💾 Sample questions for quick testing
- 🎓 Integrated course CTA

#### Python Script

```bash
# Run single question evaluation
python knowledge_graph_rag_comparison.py
```

#### Jupyter Notebook

```bash
# Launch Jupyter
jupyter notebook knowledge_graph_neo4j_with_evals.ipynb
```

Or open in [Google Colab](https://colab.research.google.com/github/hamzafarooq/multi-agent-course/blob/main/Module_4/knowledge_graph_neo4j_with_evals.ipynb)

#### Sample Questions

```bash
# Run curated evaluation sets
python sample_questions.py
```

## 💻 Code Examples

### Single Question with Judge

```python
from knowledge_graph_rag_comparison import quick_ask_with_judge

# Ask a question and get both RAG and KG answers with evaluation
result = quick_ask_with_judge("Who are the collaborators of Emily Chen?")
```

### Batch Evaluation

```python
from knowledge_graph_rag_comparison import batch_judge_questions

questions = [
    "How many articles has each researcher published?",
    "What are the ethical concerns in AI?",
    "Which researchers work on Model Optimization?"
]

results = batch_judge_questions(questions)
```

### Custom Implementation

```python
from knowledge_graph_rag_comparison import Neo4jGraphRAG

# Initialize
rag = Neo4jGraphRAG()

# Load your data
rag.load_data('https://your-data-source.csv')

# Create embeddings for semantic search
rag.create_embeddings_for_articles()

# Compare both approaches
result = rag.compare_with_judge("Your question here")

# Close connection
rag.close()
```

## 📁 Project Structure

```
Module_4_Knowledge_Graphs/
├── setup.py ⭐                             # Setup script (run this first!)
├── app.py                                  # 🎨 Streamlit web app (modern UI)
├── streamlit_helper.py                     # Helper functions for Streamlit
├── run_app.sh                              # Quick launcher (macOS/Linux)
├── run_app.bat                             # Quick launcher (Windows)
├── knowledge_graph_rag_comparison.py       # Main Python implementation
├── sample_questions.py                     # Curated evaluation question sets
├── knowledge_graph_neo4j_with_evals.ipynb  # Jupyter notebook version
├── requirements.txt                        # Python dependencies
├── .env                                    # Environment variables (not in git)
├── README.md                               # This file
├── QUICKSTART_STREAMLIT.md                 # Quick start guide
└── STREAMLIT_FEATURES.md                   # Feature documentation
```

## 📈 Data Schema

The system works with research paper data including:

- **Articles:** title, abstract, publication date
- **Researchers:** names + co-authorship
- **Topics:** research areas
- **Relationships:**
  - `PUBLISHED` (Researcher → Article)
  - `IN_TOPIC` (Article → Topic)

## 🎓 Expected Results

You will get:

- Winner declaration for each question (RAG, KG, or TIE)
- Confidence level (high/medium/low)
- Detailed metrics: accuracy, completeness, precision
- LLM reasoning explaining the decision
- Recommendations for the best approach per question type

## 📊 Evaluation Question Categories

The framework includes 8 curated question categories:

1. **Relationship Queries** — Entity-entity connections (KG expected to win)
2. **Counting & Aggregation** — Counts, totals, group-by operations (KG expected to win)
3. **Filtering Queries** — Direct filters by researcher, year, topic (KG expected to win)
4. **Topic-Based Queries** — Topic membership and hierarchy (Mixed results)
5. **Semantic/Content Queries** — Summaries, insights, explanations (RAG expected to win)
6. **Complex Multi-Hop** — Multi-step graph reasoning (KG expected to win)
7. **Temporal Queries** — Timelines, date filtering (KG expected to win)
8. **Comparison Queries** — Entity comparisons (Mixed results)



### Using Different Models

Change the model in the code:

```python
# In openai.chat.completions.create() calls
model="gpt-4o-mini"  # Current
model="gpt-5"        # More powerful

```

## 🎯 Why This Matters

Most implementations choose *either* RAG or Knowledge Graphs. This framework shows **when to use which**, backed by objective LLM evaluations — ideal for:

- Building hybrid QA systems leveraging both methods
- Understanding semantic vs. structured query trade-offs
- Making informed architectural decisions
- Demonstrating the value of Knowledge Graphs vs pure LLM approaches

## 📚 Learn More

Want to master building advanced multi-agent systems and learn how to combine RAG, Knowledge Graphs, and other AI architectures?

<div align="center">

[![Agent Engineering Bootcamp](course_img.png)](https://maven.com/boring-bot/advanced-llm?promoCode=200OFF)

### 🎓 Agent Engineering Bootcamp: Developers Edition

⭐⭐⭐⭐⭐ **4.8** (96 reviews)

**Hamza Farooq** - Founder | Ex-Google | Prof UCLA & UMN

Master production-ready multi-agent systems, RAG, Knowledge Graphs, and advanced LLM architectures. Build real-world AI applications with hands-on projects.

This course covers:
- ✅ Multi-agent system design and orchestration
- ✅ RAG, Knowledge Graphs, and hybrid approaches
- ✅ Production-ready AI architecture patterns
- ✅ Evaluation frameworks and best practices
- ✅ Real-world case studies and implementations

### [**🚀 Enroll Now - Save $200 with code 200OFF →**](https://maven.com/boring-bot/advanced-llm?promoCode=200OFF)

</div>

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Add new question categories
- Improve evaluation metrics
- Add support for other graph databases
- Enhance the LLM judge prompts

## 📝 License

APACHE 2.0 License - feel free to use this in your own projects!

## 🙏 Acknowledgments

- Built with [Neo4j](https://neo4j.com/) for graph database
- Powered by [OpenAI](https://openai.com/) for embeddings and LLM evaluation
- Dataset adapted from [generative-ai-101](https://github.com/dcarpintero/generative-ai-101)

---

**Happy Evaluating! 🚀**

*Building the future of AI, one agent at a time.*
