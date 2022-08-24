# The classic OOP example: Write a class to model a car. The class should:
#
# 1. Set the attributes model, year, and max_speed in the `__init__()` method.
# 2. Have a method that increases the `max_speed` of the car by 5 when called.
# 3. Have a method that prints the details of the car.
#
# Create at least two different objects of this `Car()` class and demonstrate
# changing the objects' attributes.

class Car:
    """Models a car"""

    def __init__(self, model, year, max_speed) -> None:
        """Defines the cars attributes

        Args:
            model (str): Model of car
            year (int): Year of car
            max_speed (int): Top speed of car
        """

        self.model = model
        self.year = year
        self.max_speed = max_speed

    def increase_max(self):
        """Increases the top speed of the car"""
        
        print(f"Your {self.model} goes faster!")
        self.max_speed += 5

    def __str__(self) -> str:
        return F"A {self.year} {self.model} with a top speed of {self.max_speed} mph."

car1 = Car("Accord", 2020, 120)
car2 = Car("F-150", 1988, 75)

Car.increase_max(car2)

print(car2)