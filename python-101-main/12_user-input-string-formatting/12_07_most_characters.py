# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings

string1 = input("Type something: ")
string2 = input("Type another thing: ")
string3 = input("Type a final thing: ")

if len(string1) > len(string2) and len(string3):
    print(len(string1), string1)
elif len(string2) > len(string1) and len(string3):
    print(len(string2), string2)
else:
    print(len(string3), string3)