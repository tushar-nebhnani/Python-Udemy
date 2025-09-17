"""
    Dowload the cover image of first 10 books from books.toscrape.com using wget.
"""

import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
import wget

BASE_URL = "https://books.toscrape.com/"
IMAGE_DIR = "images"

def sanitize_filename(title):
    return re.sub(r'[^\w\-_. ]', '', title).replace(" ", "_")

def scrape_and_dowlaod_images():
    url = BASE_URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.select("article.product_pod")[:10]

    if not os.path.exists(IMAGE_DIR):
        os.makedirs(IMAGE_DIR)

    for book in books:
        title = book.h3.a['title']
        relative_img = book.find("img")["src"]
        image_url = urljoin(BASE_URL, relative_img)
        print(f"url - {image_url}")

        filename = sanitize_filename(title) + ".jpg"
        filepath = os.path.join(IMAGE_DIR, filename)
        print(f"filepath - {filepath}\n")

        print(f"Dowloading: {title}")
        # dowload_image(image_url, filepath)
        wget.download(image_url, filepath)
    print("All 10 books cover are dowloaded.")

if __name__ == "__main__":
    scrape_and_dowlaod_images()