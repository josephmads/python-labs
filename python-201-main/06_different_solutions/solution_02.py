'''
Write a script that sorts a list of tuples based on the number value in the tuple.
For example:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

'''

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = []

value_list = []
# copies the integer from unsorted_list to value_list.
for tuple_ in unsorted_list:
    value_list.append(tuple_[1])

print(value_list)
value_list.sort() # sorts the integers.

# uses the sorted integers in value_list as a key to organize the order in
# which the tuples finally get added to sorted list.
for value in value_list:
    for tuple_ in unsorted_list:
        if tuple_[1] == value:
            sorted_list.append(tuple_)
            unsorted_list.remove(tuple_)
            break

print(sorted_list)
