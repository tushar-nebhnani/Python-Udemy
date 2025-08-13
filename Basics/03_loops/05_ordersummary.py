names = ["Hitesh", "Tushar", "Priya", "Yash"]
amt = [1000, 500, 800, 200]

for name, bill in enumerate(zip(names, amt)):
    print(f"{name} paid {bill} rupees.")