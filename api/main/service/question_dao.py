from typing import Iterator

from bson import ObjectId

from ..model.db_exception import DatabaseException
from ..model.mongodb import Database


class QuestionDao:  # probably have to add a time of creation
    """
    A class for question objects.
    """
    collection_name = 'questions'

    @staticmethod
    def get_all() -> Iterator:
        """
        Gets all questions in database.

        :return: Iterator of all questions in collection.
        """
        return Database.find_all(QuestionDao.collection_name)

    @staticmethod
    def get_by_id(_id: str) -> dict:
        """
        Gets question by its id.

        :param _id: str id of question.
        :return: question as dict.
        """
        return Database.find_one(QuestionDao.collection_name,
                                 {'_id': ObjectId(_id)})

    @staticmethod
    def create(data: dict) -> dict:
        """
        Creates question in database.

        :param data: question data for creating.
        :return: question as dict if question was created.
        :raise: DatabaseException if question couldn't be created.
        """
        for id_, choice in enumerate(data['choices'], start=1):
            choice['_id'] = id_
        result = Database.insert_one(QuestionDao.collection_name, data)
        if result.acknowledged:
            data.update({'_id': result.inserted_id})
            return data
        else:
            raise DatabaseException

    @staticmethod
    def update(_id: str, data: dict) -> dict:
        """
        Updates question data by its id.

        :param _id: id of question to update.
        :param data: data of question to update.
        :return: updated question. If DatabaseException raises, returns it.
        """
        result = Database.update_one(QuestionDao.collection_name, _id, data)
        if result:
            return result
        else:
            raise DatabaseException

    @staticmethod
    def delete(_id: str) -> dict:
        """
        Deletes question by its id.

        :param _id: id of question to delete.
        :return: deleted question. If DatabaseException raises, returns it.
        """
        result = Database.delete_one(QuestionDao.collection_name, _id)
        if result:
            return result
        else:
            raise DatabaseException
