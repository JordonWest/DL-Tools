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

@app.route("/signup", methods=["POST"])
def create_user():
	print('hit me')
	print(request.form)
	return 'hello'
@app.route("/login", methods=["POST"])
def get_user():
    given = request.get_json()
    user = User.get_or_none(email=given["email"], password=given["password"])
    if user is not None:
        return json.dumps(model_to_dict(user))
    else:
        return 'not found', status.HTTP_404_NOT_FOUND
