# Write a script that takes a sentence from the user and returns:

#     the number of lower case letters
#     the number of uppercase letters
#     the number of punctuations characters
#     the total number of characters

# Use a dictionary to store the count of each of the above.

# Note: ignore all spaces.

# Example input:

# I love to work with dictionaries!

# Example output:

# Upper case: 1
# Lower case: 26
# Punctuation: 1
# Total chars: 28

sentence = "I would like to get more sleep, please!"
sen_dict = {}
upper_case = 0
lower_case = 0
punct = 0
total_char = 0

for char in sentence:
    if char.isupper():
        upper_case += 1
    if char.islower():
        lower_case += 1
    if char in '.,!?:;':
        punct += 1
    if char != " ":
        total_char += 1
    sen_dict['Upper case'] = upper_case
    sen_dict['Lower case'] = lower_case
    sen_dict['Punctuation'] = punct
    sen_dict['Total chars'] = total_char

for each, counter in sen_dict.items():
    print(f'{each}: {counter}')
