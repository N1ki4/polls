from flask import Flask
from flask_restplus import Api
from app.database import Database


application = Flask(__name__)
api = Api(application)

from app import routes
