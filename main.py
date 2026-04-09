"""Automated Research — Paradigm Hackathon, April 9 2026."""

import argparse

from rich.console import Console
from rich.panel import Panel

from research.agent import research

console = Console()


def main():
    parser = argparse.ArgumentParser(description="Automated Research Agent")
    parser.add_argument("query", nargs="?", help="Research query (interactive if omitted)")
    parser.add_argument("-n", "--iterations", type=int, default=10, help="Max iterations (default: 10)")
    parser.add_argument("-s", "--score", type=int, default=8, help="Min score to converge (default: 8)")
    parser.add_argument("-o", "--output", default="output", help="Output directory (default: output)")
    args = parser.parse_args()

    console.print(Panel("Automated Research Agent", style="bold magenta"))

    query = args.query or console.input("[bold green]Research query:[/] ")

    result = research(query, max_iterations=args.iterations, min_score=args.score, save_dir=args.output)

    console.print(f"\n[bold]Done.[/] {result['total_papers']} papers searched across {len(result['iterations'])} iterations.")


if __name__ == "__main__":
    main()
