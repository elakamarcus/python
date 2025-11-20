import trafilatura
from trafilatura.settings import use_config
from urllib.parse import urlparse
import json
import datetime

def extract_article_info(url: str):
    # Configure Trafilatura
    config = use_config()
    config.set("DEFAULT", "EXTRACTION_TIMEOUT", "15")
    
    downloaded = trafilatura.fetch_url(url)
    if not downloaded:
        return {"error": "Failed to fetch URL"}

    # Extract structured data
    extracted = trafilatura.extract(downloaded, include_comments=False, include_tables=False, output_format="json")
    if not extracted:
        return {"error": "Failed to extract article content"}

    data = json.loads(extracted)
    
    # Add complementary metadata fields
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    extraction_time = datetime.datetime.utcnow().isoformat()

    result = {
        "url": url,
        "domain": domain,
        "title": data.get("title"),
        "author": data.get("author"),
        "date_published": data.get("date"),
        "description": data.get("description"),
        "categories": data.get("categories"),
        "tags": data.get("tags"),
        "language": data.get("language"),
        "text": data.get("text"),
        "length": len(data.get("text", "")),
        "extraction_time_utc": extraction_time
    }

    return result


if __name__ == "__main__":
    url = input("Enter a news article URL: ").strip()
    result = extract_article_info(url)
    print(json.dumps(result, indent=2, ensure_ascii=False))
