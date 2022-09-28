# Read in the first number from `integers.txt`
# and perform a calculation with it.
# Make sure to catch at least two possible Exceptions (`IOError` and `ValueError`)
# with specific `except` statements, and continue to do the calculation
# only if neither of them applies.

file_name = 'integers.txt'

try: 
    with open("integers.txt", "r") as fin:
        first_int = fin.readline().rstrip()
except FileNotFoundError:
    print("Ensure your filename is spelled correctly.")

try:
    first_int = int(first_int)
    print(first_int / 3)
except TypeError:
    print("Try converting the read-in number to an integer.")
except NameError:
    print("Var not defined because file doesn't exist.")

