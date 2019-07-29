import json
from datetime import datetime

from ..model.db_exception import DatabaseException
from ..model.mongo_engine import Question, Choice


class QuestionDao:
    @staticmethod
    def get_all():
        try:
            questions = json.loads(Question.objects.to_json())
            for q in questions:
                q['id'] = q['id']['$oid']
                q['date_time'] = datetime.utcfromtimestamp(
                    q['date_time']['$date'] / 1000)
            return questions
        except Exception as e:
            raise DatabaseException(e)

    @staticmethod
    def get_by_id(q_id):
        try:
            return Question.objects.get(_id=q_id)
        except Exception as e:
            raise DatabaseException(e)

    @ staticmethod
    def create(json_data):
        choice_list = []
        try:
            for id_, ch in enumerate(json_data['choices'], start=1):
                choice = Choice()
                choice._id = id_
                choice.text = ch['text']
                choice.votes = ch['votes']
                choice.rate = ch['rate']
                choice.rate_count = ch['rate_count']
                choice_list.append(choice)
            question = Question(choices=choice_list)
            question.text = json_data['text']
            question.save()
        except Exception as e:
            raise DatabaseException(e)
