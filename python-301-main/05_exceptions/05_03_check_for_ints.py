# Create a script that asks a user to input an integer, checks for the
# validity of the input type, and displays a message depending on whether
# the input was an integer or not.
# The script should keep prompting the user until they enter an integer.

attempt = True

while attempt == True:
    try:
        user_int = int(input("Please enter an integer: "))
        attempt = False
        print("Good job.")
    except ValueError:
        print("That isn't an integer...")
