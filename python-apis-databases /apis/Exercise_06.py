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
from pprint import pprint 

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

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

running = True

while running == True:
    print(main_menu)
    user_input = input("Enter your choice: ")
    user_input = user_input.upper()

    if user_input == "1":

        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        email = input("Enter your email address: ")

        body = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email
            }

        response = requests.post(base_url, json=body)
        response = requests.get(base_url)

        data = (response.json())

        if response.status_code == 201:
            print("Your account was successfully created.")
            pprint(data['data'][-1])

        input("Press ENTER to continue: ")    

        continue

    if user_input == "2":

        response = requests.get(base_url)
        data = (response.json())
        user_id = data["data"][64]["id"]
        task_url = base_url + f"/{user_id}" + "/tasks"
        
        response = requests.get(task_url)
        data = response.json()
        tasks_list = data["data"]

        print(f"Tasks: {tasks_list}")
        input("Press ENTER to continue: ")

        continue

    if user_input == "3":

        response = requests.get(base_url)
        data = (response.json())
        user_id = data["data"][64]["id"]
        task_url = base_url + f"/{user_id}" + "/tasks?complete=true"
        
        response = requests.get(task_url)
        data = response.json()
        tasks_list = data["data"]

        print(f"Tasks: {tasks_list}")
        input("Press ENTER to continue: ")

        continue

    if user_input == "4":

        response = requests.get(base_url)
        data = (response.json())
        user_id = data["data"][64]["id"]
        task_url = base_url + f"/{user_id}" + "/tasks?complete=false"
        
        response = requests.get(task_url)
        data = response.json()
        tasks_list = data["data"]

        print(f"Tasks: {tasks_list}")
        input("Press ENTER to continue: ")

        continue

    if user_input == "5":
        
        task_name = input("Enter a name for your task: ")
        task_des = input("Enter a description for your task: ")

        task_body = {
            "userId": 205,
            "name": task_name,
            "description": task_des,
            "completed": False
        }
        
        response = requests.get(base_url)
        data = (response.json())
        user_id = data["data"][64]["id"]
        task_url = base_url + f"/{user_id}" + "/tasks"

        response = requests.post(task_url, json=task_body)

    if user_input == "6":
        # update existing task (put) mark as complete
        pass

    if user_input == "7":
        del_task = input("Enter the task you would like to delete: ")
        response = requests.delete(base_url + del_task)

        if response.status_code == 200:
            print("Your task was successfully deleted.")

        continue

    if user_input == "Q":
        running = False
        print("Goodbye.")
        break

    else:
        print("Invalid Input")
        continue
