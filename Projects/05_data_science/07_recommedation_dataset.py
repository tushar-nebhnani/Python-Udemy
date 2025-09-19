"""
    BOOK RECOMMENDATION SYSTEM
"""

import pandas as pd

data = {
  "books": [
    {
      "title": "Dune",
      "author": "Frank Herbert",
      "genre": "Science Fiction",
      "description": "Dune is not just a book; it's a world. The level of detail in the politics, religion, and ecology of Arrakis is breathtaking. The characters are complex and the plot is a slow burn that rewards patience. A must-read for any fan of the genre."
    },
    {
      "title": "The Silent Patient",
      "author": "Alex Michaelides",
      "genre": "Thriller",
      "description": "I was hooked from the first page. The short chapters kept me reading late into the night. While I found the main character a bit frustrating at times, the final twist completely blew my mind. I didn't see it coming at all. Highly recommended for mystery lovers."
    },
    {
      "title": "Educated: A Memoir",
      "author": "Tara Westover",
      "genre": "Memoir",
      "description": "This memoir is a testament to the power of education and the resilience of the human spirit. Tara Westover's story is both heartbreaking and inspiring. Her journey from a survivalist family in rural Idaho to earning a PhD from Cambridge is incredible. I couldn't put it down."
    },
    {
      "title": "Project Hail Mary",
      "author": "Andy Weir",
      "genre": "Science Fiction",
      "description": "Andy Weir has done it again! This book is a perfect blend of hard science, humor, and heart. Ryland Grace is a fantastic protagonist, and his journey is full of clever problem-solving and unexpected turns. The relationship he forms is one of the best I've ever read. Amaze!"
    },
    {
      "title": "The Alchemist",
      "author": "Paulo Coelho",
      "genre": "Fantasy",
      "description": "I know this book is beloved by many, but I found it to be incredibly repetitive and the message too simplistic. The prose felt more like a children's story than a profound philosophical novel. It just wasn't for me."
    },
    {
      "title": "Atomic Habits",
      "author": "James Clear",
      "genre": "Self-Help",
      "description": "This is the most practical and actionable book on habits I have ever read. Clear breaks down the science of habit formation into four simple laws. The concept of '1% better every day' has already made a huge impact on my daily routine. A must-read for anyone looking for self-improvement."
    },
    {
      "title": "Gone Girl",
      "author": "Gillian Flynn",
      "genre": "Mystery",
      "description": "What a ride. This book is masterfully plotted. The narrative shifts between Nick and Amy are brilliant, and just when you think you have it figured out, Flynn pulls the rug out from under you. It's a dark and cynical look at marriage, but I couldn't stop reading."
    },
]}

df = pd.DataFrame(data)
df.to_csv("books.csv")
print("✅ Books DataSet Created.")

# TF-ID ALGORITHM