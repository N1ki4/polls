from flask import Flask
from flask_restplus import Api

application = Flask(__name__)
api = Api(application)

from . import routes
