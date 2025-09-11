# Daily Journal 
import datetime as dt

learing = input("Enter what have you learned so far? ").strip()
rating = int(input("⭐ Rate your productivity(1-5)? " ))

now = dt.datetime.now()
date_str = now.strftime("%Y-%m-%d - %I:%M %p")

journal_entry = "\n" + "-" * 50
journal_entry += f"\n🗓️ {date_str}\n{learing}"
if rating:
    journal_entry += f"\n Productivity Rating: {rating}\n"
journal_entry += "\n" + "-" * 50

with open("learning_journal.txt", "a", encoding="utf-8") as f:
    f.write(journal_entry)

print(f"Your journal entry has been saved to 'learning_journey.txt' file.")