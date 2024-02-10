# def is short for define, this is used when you want to define/create a function.
def main():
    name = input("What's your name? ")
    hello(name)

def hello(to= "world"):
    print("Hello!", to)

#If you don't call main your code will not
main()





# Ask user for their name. This will remove whitespace from str and capatlizes user's name
#name = input("What's your name? ").strip().title()

# split() is used when trying to split a user's name into first and last, this isn't the only time this can be used but it is the way I am planning on implementing
#first, last = name.split(" ")
#print("Hello, " + first)

# Say hello to user.
#If you use '+' you will have to add a space manually.
#print("Hello, " + name)

#However, if you use ',' you will not have to add a space.
#print("Hello,", name)

# This print statement will print out "Hello, *Users name*", because we changed the parameter of 'end' to not be "\n" but to "". You could also change the value of 'sep' from " " to anything you would like for a string.
#print("Hello, ", end="")
#print(name)

# If you wanted to wrap "" in a string you should try to use it in either single brackets lime this '' or you can use the \ escaping character
#print("Hello, \"friend\"")
#print('Hello, "Friend"')

# If you wanted to use string interpolation you can use f"" the f stands for format, so it is actually called a formatstring
#print(f"Hello, {name}")
