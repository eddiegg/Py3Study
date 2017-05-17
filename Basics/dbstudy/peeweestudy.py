from peewee import *
db = SqliteDatabase('./test.sqlite')
db.connect()

class Users(Model):
    id = CharField()
    name = CharField(primary_key=True)
    age = IntegerField()

    class Meta:
        database = db

class Salarys(Model):
    id = CharField(primary_key=True)
    sid = ForeignKeyField(Users,related_name='u_id')
    name = CharField()
    salary = FloatField()

    class Meta:
        database = db

db.create_tables([Users,Salarys])
db.commit()
db.close()