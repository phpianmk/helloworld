# helloworld

This repository contains a simple example script for scraping property listings from [Zoopla](https://www.zoopla.co.uk/). The script is for educational purposes only. Scraping a website may violate its terms of use, so ensure you have permission before running the script.

## Requirements

```
pip install requests beautifulsoup4
```

## Usage

Provide a postcode and the script will print listings for that area:

```
python zoopla_scraper.py SW11 1AA
```

If you receive a `403 Forbidden` response, Zoopla may be blocking automated
requests. Check their terms of use and try again later.
