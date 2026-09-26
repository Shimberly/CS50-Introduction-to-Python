import random
class Hat:
    #def __init__(self, name):
    #   self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    #When you dont want to create several instances of a Class, just make it global, so you use it kinda like a library
    @classmethod 
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

#hat = Hat()
#hat.sort("Harry")

Hat.sort("Harry")