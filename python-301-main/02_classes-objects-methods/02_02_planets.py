# Create a `Planet()` class that models attributes and methods of
# a planet object.
# Use the appropriate dunder method to get informative output with `print()`


class Planet():
    """Models planets"""

    def __init__(self, name, color, order) -> None:
        """Defines the attributes of a planet.

        Args:
            name (str): Name of the planet.
            color (str): Color of the planet.
            order (str): Order from the sun.
        """
        self.name = name
        self.color = color
        self.order = order

    def __str__(self) -> str:
        return f"{self.name} is {self.color}. It is {self.order} closest to the Sun."

mercury = Planet("Mercury", "tan", "first")
venus = Planet("Venus", "orange", "second")
earth = Planet("Earth", "blue", "third")

print(mercury)
print(earth)


