# Write a program that takes a number between 1 and 1,000,000,000
# from the user and determines whether it is divisible by 3 using an `if` statement.
# Print the result.

num = int(input("Input a number between 1 and 1,000,000,000 to see if it is divisible by 3: "))

if num % 3 != 1:
    print("Hooray your number is divisible by 3!")
else:
    print("Sorry.")