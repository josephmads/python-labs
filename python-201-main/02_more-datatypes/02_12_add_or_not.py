# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# their input is a duplicate and deduct a point.
# If the user loses 5 points, quit the program.
# They win if they manage to create a set that has more than 10 items.

points = 5
user_set = set()

while points != 0 and len(user_set) != 10:
    user_num = input("Enter a number: ")
    int(user_num)
    if user_num not in user_set:
        user_set.add(user_num)
    else:
        print("Duplicate number. You lose 1 point. Please enter a unique number: ")
        points -= 1
    
if points == 0:
    print("You lose.")
else:
    print("You win!")
