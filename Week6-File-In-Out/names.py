#name = input("What's your name? ")

# This will open the file and the 'w' lets to file now we are going to write to it, you can also use 'a' to append instead.
#with open("names.txt", "a") as file:
    # This allows us to write user input onto that file
#    file.write(f"{name}\n")
# This will close the file after we finish.
#file.close()

names = []    

with open("names.txt", "r") as file:
    for line in file :
        names.append(line.rstrip())
#    lines = file.readlines()
        
for name in sorted(names):
    print(f"hello, {name}")

#for line in lines:
#    print("Hello,", line.rstrip())