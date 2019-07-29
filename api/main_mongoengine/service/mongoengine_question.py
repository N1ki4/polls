import json
from datetime import datetime

from ..model.db_exception import DatabaseException
from ..model.mongo_engine import Question


class QuestionDao:
    @staticmethod
    def get_all():
        try:
            questions = json.loads(Question.objects.to_json())
            for q in questions:
                q['_id'] = q['_id']['$oid']
                q['date_time'] = datetime.utcfromtimestamp(
                    q['date_time']['$date'] / 1000)
            return questions
        except Exception as e:
            raise DatabaseException(e)

    @ staticmethod
    def create():
        try:
            question = Question()
            question.text = ''
            question.choices = []
            question.save()
        except Exception as e:
            raise DatabaseException(e)
