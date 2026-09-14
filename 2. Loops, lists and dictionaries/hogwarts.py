""" Example 1 """
#students = ["Hermione", "Harry", "Ron", "Draco"]
#houses = ["Gryffindor","Gryffindor","Gryffindor","Slytherin"]

#for student in students:
#    print(student)

#for i in range(len(students)):
#    print(i+1, students[i])

""" Example 2:
students = {"Hermione":"Gryffindor", 
            "Harry":"Gryffindor", 
            "Ron":"Gryffindor",
            "Draco":"Slytherin"}

#print(students["Hermione"])
for student in students:
    print(student, students[student], sep=", ")"""

""" Example 3 """
students=[
    {"name":"Hermione", "house":"Gryffindor", "patronus":"Otter"},
    {"name":"Harry", "house":"Gryffindor", "patronus":"Stag"},
    {"name":"Ron", "house":"Gryffindor", "patronus":"Jack Russell terrier"},
    {"name":"Draco", "house":"Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"],sep=", ")