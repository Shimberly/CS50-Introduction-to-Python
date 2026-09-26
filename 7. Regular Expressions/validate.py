import re

email = input("What's your email? ").strip() #.lower()

""" Option 1
if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid") """

""" Option 2
username, domain = email.split("@")

if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid") """

""" Option 3 - Using re library"""
#if re.search(r"^[^@]+@[^@]+\.edu$", email): # -> [^@] means anything but a @
#if re.search(r"^[a-zA-Z0-9_-]+@[a-zA-Z0-9_]+\.edu$", email):
if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.(com|edu|gov|es)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")