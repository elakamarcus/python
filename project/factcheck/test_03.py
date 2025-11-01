import json
import re
import requests
from urllib.parse import urlparse, quote
from newspaper import Article
from bs4 import BeautifulSoup

# -------------------------------------------------------------------------
# 1️⃣ Bias Registry
# -------------------------------------------------------------------------
BIAS_REGISTRY = {
    "bbc.com": {"bias": "Center-Left", "alignment": "Liberal", "publisher": "BBC"},
    "foxnews.com": {"bias": "Right", "alignment": "Conservative", "publisher": "Fox News"},
    "svt.se": {"bias": "Center-Left", "alignment": "Social-Democratic", "publisher": "SVT Nyheter"},
    "expressen.se": {"bias": "Right-Center", "alignment": "Liberal-Conservative", "publisher": "Expressen"},
    "aftonbladet.se": {"bias": "Left", "alignment": "Social-Democratic", "publisher": "Aftonbladet"}
}

# -------------------------------------------------------------------------
# 2️⃣ Article Extraction Layer
# -------------------------------------------------------------------------
def extract_article_metadata(url):
    article = Article(url)
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

    # Built-in NLP
    try:
        article.nlp()
        metadata["summary"] = article.summary
        metadata["keywords"] = article.keywords
    except Exception:
        pass

    # Parse HTML for schema.org and meta fallbacks
    soup = BeautifulSoup(article.html, "html.parser")

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
        except Exception:
            continue

    for meta_tag in soup.find_all("meta"):
        name = meta_tag.get("name", "").lower()
        prop = meta_tag.get("property", "").lower()
        if name in ["author", "article:author"]:
            metadata["authors"].append(meta_tag.get("content"))
        if prop in ["og:site_name", "article:publisher"]:
            metadata["publisher"] = meta_tag.get("content")

    metadata["authors"] = list(set(metadata["authors"]))
    return metadata

# -------------------------------------------------------------------------
# 3️⃣ Bias Lookup
# -------------------------------------------------------------------------
def get_bias_info(url):
    domain = urlparse(url).netloc.replace("www.", "")
    return BIAS_REGISTRY.get(domain, {"bias": "Unknown", "alignment": "Unknown", "publisher": None})

# -------------------------------------------------------------------------
# 4️⃣ Claim Extraction (simple heuristic version)
# -------------------------------------------------------------------------
def extract_claims(text, min_len=8):
    """
    Extract likely factual claims from the article.
    Currently: naive heuristic splitting by sentences.
    Later: can be replaced by transformer model.
    """
    sentences = re.split(r'(?<=[.!?]) +', text)
    claims = []
    for s in sentences:
        # Basic filtering: sentence length and factual phrasing
        if len(s.split()) >= min_len and any(keyword in s.lower() for keyword in ["is", "was", "were", "has", "have", "had", "announced", "reported", "claims", "according to"]):
            claims.append(s.strip())
    return claims[:5]  # keep top 5 for MVP

# -------------------------------------------------------------------------
# 5️⃣ Fact Checking (stub)
# -------------------------------------------------------------------------
def fact_check_claim(claim):
    """
    Placeholder for future fact-check API integration.
    Returns dummy response for now.
    """
    # Example stub for demonstration
    if "covid" in claim.lower():
        return {"claim": claim, "status": "True", "source": "Wikidata"}
    elif "election" in claim.lower():
        return {"claim": claim, "status": "Disputed", "source": "PolitiFact"}
    else:
        return {"claim": claim, "status": "Unknown", "source": None}

# -------------------------------------------------------------------------
# 6️⃣ Main Analysis Function
# -------------------------------------------------------------------------
def analyze_article(url: str):
    bias_info = get_bias_info(url)
    data = extract_article_metadata(url)

    claims = extract_claims(data["text"])
    checked_claims = [fact_check_claim(c) for c in claims]

    # Compute basic factuality score
    verified = sum(1 for c in checked_claims if c["status"] == "True")
    score = round(verified / len(checked_claims), 2) if checked_claims else None

    # Fact check title
    checked_title = [fact_check_claim(data["title"])]

    output = {
        "url": url,
        "domain": urlparse(url).netloc.replace("www.", ""),
        "publisher": data["publisher"] or bias_info.get("publisher"),
        "bias": bias_info.get("bias"),
        "political_alignment": bias_info.get("alignment"),
        "title": data["title"],
        "authors": data["authors"],
        "publish_date": data["publish_date"].isoformat() if data["publish_date"] else None,
        "summary": data["summary"],
        "keywords": data["keywords"],
        "top_image": data["top_image"],
        "word_count": len(data["text"].split()),
        "claims_extracted": claims,
        "checked_claims": checked_claims,
        "factuality_score": score,
        "checked_title": checked_title,
    }

    return output

# -------------------------------------------------------------------------
# 7️⃣ CLI Entry Point
# -------------------------------------------------------------------------
if __name__ == "__main__":
    test_url = input("Enter article URL: ").strip()
    result = analyze_article(test_url)
    print(json.dumps(result, indent=2, ensure_ascii=False))
