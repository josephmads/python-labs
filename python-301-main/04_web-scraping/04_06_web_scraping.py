# Look for a static website online that has some information that you're
# interested in. Follow the web-scraping steps described in the course to
# inspect, scrape, and parse the information.
# BE RESPECTFUL! Don't scrape sites that don't want to be scraped, and
# limit the amount of calls you make to their page by saving the response
# to a file, and parsing the content from that file.

import requests
from bs4 import BeautifulSoup

# Initial page request; response saved locally

# URL = "https://www.ecoustics.com/products/xi3-z3ro-pro-computer/"
# page = requests.get(URL)
# soup = BeautifulSoup(page.text, features="html.parser")

# str_soup = str(soup)

# with open("04_06_static_site.html", "w") as fout:
#     fout.write(str_soup)

# Read file in to parse content.

with open("04_06_static_site.html", "r") as fin:
    soup = BeautifulSoup(fin, "html.parser")

title = soup.find("h1", class_="zox-post-title left entry-title")
author = soup.find("div", class_="zox-post-byline-wrap")
author = author.text.strip()
body = soup.find("div", "zox-post-body left zoxrel zox100")
body = body.text.strip()

print(f"{title.text}\n\n{author}\n\n{body}")