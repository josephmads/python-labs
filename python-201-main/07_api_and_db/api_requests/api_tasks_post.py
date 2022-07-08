# Making POST, PUT, DELETE Request using the requests package for Tasks.

import requests
from pprint import pprint

base_url = "http://demo.codingnomads.co:8080/tasks_api/tasks"

# POST Tasks

body = {
    "userId": 205,
    "name": "todo",
    "description": "eggs, milk, bacon, cheese",
    "completed": False
  }

response = requests.post(base_url, json=body)

print(f"Response Code: {response.status_code}")
