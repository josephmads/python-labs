# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.

user_string = input("Please write something: ")

a,e,i,o,u = 0,0,0,0,0

for char in user_string:
    if char in "a":
        a += 1
    elif char in "e":
        e += 1
    elif char in "i":
        i += 1
    elif char in "o":
        o += 1
    elif char in "u": 
        u += 1

print("Total A's:", a)
print("Total E's:", e)
print("Total I's:", i)
print("Total O's:", o)
print("Total U's:", u)
