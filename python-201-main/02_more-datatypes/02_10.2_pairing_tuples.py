from resources import randlist


# print(randlist)

# Write your code below here

# code each part separately first.

list_dict = {}

# sort numbers
sorted_list = sorted(randlist)
print(sorted_list)

if len(sorted_list) % 2 != 0:
    sorted_list.append(0)

# generate empty lists based on length of sorted_list / 2
count1 = int(len(sorted_list) / 2)

# generate a dictionary with ascending numerical keys
# and with values assigned after
for n in range(count1):
    list_dict[n + 1] = []

# for loop that places numbers into lists

val = 1

for num in sorted_list:
    if len(list_dict[val]) != 2:
        list_dict[val].append(num)
    else:
        val += 1    
        list_dict[val].append(num)

print(list_dict)