# Making GET Request using the requests package for Tasks.

import requests
from pprint import pprint

base_url = "http://demo.codingnomads.co:8080/tasks_api/tasks"


# GET Tasks

response = requests.get(base_url)
data = response.json()

all_tasks = data["data"]
my_tasks = next(item for item in all_tasks if item["userId"] == 205)

pprint(f"Response Content: {my_tasks}")