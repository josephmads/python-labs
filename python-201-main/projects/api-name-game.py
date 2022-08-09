# Add an API call to your CLI game that assigns a name to your player.

import requests

min_name_len = 4

max_name_len = 9

base_url = f"https://uzby.com/api.php?min={min_name_len}&max={max_name_len}"

response = requests.get(base_url)

print(response.text)