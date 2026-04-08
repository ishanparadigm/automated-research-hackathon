"""Automated Research — Paradigm Hackathon, April 9 2026."""

from rich.console import Console
from rich.panel import Panel

from research.search import search_arxiv
from research.synthesis import synthesize

console = Console()


def main():
    console.print(Panel("Automated Research Agent", style="bold magenta"))

    query = console.input("[bold green]Research query:[/] ")

    with console.status("Searching arxiv..."):
        papers = search_arxiv(query)

    console.print(f"Found {len(papers)} papers.")

    with console.status("Synthesizing..."):
        summary = synthesize(papers, query)

    console.print(Panel(summary, title="Research Synthesis", border_style="cyan"))


if __name__ == "__main__":
    main()
