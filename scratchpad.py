def greet_many(greeting: str, *args: str) -> str:
    """Fucntion that greets many names with same greeting

    Args:
        greeting (str): the greeting to use

    Returns:
        str: Personalized greeting for each name.
    """
    greetings = ""
    for name in args:
        sentence = f"{greeting}, {name}! How are you?"
        greetings += sentence + "\n"
    return greetings

print(greet_many("hi", "Joe", "Kyle", "Steve"))

greet_many("Hi", "Joe")
greet_many("Hi", "Joe")