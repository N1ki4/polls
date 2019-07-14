import json

from flask_restplus import Resource

from app import api
from flask import request, abort

from app.database import DatabaseException
from app.models import QuestionDao, question_model

DAO = QuestionDao()


@api.route('/questions')
class QuestionList(Resource):
    @api.marshal_list_with(question_model)
    def get(self):
        return list(DAO.questions)


# @application.route('/questions', methods=['GET', 'POST'])
# def questions():

    # if request.method == "GET":
    #     result = []
    #     for question in QuestionDao.objects.find_all("questions"):
    #         result.append({"id": str(question['_id']),
    #                        "text": question['text'],
    #                        "choices": question['choices']})
    #     return json.dumps(result)
    # elif request.method == "POST":
    #     try:
    #         data = json.loads(request.data)
    #         text = data.get('text')
    #         choices = [{'id': id, 'text': c['text'], 'votes': 0}
    #                    for id, c in enumerate(data.get('choices'))]
    #         if text:
    #             return str(QuestionDao(text, choices).save())
    #     except DatabaseException:
    #         abort(400)
