# Pokemon battle simulator

from pokemon import Pokemon

# create available Pokemons

char = Pokemon("Charmander", "fire", 150)
squirt = Pokemon("Squirtle", "water", 100)
bulbi = Pokemon("Bulbasaur", "grass", 100)

poke_dict = {1: char, 2: squirt, 3: bulbi}

# allow user to choose their Pokemon

print("POKEMON\n"
"1: Charmander\n"
"2: Squirtle\n"
"3: Bulbasaur")
player_poke = int(input("Choose your Pokemon: "))

if player_poke == 1:
    player_poke = poke_dict[1]
if player_poke == 2:
    player_poke = poke_dict[2]
if player_poke == 3:
    player_poke = poke_dict[3]

# allow user to feed or battle the Pokemon



# randomly select opponent Pokemon