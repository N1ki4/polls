from flask_restplus import Resource, reqparse

from ..model.db_exception import DatabaseException
from .. import api, API_BASE_URL
from ..service.choice_dao import ChoiceDao
from ..util.dto import QuestionDto

choice_fields = QuestionDto.choice_fields
question_fields = QuestionDto.question_fields


@api.route(API_BASE_URL + '/questions/<string:q_id>/choices/<int:_id>')
@api.param('q_id', 'The question identifier')
@api.param('_id', 'The choice identifier')
class Choice(Resource):
    """
    A class for managing choices.
    """

    @api.marshal_with(choice_fields, code=200)
    def get(self, q_id: str, _id: int) -> tuple:
        """
        Gets choice by question id and choice id.

        :param q_id: question id.
        :param _id: choice id.
        :return: choice.
        """
        try:
            return ChoiceDao.get_by_id(q_id, _id), 200
        except DatabaseException as e:
            api.abort(400, e)

    @staticmethod
    def post(q_id: str, _id: int) -> tuple:
        """
        Posts rate of choice as query string.

        :param q_id: question id.
        :param _id: choice id.
        :return: question with rated choice.
        """
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('rate', type=float)
            args = parser.parse_args()
            rate = args['rate']
            if isinstance(rate, float) and 0 <= rate <= 10:
                return ChoiceDao.rate_choice(q_id, _id, rate), 204
        except DatabaseException as e:
            api.abort(400, e)
