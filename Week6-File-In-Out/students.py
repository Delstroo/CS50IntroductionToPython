import csv


# Writing to file
name = input("What's your name? ")
home = input("Where is your home? ")

with open("name.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})

# Reading file
# students = []

# with open("names.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student)

# def get_name(student):
#     return student["name"]

# def get_house(student):
#     return student["house"]

# for student in sorted(students, key=get_house):
#     print(f"{student['name']} is in {student['house']}")