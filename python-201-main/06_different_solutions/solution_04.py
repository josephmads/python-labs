'''
Write a script that sorts a list of tuples based on the number value in the tuple.
For example:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

'''

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = []

# converts the tuples in unsorted _list in lists
for tup in list(unsorted_list):

    current_min = unsorted_list[0][1]
    index = 0
# creates an index of the lists
    for i in range(0, len(unsorted_list)):
        # matches index to elements in unsorted list
        if unsorted_list[i][1] < current_min:
            current_min = unsorted_list[i][1]
            index = i
            # appends elements to new list if they match the lowest number
            # and removes them from unsorted_list before looping through again. 
    sorted_list.append(unsorted_list[index])
    unsorted_list.remove(unsorted_list[index])

print(unsorted_list)
print(sorted_list)
