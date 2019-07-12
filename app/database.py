from pymongo import MongoClient
import json


class DB:
    """A class for managing database.

    Vars:
        URI: a string for identifying request.
        client: MongoDB client
        DATABASE: database from MongoClient.
    """
    URI = "localhost:127.0.0.1:27017"
    client = MongoClient()
    DATABASE = client['films']

    @staticmethod
    def insert_one(collection: str, data: json):
        """Static method for inserting a single document to the database.

        Args:
            collection (str): Name of DB collection.
            data (JSON): Data of object in JSON representation.
        """
        DB.DATABASE[collection].insert_one(data)

    @staticmethod
    def find_one(collection: str, query: json) -> json:
        """Static method for getting a single document from the database.

        Args:
            collection (str): Name of DB collection.
            query (JSON): Query of object in JSON representation.

        Returns:
            a single document in JSON representation.
        """
        return DB.DATABASE[collection].find_one(query)

    @staticmethod
    def find_all(collection: str) -> json:
        """Static method for getting a single document from the database.

        Args:
            collection (str): Name of DB collection.

        Returns:
            a single document in JSON representation.
        """
        return list(DB.DATABASE[collection].find())
