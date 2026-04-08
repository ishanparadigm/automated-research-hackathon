"""Research agent — orchestrates search, retrieval, and synthesis."""

import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()


def research(query: str, depth: int = 3) -> str:
    """Run a research loop: search → read → synthesize → refine."""
    # TODO: Implement your research agent logic here
    raise NotImplementedError("Implement your research agent!")
