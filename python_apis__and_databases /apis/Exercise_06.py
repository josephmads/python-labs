'''

Create an application that interfaces with the user via the CLI - prompt the user with a menu such as:

Please select from the following options (enter the number of the action you'd like to take):
1) Create a new account (POST)
2) View all your tasks (GET)
3) View your completed tasks (GET)
4) View only your incomplete tasks (GET)
5) Create a new task (POST)
6) Update an existing task (PATCH/PUT)
7) Delete a task (DELETE)

It is your responsibility to build out the application to handle all menu options above.

'''

import requests

main_menu = '''
Please select from the following options (enter the number of the action you'd like to take):
1) Create a new account (POST)
2) View all your tasks (GET)
3) View your completed tasks (GET)
4) View only your incomplete tasks (GET)
5) Create a new task (POST)
6) Update an existing task (PATCH/PUT)
7) Delete a task (DELETE)
Q) Quit program
'''
print(main_menu)
user_input = input("Enter your choice: ")

while user_input != "Q" or "q":

    if user_input == "1":
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        email = input("Enter your email address: ")

        base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

        body = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email
            }

        response = requests.post(base_url, json=body)

    if user_input == "2":
        # view tasks
        pass
    if user_input == "3":
        pass
    if user_input == "4":
        pass
    if user_input == "5":
        pass
    if user_input == "6":
        pass
    if user_input == "7":
        pass


