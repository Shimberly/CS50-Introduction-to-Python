import sys

""" Option 1
try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")"""

""" Option 2: Check for errors
if len(sys.argv)<2:
    print("Too few arguments")
elif len(sys.argv)>2:
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])"""

""" Option 3
if len(sys.argv)<2:
    sys.exit("Too few arguments")
elif len(sys.argv)>2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1]) """

if len(sys.argv)<2:
    sys.exit("Too few arguments")

# Slices #
# My input is "python name.py kimberly munoz cepeda"
for arg in sys.argv[1:]:
    print("hello, my name is", arg)