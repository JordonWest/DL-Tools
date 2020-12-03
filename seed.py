import os
import sys
from playhouse.shortcuts import model_to_dict, dict_to_model
from models import *

print('Seeding users..')
squid = Users.create(username="squid", password="1", token="debugsquid")
cricket = Users.create(username="cricket", password="1", token="debugcrick")

print('Seeding cowpokes..')
Characters.create(user=squid, name='bojangles')
Characters.create(user=squid, name='Yall Might')
Characters.create(user=cricket, name='Rodeo Goat')

print('Seed complete, ready to ride!')
