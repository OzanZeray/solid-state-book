"""Fetch papers from Sci-Hub by DOI.

Usage:
    python fetch_paper.py <DOI> [output_dir]

Example:
    python fetch_paper.py 10.1103/PhysRev.98.368 papers/
"""
import sys
import os
import re
import time
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

SCIHUB_BASE = "https://sci-hub.ist"


def fetch_pdf(doi, output_dir="."):
    """Download a paper PDF from Sci-Hub by DOI."""
    url = f"{SCIHUB_BASE}/{doi}"
    print(f"Fetching: {url}")

    resp = requests.get(url, verify=False, timeout=30)
    if resp.status_code != 200:
        print(f"ERROR: HTTP {resp.status_code}")
        return None

    # Extract PDF path from <object data="...pdf"> tag
    match = re.search(r'<object[^>]+data\s*=\s*"([^"]+\.pdf)', resp.text)
    if not match:
        # Fallback: look in fetch() calls
        match = re.search(r"fetch\s*\([^)]*['\"]([^'\"]+\.pdf)", resp.text)

    if not match:
        # Check if paper is not in database
        if "veritaban" in resp.text or "not found" in resp.text.lower():
            print("ERROR: Paper not in Sci-Hub database")
        else:
            print("ERROR: Could not find PDF URL in page")
        return None

    pdf_path = match.group(1).split("#")[0]
    if pdf_path.startswith("/"):
        pdf_url = f"{SCIHUB_BASE}{pdf_path}"
    elif not pdf_path.startswith("http"):
        pdf_url = f"{SCIHUB_BASE}/{pdf_path}"
    else:
        pdf_url = pdf_path

    print(f"PDF URL: {pdf_url}")
    pdf_resp = requests.get(pdf_url, verify=False, timeout=60)

    if pdf_resp.content[:4] != b"%PDF":
        print(f"ERROR: Response is not a PDF ({len(pdf_resp.content)} bytes)")
        return None

    # Generate filename from DOI (sanitize for filesystem)
    safe_doi = doi.replace("/", "_").replace(".", "_")
    safe_doi = re.sub(r'[<>:"|?*();\[\]{}]', '_', safe_doi)
    safe_doi = safe_doi[:100]  # truncate long DOIs
    filename = f"{safe_doi}.pdf"
    filepath = os.path.join(output_dir, filename)

    os.makedirs(output_dir, exist_ok=True)
    with open(filepath, "wb") as f:
        f.write(pdf_resp.content)

    size_kb = len(pdf_resp.content) / 1024
    print(f"SUCCESS: {filepath} ({size_kb:.0f} KB)")
    return filepath


def fetch_batch(dois, output_dir="papers", delay=3):
    """Download multiple papers with rate limiting."""
    results = {}
    for i, doi in enumerate(dois):
        print(f"\n[{i+1}/{len(dois)}] {doi}")
        path = fetch_pdf(doi, output_dir)
        results[doi] = path
        if i < len(dois) - 1:
            time.sleep(delay)

    print(f"\n{'='*60}")
    success = sum(1 for v in results.values() if v)
    print(f"Downloaded {success}/{len(dois)} papers")
    return results


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    doi = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "."
    fetch_pdf(doi, output_dir)
