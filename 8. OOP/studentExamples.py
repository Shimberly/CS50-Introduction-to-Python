# Class are blueprints
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
        #self.patronus = patronus
    
    def __str__(self):
        return f"{self.name} from {self.house}"

    #Getter
    @property
    def house(self):
        return self._house
    #Setter
    @house.setter
    def house(self, house):
        if house not in ["Zurich", "Aargau", "Bern"]:
            raise ValueError("Invalid house")
        self._house = house

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if not name:
            #raise -> create your own exception
            raise ValueError("Missing name")
        self._name = name

    """ def charm(self):
        match self.patronus:
            case "Miau":
                return "🐱‍👤"
            case "Otter":
                return "🧸"
            case _:
                return "🔗" 
    """

def main():
    #name = get_name()
    #house = get_house()
    
    #name, house = get_student() #-> tuple
    
    student = get_student()
    
    # Using tuple or list
    #print(f"{student[0]} from {student[1]}")

    """ #Using dictionary
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}") """

    #Using OOP
    #print(f"{student.name} from {student.house}")
    #print("Expecto Patronum!")  
    #print(student.charm())
    #student.house = "Number Four"
    #student._house = "Number Four" #If a variable has _ it means its private, but python dont protect it, its on you
    print(student)

"""
def get_name():
    return input("Name: ")

def get_house():
    return input("House: ") """

def get_student():
    """ Example of tuple 
    # tuple -> non mutable way of pass data (similar to list)
    name = input("Name: ")
    house = input("House: ")
    return (name, house) """

    """ Example Dictionary
    # Option 1
    student = {}
    student["name"] = input("Name: ")
    student["house"] =input("House: ")
    return student 
    # Option 2
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house} """

    #Using OOP
    #student.name = input("Name: ")
    #student.house = input("House: ")
    #student = Student() #creating an OBJECT from a CLASS Student (Object also calles Instances)

    name = input("Name: ")
    house = input("House: ")
    #patronus = input("Patronus: ")
    return Student(name, house) #Passing instance variables to the class / it uses the object constructor

    
if __name__ == "__main__":
    main()