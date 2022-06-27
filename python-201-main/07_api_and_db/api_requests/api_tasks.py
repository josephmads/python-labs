# Making POST, GET, PUT, DELETE Request using the requests package for Tasks.

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

# GET Tasks

response = requests.get(base_url)
data = response.json()

my_tasks = data["data"][43]

pprint(f"Response Content: {my_tasks}")

# PUT Tasks

body = {
    "userId": 205,
    "name": "todo",
    "description": "eggs, milk, bacon, cheese, and apples",
    "completed": True
  }

response = requests.put(base_url, json=body)
print(f"Response Code: {response.status_code}")

# DELETE Tasks

response = requests.delete(base_url + "/58")

print(f"Response Code: {response.status_code}")