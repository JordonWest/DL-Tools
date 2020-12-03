from flask import request, Flask, render_template
from flask_api import status
from models import *
import datetime
import json
from playhouse.shortcuts import model_to_dict, dict_to_model
# import time

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main_page.html")

@app.route("/signup", methods=["GET", "POST"])
def create_user():
	if request.method == "POST":
		data = request.form
		if Users.get_or_none(username=data['username']):
			return render_template("signup.html", oops=True)
		user = Users.create(username=data['username'], password=data['password'])
		return render_template("character_list.html", user=user)
	elif request.method == "GET":
		return render_template("signup.html")
	
@app.route("/login", methods=["POST"])
def get_user():
	data = request.form
	user = Users.get_or_none(username=data["username"], password=data["password"])
	if user is not None:
		return render_template("character_list.html", user=user) 
	else:
		return render_template("main_page.html", oops=True) 
