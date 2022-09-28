# Write a custom exception  that inherits from `Exception()`
# Open and read in the content of the book `.txt` files in the `books/` folder
# like you did in the previous exercise.
# Raise your `PrinceException()` if the first 100 characters of a book
# contain the string "Prince".

class PrinceException(Exception):
    pass

book_list = ["books/war_and_peace.txt", "books/pride_and_prejudice.txt",
            "books/crime_and_punishment_copy.txt"]

try:
    for book in book_list:
        with open(book, "r") as fin:
            prince = fin.read(100)
            if "Prince" in prince:
                raise PrinceException
            else:
                pass

except PrinceException:
    print("You found a prince!")