# Ask the user to input their name. Then print a nice welcome message
# that welcomes them personally to your script.
# If a user enters more than one name, e.g. "firstname lastname",
# then use only their first name to overstep some personal boundaries
# in your welcome message.


name = input("What is your name?: ")
first_name = ""

for char in name:
    first_name += char
    if char == " ":
        first_name.strip()
        print(f"Hello, {first_name}")
