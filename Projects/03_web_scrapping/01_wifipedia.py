# Scrape Wikipedia H2 Headers 

import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Central_limit_theorem"

def get_h2(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch pages: \n {e}")

    soup = BeautifulSoup(response.text, "html.parser")
    h2_tags = soup.find_all("h2")
    # print(h2_tags)
    headers = []
    for tag in h2_tags:
        header_text = tag.get_text(strip=True)
        if header_text and header_text.lower() != "contents":
            headers.append(header_text)
    print(headers)

get_h2(URL)
    