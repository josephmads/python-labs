# Write a script that takes a string from the user
# and creates a list that contains a tuple for each word.
# For example:

# input = "hello world"
# result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

user_input = "hello world"

input_list = user_input.split()

result_list = [tuple(input_list[0]), tuple(input_list[1])]

print(result_list)
