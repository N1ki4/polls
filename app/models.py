from typing import Iterator

from flask_restplus import fields

from . import api
from .database import Database, DatabaseException


choice_fields = api.model('Choice', {
    '_id': fields.Integer(readonly=True),
    'text': fields.String(required=True),
    'votes': fields.Integer(default=0),
})

question_fields = api.model('Question', {
    '_id': fields.String(readonly=True),
    'text': fields.String(required=True),
    'choices': fields.List(fields.Nested(choice_fields), required=True)
})


class QuestionDao:  # probably have to add a time of creation
    """A class for question objects."""
    collection_name = 'questions'

    @staticmethod
    def get_all() -> Iterator:
        return Database.find_all(QuestionDao.collection_name)

    @staticmethod
    def get_by_id(_id):
        return Database.find_one(QuestionDao.collection_name, {'_id': _id})

    @staticmethod
    def create(data):
        for id_, choice in enumerate(data['choices'], start=1):
            choice['_id'] = id_
        result = Database.insert_one(QuestionDao.collection_name, data)
        if result.acknowledged:
            data.update({'_id': result.inserted_id})
            return data
        else:
            raise DatabaseException
