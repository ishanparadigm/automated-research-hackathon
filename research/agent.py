"""Research agent — the tight loop."""

import json
import os
from datetime import datetime

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from research.search import search_all
from research.synthesis import judge, refine_query, synthesize

console = Console()


def research(query: str, max_iterations: int = 10, min_score: int = 8, save_dir: str = "output") -> dict:
    """
    The tight loop:
        1. Search papers (arxiv + Semantic Scholar)
        2. Synthesize findings
        3. Judge quality (LLM-as-judge, 1-10)
        4. Score >= threshold? Keep and refine. Below? Reformulate.
        5. Repeat until max_iterations or convergence.

    Returns the full research state: query history, knowledge base, scores.
    """
    os.makedirs(save_dir, exist_ok=True)

    knowledge = []
    all_papers = []
    iterations = []
    current_query = query

    for i in range(max_iterations):
        console.rule(f"[bold blue]Iteration {i + 1}/{max_iterations}")
        console.print(f"[dim]Query:[/] {current_query}")

        # 1. Search
        with console.status("Searching..."):
            papers = search_all(current_query, max_results=10)
        console.print(f"Found {len(papers)} papers")

        if not papers:
            console.print("[yellow]No papers found, refining query...[/]")
            current_query = refine_query(query, knowledge, "no results found for current query")
            continue

        all_papers.extend(papers)

        # 2. Synthesize
        with console.status("Synthesizing..."):
            synthesis = synthesize(papers, query)

        # 3. Judge
        with console.status("Evaluating..."):
            evaluation = judge(synthesis, query)

        score = evaluation["score"]
        gaps = evaluation["gaps"]

        # Log iteration
        iteration_data = {
            "iteration": i + 1,
            "query": current_query,
            "papers_found": len(papers),
            "score": score,
            "reasoning": evaluation["reasoning"],
            "gaps": gaps,
        }
        iterations.append(iteration_data)

        # Display
        color = "green" if score >= min_score else "yellow" if score >= 5 else "red"
        console.print(f"[{color}]Score: {score}/10[/] — {evaluation['reasoning']}")
        if gaps:
            console.print(f"[dim]Gaps: {gaps}[/]")

        # 4. Keep/discard
        if score >= min_score - 2:  # keep anything reasonably good
            knowledge.append(synthesis)
            console.print("[green]✓ Added to knowledge base[/]")

        # 5. Check convergence
        if score >= min_score and len(knowledge) >= 2:
            console.print(f"\n[bold green]Converged at iteration {i + 1} with score {score}/10[/]")
            break

        # 6. Refine query for next iteration
        with console.status("Refining query..."):
            current_query = refine_query(query, knowledge, gaps)

    # Final synthesis across all accumulated knowledge
    console.rule("[bold magenta]Final Synthesis")
    with console.status("Producing final synthesis..."):
        if len(knowledge) > 1:
            final = synthesize(
                [{"title": f"Finding {i+1}", "summary": k[:2000], "published": ""} for i, k in enumerate(knowledge)],
                query,
            )
        elif knowledge:
            final = knowledge[0]
        else:
            final = "No sufficient findings accumulated."

    console.print(Panel(final, title="Final Research Synthesis", border_style="cyan"))

    # Save results
    result = {
        "original_query": query,
        "iterations": iterations,
        "total_papers": len(all_papers),
        "knowledge_entries": len(knowledge),
        "final_synthesis": final,
        "timestamp": datetime.now().isoformat(),
    }

    output_path = os.path.join(save_dir, f"research_{datetime.now().strftime('%H%M%S')}.json")
    with open(output_path, "w") as f:
        json.dump(result, f, indent=2)
    console.print(f"\n[dim]Results saved to {output_path}[/]")

    # Summary table
    table = Table(title="Iteration Summary")
    table.add_column("Iter", style="cyan")
    table.add_column("Query", max_width=50)
    table.add_column("Papers", justify="right")
    table.add_column("Score", justify="right")
    for it in iterations:
        color = "green" if it["score"] >= min_score else "yellow" if it["score"] >= 5 else "red"
        table.add_row(str(it["iteration"]), it["query"][:50], str(it["papers_found"]), f"[{color}]{it['score']}[/]")
    console.print(table)

    return result
