# Self-Intro Script Generator 
# Question: Create a python script that interacts with the user and generators a personalized self-introduction.
import datetime as dt

name = input("What is your name? ").strip()
age = int(input("How old are you? "))
city = input("Which city do you live in? ").strip()
profession = input("What's is your profession? ").strip()
hobby = input("What is your favourite hobby? ").strip()

# we can write our intro in tuple so once its created we don't need to worry about it being changing.
intro_message = (
    f"Hello! my name is {name}, I'm {age} years old and live in {city}.\n" 
    f"I work as a {profession} and I absolutely enjoy {hobby} in my free time.\n"
    f"Nice to meet you!"
)
current_date = dt.date.today().isoformat()
intro_message += f"\nLogged on: {current_date}"

border = "*" * 80

final_output = f"{border}\n{intro_message}\n{border}"
print(final_output)