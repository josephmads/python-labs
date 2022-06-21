import requests
from pprint import pprint

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"
params_dict = {"first_name": "test"}

response = requests.get(base_url)

data = (response.json())

pprint(data['data'][0]['first_name'])

# print(f"Response Content: {response.content}")
# print(f"Response Status Code: {response.status_code}")
# print(f"Response Headers: {response.headers}")
# print(f"Response Encoding: {response.encoding}")
# print(f"Response URL: {response.url}")