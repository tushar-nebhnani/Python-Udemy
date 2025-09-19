import pandas as pd
import numpy as np
import random

# Generating DataSet
toxic_comments = [
    "You're so dumb",
    "You're Trash",
    "You're a loser",
    "Can't believe people like this",
    "This is the worst video I've ever seen.",
    "Literally nobody asked for this.",
    "Get a real job.",
    "What a waste of my time.",
    "The background music is so annoying.",
    "I knew more about this topic when I was 5.",
    "CHECK OUT MY CHANNEL!!!! SUBSCRIBE!!!",
    "Your voice is so irritating.",
    "Click here for free stuff now >>> [suspicious link]",
    "This is completely wrong and misleading."
]

supportive_comments = [
    "This helped me a lot",
    "So clear and helpful",
    "Wow, I finally understand this concept. Thank you!",
    "This is incredibly underrated content.",
    "You explained that perfectly.",
    "Keep up the great work! Can't wait for the next one.",
    "Subscribed! Your content is amazing.",
    "This was exactly what I was looking for.",
    "Great video, I learned something new today.",
    "I really appreciate the effort you put into these.",
    "You deserve way more views.",
    "Could you do a video on [related topic] next? This was fantastic!"
]
data = []

for i in range(50):
    data.append({"comment": random.choice(toxic_comments), "label": "toxic"})
    data.append({"comment": random.choice(supportive_comments), "label": "support"})

df = pd.DataFrame(data)
df.to_csv("youtube_comments.csv")
print("✅ Data Saved Succesfully.")