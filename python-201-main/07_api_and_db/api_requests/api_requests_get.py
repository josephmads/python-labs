# Making a Get Request using the requests package.

import requests
from pprint import pprint

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"
params_dict = {"first_name": "test"}

response = requests.get(base_url)

data = (response.json())

all_users = data["data"]

my_user = next(item for item in all_users if item["id"] == 205)
first_n = my_user["first_name"]

pprint(f"Response Content: {first_n}")

# print(f"Response Content: {response.content}")
# print(f"Response Status Code: {response.status_code}")
# print(f"Response Headers: {response.headers}")
# print(f"Response Encoding: {response.encoding}")
# print(f"Response URL: {response.url}")