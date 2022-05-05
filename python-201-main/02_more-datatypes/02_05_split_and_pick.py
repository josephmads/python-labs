# Write a script that takes in a string from the user.
# Using the `split()` method, create a list of all the words in the string
# and print back the most common word in the text.

user_input = input("Write a sentence: ")
ui_list = user_input.split()
num = 0


for word in ui_list:
    # count the occurences of the word in the list
    w_count = ui_list.count(word)
    if w_count > num:
        num = w_count
        common_word = word
   
print(common_word)
