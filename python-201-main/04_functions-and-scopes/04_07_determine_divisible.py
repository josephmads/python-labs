# Write a script where you complete the following tasks:
# - define a function that determines whether the number is
#   divisible by 4 OR 7 and returns a boolean
# - define a function that determines whether a number is
#   divisible by both 4 AND 7 and returns a boolean
# - take in a number from the user between 1 and 1,000,000,000
# - call your functions, passing in the user input as the arguments,
#   and set their output equal to new variables 
# - print your the result variables with descriptive messages

def div_4_OR_7(num: int) -> int:
    """Determines if a number is divisible by 4 or 7.

    Args:
        num (int): Takes a number

    Returns:
        bool: Returns True if number is divisble by 4 or 7, else False. 
    """
    if num % 4 == 0:
        answer = True
    elif num % 7 == 0:
        answer = True
    else:
        answer = False
    return answer

def div_4_AND_7(num: int) -> int:
    """Determines if number is divisble by 4 and 7.

    Args:
        num (int): Takes a number

    Returns:
        int: Returns True if number is divisible by 4 and 7, else False.
    """
    if num % 4 == 0 and num % 7 == 0:
        answer = True
    else:
        answer = False
    return answer

user_input = int(input("Pick a number between 1 and 1,000,000,000: "))

four_or_seven = div_4_OR_7(user_input)
four_and_seven = div_4_AND_7(user_input)

print(f'Your number is divisible by 4 OR 7: {four_or_seven}\n'
    f'Your number is divisible by 4 AND 7: {four_and_seven}')