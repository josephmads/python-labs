# Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#
# String input: hello world
# Letter input: o
# Result: 4

from operator import index


phrase = input("Write a small phrase: ")
letter = input("Type one letter from that phrase: ")

i = phrase.index(letter)
print("Index:", i)