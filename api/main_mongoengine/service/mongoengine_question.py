from ..model.db_exception import DatabaseException
from ..model.mongo_engine import Question


class QuestionDao:
    @staticmethod
    def get_all():
        try:
            return Question.objects()
        except Exception as e:
            raise DatabaseException(e)
