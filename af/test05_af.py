import requests
import pandas as pd
from langdetect import detect, DetectorFactory
from datetime import datetime
import os
import time
import math

# Reproducibility for langdetect
DetectorFactory.seed = 0

# API settings
MUNICIPALITY_CODE = "0180"  # Stockholm municipality
BASE_URL = "https://jobsearch.api.jobtechdev.se/search"
PAGE_SIZE = 100
MAX_PAGES = 150  # safety limit

# Keyword lists
ENGLISH_KEYWORDS = [
    "english", "engelska", "fluent in english",
    "business english", "apply in english",
    "good command of english", "chinese", "china", "kina", "kinesiska", "mandarin"
]
NEGATIVE_KEYWORDS = [
    "no english", "not english", "städare", "skötare", "fluent in Swedish", "care assistant", "obehindrat på både svenska", "obehindrat på svenska"
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
    t = (text or "").lower()
    if any(neg in t for neg in NEGATIVE_KEYWORDS):
        return False
    return any(pos in t for pos in ENGLISH_KEYWORDS)


def fetch_ads(offset=0):
    """Fetch ads from API for Stockholm. Returns (json, request_url)."""
    params = {
        "municipality": MUNICIPALITY_CODE,
        "offset": offset,
        "limit": PAGE_SIZE
    }
    resp = requests.get(BASE_URL, params=params, timeout=15)
    resp.raise_for_status()
    return resp.json(), resp.url


def extract_total(resp_json):
    """Try to extract an integer total from several possible shapes."""
    total = resp_json.get("total")
    # If it's already an int/float -> return int
    if isinstance(total, (int, float)):
        return int(total)
    # If it's a dict, try common keys
    if isinstance(total, dict):
        for key in ("value", "count", "total", "hits", "totalCount", "total_results"):
            v = total.get(key)
            if isinstance(v, (int, float)):
                return int(v)
            try:
                if v is not None:
                    return int(v)
            except Exception:
                pass
    # Some APIs place total elsewhere
    for alt_key in ("totalResults", "hitsTotal", "count", "total_count"):
        v = resp_json.get(alt_key)
        if isinstance(v, (int, float)):
            return int(v)
        try:
            if v is not None:
                return int(v)
        except Exception:
            pass
    # Can't find numeric total, return None to indicate unknown
    return None


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
    matching_count = 0

    # Fetch first page to read total (and to validate response shape)
    try:
        first_page_json, first_url = fetch_ads(offset=0)
    except Exception as e:
        print(f"ERROR fetching first page: {e}")
        return

    total_jobs = extract_total(first_page_json)
    if total_jobs is not None:
        print(f"🔎 Total jobs reported by API: {total_jobs}")
        max_pages = min(MAX_PAGES, math.ceil(total_jobs / PAGE_SIZE) if total_jobs > 0 else 0)
        print(f"Will fetch up to {max_pages} pages (page size {PAGE_SIZE})")
    else:
        print("⚠️ Could not extract numeric 'total' from API response — falling back to iterative fetch.")
        max_pages = MAX_PAGES

    # Use iterative offset loop — safer and gives control
    offset = 0
    prev_ids = set()
    page_num = 0
    pages_to_fetch = max_pages if (total_jobs is not None) else MAX_PAGES

    while page_num < pages_to_fetch:
        page_num += 1
        try:
            page_json, request_url = fetch_ads(offset=offset)
        except Exception as e:
            print(f"ERROR fetching offset {offset}: {e}")
            break

        # Debug: print requested URL so you can validate offset progression
        print(f"[Page {page_num}] Request URL: {request_url}")

        hits = page_json.get("hits", [])
        current_ids = {str(job.get("id")) for job in hits if job.get("id") is not None}

        # stop conditions
        if not hits:
            print(f"[Page {page_num}] No hits returned — reached end.")
            break
        if current_ids == prev_ids:
            print(f"[Page {page_num}] IDs identical to previous page — stopping to avoid loop.")
            break

        prev_ids = current_ids

#        print(f"[Page {page_num}] Processing {len(hits)} jobs (offset {offset}).")

        for job in hits:
            job_id = str(job.get("id"))
            if job_id in seen_ids:
                continue  # skip already applied

            title = job.get("headline", "") or ""
            text = job.get("description", {}).get("text", "") if job.get("description") else ""
            must_have = " ".join(job.get("mustHave", []) or [])
            nice_to_have = " ".join(job.get("niceToHave", []) or [])

            combined = " ".join([title, text, must_have, nice_to_have])

            lang = detect_lang(combined)
            english_flag = mentions_english(combined)

            if lang == "en" or english_flag:
                addr = job.get("workplaceAddress", {}) or {}
                ads.append({
                    "job_id": job_id,
                    "title": title,
                    "employer": (job.get("employer") or {}).get("name", ""),
                    "lang": lang,
                    "english_flag": english_flag,
                    "municipality": addr.get("municipality", ""),
                    "region": addr.get("region", ""),
                    "city": addr.get("city", ""),
                    "streetAddress": addr.get("streetAddress", ""),
                    "url": job.get("webpageUrl", ""),
                    "text_excerpt": (text or "")[:300].replace("\n", " ") + "..."
                })
                matching_count += 1

        print(f"[Progress] Found {matching_count} matching jobs so far.\n")

        # advance
        offset += PAGE_SIZE
        time.sleep(0.4)  # be polite

    # Save results
    if ads:
        df = pd.DataFrame(ads)
        df.to_csv(OUTPUT_FILE, index=False)
        print(f"✅ Saved {len(df)} English-friendly jobs to {OUTPUT_FILE}")
    else:
        print("No matching jobs found.")


if __name__ == "__main__":
    main()
