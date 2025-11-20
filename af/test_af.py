import requests
import pandas as pd
from langdetect import detect, DetectorFactory
from datetime import datetime
import os

# Reproducibility for langdetect
DetectorFactory.seed = 0

# API settings
MUNICIPALITY_CODE = "0180"  # Stockholm
BASE_URL = "https://jobsearch.api.jobtechdev.se/search"
PAGE_SIZE = 1000

# Keyword lists
ENGLISH_KEYWORDS = [
    "english", "engelska", "fluent in english",
    "business english", "apply in english",
    "good command of english"
]
NEGATIVE_KEYWORDS = [
    "no english", "not english"
]

# File paths
OUTPUT_FILE = "stockholm_english_jobs.csv"
TRACKER_FILE = "applied_jobs.csv"


def detect_lang(text):
    """Detect primary language of text"""
    try:
        return detect(text)
    except:
        return "unknown"


def mentions_english(text):
    """Check if ad text mentions English requirements"""
    t = text.lower()
    if any(neg in t for neg in NEGATIVE_KEYWORDS):
        return False
    return any(pos in t for pos in ENGLISH_KEYWORDS)


def fetch_ads(page=1):
    """Fetch ads from API for Stockholm"""
    params = {
        "municipality": MUNICIPALITY_CODE,
        "page": page,
        "pageSize": PAGE_SIZE
    }
    resp = requests.get(BASE_URL, params=params, timeout=10)
    resp.raise_for_status()
    return resp.json()


def load_tracker():
    """Load already applied job IDs"""
    if os.path.exists(TRACKER_FILE):
        df = pd.read_csv(TRACKER_FILE)
        return set(df["job_id"].astype(str).tolist())
    return set()


def save_tracker(job_ids):
    """Append new applied jobs to tracker"""
    df = pd.DataFrame(job_ids, columns=["job_id"])
    df["applied_at"] = datetime.now().isoformat()
    if os.path.exists(TRACKER_FILE):
        df.to_csv(TRACKER_FILE, mode="a", header=False, index=False)
    else:
        df.to_csv(TRACKER_FILE, index=False)


def main():
    ads = []
    seen_ids = load_tracker()

    # Fetch first page (you can loop if you want more)
    data = fetch_ads(page=1)
    for job in data.get("hits", []):
        job_id = str(job.get("id"))
        if job_id in seen_ids:
            continue  # skip already applied

        title = job.get("headline", "")
        text = job.get("description", {}).get("text", "")
        must_have = " ".join(job.get("mustHave", []))
        nice_to_have = " ".join(job.get("niceToHave", []))

        combined = " ".join([title, text, must_have, nice_to_have])

        lang = detect_lang(combined)
        english_flag = mentions_english(combined)

        if lang == "en" or english_flag:
            ads.append({
                "job_id": job_id,
                "title": title,
                "employer": job.get("employer", {}).get("name", ""),
                "lang": lang,
                "english_flag": english_flag,
                "url": job.get("webpageUrl", ""),
                "text_excerpt": text[:300].replace("\n", " ") + "..."
            })

    # Save to CSV
    if ads:
        df = pd.DataFrame(ads)
        df.to_csv(OUTPUT_FILE, index=False)
        print(f"[+] Saved {len(df)} English-friendly jobs to {OUTPUT_FILE}")
    else:
        print("[-] No matching jobs found.")

    # Example: if you manually apply, add IDs to tracker:
    # save_tracker([job["job_id"] for job in ads])


if __name__ == "__main__":
    main()
