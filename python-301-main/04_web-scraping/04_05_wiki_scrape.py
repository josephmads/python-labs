# Write a web scraper that fetches the information from the Wikipedia page
# on Web scraping. Extract all the links on the page and filter them so the
# navigation links are excluded.
# Programmatically follow one of the links that lead to another Wikipedia article,
# extract the text content from that article, and save it to a local text file.
# BONUS TASK: Use RegExp to find all numbers in the text.

import re
import requests
from bs4 import BeautifulSoup


URL = "https://en.wikipedia.org/wiki/Web_scraping"
page = requests.get(URL)
soup = BeautifulSoup(page.text, features="html.parser")

links = soup.find_all(href=True)

link_list = [(link["href"]) for link in links]

# Link to another Wikipedia page, extract text, save to local text file.

URL2 = f"https://en.wikipedia.org/{link_list[170]}"

page2 = requests.get(URL2)
soup2 = BeautifulSoup(page2.text, features="html.parser")
content = soup2.find_all("p")

title = soup2.find("h1", id="firstHeading")
body = soup2.find("div", id="bodyContent")

with open("EFF_Wiki.txt", "w") as fout:
    fout.write(f"{title.text}\n{body.text}")
