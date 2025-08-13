class InvalidChaiError(Exception): pass

def bill(flavour, cups):
    menu = {"masala chai": 20, "ginger": 40}
    try:
        if flavour not in menu:
            raise InvalidChaiError("Chai is not available.")
        if not isinstance(cups, int): # used to check the instance of the variable.
            raise TypeError("Number of cups must be an integer.")
        total = menu[flavour] * cups
        print(f"Total cost: {total}")
    except Exception as e:
        print("Error: ", e)
    finally:
        print("Thank You.")
        print("-" * 30)

bill("mint", 2)
bill("masala chai", 2) 
bill("masala chai", "two") 
bill("mint", "two")