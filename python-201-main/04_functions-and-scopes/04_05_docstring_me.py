# Add a Google-style docstring to the function below. Your docstring
# should at least describe what it does, what arguments it takes,
# and what it returns.

def km_to_miles(km):
    """Converts Kilometers to Miles

    Args:
        km (int): An amount of kilometers

    Returns:
        int: the conversion into miles
    """
    miles = km * 0.6
    return miles

print(km_to_miles.__doc__)
