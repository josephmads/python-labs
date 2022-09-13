# Project: Cook Soup
# For this project, you'll create a custom Soup() class 
# that can take Ingredient() and Spice() objects, 
# and use them to look up soup recipes on the Internet.

from webbrowser import open_new

class Ingredient:
    """Models an Ingredient."""

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def expire(self):
        """Expires the ingredient item."""
        print(f"whoops, these {self.name} went bad...")
        self.name = "expired " + self.name

    def __str__(self):
        return f"You have {self.amount} {self.name}."


class Spice(Ingredient):
    """Models a spice to flavor your food."""

    def __init__(self, name, amount, taste):
        super().__init__(name, amount)
        self.taste = taste

    def grind(self):
        print(f"You have now {self.amount} of ground {self.name}.")

    def sprinkle(self):
        print(f"You sprinkle a pinch of {self.name} on your ingredients.")

    def expire(self):
        if self.name == "salt":
            print(f"{self.name} never expires!")
        else:
            print(f"Your {self.name} has expired. But it's probably still good.")
        self.name = "old " + self.name

class Soup():

    def __init__(self, *args) -> None:
        self.args = args

    def cook(self):
        ing_search = "soup+recipe"
        for item in self.args:
            ing_search += f"+{item.name}"
        return open_new(f"https://www.google.com/search?q={ing_search}")

    def __str__(self) -> str:
        return f"You are making {self.args[0].name} soup!"


if __name__ == "__main__":
    
    t = Ingredient("tomatoes", 3)
    m = Ingredient("mushrooms", 4)
    b = Spice("basil", 5, "herby")

    soup = Soup(t, m, b)

    soup.cook()
    print(soup)