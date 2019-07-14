from flask import Flask
from flask_restplus import Api
from pymongo import MongoClient

from .config import config_by_name

client = MongoClient()
db = client['polls']

app = Flask(__name__)
api = Api(app)

from app.main.controller import question_controller
