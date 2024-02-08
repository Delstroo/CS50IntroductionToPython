#x = float(input("What's x? "))
#y = float(input("What's y? "))

#Input will only return it as a str value, so you will need to use the int() to change the value that is added.
#z = round(x + y, 3)
#print(f"{z:,}")

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

# This squares a number that has been added in using 'n' as a generic
def square(n):
    return n * n

main()