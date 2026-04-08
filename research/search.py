"""Search & retrieval — arxiv, semantic scholar, web."""

import arxiv


def search_arxiv(query: str, max_results: int = 10) -> list[dict]:
    """Search arxiv for papers matching the query."""
    search = arxiv.Search(query=query, max_results=max_results, sort_by=arxiv.SortCriterion.Relevance)
    results = []
    for paper in search.results():
        results.append({
            "title": paper.title,
            "summary": paper.summary,
            "url": paper.entry_id,
            "published": str(paper.published),
            "authors": [a.name for a in paper.authors],
        })
    return results
