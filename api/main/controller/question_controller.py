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
    @api.marshal_with(question_fields)
    def get(self, _id: str) -> dict:
        result = QuestionDao.get_by_id(_id)
        if result:
            return result
        api.abort(400)

    @api.marshal_with(question_fields, code=200)
    def patch(self, _id) -> tuple:
        json_data = json.loads(request.data)
        result = QuestionDao.update(_id, json_data), 200
        if result:
            return result
        api.abort(400)
