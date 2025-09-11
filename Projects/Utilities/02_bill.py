# Bill Spilt
import textwrap as tw

total_person = int(input("Enter the total number of people: "))

names = []
for i in range(0, total_person):
    name = input(f"Enter name for {i+1}th person: ").strip()
    names.append(name)

amt = float(input("Enter the total bill: "))

individual_share = round(amt / total_person, 2)

print("*" * 50)
print(f"Total Bill: {amt}")
print(f"Each person owes {individual_share} rupees")
for name in names:
    share = f"{name} has to pay {individual_share}."
    print(tw.dedent(share)) 

print()
print("*" * 50)