from flask_restplus import Resource

from api.main.model.db_exception import DatabaseException
from api.main.service.choice_service import ChoiceService
from api.main.util.dto import QuestionDto
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
        :return: HTTP status code with empty body.
        """
        try:
            return ChoiceService.vote(q_id, _id), 204
        except DatabaseException as e:
            api.abort(400, e)
