# Write a unittest test suite to test the rescrape module

import unittest
import rescrape

class TestRescrape(unittest.TestCase):

    def setUp(self):
        self.BASE_URL = "https://codingnomads.github.io/recipes/"
        self.URL = "https://codingnomads.github.io/recipes/recipes/1-garlic-butter-steak.html"
        self.html = rescrape.get_html_content(self.BASE_URL)
        self.soup = rescrape.make_soup(self.html)
        self.URL_soup = rescrape.make_soup(rescrape.get_html_content(self.URL))

    # requests can establish a connection and receive a valid response
    def test_get_valid_html_response(self):
        index_page = rescrape.get_page_content(self.BASE_URL)
        self.assertEqual(index_page.status_code, 200)

    # the response contains HTML code
    def test_get_html_content(self):
        page = rescrape.get_html_content(self.BASE_URL)
        self.assertIn("<!DOCTYPE html>", page)

    # the HTML can be successfully converted to a Beautiful Soup object
    def test_make_soup(self):
        soup = rescrape.make_soup(self.html)
        self.assertEqual(str(type(soup)), "<class 'bs4.BeautifulSoup'>")

    # can identify all links from the index page
    def test_get_recipe_links(self):
        links = rescrape.get_recipe_links(self.soup)
        self.assertIn(".html", links[0])

    # can identify the author of a recipe
    def test_get_author(self):
        author = rescrape.get_author(self.URL_soup)
        self.assertEqual(author, "Divider1")

    # can get the main recipe text
    def test_get_recipe(self):
        recipe = rescrape.get_recipe(self.URL_soup)
        self.assertEqual(type(recipe), str)


if __name__ == "__main__":
    unittest.main()
