name = input("What's your name? ")

# This could be done with 'if' and 'elif', however this is a clean way to integrate this way to check on what the name the user is and determine what house they will be in.
match name: 
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Hufflepuff")