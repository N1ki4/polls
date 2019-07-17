from typing import Iterator

from app.main.model.mongodb import Database
from app.main.model.db_exception import DatabaseException


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
        return Database.find_one(QuestionDao.collection_name, {'_id': _id})

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
