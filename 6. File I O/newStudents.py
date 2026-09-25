import csv

name = input("What's your name? ")
home = input("What's your home? ")

with open("newStudents.csv", "a", newline="") as file:
# I need to use newline because on Windows the csv add a line space. On MAC it does not :c
    """
    writer= csv.writer(file)
    writer.writerow([name, home]) """

    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})