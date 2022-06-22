# Making a POST Request using the requests package.

import requests

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

body = {
    "first_name": "Leroy",
    "last_name": "Jenkins",
    "email": "oldschool@memes.biz"
    }

response = requests.post(base_url, json=body)

print(f"Response Code: {response.status_code}")

response = requests.get(base_url)

print(f"Response Content: {response.content}")