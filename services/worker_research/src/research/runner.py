from .sources.web_search import search_web
from .sources.tools_catalog import fetch_tools

def run_research(topic: str) -> dict:
    return {"topic": topic, "news": search_web(topic), "tools": fetch_tools()}
