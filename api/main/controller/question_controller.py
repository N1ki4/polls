import json

from flask import request
from flask_restplus import Resource

from api.main import api, API_BASE_URL
from api.main.model.db_exception import DatabaseException
from api.main.service.question_service import QuestionService
from api.main.util.dto import QuestionDto

question_fields = QuestionDto.question_fields


@api.route(API_BASE_URL + '/questions/<string:q_id>')
@api.param('q_id', 'The question identifier')
class Question(Resource):
    """
    A class for managing question.
    """

    @api.marshal_with(question_fields, code=200)
    def get(self, q_id: str) -> tuple:
        """
        Gets question by its id.

        :param q_id: id of question to get.
        :return: question.
        """
        try:
            return QuestionService.get_by_id(q_id), 200
        except DatabaseException as e:
            api.abort(400, e)

    @staticmethod
    def patch(q_id: str) -> tuple:
        """
        Partly updates question by its id.

        :param q_id: id of question to update.
        :return: HTTP status code with empty body.
        """
        json_data = json.loads(request.data, encoding='utf-8')
        try:
            return QuestionService.update_for_patch(q_id, json_data), 204
        except DatabaseException as e:
            api.abort(400, e)

    @staticmethod
    def delete(q_id: str) -> tuple:
        """
        Deletes question by its id.

        :param q_id: id of question to delete.
        :return: HTTP status code with empty body.
        """
        try:
            return QuestionService.delete(q_id), 204
        except DatabaseException as e:
            api.abort(400, e)
