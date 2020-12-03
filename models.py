from peewee import *

db=SqliteDatabase('cowboy.db')

# check out validators
class BaseModel(Model):
  class Meta:
    database=db

class Users(BaseModel):
  name = CharField(unique=True, null=False)
  password = CharField(null=False)

db.connect()
db.create_tables([Users])
