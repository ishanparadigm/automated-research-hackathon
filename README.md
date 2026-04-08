# Automated Research Hackathon

**Paradigm Automated Research Hackathon — April 9, 2026 | San Francisco**

> Compete on optimization challenges or build autoresearch projects.

Hackathon details: https://paradigm.xyz/automated-research-hackathon/

## Project

*TODO: Describe your project here after the hackathon kicks off.*

## Quick Start

```bash
# Clone the repo
git clone https://github.com/ishanparadigm/automated-research-hackathon.git
cd automated-research-hackathon

# Set up Python environment
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Set your API keys
cp .env.example .env
# Edit .env with your keys

# Run
python main.py
```

## Structure

```
├── main.py              # Entry point
├── research/            # Research automation modules
│   ├── __init__.py
│   ├── agent.py         # Research agent logic
│   ├── search.py        # Search & retrieval
│   └── synthesis.py     # Synthesis & summarization
├── utils/               # Shared utilities
│   └── __init__.py
├── notebooks/           # Exploration notebooks
├── data/                # Data directory (gitignored)
├── requirements.txt
└── .env.example
```

## Tech Stack

- **Python 3.11+**
- **Anthropic Claude API** — reasoning & synthesis
- **LangChain / LlamaIndex** — orchestration (optional)
- **FAISS / ChromaDB** — vector search
- **Arxiv API / Semantic Scholar** — paper retrieval

## License

MIT
