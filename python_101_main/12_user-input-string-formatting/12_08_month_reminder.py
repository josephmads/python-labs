# Take in a number between 1 and 12 from the user
# and print the name of the associated month:
# "January", "February", ... "December"
# Print "Error" if the number from the user is not between 1 and 12.
# Use a nested `if` statement.

num = int(input("Type a number between 1 - 12: "))

if 1 <= num <= 12:
    if num == 1:
        print("January")
    elif num == 2:
        print("February")
    elif num == 3:
        print("March")
    elif num == 4:
        print("April")
    elif num == 5:
        print("May")
    elif num == 6:
        print("June")
    elif num == 7:
        print("July")
    elif num == 8:
        print("August")
    elif num == 9:
        print("September")
    elif num == 10:
        print("October")
    elif num == 11:
        print("November")
    elif num == 12:
        print("December")
else:
    print("Error")