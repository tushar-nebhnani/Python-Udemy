# Emoji Enhancer Script 

emoji_map = {
    "happy": "😊", 
    "code": "💻",
    "love": "❤️",
    "tea": "🍵",
    "music": "🎧"
}

message = input("Enter your message: ")
updated_words = []
# process each word 
for word in message.split():
    cleaned = word.lower().strip(".,!?")
    emoji = emoji_map.get(cleaned, "")
    if emoji:
        updated_words.append(f"{word}{emoji} ")
    else:
        updated_words.append(word)
    
updated_message = " ".join(updated_words)
print(f"Enhanced Message: {updated_message}")

