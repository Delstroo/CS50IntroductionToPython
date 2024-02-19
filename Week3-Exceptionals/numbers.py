#This talks about the usages of the `try` and `except` methods, that will ensure that when we ask for int we will get an int or an error message.

try:
    x = int(input("Whats x?"))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer.")

print(f"x is {x}")