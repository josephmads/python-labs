# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.


n = int(input("Enter a number between 1 and 1,000,000,000: "))
number = 0

while number != n:
    print("searching...")
    number += 1
    if number == n:
        print("Is this your number?:",number)