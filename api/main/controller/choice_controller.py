from flask_restplus import Resource

from .. import api, API_BASE_URL
from ..service.choice_dao import ChoiceDao
from ..util.dto import QuestionDto

choice_fields = QuestionDto.choice_fields


@api.route(API_BASE_URL + '/questions/<string:q_id>/choices/<int:c_id>')
@api.param('q_id', 'The question identifier')
@api.param('c_id', 'The choice identifier')
class Choice(Resource):
    """
    A class for managing choices.
    """

    @api.marshal_with(choice_fields)
    def get(self, q_id: str, c_id: int) -> dict:
        """
        Gets choice by question id and choice id.

        :param q_id: question id.
        :param c_id: choice id.
        :return: choice.
        """
        result = ChoiceDao.get_by_id(q_id, c_id)
        if result:
            return result
        api.abort(400)

    @api.marshal_with(choice_fields, code=200)
    def patch(self, q_id: str, c_id: int) -> tuple:
        """
        Apply vote method on choice
        :param q_id: question id.
        :param c_id: choice id.
        :return: choice with + 1 votes field.
        """
        result = ChoiceDao.vote(q_id, c_id), 200
        if result:
            return result
        api.abort(400)
