# Use your `Ingredients` class to create a URL to an online search
# that allows to look for recipes for dishes made from the
# available ingredients.

from webbrowser import open_new

class Ingredient:
    """Models a food item used as an ingredient."""

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def expire(self):
        """Expires the ingredient."""
        print(f"whoops, these {self.name} went bad...")
        self.name = "expired " + self.name

    def __add__(self, other):
        """Combines two ingredients."""
        new_name = self.name + other.name
        if self.amount < other.amount:
            new_amount = self.amount
        else:
            new_amount = other.amount
        return Ingredient(name=new_name, amount=new_amount)

    def get_info(self):
        return open_new(f"https://en.wikipedia.org/wiki/{self.name}")
    
    def __str__(self):
        return f"{self.name} ({self.amount})"
    
    def __repr__(self):
        return f"Ingredient(name={self.name}, amount={self.amount})"

peas = Ingredient("peas", 50)
carrot = Ingredient("carrot", 5)
ham = Ingredient("ham cubes", 20)

peas.get_info()