ticket_class = input("Enter the class of your ticket (luxury/AC/sleeper/general): ").lower()

match ticket_class:
    case "luxury":
        print("You have a completely luxury journey.")
    case "ac":
        print("You won't feel hot for sure.")
    case "sleeper":
        print("You may feel hot but you can survive")
    case "general":
        print("Make sure to get a seat.")
    case _:
        print("Invalid ticket class")