# search for all .jpg files in Pictures
# compile list of .jpg's with complete path to each file

# use for loops and conditional statements
# and nested loops
# pathlib

import pathlib

path = pathlib.Path("/home/joe/Pictures/")

for filepath in path.rglob("*.JPG"):
    print(filepath)
