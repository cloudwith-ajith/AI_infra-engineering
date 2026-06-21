name = input("What's you house? ")

match name:
    case "harry" | "hermione" |" ron":
        print("gryffinndor")
    case "daro":
        print("slytherin")
    case _:
        print("who? ")
        