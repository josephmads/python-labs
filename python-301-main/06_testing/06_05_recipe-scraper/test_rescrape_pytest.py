# Install `pytest` in a virtual environment and rewrite the test suite
# for your web scraper using `pytest` instead of `unittest`.

import pytest
import rescrape

BASE_URL = "https://codingnomads.github.io/recipes/"

def test_get_valid_response():
    index_page = rescrape.get_page_content(BASE_URL)
    assert index_page.status_code == 200