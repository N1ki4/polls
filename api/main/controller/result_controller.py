from flask_restplus import Resource

from ..model.db_exception import DatabaseException
from ..service.question_dao import QuestionDao
from .. import api, API_BASE_URL
from ..util.dto import QuestionDto

question_fields = QuestionDto.question_fields


@api.route(API_BASE_URL + '/questions/<string:q_id>/result')
@api.param('q_id', 'The question identifier')
class Result(Resource):
    """
    A class for managing result of poll.
    """

    @api.marshal_with(question_fields)
    def get(self, q_id: str):
        """
        Gets question and its choice with max votes.

        :param q_id: id of question to get.
        :return: question and its choice with max votes.
        """
        try:
            return QuestionDao.result(q_id)
        except Exception as e:
            raise DatabaseException(e)
