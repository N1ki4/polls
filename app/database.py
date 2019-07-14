from pymongo import MongoClient
from typing import Iterator


class Database:
    """A class for managing database.

    Vars:
        URI: a string for identifying request.
        client: MongoDB client
        DATABASE: database from MongoClient.
    """
    URI = "localhost:127.0.0.1:27017"
    client = MongoClient()
    DATABASE = client['polls']

    @staticmethod
    def insert_one(collection: str, data: dict):
        """Static method for inserting a single document to the database.

        Args:
            collection (str): Name of DB collection.
            data (dict): Data of object.
        """
        return Database.DATABASE[collection].insert_one(data)

    @staticmethod
    def find_one(collection: str, query: dict) -> dict:
        """Static method for getting a single document from the database.

        Args:
            collection (str): Name of DB collection.
            query (dict): Query of object.

        Returns:
            a single document in JSON representation.
        """
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def find_all(collection: str) -> Iterator:
        """Static method for getting a single document from the database.

        Args:
            collection (str): Name of DB collection.

        Returns:
            a list of objects.
        """
        return Database.DATABASE[collection].find()


class DatabaseException(Exception):
    pass
