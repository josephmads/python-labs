'''
Consider each of the tasks below as a separate database query. Using SQLAlchemy, which is the necessary code to:

- Select all the actors with the first name of your choice

- Select all the actors and the films they have been in

- Select all the actors that have appeared in a category of a comedy of your choice

- Select all the comedic films and sort them by rental rate

- Using one of the statements above, add a GROUP BY statement of your choice

- Using one of the statements above, add a ORDER BY statement of your choice

'''

import sqlalchemy
from pprint import pprint
import os

password = os.environ["PASSWORD"]

engine = sqlalchemy.create_engine(f"mysql+pymysql://joe:{password}@localhost/sakila")
connection = engine.connect()
metadata = sqlalchemy.MetaData()

actor = sqlalchemy.Table("actor", metadata, autoload=True, autoload_with=engine)
film = sqlalchemy.Table("film", metadata, autoload=True, autoload_with=engine)
film_actor = sqlalchemy.Table("film_actor", metadata, autoload=True, autoload_with=engine)
category = sqlalchemy.Table("category", metadata, autoload=True, autoload_with=engine)
film_category = sqlalchemy.Table("film_category", metadata, autoload=True, autoload_with=engine)

# 1. Select all actors with a specific first name

query1 = sqlalchemy.select([actor]).where(actor.columns.first_name == "MARY")
result_proxy1 = connection.execute(query1)

result_set1 = result_proxy1.fetchall()
pprint(result_set1)

# 2. Select all actors and films they have been in

join_actor_film_actor = actor.join(film_actor, film_actor.columns.actor_id == actor.columns.actor_id)
join_statement = join_actor_film_actor.join(film, film.columns.film_id == film_actor.columns.film_id)

query2 = sqlalchemy.select([film.columns.film_id, film.columns.title, actor.columns.first_name, actor.columns.last_name]).select_from(join_statement)

result_proxy2 = connection.execute(query2)
result_set2 = result_proxy2.fetchall()
pprint(result_set2)

# 3. Select actors in a comedy

join_fa_fc = film_actor.join(film_category, film_category.columns.film_id == film_actor.columns.film_id)
join_fafc_cat = join_fa_fc.join(category, category.columns.category_id == film_category.columns.category_id)
join_statement2 = join_fafc_cat.join(actor, actor.columns.actor_id == film_actor.columns.actor_id)

query3 = sqlalchemy.select([actor.columns.first_name, actor.columns.last_name, category.columns.name]).select_from(join_statement2).where(category.columns.name == "Comedy")

result_proxy3 = connection.execute(query3)
result_set3 = result_proxy3.fetchall()
pprint(result_set3)

# 4. Select all comedies and sort them by rental rate

join_f_fc = film.join(film_category, film_category.columns.film_id == film.columns.film_id)
join_statement4 = join_f_fc.join(category, category.columns.category_id == film_category.columns.category_id)

query4 = sqlalchemy.select([film.columns.title, film.columns.rental_rate, category.columns.name,]).select_from(join_statement4)
query4_filter = query4.where(category.columns.name == "Comedy").order_by(sqlalchemy.asc(film.columns.rental_rate))

result_proxy4 = connection.execute(query4_filter)
result_set4 = result_proxy4.fetchall()
pprint(result_set4)

# 5. Add a GROUP BY statement to one of the previous queries

join_actor_film_actor = actor.join(film_actor, film_actor.columns.actor_id == actor.columns.actor_id)
join_statement5 = join_actor_film_actor.join(film, film.columns.film_id == film_actor.columns.film_id)

query5 = sqlalchemy.select([actor.columns.actor_id, actor.columns.first_name, actor.columns.last_name, sqlalchemy.func.count(actor.columns.actor_id)]).select_from(join_statement5).group_by(actor.columns.actor_id)

result_proxy5 = connection.execute(query5)
result_set5 = result_proxy5.fetchall()
pprint(result_set5)

# 6. See example .4