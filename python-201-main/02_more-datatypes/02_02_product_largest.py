# Take in a few numbers from the user and place them in a list.
# If you want, you can instead use the provided randomly generated
# list called `randlist` to simulate the user input.
#
# Find the largest number in the list and print the result.
# Calculate the product of all of the numbers in the list.

from resources import randlist

my_list = (randlist)
my_list.sort()
print(my_list, my_list[-1])

total = 0

for num in my_list:
    total += num
print(total)