from typing import Iterator

from bson import ObjectId
from pymongo import ReturnDocument
from pymongo.results import InsertOneResult

from .. import db


class Database:
    """
    A class for managing database.
    """

    @staticmethod
    def find_one(collection: str, query: dict) -> dict:
        """
        Static method for getting a single document from the database.

        :param collection: name of DB collection.
        :param query: query of object to find.
        :return: a single document as dict.
        """
        return db[collection].find_one(query)

    @staticmethod
    def find_all(collection: str) -> Iterator:
        """
        Static method for getting a single document from the database.

        :param collection: name of DB collection.
        :return: a list of objects.
        """
        return db[collection].find()

    @staticmethod
    def insert_one(collection: str, data: dict) -> InsertOneResult:
        """
        Static method for inserting a single document to the database.

        :param collection: name of DB collection.
        :param data: data of question for inserting.
        :return: InsertOneResult of new question in database.
        """
        return db[collection].insert_one(data)

    @staticmethod
    def update_one(collection: str, _id: ObjectId, data: dict) -> dict:
        return db[collection].find_one_and_update(
            {'_id': ObjectId(_id)}, {'$set': data},
            return_document=ReturnDocument.AFTER)