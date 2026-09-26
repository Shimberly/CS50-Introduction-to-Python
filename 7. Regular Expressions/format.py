import re

name = input("What's your name? ").strip()

""" Option 1 
if "," in name:
    last, first = name.split(", ?")
    name= (f"{first} {last}")
print(f"hello, {name}") """

""" Option 2
matches = re.search(r"^(.+), *(.+)$", name)
if matches:
    last, first = matches.groups()
    name= (f"{first} {last}") """

# Option 3
if matches := re.search(r"^(.+), *(.+)$", name): # := -> new operator that allows you to asign and ask a boolean at the same time
    name = matches.group(2) + " " + matches.group(1)

print(f"hello, {name}")