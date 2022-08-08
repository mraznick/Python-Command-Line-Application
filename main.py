from peewee import *

db = PostgresqlDatabase('contacts', user='mraznick', password='',
                        host='localhost', port=5432)

db.connect()
