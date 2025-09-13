# Stylish Instagram Bio Generator
import textwrap as tw

name = input("Enter your name: ").strip()
profession = input("What's is your profession: ").strip()
passion = input("Enter your passion(in one line): ").strip()
emoji = input("Enter your favourite emoji: ")
handle = input("Enter your social media handle: ").strip()

print("\nChoose your style: ")
print("1. Simple lines")
print("2. Vertical flair")
print("3. Emoji sandwich")

style = int(input("Enter your choice: "))

def generate_style(style):
    if style == 1:
        return f"{emoji} {name} | {profession} \n {handle}"
    elif style == 2:
        return f"{emoji}{name}\n{profession}\n{passion}\n{handle}"
    elif style == 3:
        return f"{emoji*3}\n {name} - {profession}\n{passion}\n{handle}"
    
bio = generate_style(style)

print("Your Stylish Bio: ")
print("*" * 50)
print(tw.dedent(bio))
print("*" * 50)

save = input("Do you want to save this in a file?(y/n): ")

if save == 'y':
    filename = f"{name.lower().replace(' ',"_")}_bio.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(bio)
    print("File Saved.")