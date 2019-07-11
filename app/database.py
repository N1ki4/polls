from pymongo import MongoClient


class DB:
    URI = "localhost:127.0.0.1:27017"
    DATABASE = None

    @staticmethod
    def __init__():
        client = MongoClient()
        DB.DATABASE = client['films']

    @staticmethod
    def insert(collection, data):
        DB.DATABASE[collection].insert(data)

    @staticmethod
    def find_one(collection, query):
        return DB.DATABASE[collection].find_one(query)
