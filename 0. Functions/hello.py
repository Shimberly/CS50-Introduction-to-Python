# Ask user for their name
name = input("Whats your name? ").strip().title()

# Using METHODS

#Capitalize user's name
#name = name.capitalize()
#name = name.title()
#Remove whitespace from str and capitalize
#name = name.strip().title()

#Split user's name into first name and last name
first, last = name.split(" ")

"""
Esto es
para comentarios grandes
"""

# Say hello to user
# Different ways of using function PRINT
"""
print("Hello,", name) #recieve 2 arguments and put the middle space automatically
print("Hola, "+ name) #using concatenation
print("Hallo, ", end="") #using print parameters (end)
print(name)
print("Bonjour,", name, sep='_') #using print parameters (sep)
print(f"Annyeong, {name}")
"""
print(f"Annyeong, {first}")
# 3 ways of using quotes inside a print
"""
print("Your name is 'Kim'")
print('Your name is "Kim"')
print("Your name is \"Kim\"")
"""

