# Making a PUT Request using the requests package.

import requests

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

response = requests.delete(base_url + "/211")

print(response.status_code)