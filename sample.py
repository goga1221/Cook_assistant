import sqlite3
from db_class import *
from parse_url import *

cs_db = DB() 
cs_db.create_db()
cs_db.query("INSERT INTO clients (name) values ('Ivan')")
cs_db.query("INSERT INTO recepies (name) values ('test recepie')")
cs_db.query("INSERT INTO favourites (id_client, id_recepie) values (1, 1)")
cs_db.query("INSERT INTO favourites (id_client, id_recepie) values (1, 1)")
print(cs_db.query('SELECT * FROM clients'))
clients_list = (['Vasya'], ['Petya'])
cs_db.insert_many('clients', clients_list)
print(cs_db.query('SELECT * FROM clients WHERE id=1'))
cs_db.query("INSERT INTO recepies (name, category, recepie, ingredients) VALUES ('name test 1', 'cat test 1','recepie 1','мука, соль')")
cs_db.query("INSERT INTO recepies (name, category, recepie, ingredients) VALUES ('name test 2', 'cat test 2','recepie 2','вода, сахар')")
cs_db.query("INSERT INTO recepies (name, category, recepie, ingredients) VALUES ('name test 3', 'cat test 3','recepie 3','топор, каша, любовь')")
print(cs_db.get_random_recepie())
print(cs_db.get_favourites("Ivan"))
print(cs_db.get_recepie_by_name('name test 3'))
print(cs_db.get_recepie_by_ingredients(['соль']))
print(cs_db.get_recepie_by_ingredients(['соль','вода']))
print(cs_db.get_recepie_by_ingredients(['топор','любовь']))

