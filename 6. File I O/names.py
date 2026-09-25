""" Example 1 
names = []

for _ in range(3):
    names.append(input("What's your name? "))

for name in sorted(names):
    print(f"hello, {name}") """

# name = input("What's your name? ")

# Write a file
""" Option 1 
# Open or create (if not exist) a file
#file = open("names.txt", "w") # w for write, but Overwrite what's in the file
file = open("names.txt", "a") # a is for append
file.write(f"{name}\n")
file.close() # Close and save """

""" Option 2 - Using with, automatically close the file """
""" with open("names.txt", "a") as file:
    file.write(f"{name}\n") """

# Read a file
""" Option 1
with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello", line.rstrip()) #rstrip for remove the line space """

""" Option 2 
with open("names.txt") as file:
    for line in sorted(file):
        print("hello", line.rstrip()) """

""" Option 3 """
names = []
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"hello, {name}")