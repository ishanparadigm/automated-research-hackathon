# Background Reading

Curated reading list for the [Paradigm Automated Research Hackathon](https://paradigm.xyz/automated-research-hackathon/) (April 9, 2026).

---

## The Two Big Inspirations

### 1. Karpathy — AutoResearch
- **Repo:** https://github.com/karpathy/autoresearch
- **Tweet thread:** https://x.com/karpathy/status/2030371219518931079
- **TL;DR:** ~630 lines of Python. An AI coding agent autonomously runs ML experiments on a single GPU: one file, one GPU, one metric (val loss), 5-min training budget per experiment (~12/hr, ~100 overnight). A human writes objectives in `program.md`, the agent modifies `train.py`, checks if loss improved, keeps or discards, commits, repeats. Over ~2 days it found ~20 additive optimizations → **11% training speedup** on a larger model.
- **Implications:** Demonstrates that even a simple agent loop (propose → run → evaluate → commit) can produce real, additive research gains. Karpathy's next vision — making it "asynchronously massively collaborative" SETI@home-style — suggests the unlock is not smarter agents but more parallel ones.

### 2. OpenAI — Parameter Golf
- **Blog:** https://openai.com/index/parameter-golf/
- **Repo:** https://github.com/openai/parameter-golf
- **TL;DR:** Open competition: train the best language model that fits in **16MB** and trains in **under 10 minutes on 8×H100s**. Scored on bits-per-byte (BPB) on FineWeb validation, tokenizer-agnostic. No constraints on architecture, data, or training steps beyond the time wall. $1M in compute credits. Runs March 18 – April 30, 2026.
- **Implications:** Reframes ML research as a constrained optimization game — perfect for automated search. The lack of architecture constraints makes this a playground for neural architecture search, quantization-aware training, depth recurrence, and creative tokenization.

---

## Automated Scientific Discovery

### 3. The AI Scientist (Sakana AI, 2024)
- **Paper:** https://arxiv.org/abs/2408.06292
- **Project page:** https://sakana.ai/ai-scientist/
- **TL;DR:** End-to-end pipeline where an LLM generates research ideas, writes experiment code, runs experiments, analyzes results, writes full papers, and auto-reviews them. Demonstrated on small ML tasks (diffusion, language modeling, learning dynamics).
- **Implications:** First proof that a single system can close the entire research loop. Quality was low (most papers wouldn't pass peer review), but established the template everyone else is iterating on.

### 4. The AI Scientist v2 (Sakana AI, 2025)
- **Paper:** https://arxiv.org/abs/2504.08066
- **TL;DR:** Uses agentic tree search to iteratively formulate hypotheses, design experiments, analyze data, and write manuscripts. Produced the **first entirely AI-generated paper accepted at a peer-reviewed workshop**, exceeding the average human acceptance threshold.
- **Implications:** The gap between v1 and v2 shows how fast this is moving. Tree search over research strategies (not just single-shot generation) seems to be the key upgrade.

### 5. Agent Laboratory (Johns Hopkins, 2025)
- **Paper:** https://arxiv.org/abs/2501.04227
- **TL;DR:** Autonomous research framework that takes a human-provided idea and progresses through literature review, experimentation, and report writing. Uses o1-preview to generate ML code achieving SOTA. Reduces research expenses by 84% vs prior autonomous methods. Supports human-in-the-loop feedback at each stage.
- **Implications:** The human-in-the-loop design is pragmatic — full autonomy is fragile, but a human steering high-level direction while the agent handles execution scales well.

### 6. Coscientist (CMU, 2023 — Nature)
- **Paper:** https://www.nature.com/articles/s41586-023-06792-0
- **TL;DR:** GPT-4-driven system that autonomously designs, plans, and executes chemistry experiments using internet search, code execution, and robotic lab automation. Successfully optimized palladium-catalyzed cross-couplings and controlled liquid-handling instruments without human intervention.
- **Implications:** Extends automated research beyond in-silico ML experiments into the physical world. The integration of robotics + LLM planning is a template for wet-lab automation.

### 7. ChemCrow (EPFL, 2024 — Nature Machine Intelligence)
- **Paper:** https://www.nature.com/articles/s42256-024-00832-8
- **TL;DR:** LLM chemistry agent with 18 expert-designed tools for organic synthesis, drug discovery, and materials design. Autonomously synthesized an insect repellent, three organocatalysts, and guided discovery of a novel chromophore.
- **Implications:** Shows that domain-specific tool augmentation (not just general reasoning) is critical for real scientific work. The 18 tools are doing the heavy lifting.

### 8. PaperQA2 & Robin (FutureHouse, 2024-2025)
- **Paper:** https://arxiv.org/abs/2409.13740
- **Robin announcement:** https://www.futurehouse.org/research-announcements/demonstrating-end-to-end-scientific-discovery-with-robin-a-multi-agent-system
- **TL;DR:** PaperQA2 achieves higher accuracy than PhD-level researchers at retrieving and synthesizing scientific literature. Robin orchestrates multiple specialized agents into a discovery pipeline and identified ripasudil as a potential treatment for dry age-related macular degeneration — a genuine novel finding.
- **Implications:** First credible claim of an AI system making a real scientific discovery autonomously. The multi-agent specialization (Crow for literature, Falcon for hypotheses, Finch for experiments) is a pattern worth studying.

### 9. Hypothesis Generation with LLMs (U. Chicago, 2024)
- **Paper:** https://arxiv.org/abs/2404.04326
- **TL;DR:** Systematic study of LLMs generating scientific hypotheses from data. Iteratively generates and refines hypotheses from small example sets. Shows LLMs can produce plausible, novel hypotheses while identifying key failure modes.
- **Implications:** Hypothesis generation is the hardest part of the research loop to automate. This paper maps out where LLMs succeed and fail, which is essential for knowing when to trust the agent.

### 10. Can LLMs Generate Novel Research Ideas? (Stanford, 2024)
- **Paper:** https://arxiv.org/abs/2409.04109
- **TL;DR:** 100+ NLP researchers blind-rated LLM-generated ideas vs human-generated ones. LLM ideas were rated **more novel** but slightly less feasible.
- **Implications:** The novelty/feasibility tradeoff is the core tension. Automated research systems need a feasibility filter (experiment execution) to complement their idea generation — which is exactly what the hackathon is about.

---

## AI for Mathematics

### 11. FunSearch (DeepMind, 2024 — Nature)
- **Paper:** https://www.nature.com/articles/s41586-023-06924-6
- **Blog:** https://deepmind.google/discover/blog/funsearch-making-new-discoveries-in-mathematical-sciences-using-large-language-models/
- **TL;DR:** LLM + evolutionary search discovers new mathematical constructions, improving the best-known solution to the cap set problem. Published in Nature.
- **Implications:** LLMs as mutation operators in evolutionary program search is a powerful paradigm. The key insight: LLMs don't need to solve the problem — they just need to propose candidates that an evaluator can score.

### 12. AlphaProof (DeepMind, 2024-2025 — Nature)
- **Blog:** https://deepmind.google/blog/ai-solves-imo-problems-at-silver-medal-level/
- **Paper:** https://www.nature.com/articles/s41586-025-09833-y
- **TL;DR:** AlphaZero-inspired system that learns formal mathematical proofs via RL, trained on millions of auto-formalized problems. Solved 4/6 problems at the 2024 International Mathematical Olympiad (silver-medal level), including the hardest problem that only 5 humans solved.
- **Implications:** Shows that reinforcement learning over formal verification can achieve superhuman mathematical reasoning. The test-time RL approach (thinking harder at inference) is directly relevant to research agents that need to verify their own outputs.

---

## Agent Architectures & Foundations

### 13. ReAct (Princeton/Google, 2023 — ICLR)
- **Paper:** https://arxiv.org/abs/2210.03629
- **TL;DR:** Interleaves reasoning traces and task-specific actions in LLMs. Reasoning helps track/update plans; actions query external sources. 25-35% improvement over pure chain-of-thought or pure action methods.
- **Implications:** The foundational pattern for research agents. If your agent can't reason about what to do next AND take actions, it's missing half the picture.

### 14. Reflexion (Princeton, 2023 — NeurIPS)
- **Paper:** https://arxiv.org/abs/2303.11366
- **TL;DR:** Reinforces language agents through verbal self-reflection instead of weight updates. Agents reflect on failures and store reflections in episodic memory. Achieves 91% on HumanEval coding.
- **Implications:** Self-reflection is cheap and effective. A research agent that reflects on why an experiment failed (and remembers it) will avoid repeating dead ends.

### 15. Anthropic — Building Effective Agents (2024)
- **Blog:** https://www.anthropic.com/research/building-effective-agents
- **TL;DR:** Describes five agentic workflow patterns: prompt chaining, routing, parallelization, orchestrator-workers, and evaluator-optimizer. Core thesis: the most successful agents use simple, composable patterns — not complex frameworks.
- **Implications:** Start simple. A prompt chain that works beats an elaborate multi-agent system that doesn't. Add complexity only when simpler approaches hit a wall.

### 16. Andrew Ng — Four Agentic Design Patterns (2024)
- **Blog:** https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/
- **TL;DR:** Four patterns driving agentic AI: Reflection, Tool Use, Planning, and Multi-Agent Collaboration. Argued these workflows would drive more progress than the next foundation model generation.
- **Implications:** A good mental framework for hackathon architecture decisions. Which of these four patterns does your system need? Probably all of them, but start with one.

### 17. CodeAct (UIUC, 2024 — ICML)
- **Paper:** https://arxiv.org/abs/2402.01030
- **TL;DR:** Uses executable Python code as a unified action space for LLM agents instead of JSON/text. Code actions can compose tools, revise prior actions, and self-debug. Outperforms JSON-based actions by 20% with 30% fewer steps.
- **Implications:** If your research agent is writing code anyway, let it use code as its action language. This is why coding agents (SWE-agent, Karpathy's autoresearch) work so well.

### 18. AutoGen (Microsoft Research, 2023)
- **Paper:** https://arxiv.org/abs/2308.08155
- **TL;DR:** Framework where customizable agents collaborate through multi-agent conversation. Agents can combine LLMs, human inputs, and tools. Effective across math, coding, Q&A, and decision-making.
- **Implications:** Multi-agent conversation is a natural fit for research: one agent proposes, another critiques, a third implements. The debate pattern often produces better results than a single agent.

---

## Efficient Training & Model Compression

### 19. NanoGPT Speedrunning (Keller Jordan, 2024)
- **Repo:** https://github.com/KellerJordan/modded-nanogpt
- **TL;DR:** Community effort to train GPT-2 124M to target validation loss as fast as possible. Reduced wall-clock from Karpathy's ~45 minutes to under 4 minutes on 8×H100. Innovations include the Muon optimizer, rotary embeddings, value-residual connections, and exotic LR schedules. **Direct precursor to Parameter Golf.**
- **Implications:** The leaderboard shows that training recipes matter more than architecture at small scale. Optimizer choice alone accounts for 2-3× speedup.

### 20. Cramming (U. Maryland, 2023 — ICML)
- **Paper:** https://arxiv.org/abs/2212.14034
- **TL;DR:** How far can you push BERT training under a strict 24-hour single-GPU budget? With careful recipe tuning (LR schedules, data ordering, architectural tweaks), matches full BERT downstream performance.
- **Implications:** Compute-bounded training optimization is a solved research methodology. The systematic ablation approach here is exactly what an automated agent should be doing.

### 21. The Era of 1-bit LLMs / BitNet b1.58 (Microsoft Research, 2024)
- **Paper:** https://arxiv.org/abs/2402.17764
- **TL;DR:** Every weight is ternary ({-1, 0, 1}). Achieves competitive performance with full-precision LLMs while dramatically reducing memory and compute. 
- **Implications:** Extreme quantization is viable and opens new architecture design space. For Parameter Golf's 16MB constraint, ternary weights mean ~3× more parameters in the same budget.

### 22. Textbooks Are All You Need / Phi-1 (Microsoft Research, 2023)
- **Paper:** https://arxiv.org/abs/2306.11644
- **TL;DR:** A 1.3B model trained on high-quality synthetic "textbook" data matches much larger models on coding benchmarks.
- **Implications:** Data quality can substitute for parameter count. For constrained training, curating or synthesizing better data may be more impactful than architecture search.

### 23. Scaling LLM Test-Time Compute (UC Berkeley / DeepMind, 2024)
- **Paper:** https://arxiv.org/abs/2408.03314
- **TL;DR:** Allocating more compute at inference (search, verification, revision) can outperform using a larger model. Establishes scaling laws for test-time compute.
- **Implications:** A smaller model that "thinks longer" can beat a bigger one that answers immediately. Relevant to both parameter golf (small model + inference tricks) and research agents (iterative refinement beats one-shot).

---

## Benchmarks & Evaluation

### 24. AgentBench (Tsinghua, 2024 — ICLR)
- **Paper:** https://arxiv.org/abs/2308.03688
- **TL;DR:** First systematic benchmark evaluating LLMs as agents across 8 environments (OS, DB, web, etc.). Large gap between top commercial models and open-source alternatives. Main bottlenecks: long-term reasoning and instruction following.
- **Implications:** Know your agent's limits. If it can't follow multi-step instructions reliably, more tools won't help.

### 25. tau-bench (Sierra AI, 2024)
- **Blog:** https://sierra.ai/blog/benchmarking-ai-agents
- **TL;DR:** Tests agents on realistic tasks with dynamic user interaction. Even GPT-4 agents succeed in <50% of tasks; only ~25% success when repeating the same task 8 times.
- **Implications:** Agent reliability is still the bottleneck. For a hackathon, build in retries and fallbacks — your agent will fail at least half the time.

### 26. MLAgentBench (2023)
- **Paper:** https://arxiv.org/abs/2310.03302
- **TL;DR:** Standardized benchmark for AI agents doing ML experimentation — improving models, debugging, analyzing results.
- **Implications:** If you want to evaluate your hackathon agent, this is the closest existing benchmark.

---

## Systems & Products

### 27. OpenAI Deep Research
- https://openai.com/index/introducing-deep-research/
- Agent that autonomously browses the web and produces long-form research reports. Aimed at both scientific and general research.

### 28. Google DeepMind AI Co-Scientist
- https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/
- Multi-agent generate-debate-evolve system for scientific hypothesis generation.

### 29. SWE-agent (Princeton, 2024)
- **Paper:** https://arxiv.org/abs/2405.15793
- Autonomous GitHub issue resolution. Architecture template (LLM + tool use + iterative debugging) is directly transferable to research agents.

---

## Essential Blog Posts

- **Lilian Weng — "LLM Powered Autonomous Agents"** — https://lilianweng.github.io/posts/2023-06-23-agent/ — foundational post on agent architecture (planning, memory, tool use)
- **Harrison Chase — "What is a Cognitive Architecture?"** — https://blog.langchain.com/what-is-a-cognitive-architecture/ — framework for thinking about how agents reason, remember, and select actions
- **Anthropic — Claude tool use docs** — https://docs.anthropic.com/en/docs/build-with-claude/tool-use — practical patterns for building agentic workflows
- **Karpathy — llm.c** — https://github.com/karpathy/llm.c — pure C/CUDA GPT-2 training in ~$5, baseline for the speedrunning community
