# Making PUT Request using the requests package for Tasks.

import requests
from pprint import pprint

base_url = "http://demo.codingnomads.co:8080/tasks_api/tasks"

# PUT Tasks

body = {
    "userId": 205,
    "name": "todo",
    "description": "eggs, milk, bacon, cheese, and apples",
    "completed": True
  }

response = requests.put(base_url, json=body)
print(f"Response Code: {response.status_code}")