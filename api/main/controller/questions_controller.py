import json

from flask import request
from flask_restplus import Resource

from .. import api, API_BASE_URL
from ..service.question_dao import QuestionDao
from ..util.dto import QuestionDto

question_fields = QuestionDto.question_fields


@api.route(API_BASE_URL + '/questions')
class QuestionsList(Resource):
    """
    A class for managing questions list.
    """

    @api.marshal_list_with(question_fields)
    def get(self) -> list:
        """
        Gets list of questions.

        :return: list of questions.
        """
        result = list(QuestionDao.get_all())
        if result:
            return result
        api.abort(400)

    @api.expect(question_fields, validate=True)
    @api.marshal_with(question_fields, code=201)
    def post(self) -> tuple:
        """
        Creates new question.
        If question wasn't created, sends 400 error.

        :return: question if question was created.
        """
        json_data = json.loads(request.data, encoding='utf-8')
        result = QuestionDao.create(json_data), 201
        if result:
            return result
        api.abort(400)
