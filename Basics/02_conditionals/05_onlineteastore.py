name = input("Enter your name: ").lower().capitalize()
order_amt = int(input(f"{name}, Enter your order amount: "))

delivery_fee = 0 if order_amt > 300 else 30

print(f"{name}, your delivery fees is: {delivery_fee}")