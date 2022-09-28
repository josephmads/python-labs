# Write a script that takes in two numbers from the user and calculates the quotient.
# Use a try/except statement so that your script can handle:
#
# - if the user enters a string instead of a number
# - if the user enters a zero as the divisor
#
# Test it and make sure it does not crash when you enter incorrect values.

calc = True
while calc == True:
    try:
        dividend = int(input("Enter the number to be divided: "))
        divisor = int(input("Enter the the divisor: "))
        quotient = dividend / divisor
        print(f"{dividend} divided by {divisor} equals {quotient}")
        calc = False
    except ZeroDivisionError:
        print("You can't divide a number by zero.")
    except ValueError:
        print("Enter a number, not a letter.")
    except Exception as e:
        print(f"{e} has occured.")