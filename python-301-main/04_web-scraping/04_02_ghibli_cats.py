# Read through the documentation of the Ghibli API and reproduce the example
# listed at https://ghibliapi.herokuapp.com/#section/Use-Case in Python.
# Try skim the Haskell code example and see if you can understand anything.
# Don't worry if you don't, it's a completely different language :)
#
# Your task is to use the API to find information about all the cats that
# appear in Studio Ghibli films.

import requests

BASE_URL = "https://ghibliapi.herokuapp.com/species/603428ba-8a86-4b0b-a9f1-65df6abef3d3"
response = requests.get(BASE_URL)

data = response.json()
links = data["people"]

print("Studio Ghibli Cats:")

for link in links:
    page = requests.get(link)
    page_data = page.json()
    
    name = page_data["name"]
    gender = page_data["gender"]
    hair = page_data["hair_color"]
    eye = page_data["eye_color"]

    print(f"name: {name}, gender: {gender}, hair color: {hair}, eye color: {eye}")


