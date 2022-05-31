# Reproduce the functionality of Python's built-in `enumerate()` function.
# Define a function called `my_enumerate()` that takes an iterable as input
# and gives back both the element as well as its index position as an integer.

def my_enumerate(iterable, start=0):  # add your arguments
      # assigns the start inex to a variable and starts the enumeration 
      count = start
      # iterates through iterable and yields the starting index
      # plus each item in the iterable.
      for item in iterable:
            yield count, item
            # adds 1 to the enumeration count before going through the iterable again
            count += 1


courses = ['Intro', 'Intermediate', 'Advanced', 'Professional']

for index, course in my_enumerate(courses, start=1):
    print(f"{index}: {course} Python")