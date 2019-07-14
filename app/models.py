from app.database import Database, DatabaseException
from app import api
from flask_restplus import fields, Api, Resource


class ModelBase:
    collection_name = None
    objects = Database

    def save(self):
        result = Database.insert_one(collection=self.collection_name,
                                     data=self.as_dict())
        if result.acknowledged:
            return result.inserted_id
        else:
            raise DatabaseException

    def as_dict(self) -> dict:
        """Returns question information in json representation.

        Returns:
            question information in json representation.
        """
        return vars(self)


question_model = api.model('Question', {
    '_id': fields.String(readonly=True),
    'text': fields.String(required=True),
    'choices': fields.List(fields.String)
})


class QuestionDao(ModelBase):  # probably have to add a time of creation
    """A class for question objects."""
    collection_name = 'questions'

    def __init__(self):
        self.questions = QuestionDao.objects.find_all(self.collection_name)

    def get(self, _id):
        for question in self.questions:
            if question['id'] == _id:
                return question
        api.abort(404, "Question {} doesn't exist".format(_id))


class Choice(ModelBase):  # issue with question relations
    collection_name = 'choices'

    def __init__(self, text, votes=0):
        self.text = text
        self.votes = votes
