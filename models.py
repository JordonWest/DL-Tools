from peewee import *

db=SqliteDatabase('cowboy.db')

# check out validators
class BaseModel(Model):
	class Meta:
		database=db

class Users(BaseModel):
	username = CharField(unique=True, null=False)
	password = CharField(null=False)
	token = CharField(null=False)

class Characters(BaseModel):
	user = ForeignKeyField(Users, backref="characters")
	name = CharField(null=False)


db.connect()
db.create_tables([Users, Characters])
