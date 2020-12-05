from flask import request, Flask, render_template
from flask_api import status
from models import *
import datetime
import json
from playhouse.shortcuts import model_to_dict, dict_to_model
import os
import secrets

app = Flask(__name__)

@app.route("/")
def main():
	debug = True if os.environ["DEBUG"] == 'true' else False
	print(debug)
	return render_template("main_page.html", debug=debug)

@app.route("/signup", methods=["GET", "POST"])
def create_user():
	if request.method == "POST":
		data = request.form
		if Users.get_or_none(username=data['username']):
			return render_template("signup.html", oops=True)
		token = secrets.token_hex(16)
		user = Users.create(username=data['username'], password=data['password'], token=token)
		return render_template("character_list.html", user=user)
	elif request.method == "GET":
		return render_template("signup.html")
	
@app.route("/login", methods=["POST"])
def get_user():
	data = request.form
	user = Users.get_or_none(username=data["username"], password=data["password"])
	if user is not None:
		characters = Characters.select().where(Characters.user==user)
		return render_template("character_list.html", user=user, characters=characters) 
	else:
		return render_template("main_page.html", oops=True) 
#debounce
@app.route("/character_detail/<user_id>/<token>/<id>", methods=["GET", "POST"])
def cowpoke_detail(user_id, token, id):
	user = Users.get(id=user_id)
	if user.token != token:
		return "Invalid token provided in URL"
	character = Characters.get_or_none(id=id)
	if request.method == "GET":
		return render_template("character_detail.html", character=character, user=user)
	elif request.method == "POST":
		return f'You have attempted to update {character.name}'
	
