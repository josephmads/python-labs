# Making DELETE Request using the requests package for Tasks.

import requests
from pprint import pprint

base_url = "http://demo.codingnomads.co:8080/tasks_api/tasks"

# DELETE Tasks

response = requests.delete(base_url + "/58")

print(f"Response Code: {response.status_code}")