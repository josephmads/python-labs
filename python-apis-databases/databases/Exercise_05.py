'''
Using the API from the API section, write a program that makes a request to
get all of the users and all of their tasks.

Create tables in a new local database to model this data.

Think about what tables are required to model this data. Do you need two tables? Three?

Persist the data returned from the API to your database.

NOTE: If you run this several times you will be saving the same information in the table.
To prevent this, you should add a check to see if the record already exists before inserting it.

'''

import requests
import sqlalchemy as sa
import os
import datetime

# MySQL

password = os.environ["PASSWORD"]

engine = sa.create_engine(f"mysql+pymysql://joe:{password}@localhost/demo_api_data")
connection = engine.connect()
metadata = sa.MetaData()

# API

users_url = "http://demo.codingnomads.co:8080/tasks_api/users"
tasks_url = "http://demo.codingnomads.co:8080/tasks_api/tasks"

user_response = requests.get(users_url)
tasks_response = requests.get(tasks_url)

user_data = (user_response.json())
tasks_data = (tasks_response.json())

# Check If Exists

# Create Tables

api_users = sa.Table("api_users", metadata,
                    sa.Column("user_id", sa.Integer(), primary_key=True),
                    sa.Column("email", sa.String(100), nullable=False),
                    sa.Column("first_name", sa.String(100), nullable=False),
                    sa.Column("last_name", sa.String(100), nullable=False),
                    sa.Column("created_at", sa.BigInteger(), nullable=False),
                    sa.Column("updated_at", sa.BigInteger(), nullable=False)
                    )

api_tasks = sa.Table("api_tasks", metadata,
                    sa.Column("task_id", sa.Integer(), primary_key=True),
                    sa.Column("user_id", sa.ForeignKey("api_users.user_id", ondelete="CASCADE")),
                    sa.Column("name", sa.String(255), nullable=False),
                    sa.Column("description", sa.String(255), nullable=False),
                    sa.Column("created_at", sa.BigInteger(), nullable=False),
                    sa.Column("updated_at", sa.BigInteger(), nullable=False),
                    sa.Column("completed", sa.Boolean(), nullable=False)
                    )


# metadata.drop_all(engine)
# metadata.create_all(engine)


# Persist Data

user_table = sa.select(api_users.columns.user_id)
proxy = connection.execute(user_table)
result = proxy.fetchall()

counter = 0
    
for user in user_data["data"]:
    result_id = result[counter][0]
    counter += 1

    if user["id"] == result_id:
        print("User exists")
    
    else:
        insert_user = sa.insert(api_users).values(user_id=user["id"], email=user["email"], first_name=user["first_name"], 
                                last_name=user["last_name"], created_at=user["created_at"], updated_at=user["updated_at"])
        connection.execute(insert_user)
        print("Record added")
        
# Cannot get code below to work as it should because task_table is reading the data out of order from how it is stored in MySQL.

task_table = sa.select(api_tasks.columns.task_id)
proxy = connection.execute(task_table)
result = proxy.fetchall()

counter = 0

for task in tasks_data["data"]:
    result_id = result[counter][0]
    print(result_id)
    counter += 1
    
    if task["id"] == result_id:
        print("Task exists")

    else:
        insert_task = sa.insert(api_tasks).values(task_id=task["id"], user_id=task["userId"], name=task["name"],
                                description=task["description"], created_at=task["createdAt"], updated_at=task["updatedAt"],
                                completed=task["completed"])
        connection.execute(insert_task)
        print("Record added")