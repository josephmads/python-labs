# Convert some sequences you got to know into other sequences:
# - Convert the string shown below into a tuple.
# - Convert the tuple into a list.
# - Change the `c` character in your list into a `k`
# - Convert the list back into a tuple.

string = "codingnomads"

tup1 = tuple(string)
list1 = list(tup1)

list1.insert(1, "k")
list1.remove("c")

tup2 = tuple(list1)