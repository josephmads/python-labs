# Import pathlib
# Find the path to my Desktop
# List all the files on there
# Filter for screenshots only
# Create a new folder
# Move the screenshots in there

import pathlib

path = pathlib.Path("/home/joe")

for filepath in path.iterdir():
    print(filepath.name)
