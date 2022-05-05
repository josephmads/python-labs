# Print the total number of vowels that are used in the lorem ipsum text.

lorem_ipsum = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut 
aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in 
voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt 
mollit anim id est laborum."""

total_vowels = 0

for char in lorem_ipsum:
    if char in "aeiou":
        total_vowels += 1

print(total_vowels)
        
# used the forum to find my answer. I learned the variables in a for loop
# can come from outside the loop and that each line in a for loop doesn't have to
# explicitly reference a variable or operator from a preceding line. 

