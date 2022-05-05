# Search StackOverflow for code snippets that contain list comprehensions.
# Rewrite the list comprehensions as a plain old for loops.

xs = ['a', 'b', 'c', 'd', 'b', 'b', 'b', 'b']
# xs = [x for x in xs if x != 'b']
# print(xs)

xs2 = []
for x in xs:
    if x != "b":
        xs2.append(x)

print(xs2)
