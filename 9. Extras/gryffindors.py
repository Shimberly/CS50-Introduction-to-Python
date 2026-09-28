"""
students = [
    {"name": "Hermione", "house":"Gryffindor"},
    {"name": "Harry", "house":"Gryffindor"},
    {"name": "Ron", "house":"Gryffindor"},
    {"name": "Draco", "house":"Slytherin"},
    {"name": "Padma", "house":"Ravenclaw"},
]
"""

"""
# List Comprehension with conditional
gryffindors = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]

print(*sorted(gryffindors))
"""

"""
# Using FILTER function
def is_gryffindor(s):
    return s["house"] == "Gryffindor"

gryffindors = filter(is_gryffindor, students)
# lambda is for making anonymous functions
for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])
"""

students = ["Hermione", "Harry", "Ron"]

""" Basic option
gryffindors = []
for student in students:
    gryffindors.append({"name": student, "house":"Gryffindors"})
"""

#List Comprehension
gryffindors = [{"name": student, "house":"Gryffindors"} for student in students]
#Result: [{'name': 'Hermione', 'house': 'Gryffindors'}, {'name': 'Harry', 'house': 'Gryffindors'}, {'name': 'Ron', 'house': 'Gryffindors'}]

# Dictionary Comprehension
gryffindors={student: "Gryffindor" for student in students}
# Result: {'Hermione': 'Gryffindor', 'Harry': 'Gryffindor', 'Ron': 'Gryffindor'}

#print(gryffindors)

""" Example of enumeration """
#for i in range(len(students)):
#    print(i+1, students[i])

# Enumerate function
for i, student in enumerate(students):
    print(i+1, student)
