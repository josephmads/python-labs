# For this project, your task is to create a CLI that takes as an input
# the names of ingredients from a user. Then, your code will fetch
# the recipe information from the CodingNomads recipe collection,
# and search through the text of the recipes to find ones that include
# the provided ingredients.
#
# Note: Feel free to integrate your custom Ingredient() and Soup() classes
# into the code base, to get some additional practice in working with your
# custom Python classes.


import requests
from bs4 import BeautifulSoup

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

def user_ingredients():

    user_input1 = input("Enter the name of your ingredient: ")
    user_input2 = input(f"Enter the amount of {user_input1} you have: ")
    user_ing = Ingredient(user_input1, user_input2)
    return ingredients_list.append(user_ing.name)

# Gather ingredients

ingredients_list = []
recipes_list = []

user_ingredients()

gathering = True

while gathering == True:
    more = input("Do you have more ingredients? [Y]es/[N]o: ")
    if more.lower() == "y":
        user_ingredients()
        continue
    elif more.lower() == "n":
        print("Ok. Let's find some recipes to make with your ingredients.")
        gathering = False
        continue
    else:
        print("I'll take that as a no.\n" 
        "Let's find some recipes to make with your ingredients.")
        gathering = False
        continue

 

base_url = "https://codingnomads.github.io/recipes/"

link_page = requests.get(base_url)

link_soup = BeautifulSoup(link_page.text, features="html.parser")
links = link_soup.find_all("a")

link_list = [(link["href"]) for link in links]

for link in link_list:
    
    URL = f"https://codingnomads.github.io/recipes/{link}"

    page = requests.get(URL)
    soup = BeautifulSoup(page.text, features="html.parser")

    title = soup.find("h1", class_="title")
    author = soup.find("p", class_="author")
    recipe = soup.find("div", class_="md")

    for ingredient in ingredients_list:
        search = ingredient in recipe.text
        if search == True:
            recipes_list.append(title.text)
        else:
            pass
    breakpoint()

    # if ingredients found in recipe return title. make a function

print("Here are the recipes:")

for recipe in recipes_list:
    print(recipe)