from newspaper import Article
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re
import json
import requests

# Prepare NLP framework
import nltk
nltk.download('punkt_tab')

# Attempt to get BIAS if the article exists in DB
def get_bias_from_domain(url, bias_file="bias_registry.json"):
    with open(bias_file) as f:
        bias_db = json.load(f)
    domain = urlparse(url).netloc.replace("www.", "")
    return bias_db.get(domain, {"bias": "Unknown"})

def extract_article_metadata(url):
    article = Article(url, language='en')
    article.download()
    article.parse()

    metadata = {
        "title": article.title,
        "authors": article.authors or [],
        "publish_date": article.publish_date,
        "text": article.text,
        "top_image": article.top_image,
        "summary": None,
        "keywords": None,
        "publisher": None
    }

    # Attempt built-in NLP
    article.nlp()
    metadata["summary"] = article.summary
    metadata["keywords"] = article.keywords

    # Fallback: parse HTML manually
    soup = BeautifulSoup(article.html, 'html.parser')

    # Try JSON-LD schema.org
    for script in soup.find_all("script", {"type": "application/ld+json"}):
        try:
            data = json.loads(script.string)
            if isinstance(data, dict):
                if "author" in data:
                    if isinstance(data["author"], dict) and "name" in data["author"]:
                        metadata["authors"].append(data["author"]["name"])
                    elif isinstance(data["author"], list):
                        for a in data["author"]:
                            if isinstance(a, dict) and "name" in a:
                                metadata["authors"].append(a["name"])
                if "publisher" in data and "name" in data["publisher"]:
                    metadata["publisher"] = data["publisher"]["name"]
        except json.JSONDecodeError:
            continue

    # Fallback: meta tags
    for meta_tag in soup.find_all("meta"):
        if meta_tag.get("name", "").lower() in ["author", "article:author"]:
            metadata["authors"].append(meta_tag.get("content"))
        if meta_tag.get("property", "").lower() in ["og:site_name", "article:publisher"]:
            metadata["publisher"] = meta_tag.get("content")

    # Fallback: regex search for "By ..." in the text
    if not metadata["authors"]:
        text_sample = article.text[:500]
        match = re.search(r"(?i)\bby ([A-Z][a-z]+ [A-Z][a-z]+)", text_sample)
        if match:
            metadata["authors"].append(match.group(1))

    metadata["authors"] = list(set(metadata["authors"]))  # deduplicate
    return metadata
