
# This splits this into two seperate functions, one to check to see if an input is even, and the main() function will allow for user input and spit out a response.

def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else: 
        print("Odd")


def is_even(n):
    # This is one way to handle this return method. This is called being 'Pythonic Expression'
    #return True if n % 2 == 0 else False
    
    # A refined version of this could look like this
    return n % 2 ==0
    
    #  This is another way you can handle this return method
    #        if n % 2 == 0:
    #        return True
    #    else:
    #        return False
main()

#This is used to show how '%' is used, in this case it is to check to see if input is even or odd

# x = int(input("What's x? "))

# if x % 2 == 0:
#    print("Even")
# else: 
#    print("Odd")