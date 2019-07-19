import json

from flask import request
from flask_restplus import Resource

from api.main import api, API_BASE_URL
from api.main.service.question_dao import QuestionDao
from api.main.util.dto import QuestionDto

question_fields = QuestionDto.question_fields


@api.route(API_BASE_URL + '/questions/<string:_id>')
@api.param('_id', 'The question identifier')
class Question(Resource):
    """
    A class for managing question.
    """

    @api.marshal_with(question_fields)
    def get(self, _id: str) -> dict:
        """
        Gets question by its id.

        :param _id: id of question to get.
        :return: question.
        """
        result = QuestionDao.get_by_id(_id)
        if result:
            return result
        api.abort(400)

    @api.marshal_with(question_fields, code=200)
    def patch(self, _id: str) -> tuple:
        """
        Partly updates question by its id.

        :param _id: id of question to update.
        :return: updated question.
        """
        json_data = json.loads(request.data, encoding='utf-8')
        result = QuestionDao.update(_id, json_data), 200
        if result:
            return result
        api.abort(400)

    @api.marshal_with(question_fields, code=204)
    def delete(self, _id: str):
        """
        Deletes question by its id.

        :param _id: id of question to delete.
        :return: 204 status code.
        """
        result = QuestionDao.delete(_id), 204
        if result:
            return '', 204
        api.abort(400)
