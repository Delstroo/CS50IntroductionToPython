x = int(input("What's x? "))
y = int(input("What's y? "))

# There are a few ways you could go about handling these questions the most simple and most complex being.
# if x < y:
#    print("x is less than y")

# if x > y:
#    print("x is greater than y")

# if x == y: 
#   print("x is equal to y")


# The next way you could handle it is by adding elif instead of just if.
# if x < y:
#    print("x is less than y")

# elif x > y:
#    print("x is greater than y")

# elif x == y: 
#    print("x is equal to y")


# Another way you could handle this and by removing some complexity is being having it end with an else.
# if x < y:
#    print("x is less than y")

# elif x > y:
#    print("x is greater than y")

# else if x == y: 
#    print("x is equal to y")


# Another way you can run this in a simple way is like. This will use the 'or' method along with the 'else' method to clean up code and reduce on the ammount of logic that is being used.
# if x < y or x > y:
#    print("x is not equal to y")
# else: 
#    print("x is equal to y")


# A cleaner way to ask this question is by doing this
    
if x != y:
    print("x is not equal to y")
else :
    print("x is equal to y")