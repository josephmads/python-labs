# The import below gives you a new random list of numbers,
# called `randlist`, every time you run the script.
#
# Write a script that takes this list of numbers and:
#     - sorts the numbers
#     - stores the numbers in tuples of two in a new list
#     - prints each tuple
#
# If the list has an odd number of items,
# add the last item to a tuple together with the number `0`.
#
# Note: This lab might be challenging! Make sure to discuss it 
# with your mentor or chat about it on our forum.

from resources import randlist


# print(randlist)

# Write your code below here

# code each part separately first.

# sort numbers
sorted_list = sorted(randlist)
print(sorted_list)

# for loop that places numbers into list of tuples of two

tup_list = []
tup1 = []

while len(sorted_list) >= 2:
    for num in sorted_list:
        tup1.append(sorted_list.pop(0))
        tup1.append(sorted_list.pop(0))
        tup1 = tuple(tup1)
        tup_list.append(tup1)
        tup1 = []

if len(sorted_list) == 1:
        tup1.append(sorted_list.pop(0))
        tup1.append(0)
        tup1 = tuple(tup1)
        tup_list.append(tup1)
            
print(tup_list)
