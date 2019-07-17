import json

from flask import request
from flask_restplus import Resource

from app.main import api
from app.main.model.question_dao import QuestionDao
from app.main.util.dto import QuestionDto

question_fields = QuestionDto.question_fields


@api.route('/questions')
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
        if list(QuestionDao.get_all()):
            return list(QuestionDao.get_all())
        api.abort(400)

    @api.expect(question_fields, validate=True)
    @api.marshal_with(question_fields, code=201)
    def post(self) -> tuple:
        """
        Creates new question.
        If question wasn't created, sends 400 error.

        :return: question if question was created.
        """
        json_data = json.loads(request.data)
        result = QuestionDao.create(json_data), 201
        if result:
            return result
        api.abort(400)
