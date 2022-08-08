from peewee import *

db = PostgresqlDatabase('blackbook', user='mraznick', password='',
                        host='localhost', port=5432)

db.connect()


class BaseModel(Model):
    class Meta:
        database = db


class Contact(BaseModel):
    first_name = CharField()
    last_name = CharField()
    phone_number = CharField()


db.drop_tables([Contact])
db.create_tables([Contact])

mitch = Contact(first_name='Mitch', last_name='Raznick',
                phone_number=('402-980-4919'))
mitch.save()

john = Contact(first_name='John', last_name='Smith',
               phone_number=('402-474-9871'))
john.save()

jane = Contact(first_name='Jane', last_name='Doe', phone_number='914-765-3398')
jane.save()

all_contacts = Contact.select()
print([contact.first_name and contact.last_name and contact.phone_number for contact in all_contacts])

first_contact = Contact.get(Contact.first_name == 'Mitch')
print(first_contact.first_name)

first_contact.first_name = 'Mitchell'
first_contact.save()
print(first_contact.first_name)
