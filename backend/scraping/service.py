from typing import List, Dict
import requests

from scraping.scraper import scrape_page


def scrape_website(base_url: str) -> List[Dict]:
    """
    Scrape homepage + common relevant pages
    """

    pages_to_try = [
        base_url,
        f"{base_url.rstrip('/')}/about",
        f"{base_url.rstrip('/')}/contact",
        f"{base_url.rstrip('/')}/careers",
    ]

    scraped_pages = []

    for url in pages_to_try:
        try:
            content = scrape_page(url)
            if content:
                scraped_pages.append({
                    "url": url,
                    "content": content
                })
        except requests.RequestException:
            continue

    return scraped_pages
