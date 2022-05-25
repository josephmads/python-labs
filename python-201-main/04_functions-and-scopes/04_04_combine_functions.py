# Combine the `greet()` function that you developed in the course materials
# with the `write_letter()` function from the previous exercise.
# Write both functions in this script and call `greet()` within `write_letter()`
# to let `greet()` take care of creating the greeting string.

def greet(greeting, name):
    sentence = f"{greeting}, {name}! How are you?"
    return sentence

def write_letter(name, text):
    print(greet("Hiya!", name))
    print(text)
    print(f'So long, {name}')

write_letter("Johnny", "I am fine. Did you have a good summer? I did.")