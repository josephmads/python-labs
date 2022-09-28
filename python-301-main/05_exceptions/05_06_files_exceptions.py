# In this exercise, you will practice both File I/O as well as using Exceptions
# in a real-world scenario.
#
# This folder contains another folder called `books/` that contains three text files
# of books from Project Gutenberg:
# 1. war_and_peace.txt
# 2. pride_and_prejudice.txt
# 3. crime_and_punishment.txt
#
# 1) Open `war_and_peace.txt`, read the whole file content and store it in a variable
# 2) Open `crime_and_punishment.txt` and overwrite the whole content with an empty string
# 3) Loop over all three files and print out only the first character each. Your program
#    should NEVER terminate with a Traceback.
#     a) Which exception can you expect to encounter? Why?
#     b) How do you catch it to avoid the program from terminating with a traceback?

book_list = ["books/war_and_peace.txt", "books/pride_and_prejudice.txt",
            "books/crime_and_punishment.txt"]

with open(book_list[0], "r") as fin:
    war = fin.read()

with open(book_list[2], "w") as fout:
    fout.write("")

for book in book_list:
    with open(book, "r") as fin:
        print(fin.read(1))
