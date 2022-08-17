# Use a quotes API, e.g. http://quotes.stormconsultancy.co.uk/random.json
# to fetch a random quote. Then use string manipulation to convert it to
# Doge speech (https://blogs.unimelb.edu.au/sciencecommunication/2016/10/22/how-to-speak-doge/)
# Create a tiny webpage that displays a doge image together
# with the altered quote. You can get an image URL from another API:
# http://shibe.online/api/shibes
# Write the code logic to make the API calls and assign the output to
# `doged_quote` and `doge_image_url` respectively.
# Then write the `html` string to a `.html` file and look at it in your browser.


from pathlib import Path
import requests

# Image API

img_url = "http://shibe.online/api/shibes?count=1"
img = requests.get(img_url).json()[0]

# Quotes API

quote_url = "http://quotes.stormconsultancy.co.uk/random.json"
quote = requests.get(quote_url).json()["quote"]
author = requests.get(quote_url).json()["author"]

# HTML Structure

html = f"<p>{quote} - {author}</p><img src='{img}'>"

# Write to file

f = Path().home().joinpath("Desktop").joinpath("index.html")

f.write_text(html)