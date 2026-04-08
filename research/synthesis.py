"""Synthesis — summarize and combine research findings."""

import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()


def synthesize(papers: list[dict], query: str) -> str:
    """Synthesize a set of papers into a coherent research summary."""
    paper_texts = "\n\n".join(
        f"**{p['title']}**\n{p['summary']}" for p in papers
    )

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4096,
        messages=[{
            "role": "user",
            "content": f"You are a research assistant. Given the following papers, write a synthesis addressing: {query}\n\n{paper_texts}",
        }],
    )
    return response.content[0].text
