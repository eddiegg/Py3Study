from peewee import *
from datetime import date

db = SqliteDatabase('./StudyDB.sqlite')

class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db # This model uses the "people.db" database.

class Pet(Model):
    owner = ForeignKeyField(Person, related_name='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db # this model uses the "people.db" database

db.connect()

# db.create_tables([Person,Pet])
#
# uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15), is_relative=True)
# uncle_bob.save() # bob is now stored in the database
# grandma = Person.create(name='Grandma', birthday=date(1935, 3, 1), is_relative=True)
# herb = Person.create(name='Herb', birthday=date(1950, 5, 5), is_relative=False)
# grandma.name = 'Grandma L.'
# grandma.save()  # Update grandma's name in the database.
# bob_kitty = Pet.create(owner=uncle_bob, name='Kitty', animal_type='cat')
# herb_fido = Pet.create(owner=herb, name='Fido', animal_type='dog')
# herb_mittens = Pet.create(owner=herb, name='Mittens', animal_type='cat')
# herb_mittens_jr = Pet.create(owner=herb, name='Mittens Jr', animal_type='cat')

bob=Person.get(Person.name=='Bob')
print(bob.birthday)

for pp in Person.select():
    print(pp.name,pp.is_relative)

# query = Pet.select().where(Pet.animal_type == 'cat')
# for pet in query:
#     print(pet.name, pet.owner.name)

for pet in Pet.select().join(Person).where(Person.name=='Herb'):
    print(pet.name, pet.owner.name)

for person in Person.select():
    print(person.name, person.pets.count(), '宠物') #pets终于用上了
