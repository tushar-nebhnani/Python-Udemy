# alive calculator
# better approach will be to wrap everything in a function, loop it

age = float(input("Enter your age: "))
days_old = round(age * 365.25)
hours_old = round(days_old * 24)
min_old = round(hours_old * 60)

print("You are approximately: ")
print(f"    - {days_old} days old.") 
print(f"    - {hours_old} hours old.")
print(f"    - {min_old} minutes old.")

print('hello' + 5)