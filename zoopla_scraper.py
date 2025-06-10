"""
Example script to scrape property listings from Zoopla.

This script is for educational purposes only. Scraping websites may breach Zoopla's terms of use. Always check and respect a website's robots.txt and terms of service before scraping.
"""

import requests
from bs4 import BeautifulSoup


def fetch_listings(url: str):
    """Fetch property listings from a Zoopla results page."""
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    listings = []
    for article in soup.select("article"):  # Zoopla uses <article> for each listing
        address = article.select_one(".listing-results-address")
        price = article.select_one(".listing-results-price")
        summary = article.select_one(".listing-results-wrapper")
        listings.append({
            "address": address.get_text(strip=True) if address else None,
            "price": price.get_text(strip=True) if price else None,
            "summary": summary.get_text(strip=True) if summary else None,
        })
    return listings


def build_search_url(postcode: str) -> str:
    """Return the Zoopla search URL for the given postcode."""
    postcode = postcode.strip().replace(" ", "")
    return f"https://www.zoopla.co.uk/for-sale/property/{postcode}/?q={postcode}"


def main():
    import argparse
    parser = argparse.ArgumentParser(
        description="Scrape property data for a given postcode",
    )
    parser.add_argument(
        "postcode",
        help="UK postcode to search on Zoopla",
    )
    args = parser.parse_args()

    url = build_search_url(args.postcode)
    for item in fetch_listings(url):
        print(item)


if __name__ == "__main__":
    main()
