'''

All of the following exercises should be done using sqlalchemy.

Using the provided database schema, write the necessary code to print information about the film and category table.

'''

import sqlalchemy
import os

password = os.environ["PASSWORD"]

engine = sqlalchemy.create_engine(f"mysql+pymysql://joe:{password}@localhost/sakila")
connection = engine.connect()
metadata = sqlalchemy.MetaData()

film = sqlalchemy.Table("film", metadata, autoload=True, autoload_with=engine)
category = sqlalchemy.Table("category", metadata, autoload=True, autoload_with=engine)

print(film.columns.keys())
print(category.columns.keys())