# Making a PUT Request using the requests package.

import requests

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

body = {
    "first_name": "Leeeeeeeroy",
    "last_name": "Jenkins!",
    "email": "oldschool@memes.biz"
}

response = requests.put(base_url + "/205", json=body)

print(f"Response Code: {response.status_code}")

response = requests.get(base_url)
print(f"Response Content: {response.content}")

