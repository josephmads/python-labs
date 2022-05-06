# Print out every prime number between 1 and 1000.

#use division or modulus

for number in range(2, 1001):
    for i in range(2, number):
        if (number % i) == 0:
            break
    else:
        print(number)