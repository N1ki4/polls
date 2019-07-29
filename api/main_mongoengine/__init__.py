from flask import Flask
from flask_restplus import Api
from mongoengine import connect

from .config import config_by_name


connection = connect('polls')

app = Flask(__name__)
api = Api(app)

API_BASE_URL = '/api/polls'

from .controller import *
