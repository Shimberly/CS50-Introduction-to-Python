import csv

""" Example 1
with open("students.csv") as file:
    for line in file:
        
        #row = line.rstrip().split(",")
        #print(f"{row[0]} lives in {row[1]}") 

        name, house = line.rstrip().split(",")
        print(f"{name} lives in {house}") """

students = []

""" Example 2 

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house":house}
        students.append(student) """

# Example 3 -  using CSV module
with open("students.csv") as file:        
     
    
    """ Option 1
    reader = csv.reader(file) #Read as a list
    for name, house in reader:
        students.append({"name": name, "house":house}) """

    """ Option 2 """
    reader = csv.DictReader(file) #Read as a dictionary
    for row in reader:
        students.append({"name": row["name"], "house":row["home"]})
# Option 1
# def get_name(student):
#    return student['name']

# def get_house(student):
#    return student['house'] 

#for student in sorted(students, key=get_name, reverse=True): 

# Option 2 - Anonymus function, directly used 
for student in sorted(students, key=lambda student: student["name"]): 
    print(f"{student['name']} lives in {student['house']}") 


