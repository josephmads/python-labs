# Demonstrate how to create a generator object.
# Print the object to the console to see what you get.
# Then iterate over the generator object and print out each item.

gen = (x for x in range(10))

print(gen)

for n in gen:
    print(n)

