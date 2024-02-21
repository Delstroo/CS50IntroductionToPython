def main():
    hello("World")
    goodbye("World")

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

# '__`name`__' is a special variable who's value is set by python to be "main" when you run a file from the command line
if __name__ == "__main__":
    main()