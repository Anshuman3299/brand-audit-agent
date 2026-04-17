from tavily import TavilyClient
import os
from dotenv import load_dotenv
load_dotenv(override=True)

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def search_brand_mentions(brand_name, query_type="general"):
    queries = {
        "reviews": f"{brand_name} customer reviews complaints praise 2024",
        "news": f"{brand_name} brand news reputation scandal controversy 2024",
        "social": f"{brand_name} public opinion social media sentiment Twitter Reddit",
        "general": f"{brand_name} brand perception public image reputation"
    }
    query = queries.get(query_type, queries["general"])
    try:
        response = client.search(
            query=query,
            search_depth="advanced",
            max_results=5
        )
        results_text = f"Search results for '{query}':\n\n"
        for i, result in enumerate(response.get("results", []), 1):
            title = result.get("title", "No title")
            url = result.get("url", "")
            content = result.get("content", "No content available")
            results_text += f"Source {i}: {title}\n"
            results_text += f"URL: {url}\n"
            results_text += f"Content: {content[:500]}...\n\n"
        return results_text
    except Exception as e:
        return f"Search failed: {str(e)}"

def run_all_searches(brand_name):
    return {
        "reviews": search_brand_mentions(brand_name, "reviews"),
        "news": search_brand_mentions(brand_name, "news"),
        "social": search_brand_mentions(brand_name, "social")
    }
