# Write a script that takes the following two dictionaries
# and creates a new dictionary by combining the common keys
# and adding the values of duplicate keys together.
# Use `for` loops to iterate over these dictionaries
# to accomplish this task.
#
# Example output:
# result = {"a": 3, "b": 2, "c": 7 , "d": 2}

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

new_dict = {}

for k1, v1 in dict_1.items():
    new_dict[k1] = v1
for k1, v1 in dict_1.items():
    for k2, v2 in dict_2.items():
        if k2 not in new_dict.keys():
            new_dict[k2] = v2
        if k1 == k2:
            new_dict[k1] = v1 + v2
      
print(new_dict)
