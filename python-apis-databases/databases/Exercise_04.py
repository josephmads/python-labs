'''

Please create a new Python application that interfaces with a brand new database.
This application must demonstrate the ability to:

    - create at least 3 tables
    - insert data to each table
    - update data in each table
    - select data from each table
    - delete data from each table
    - use at least one join in a select query

BONUS: Make this application something that a user can interact with from the CLI. Have options
to let the user decide what tables are going to be created, or what data is going to be inserted.
The more dynamic the application, the better!


'''


import sqlalchemy as sa
import os
from pprint import pprint

password = os.environ["PASSWORD"]

engine = sa.create_engine(f"mysql+pymysql://joe:{password}@localhost/boat_charter")
connection = engine.connect()
metadata = sa.MetaData()

### Create Tables

captains = sa.Table("captains", metadata,
                    sa.Column("cap_id", sa.Integer(), primary_key=True),
                    sa.Column("first_name", sa.String(255), nullable=False),
                    sa.Column("last_name", sa.String(255), nullable=False),
                    sa.Column("email", sa.String(255), nullable=False),
                    sa.Column("rating", sa.Integer(), nullable=False)
                    )

boats = sa.Table("boats", metadata,
                sa.Column("boat_id", sa.Integer(), primary_key=True),
                sa.Column("boat_name", sa.String(255), nullable=False),
                sa.Column("boat_length", sa.Integer(), nullable=False)
                )

charters = sa.Table("charters", metadata,
                    sa.Column("charter_id", sa.Integer(), primary_key=True),
                    sa.Column("start_date", sa.DateTime(), nullable=False),
                    sa.Column("boat_id", sa.ForeignKey("boats.boat_id", ondelete="CASCADE")),
                    sa.Column("cap_id", sa.ForeignKey("captains.cap_id", ondelete="CASCADE")),
                    sa.Column("return_date", sa.DateTime(), nullable=False)
                    )

# metadata.create_all(engine)

captains = sa.Table("captains", metadata, autoload=True, autoload_with=engine)
boats = sa.Table("captains", metadata, autoload=True, autoload_with=engine)
charters = sa.Table("captains", metadata, autoload=True, autoload_with=engine)



### Insert Data 

insert_stmt = sa.insert(captains).values(cap_id=1, first_name="Joseph", last_name="Madsen", email="joemadsen@mail.com", rating=32)
# insert_result = connection.execute(insert_stmt)

def insert_table():
    
    print("TABLES \n"
    "1. captains\n"
    "2. boats\n"
    "3. charters")
    table = int(input("Enter the number of the table to insert to: "))

    if table == 1:
        table = captains
        f_name = input("Enter the new captain's FIRST NAME: ")
        l_name = input("Enter the new captain's LAST NAME: ")
        email_in = input("Enter the new captain's EMAIL: ")
        rating_in = input("Enter the new captain's RATING: ")

        ins_table = sa.insert(table).values(first_name=f_name, last_name=l_name, email=email_in, rating=rating_in)
        result = (connection.execute(ins_table))
        print("New record created.")

    if table == 2:
        table = boats
        name = input("Enter the new boat's NAME: ")
        length = input("Enter the new boat's LENGTH: ")

        ins_table = sa.insert(table).values(boat_name=name, boat_length=length)
        result = (connection.execute(ins_table))
        print("New record created.")

    if table == 3:
        table = charters
        s_date = input("Enter the charter START DATE (yyyy-mm-dd): ")
        b_id = input("Enter the charter BOAT ID: ")
        c_id = input("Enter the charter CAPTAIN ID: ")
        r_date = input("Enter the charter END DATE (yyyy-mm-dd): ")

        ins_table = sa.insert(table).values(start_date=s_date, boat_id=b_id, cap_id=c_id, return_date=r_date)
        result = (connection.execute(ins_table))
        print("New record created.")
    
    else:
        print("Invalid choice.")


### Update Data

# update_stmt = sa.update(captains).values(last_name="Snodgrass").where(captains.columns.cap_id == 1)
# update_result = connection.execute(update_stmt)

def display_table(table):
        
    display = sa.select(table)
    proxy = connection.execute(display)
    result = proxy.fetchall()

    for row in result:
        print(row)

def update_table():

    print("TABLES \n"
    "1. captains\n"
    "2. boats\n"
    "3. charters")
    table = int(input("Enter the number of the table to update: "))

    def upd_val(value, id):

        upd_table = sa.update(table).values({value : value_update}).where(table.columns[id] == update_id)
        result = connection.execute(upd_table)
        print("Record updated.")

    if table == 1:
        table = captains
        where_id = "cap_id"

        display_table(table)

        update_id = int(input("Enter the ID of the row to update: "))

        print("\nVALUES \n"
        "1. First Name \n"
        "2. Last Name \n"
        "3. Email \n"
        "4. Rating \n")

        value_choice = int(input("Enter the number of the value to update: "))
        value_update = input("Enter the new value: ")

        value_dict = {
            1 : "first_name",
            2 : "last_name",
            3 : "email",
            4 : "rating"
        }

        upd_val(value_dict[value_choice], where_id)

    if table == 2:
        table = boats
        where_id = "boat_id"

        display_table(table)

        update_id = int(input("Enter the ID of the row to update: "))

        print("\nVALUES \n"
        "1. Boat Name \n"
        "2. Boat Length"
        )

        value_choice = int(input("Enter the number of the value to update: "))
        value_update = input("Enter the new value: ")

        value_dict = {
            1 : "boat_name",
            2 : "boat_length"
        }

        upd_val(value_dict[value_choice], where_id)

    if table == 3:
        table = charters
        where_id = "charter_id"

        display_table(table)

        update_id = int(input("Enter the ID of the row to update: "))

        print("\nVALUES \n"
        "1. Start Date \n"
        "2. Boat ID \n"
        "3. Captain ID \n"
        "4. Return Date"
        )

        value_choice = int(input("Enter the number of the value to update: "))
        value_update = input("Enter the new value: ")

        value_dict = {
            1 : "start_date",
            2 : "boat_id",
            3 : "cap_id",
            4 : "return_date"
        }

        upd_val(value_dict[value_choice], where_id)

update_table()

### Select Data

select_stmt = sa.select(captains)

select_proxy = connection.execute(select_stmt)
select_result = select_proxy.fetchall()

pprint(select_result)

### Select/Join Data



### Delete Tables and/or Columns

# captains = sa.Table("captains", metadata, autoload=True, autoload_with=engine)

# delete_table = sa.delete(captains).where(captains.columns.cap_id)
# results = connection.execute(delete_table)

#metadata.drop_all(engine)

