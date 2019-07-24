from typing import Iterator

from bson import ObjectId
from datetime import datetime, timedelta

from api.main import API_BASE_URL, api
from ..model.db_exception import DatabaseException
from ..model.mongodb import Database


class QuestionDao:
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
            choice['votes'] = 0
            choice['rate'] = 0
            choice['rate_count'] = 0
        data.update({'date_time': datetime.now()})
        result = Database.insert_one(QuestionDao.collection_name, data)
        if result.acknowledged:
            ch_list = QuestionDao.get_by_id(result.inserted_id)['choices']
            for ch in ch_list:
                ch['vote_link'] = QuestionDao.create_vote_link(
                    result.inserted_id, ch)
            return QuestionDao.update(result.inserted_id, {'choices': ch_list})
        else:
            raise DatabaseException

    @staticmethod
    def create_vote_link(q_id: str, choice: dict) -> str:
        return 'http://127.0.0.1:5000' + API_BASE_URL + '/questions/' + \
               f'{q_id}' + f'/choices/{choice.get("_id")}' + '/vote'

    @staticmethod
    def update(_id: str, data: dict) -> dict:
        """
        Updates question data by its id.

        :param _id: id of question to update.
        :param data: data of question to update.
        :return: updated question. If DatabaseException raises, returns it.
        :raise: DatabaseException if question couldn't be updated.
        """
        result = Database.update_one(QuestionDao.collection_name, _id, data)
        if result:
            return result
        else:
            raise DatabaseException

    @staticmethod
    def update_for_patch(_id: str, data: dict) -> dict:
        """
        Updates question data by its id for patch method checking time of
        creation.

        :param _id: id of question to update.
        :param data: data of question to update.
        :return: updated question. If DatabaseException raises, returns it.
        :raise: DatabaseException if question couldn't be updated.
        """
        result = None
        question = QuestionDao.get_by_id(_id)
        if datetime.now() - question['date_time'] <= timedelta(seconds=10):
            result = Database.update_one(QuestionDao.collection_name, _id,
                                         data)
        else:
            api.abort(401)
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
        :raise: DatabaseException if there isn't a question with _id.
        """
        result = Database.delete_one(QuestionDao.collection_name, _id)
        if result:
            return result
        else:
            raise DatabaseException
