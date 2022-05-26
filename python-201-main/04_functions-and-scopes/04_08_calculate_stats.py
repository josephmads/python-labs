# Write a function named `stats()` that takes in a list of numbers
# and finds the maximum, minimum, average and sum of the numbers.
# Print these values to the console you call the function.

import math

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(num_list):
  # define the function here
  num_list.sort()
  maximum = num_list[-1]
  minimum = num_list[0]
  total = sum(num_list)
  average = total / len(num_list)
  print(f'Maximum number: {maximum}\nMinimum number: {minimum}\nAverage: {average}\nSum of numbers: {total}')

# call the function below here
stats(example_list)