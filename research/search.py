"""Search & retrieval — arxiv, semantic scholar, web."""

import arxiv
import httpx


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


def search_semantic_scholar(query: str, max_results: int = 10) -> list[dict]:
    """Search Semantic Scholar for papers. Returns title, abstract, citation count, url."""
    resp = httpx.get(
        "https://api.semanticscholar.org/graph/v1/paper/search",
        params={
            "query": query,
            "limit": max_results,
            "fields": "title,abstract,citationCount,url,year,authors",
        },
        timeout=30,
    )
    resp.raise_for_status()
    results = []
    for paper in resp.json().get("data", []):
        if not paper.get("abstract"):
            continue
        results.append({
            "title": paper["title"],
            "summary": paper.get("abstract", ""),
            "url": paper.get("url", ""),
            "published": str(paper.get("year", "")),
            "authors": [a["name"] for a in paper.get("authors", [])],
            "citations": paper.get("citationCount", 0),
        })
    return results


def search_all(query: str, max_results: int = 10) -> list[dict]:
    """Search both arxiv and Semantic Scholar, deduplicate by title."""
    papers = search_arxiv(query, max_results=max_results)
    try:
        s2_papers = search_semantic_scholar(query, max_results=max_results)
        seen_titles = {p["title"].lower() for p in papers}
        for p in s2_papers:
            if p["title"].lower() not in seen_titles:
                papers.append(p)
                seen_titles.add(p["title"].lower())
    except Exception:
        pass  # S2 rate limits are tight, fall back to arxiv-only
    return papers
