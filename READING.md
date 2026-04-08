# Background Reading

Curated reading list for the Paradigm Automated Research Hackathon.

---

## The Two Big Inspirations

### Karpathy — AutoResearch
- **Repo:** https://github.com/karpathy/autoresearch
- **Tweet thread:** https://x.com/karpathy/status/2030371219518931079
- ~630 lines of Python. An AI coding agent autonomously runs ML experiments on a single GPU: one file, one GPU, one metric (val loss), 5-min training budget per experiment (~12/hr, ~100 overnight). A human writes objectives in `program.md`, the agent modifies `train.py`, checks if loss improved, keeps or discards, commits, repeats. Over ~2 days it found ~20 additive optimizations → **11% training speedup** on a larger model. Karpathy's next vision: making it "asynchronously massively collaborative" for agents, SETI@home-style.

### OpenAI — Parameter Golf
- **Blog:** https://openai.com/index/parameter-golf/
- **Repo:** https://github.com/openai/parameter-golf
- Open competition: train the best language model that fits in **16MB** and trains in **under 10 minutes on 8×H100s**. Scored on bits-per-byte (BPB) on FineWeb validation, tokenizer-agnostic. No constraints on architecture, data, or training steps beyond the time wall. Pushes toward depth recurrence, parameter tying, quantization-aware training, bitnets, novel tokenizers. $1M in compute credits from OpenAI. Runs March 18 – April 30, 2026.

---

## Key Papers

| Paper | Year | TL;DR |
|-------|------|-------|
| [The AI Scientist](https://arxiv.org/abs/2408.06292) (Sakana AI) | 2024 | End-to-end: LLM generates ideas, writes code, runs experiments, writes papers, auto-reviews. |
| [FunSearch](https://www.nature.com/articles/s41586-023-06924-6) (DeepMind) | 2024 | LLM + evolutionary search discovers new math constructions (cap set problem). Published in Nature. |
| [Can LLMs Generate Novel Research Ideas?](https://arxiv.org/abs/2409.04109) | 2024 | 100+ NLP researchers blind-rated LLM ideas vs human ideas — LLM ideas rated *more novel*, slightly less feasible. |
| [MLAgentBench](https://arxiv.org/abs/2310.03302) | 2023 | Benchmark for evaluating AI agents on ML experimentation tasks. |
| [ResearchAgent](https://arxiv.org/abs/2404.07738) | 2024 | Iterative research idea generation over scientific literature. |
| [SWE-agent](https://arxiv.org/abs/2405.15793) | 2024 | Autonomous GitHub issue resolution — architecture template for research agents. |

---

## Systems & Products

- **OpenAI Deep Research** — https://openai.com/index/introducing-deep-research/ — agent that browses the web and produces long-form research reports
- **Google DeepMind AI Co-Scientist** — https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/ — multi-agent generate-debate-evolve system for hypotheses
- **Anthropic Claude tool use** — https://docs.anthropic.com/en/docs/build-with-claude/tool-use — patterns for building agentic research workflows

---

## Blog Posts & References

- **Lilian Weng — "LLM Powered Autonomous Agents"** — https://lilianweng.github.io/posts/2023-06-23-agent/ — foundational post on agent architecture (planning, memory, tool use)
- **DeepMind FunSearch blog** — https://deepmind.google/discover/blog/funsearch-making-new-discoveries-in-mathematical-sciences-using-large-language-models/
- **Sakana AI Scientist project page** — https://sakana.ai/ai-scientist/
