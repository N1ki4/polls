from flask import Flask
from pymongo import MongoClient
from flask_restplus import Api

app = Flask(__name__)
api = Api(app)
client = MongoClient('localhost', 27017)

from app import routes
