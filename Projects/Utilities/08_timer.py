# Count Down Timer 
import time as t

while True:
    try:
        seconds = int(input("⏰ Enter the time(in seconds): "))
        if seconds < 1:
            print("Please enter a number greater than 0.")
            continue
        break
    except ValueError:
        print("Invalid input, please error a whole number.")

print("\n🔔 Timer started...")
for remaining in range(seconds, 0, -1):
    mins, secs = divmod(remaining, 60)
    time_format = f"{mins:02}:{secs:02}"
    print(f"⏲️ Time left: {time_format}", end="\r")
    t.sleep(1)

print("\n Time's up!")
print("\a")