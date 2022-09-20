import requests
from bs4 import BeautifulSoup


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

    print(f"{title.text}\n{author.text}\n{recipe.text}")