"""
    Quote of the Day Image Maker: 
"""
import os 
import requests
from bs4 import BeautifulSoup
import textwrap
from PIL import Image, ImageDraw, ImageFont


BASE_URL = "https://quotes.toscrape.com"
OUTPUT_DIR = "quotes"

def fetch_quotes(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"ERROR: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.select("div.quote")

    quote_data = []

    for quote in quotes[:5]:
        text = quote.find("span", class_="text").text.strip('“”')
        author = quote.find("small", class_="author").text

        quote_data.append((text, author))

    return quote_data

def create_image(text, author, index):
    width, height = 800, 400
    background_color = "#efd07b"
    text_color = "#4B4646"

    image = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(image)
    
    font = ImageFont.load_default()
    author_font = ImageFont.load_default()

    wrapped = textwrap.fill(text, width=60)
    author = f"- {author}"

    y_text = 60
    draw.text((40, y_text), wrapped, font=font, fill=text_color)

    y_text += wrapped.count('\n') * 15 + 40
    draw.text((500, y_text), author, font=font, fill=text_color)

    # save image
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    filename = os.path.join(OUTPUT_DIR, f"quote_{index+1}.png")
    image.save(filename)
    print(f"✅ Saved: {filename}")

def main():
    quotes = fetch_quotes(BASE_URL)
    for idx, (text, author) in enumerate(quotes):
        create_image(text, author, idx)

if __name__ == "__main__":
    main()