# Write code that removes all duplicates from a list.
# Solve this challenge in two ways:
# 1. Convert to a different data type
# 2. Use a loop and a second list to solve it more manually

list_ = [1, 2, 3, 4, 3, 4, 5]

set1 = set(list_)
print(set1)

no_dups = []

for num in list_:
    if num not in no_dups:
        no_dups.append(num)

print(no_dups) 

list_ = list(set1)
print(list_)