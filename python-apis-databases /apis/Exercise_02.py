'''
Building on the previous example, create a list of all of the emails of the users and print
the list to the console.

'''

import requests
from pprint import pprint

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

response = requests.get(base_url)

data = (response.json())

counter = len(data['data'])
counter2 = 0
email_list =[]

while counter != 0:
    email = data['data'][counter2]['email']
    email_list.append(email)
    counter -= 1
    counter2 += 1

print(email_list)