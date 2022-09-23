# Use the Pokemon API at https://pokeapi.co/ to assemble a team of your
# six favorite Pokémon.
# Your task is to fetch information about six Pokémon through the
# necessary API calls and include the information in your local script.
# This information should include at least:
# - name
# - number
# - types
#
# You can improve on your project even more by writing the data to a small
# `.html` page which allows you to also display the sprites of each Pokémon.
# Check out the guides they provide: https://pokeapi-how.appspot.com/page5

import requests


BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
response = requests.get(BASE_URL)
data = response.json()

poke_list = [0, 17, 13, 5, 8]

print("Pokemon Info")

for num in poke_list:

    poke = data["results"][num]["url"]
    p_data = requests.get(poke).json()
    p_name = p_data["name"]
    p_number = p_data["id"]
    p_type = p_data["types"][0]["type"]["name"]

    print(f"name: {p_name}\n"
          f"number: {p_number}\n"
          f"type: {p_type}\n")
