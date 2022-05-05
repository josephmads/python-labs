# Use the built-in `sys` module to explicitly quit your script.
# Include this functionality into a loop where you're asking the user
# for input in an infinite `while` loop.
# If the user enters the word "quit", you can exit the program
# using a functionality provided by this module.

from sys import exit

q = ""

while q !="quit":
    q = input("Try to stop me: ")
    if q == "quit":
        exit()
    else:
        print("Hahaha, you'll never leave this loop!!")