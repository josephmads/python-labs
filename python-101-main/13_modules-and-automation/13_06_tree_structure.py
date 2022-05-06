# Write a script that walks through a nested folder structure 
# and prints out all the Python files it can find.
# Run it in your labs folder and add formatting for nicer viewing.

import pathlib

# find the filepath to python101
labs_folder = pathlib.Path("/home/joe/codingnomads/python_101_main/")

# labs = pathlib.Path(labs_folder)

# for filepath in labs_folder.rglob("*.py"):
#     print(filepath.name)

for filepath in labs_folder.iterdir():
    if filepath.is_dir():
        for file in filepath.iterdir():
            if file.suffix == ".py":
                print(file.name)
    