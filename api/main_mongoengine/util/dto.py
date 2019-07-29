from flask_restplus import fields

from .. import api


class QuestionDto:
    """
    A class for question data transfer object.
    It is responsible for carrying data between processes.
    Custom database objects are creating here.
    """

    choice_fields = api.model('Choice', {
        '_id': fields.Integer(readonly=True),
        'text': fields.String(required=True),
        'vote_link': fields.Url('vote'),
        'votes': fields.Integer(default=0),
        'rate': fields.Float(default=0),
        'rate_count': fields.Integer(default=0),
    })

    question_fields = api.model('Question', {
        '_id': fields.String(readonly=True),
        'text': fields.String(required=True),
        'date_time': fields.DateTime(dt_format='rfc822'),
        'choices': fields.List(fields.Nested(choice_fields),
                               attribute=lambda x: [dict(**choice, q_id=x['_id'])
                                                    for choice in x['choices']],
                               required=True)
    })
