# Write a script that demonstrates a try/except/else statement.
# For example, you can revisit the course module about database interactions
# and include a try/except/else statement based on what to do whether or not
# the database connection can be established.

attempt = True

while attempt == True:
    try:
        user_int = int(input("Please enter an integer: "))
        attempt = False
    except ValueError:
        print("That isn't an integer...")
    else:
        print("Good job.")
