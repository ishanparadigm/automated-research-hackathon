"""Synthesis — summarize, judge, and refine research findings."""

import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()

MODEL = "claude-sonnet-4-6"


def _call(system: str, user: str, max_tokens: int = 4096) -> str:
    """Single Claude call with system + user message."""
    response = client.messages.create(
        model=MODEL,
        max_tokens=max_tokens,
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    return response.content[0].text


def synthesize(papers: list[dict], query: str) -> str:
    """Synthesize a set of papers into a coherent research summary."""
    paper_texts = "\n\n".join(
        f"**{p['title']}** ({p.get('published', 'n/a')})\n{p['summary']}" for p in papers
    )
    return _call(
        system="You are a research assistant. Write a concise synthesis of the provided papers. Focus on key findings, agreements, contradictions, and open questions.",
        user=f"Research question: {query}\n\nPapers:\n{paper_texts}",
    )


def judge(synthesis: str, query: str) -> dict:
    """Judge how well a synthesis answers the research query. Returns score (1-10) and reasoning."""
    result = _call(
        system=(
            "You are a research quality evaluator. Score the synthesis on a scale of 1-10 for how well it answers the research question. "
            "Respond in exactly this format:\n"
            "SCORE: <number>\n"
            "REASONING: <one paragraph>\n"
            "GAPS: <comma-separated list of what's missing or unclear>"
        ),
        user=f"Research question: {query}\n\nSynthesis:\n{synthesis}",
        max_tokens=1024,
    )
    lines = result.strip().split("\n")
    score = 5
    reasoning = ""
    gaps = ""
    for line in lines:
        if line.startswith("SCORE:"):
            try:
                score = int(line.split(":")[1].strip())
            except ValueError:
                pass
        elif line.startswith("REASONING:"):
            reasoning = line.split(":", 1)[1].strip()
        elif line.startswith("GAPS:"):
            gaps = line.split(":", 1)[1].strip()
    return {"score": score, "reasoning": reasoning, "gaps": gaps}


def refine_query(original_query: str, knowledge: list[str], gaps: str) -> str:
    """Generate a refined follow-up query based on what we know and what's missing."""
    context = "\n\n".join(f"[Finding {i+1}]: {k[:500]}" for i, k in enumerate(knowledge))
    return _call(
        system=(
            "You are a research strategist. Given the original query, accumulated knowledge, and identified gaps, "
            "generate a single refined search query (one line, no quotes) that would fill the most important gap."
        ),
        user=f"Original query: {original_query}\n\nKnowledge so far:\n{context}\n\nGaps: {gaps}",
        max_tokens=256,
    ).strip()
