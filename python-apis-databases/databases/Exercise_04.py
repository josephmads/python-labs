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

### VARIABLES AND FUNCTIONS

captains = sa.Table("captains", metadata, autoload=True, autoload_with=engine)
boats = sa.Table("boats", metadata, autoload=True, autoload_with=engine)
charters = sa.Table("charters", metadata, autoload=True, autoload_with=engine)

show_tables = ("\nTABLES \n"
               "1. captains\n"
               "2. boats\n"
               "3. charters\n"
               "0. MAIN MENU")

table_dict = {
    1 : captains,
    2 : boats,
    3 : charters
}

## Display Table

def display_table(table_choice):
    """Displays MySQL table.

    Args:
        table_choice (int): selects the table
        to be displayed.
    """
        
    display = sa.select(table_choice)
    proxy = connection.execute(display)
    result = proxy.fetchall()

    row_title = ""
    row_value = ""
    labels = table_choice.columns.keys()

    print("\nTABLE")

    for label in labels:
        label += ", "
        row_title += label 
    print(row_title)

    for row in result:
        for item in row:
            item = str(item)
            item += ", "
            row_value += item
        print(row_value)
        row_value = ""

### Insert Data 

def insert_table():
    
    sub_loop = True
    while sub_loop == True:

        print(show_tables)
        table_choice = int(input("Enter the number of the table to insert to: "))

        if table_choice == 1:
            table_choice = captains
            f_name = input("Enter the new captain's FIRST NAME: ")
            l_name = input("Enter the new captain's LAST NAME: ")
            email_in = input("Enter the new captain's EMAIL: ")
            rating_in = input("Enter the new captain's RATING: ")

            ins_table = sa.insert(table_choice).values(first_name=f_name, last_name=l_name, email=email_in, rating=rating_in)
            result = (connection.execute(ins_table))
            print("New record created.")
            continue

        if table_choice == 2:
            table_choice = boats
            name = input("Enter the new boat's NAME: ")
            length = input("Enter the new boat's LENGTH: ")

            ins_table = sa.insert(table_choice).values(boat_name=name, boat_length=length)
            result = (connection.execute(ins_table))
            print("New record created.")
            continue

        if table_choice == 3:
            table_choice = charters
            s_date = input("Enter the charter START DATE (yyyy-mm-dd): ")
            b_id = input("Enter the charter BOAT ID: ")
            c_id = input("Enter the charter CAPTAIN ID: ")
            r_date = input("Enter the charter END DATE (yyyy-mm-dd): ")

            ins_table = sa.insert(table_choice).values(start_date=s_date, boat_id=b_id, cap_id=c_id, return_date=r_date)
            result = (connection.execute(ins_table))
            print("New record created.")
            continue

        if table_choice == 0:
            sub_loop = False
            return(print("Back to main menu...\n"))
        
        else:
            print("Invalid choice.")
            continue

### Update Data

def update_table():

    sub_loop = True
    while sub_loop == True:

        print(show_tables)
        table_choice = int(input("Enter the number of the table to update: "))

        def upd_val(value, id):

            upd_table = sa.update(table_choice).values({value : value_update}).where(table_choice.columns[id] == update_id)
            result = connection.execute(upd_table)
            print("Record updated.")

        if table_choice == 1:
            table_choice = captains
            where_id = "cap_id"

            display_table(table_choice)

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
            continue

        if table_choice == 2:
            table_choice = boats
            where_id = "boat_id"

            display_table(table_choice)

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
            continue

        if table_choice == 3:
            table_choice = charters
            where_id = "charter_id"

            display_table(table_choice)

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
            continue

        if table_choice == 0:
            sub_loop = False
            return(print("Back to main menu...\n"))
        
        else:
            print("Invalid choice.")
            continue


### Select Data

def select_table():

    sub_loop = True
    while sub_loop == True:

        print(show_tables)
        table_choice = int(input("Enter the number of the table to view: "))

        if table_choice in [1,2,3]:
            display_table(table_dict[table_choice])
            input("Hit ENTER to continue...")
            continue

        if table_choice == 0:
            sub_loop = False
            return(print("Back to main menu...\n"))

        else:
            print("Invalid choice.")
            continue
            
### Select/Join Data



### Delete Tables and/or Columns

def delete_from_table():

    sub_loop = True
    while sub_loop == True:
    
        print(show_tables)
        table_choice = int(input("Enter the number of the table to delete from: "))

        def delete_row(id):

            del_row = sa.delete(table_choice).where(table_choice.columns[id] == delete_id)
            result = connection.execute(del_row)
            print("Record deleted.")

        if table_choice == 1:
            table_choice = captains
            where_id = "cap_id"

            display_table(table_choice)

            delete_id = int(input("Enter the ID of the row to delete: "))

            delete_row(where_id)
            continue

        if table_choice == 2:
            table_choice = boats
            where_id = "boat_id"

            display_table(table_choice)

            delete_id = int(input("Enter the ID of the row to delete: "))

            delete_row(where_id)
            continue

        if table_choice == 3:
            table_choice = charters
            where_id = "charter_id"

            display_table(table_choice)

            delete_id = int(input("Enter the ID of the row to delete: "))

            delete_row(where_id)
            continue

        if table_choice == 0:
                sub_loop = False
                return(print("Back to main menu..."))
            
        else:
            print("Invalid choice.")
            continue

## Main Program

def main():

    main_loop = True
    while main_loop == True:

        print("MAIN MENU\n"
        "1. Insert\n"
        "2. Update\n"
        "3. Select\n"
        "4. Delete\n"
        "0. QUIT")

        choice = int(input("Enter a number for your choice: "))

        if choice == 1:
            insert_table()
            continue

        if choice == 2:
            update_table()
            continue

        if choice == 3:
            select_table()
            continue

        if choice == 4:
            delete_from_table()
            continue

        if choice == 0:
            main_loop == False
            print("\nGoodbye.")
            break

        else:
            print("Invalid choice.")
            continue

main()