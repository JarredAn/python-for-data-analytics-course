decision = input("Enter P for pizza, B for burger or T for turkey leg: ")

match decision:
    case "P":
        print("You ordered a pizza!")
    case "B":
        print("You ordered a burger!")
    case "T":
        print("You ordered a turkey leg!")
    case _:
        print("You did not enter a valid choice.")
