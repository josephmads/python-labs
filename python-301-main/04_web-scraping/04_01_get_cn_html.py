# In three lines of code, fetch the HTML text from CodingNomads'
# main page and print it to your console.
#
# If you run into encoding/decoding errors, you're experiencing something
# very common. head over to StackOverflow and find a solution!

import requests
from bs4 import BeautifulSoup

base_url = "https://codingnomads.co/"
page = requests.get(base_url)
print(BeautifulSoup(page.text, features="html.parser"))