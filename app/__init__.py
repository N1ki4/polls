from flask import Flask
from flask_pymongo import PyMongo
from flask_restplus import Api

app = Flask(__name__)
api = Api(app)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

from app import routes
