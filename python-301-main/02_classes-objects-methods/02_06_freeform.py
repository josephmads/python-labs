# Write a script with three classes that model everyday objects.
# - Each class should have an `__init__()` method that sets at least 3 attributes
# - Include a `__str__()` method in each class that prints out the attributes
#     in a nicely formatted string.
# - Overload the `__add__()` method in one of the classes so that it's possible
#     to add attributes of two instances of that class using the `+` operator.
# - Create at least two instances of each class.
# - Once the objects are created, change some of their attribute values.
#
# Be creative. Have some fun. :)
# Using objects you can model anything you want:
# Animals, paintings, card games, sports teams, trees, people etc...

class Doggy:
    """Models a dog"""

    def __init__(self, name, breed, weight, sex, age, color) -> None:
        self.name = name
        self.breed = breed
        self.weight = weight
        self.sex = sex
        self.age = age
        self.color = color

    def __add__(self, other):
        """Combines two breeds to make a new breed.

        Args:
            other (Dog): takes two Dog objects for arguments.

        Returns:
            Dog: returns a new Dog object that is a combination of the arguments.
        """
        new_name = self.name[:3] + other.name[3:]
        new_breed = self.breed + " " + other.breed
        new_weight = (self.weight + other.weight) / 2
        if len(new_breed) % 2:
            new_sex = "male"
        else:
            new_sex = "female"
        new_color = self.color + " and " + other.color

        return Doggy(name=new_name, breed=new_breed, weight=new_weight, sex=new_sex, age=1, color=new_color)

    def __str__(self) -> str:
        return f"{self.name} is a {self.sex} {self.breed} and has {self.color} fur. {self.name} is {self.age} years old and weighs {self.weight} pounds."

class House:
    """Models a house."""

    def __init__(self, square_feet, bedrooms, bathrooms, lot) -> None:
        self.square_feet = square_feet
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.lot = lot

    def __str__(self) -> str:
        return f"This house is {self.square_feet} square feet. It has {self.bedrooms} bedrooms, {self.bathrooms} bathrooms, and sits on {self.lot}"

class Beverage:
    """Models a beverage."""

    def __init__(self, name, price, container, size, abv) -> None:
        self.name = name
        self.price = price
        self.container = container
        self.size = size
        self.abv = abv

    def __str__(self) -> str:
        return f"{self.name} - ${self.price} - Served in a {self.size} {self.container}. {self.abv}% ABV"

# Doggies

pita = Doggy("Pita", "Chocolate Lab", 50, "female", 6, "brown")
dennis = Doggy("Dennis", "Maltese", 5, "male", 9, "white")

puppy = pita + dennis

print(puppy)

# Houses

my_house = House(2000, 4, 2, ".5 acres")
dream_house = House(1000, 2, 1, "10 acres")

my_house.bathrooms = 3

print(my_house)

# Beverage

summit_epa = Beverage("Summit EPA", 5, "can", "12 oz", 4.2)
corona = Beverage("Corona", 4, "bottle", "355 ml", 3)

print(summit_epa, corona)