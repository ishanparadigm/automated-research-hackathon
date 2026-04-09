# Ecosystem & Tools

Everything useful for building an automated research agent — APIs, MCP servers, payment protocols, and what the best repos actually depend on.

---

## What the Best Auto-Research Repos Use

### Karpathy's AutoResearch (minimal)
- **Stack:** PyTorch, numpy, matplotlib, tiktoken — that's it
- **Agent:** Claude Code or Codex pointed at a `program.md` skill file, looping
- **Infra:** Single NVIDIA GPU, `uv` package manager
- **No external APIs.** Fully self-contained. One file, one GPU, one metric.

### Sakana AI Scientist (full pipeline)
- **LLMs:** Anthropic, OpenAI, Google Generative AI, DeepSeek (via OpenRouter)
- **Code editing:** `aider-chat` (AI pair-programming tool — the LLM edits experiment code through it)
- **Paper search:** Semantic Scholar API for novelty checking
- **ML:** PyTorch, transformers, datasets, tiktoken
- **Experiment tracking:** Weights & Biases (`wandb`)
- **Paper generation:** LaTeX (`texlive-full`), pypdf, pymupdf4llm
- **Key insight:** Uses `aider` as the code-editing interface, not raw LLM output

### Agent Laboratory (human-in-the-loop)
- **LLMs:** OpenAI (o1, gpt-4o, o3-mini), DeepSeek
- **Paper search:** `arxiv` + `semanticscholar` Python packages
- **ML:** PyTorch, transformers, scikit-learn, scipy, statsmodels
- **NLP:** spaCy, NLTK
- **Data:** HuggingFace datasets
- **Paper generation:** LaTeX (pdflatex)
- **Key insight:** TF-IDF based paper relevance matching, copilot mode for human steering

### FutureHouse PaperQA / Robin (production-grade)
- **Search index:** Tantivy (Rust-based full-text search, like Lucene)
- **Vector store:** Qdrant, usearch, or FAISS
- **PDF parsing:** PyMuPDF, pypdf, Docling
- **Paper APIs:** Semantic Scholar + Crossref + OpenAlex + Unpaywall + Retraction Watch
- **LLM integration:** Custom `fhlmi` library, LiteLLM
- **Optional:** Zotero integration, OpenReview
- **Key insight:** Uses 5+ paper metadata APIs together for comprehensive coverage

---

## Research APIs

| API | Coverage | Auth | Cost | Best For |
|-----|----------|------|------|----------|
| **[Semantic Scholar](https://api.semanticscholar.org/)** | ~200M papers | API key for higher limits | Free | Citation graphs, AI-extracted features, TLDRs |
| **[OpenAlex](https://docs.openalex.org/)** | 250M+ works | No key (polite pool w/ email) | Free | Bulk metadata, open access, concepts |
| **[arXiv API](https://info.arxiv.org/help/api/)** | 2.4M+ preprints | None | Free | Real-time preprint access, full text |
| **[Crossref](https://api.crossref.org/)** | 150M+ DOIs | Polite pool w/ email | Free | DOI resolution, BibTeX, bibliographic metadata |
| **[Unpaywall](https://unpaywall.org/products/api)** | OA status for DOIs | Email param | Free | Finding open access PDF URLs |
| **[PubMed/NCBI](https://www.ncbi.nlm.nih.gov/home/develop/api/)** | 36M+ biomedical | API key for higher limits | Free | Biomedical literature |
| **[OpenReview](https://docs.openreview.net/)** | Conference papers | Python client | Free | ICLR, NeurIPS reviews + papers |
| **[CORE](https://core.ac.uk/services/api)** | 300M+ OA papers | API key | Free | Full-text open access aggregator |
| **[Elicit](https://elicit.com/api)** | 200M+ (uses S2 + OpenAlex) | API key | Paid | AI-powered extraction, structured reports |
| **[Consensus](https://consensus.app/)** | 200M+ | API key | Paid | Consensus synthesis across studies |

**Recommended combo for hackathon:** Semantic Scholar (primary search + citations) + arXiv (full text) + OpenAlex (bulk metadata fallback). All free, no setup friction.

---

## MCP Servers for Research

| Server | Sources | GitHub |
|--------|---------|--------|
| **PaperMCP** | ArXiv, HuggingFace, Google Scholar, OpenReview, DBLP, PapersWithCode (32 tools) | [ScienceAIHub/PaperMCP](https://github.com/ScienceAIHub/PaperMCP) |
| **paper-search-mcp** | ArXiv, PubMed, bioRxiv, Semantic Scholar | [openags/paper-search-mcp](https://github.com/openags/paper-search-mcp) |
| **arxiv-mcp-server** | ArXiv (HTML+PDF), Semantic Scholar for citations | [blazickjp/arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server) |
| **Scientific-Papers-MCP** | ArXiv, OpenAlex, PMC, Europe PMC, bioRxiv/medRxiv, CORE | [benedict2310/Scientific-Papers-MCP](https://github.com/benedict2310/Scientific-Papers-MCP) |
| **semanticscholar-MCP-Server** | Semantic Scholar (papers, authors, citations) | [JackKuo666/semanticscholar-MCP-Server](https://github.com/JackKuo666/semanticscholar-MCP-Server) |

**PaperMCP** is the most comprehensive (32 tools across 6+ sources). If you only pick one, pick that.

---

## Payment Protocols for AI Agents

### x402 (Coinbase)
- **What:** Open HTTP-native payment protocol using the HTTP 402 status code
- **How:** Client requests resource → server returns 402 with price → client sends signed USDC payment in `X-PAYMENT` header → facilitator verifies and settles onchain → server delivers content
- **Chains:** Base (Ethereum L2), Solana (400ms finality, $0.00025/tx)
- **Scale:** 50M+ transactions, $10M+ volume
- **Foundation members:** Google, AWS, Visa, Circle, Anthropic, Cloudflare, Vercel
- **GitHub:** [coinbase/x402](https://github.com/coinbase/x402)
- **Docs:** [docs.cdp.coinbase.com/x402](https://docs.cdp.coinbase.com/x402/welcome)
- **MCP integration:** [Zuplo x402 + MCP](https://zuplo.com/blog/mcp-api-payments-with-x402) — enables MCP servers to charge via stablecoin micropayments

### AP2 — Agent Payments Protocol (Google)
- **What:** Open protocol for agent-to-merchant transactions using Verifiable Digital Credentials
- **Payment-agnostic:** Credit/debit, bank transfers, wallets, AND stablecoins (via x402)
- **Collaborators:** 60+ companies (Mastercard, PayPal, Coinbase)
- **GitHub:** [google-agentic-commerce/AP2](https://github.com/google-agentic-commerce/AP2)

### Hackathon angle
x402 is the most buildable — the SDK is ready, it works with USDC on Base/Solana, and there's already an MCP integration. An auto-research agent that pays for premium API access or paywalled papers via x402 micropayments would be a compelling demo.

---

## Quick-Start Dependency Tiers

### Tier 1: Get something working in 30 min
```
anthropic, arxiv, rich, python-dotenv
```

### Tier 2: Add literature depth
```
semanticscholar, httpx, tiktoken, chromadb (or faiss-cpu)
```

### Tier 3: Full research agent
```
aider-chat, wandb, transformers, datasets, langchain
```

### Tier 4: Payments & advanced integrations
```
x402 SDK, MCP server (PaperMCP), tantivy
```
