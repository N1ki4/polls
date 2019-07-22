import json

from flask import request
from flask_restplus import Resource

from api.main.service.choice_dao import ChoiceDao
from api.main.util.dto import QuestionDto
from .. import api, API_BASE_URL

question_fields = QuestionDto.question_fields


@api.route(API_BASE_URL + '/questions/<string:q_id>/choices/<int:c_id>/action')
@api.param('q_id', 'The question identifier')
@api.param('c_id', 'The choice identifier')
class Vote(Resource):

    @api.marshal_with(question_fields)
    def post(self, q_id: str, c_id: int):
        json_data = json.loads(request.data, encoding='utf-8')
        return ChoiceDao.vote(q_id, c_id, json_data)

