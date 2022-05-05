# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.

import random

num = random.randint(1, 10)
count = 5
guess = None

while guess != num and count != 0:
    guess = int(input(f"You have {count} tries to guess a number between 1 and 10: "))
    count -= 1
    if guess == num:
        print("Hooray, you win!")
        break
    elif count == 0:
        print("You lose... like a loser.")
    else:
        print("Try again.")
