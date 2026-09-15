import cowsay
import sys
from sayings import goodbye

""" Example 1
if len(sys.argv) == 2:
    #cowsay.cow("hello, "+ sys.argv[1])
    cowsay.trex("hello, "+ sys.argv[1]) """

if len(sys.argv) == 2:
    goodbye(sys.argv[1])