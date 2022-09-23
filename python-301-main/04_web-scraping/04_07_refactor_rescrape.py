# Refactor your web scraping script and wrap all the functionality into
# separate functions. This is a great exercise to revisit writing functions
# as well as for refactoring your code. It'll also help you in an upcoming
# section of the course when you'll write tests for your web scraper.

import requests
from bs4 import BeautifulSoup

def convert_to_soup(website):
    """Converts a website into a BeautifulSoup text object.

    Args:
        website (str): The url of the website
    """
    page = requests.get(website)
    soup = BeautifulSoup(page.text, "html.parser")
    return soup

def local_save(soup, filename):
    """Converts BeautifulSoup object to str to save a local copy of a website,
    and returns the local copy. 

    Args:
        soup (bs4): BeautifulSoup object
        filename (str): Name of local copy

    Returns:
        bs4: local copy of website
    """
    soup_string = str(soup)
    with open(filename, "w") as fout:
        fout.write(soup_string)

    with open(filename, "r") as fin:
        local_soup = BeautifulSoup(fin, "html.parser")

    return local_soup

URL = "https://www.ecoustics.com/products/xi3-z3ro-pro-computer/"

soup = convert_to_soup(URL)
new_soup = local_save(soup, "ecoustics-Xi3.html")

title = new_soup.find("h1", class_="zox-post-title left entry-title")
author = new_soup.find("div", class_="zox-post-byline-wrap")
author = author.text.strip()
body = new_soup.find("div", "zox-post-body left zoxrel zox100")
body = body.text.strip()

print(f"{title.text}\n\n{author}\n\n{body}")