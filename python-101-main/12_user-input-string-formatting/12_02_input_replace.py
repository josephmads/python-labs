# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please

phrase = input("Write a phrase: ")
sym = input("Type a symbol: ")
new_phrase = ""

for char in range(0, len(phrase)):
    if(phrase[char] == phrase[0]):
        new_phrase += sym
    else: 
        new_phrase += phrase[char]

print(new_phrase)