choice = input("Enter a number from 1 to 3: ")
match choice:
    case "1":
        print("You selected One")
    case "2":
        print("You selected Two")
    case "3":
        print("You selected Three")
    case _:
        print("Invalid choice")
