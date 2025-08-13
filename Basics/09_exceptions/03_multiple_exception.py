def process_order(item, quantity):
    try:
        price = {"masala": 20}[item] # retrive item from a dictionary.
        cost = price * quantity
        print(f"Total cost: {cost}")
    except KeyError:
        print("Sorry, the chai is not on menu.")
    except TypeError:
        print("Quantity must be in number")
    finally:
        print("Order Complete. Next customer...")
        print("-" * 30)

process_order("ginger", 2)
process_order("masala", 2)
process_order("ginger", "two")