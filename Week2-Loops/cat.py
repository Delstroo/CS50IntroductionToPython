def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break    
    return n

def meow(n):
    for i in range(n):
        print(f"meow {i}")

main()


#This is an example of a user based for loop.
#while True:
#    n = int(input("What's n? "))
#    if n > 0:
#        break

#for _ in range(n):
#    print("meow")

#This is a simple for loop using the range method,
#for i in range(0, 99):
#    print(f"dog {i}")


#This is a simple example of a while loop.
#i = 3

#while 0 != i:
#    print("meow")
#   i = i - 1