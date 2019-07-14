import json

from flask import request
from flask_restplus import Resource

from . import api
from .models import QuestionDao, question_fields


@api.route('/questions')
class QuestionList(Resource):
    @api.marshal_list_with(question_fields)
    def get(self):
        return list(QuestionDao.get_all())

    @api.expect(question_fields, validate=True)
    @api.marshal_with(question_fields, code=201)
    def post(self):
        json_data = json.loads(request.data)
        result = QuestionDao.create(json_data), 201
        if result:
            return result
        api.abort(400)
