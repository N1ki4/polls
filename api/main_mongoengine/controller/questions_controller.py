from flask import request
from flask_restplus import Resource

from ..model.db_exception import DatabaseException
from .. import api, API_BASE_URL
from ..service.mongoengine_question import QuestionDao
from ..util.dto import QuestionDto

question_fields = QuestionDto.question_fields


@api.route(API_BASE_URL + '/questions')
class QuestionsList(Resource):
    """
    A class for managing questions list.
    """

    @api.marshal_list_with(question_fields, code=200)
    def get(self) -> tuple:
        """
        Gets list of questions.

        :return: list of questions.
        """
        try:
            return list(QuestionDao.get_all()), 200
        except DatabaseException as e:
            api.abort(400, e)

    @api.expect(question_fields, validate=True)
    def post(self) -> tuple:
        """
        Creates new question.
        If question wasn't created, sends 400 error.

        :return: question if question was created.
        """
        try:
            return QuestionDao.create(), 201
        except DatabaseException as e:
            api.abort(400, e)
