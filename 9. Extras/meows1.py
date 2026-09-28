""" Example 1: Constants
# this is a constant, but python is not strict so you can manualy change it
MEOWS = 3

for _ in range(MEOWS):
    print("meow") """

""" Example 2: Class variables
class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")

cat = Cat()
cat.MEOWS = 4 # Its not an error but its not working
cat.meow() """

# Example 3: type hints 
# # pip install mypy

""" def meow(n: int) -> None: #Type hint
    for _ in range(n):
        print("meow") """

def meow(n: int) -> str: #Type hint
    #Docstrings use triple quotes. There is tools that takes this strings out to make documentation
    """ 
    Meow n times.
    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    """
    return "meow\n" * n

#number = input("Number: ") #this will give an error
#Type hint
number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")

# use in terminal: mypy meows.py