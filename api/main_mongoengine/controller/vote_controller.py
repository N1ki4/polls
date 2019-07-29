from flask_restplus import Resource

from ..model.db_exception import DatabaseException
from ..service.choice_dao import ChoiceDao
from ..util.dto import QuestionDto
from .. import api, API_BASE_URL

question_fields = QuestionDto.question_fields


@api.route(API_BASE_URL + '/questions/<string:q_id>/choices/<int:_id>/vote')
@api.param('q_id', 'The question identifier')
@api.param('_id', 'The choice identifier')
class Vote(Resource):
    """
    A class for voting.
    """

    @staticmethod
    def post(q_id: str, _id: int) -> tuple:
        """
        Votes for choice in question.

        :param q_id: question id.
        :param _id: choice id.
        :return: updated question.
        """
        try:
            return ChoiceDao.vote(q_id, _id), 204
        except DatabaseException as e:
            api.abort(400, e)
