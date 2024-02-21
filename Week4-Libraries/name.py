import sys

arg = sys.argv

if len(arg) < 2:
    sys.exit("Too few arguments")
# elif len(arg) > 2:
#     sys.exit("Too many arguments")
else:
    print(arg[1])

# sys.argv[1:] is what is considered a slice in the list `[1:]` is the syntax used
    for arg in sys.argv[1:]:
        print("Hello, my name is.", arg)