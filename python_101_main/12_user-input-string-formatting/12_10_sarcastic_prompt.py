# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.

usr_string = "Create a sarcastic program that asks a user for their honest opinion"
sarcasm = ""
index = 0

for char in usr_string:
    if index % 2 == 0:
        sarcasm += char.upper() 
        index += 1
    else:
        sarcasm += char
        index += 1

print(sarcasm)


# word = "hello there"

# for index, char in enumerate(word):
#     if index % 2 == 0:
#         print(char.upper())
#     else:
#         print(char.lower())