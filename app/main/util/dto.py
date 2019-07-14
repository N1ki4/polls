from flask_restplus import fields

from app.main import api


class QuestionDto:
    """
    A class for question data transfer object.
    It is responsible for carrying data between processes.
    Custom database objects are creating here.
    """

    choice_fields = api.model('Choice', {
        '_id': fields.Integer(readonly=True),
        'text': fields.String(required=True),
        'votes': fields.Integer(default=0),
    })

    question_fields = api.model('Question', {
        '_id': fields.String(readonly=True),
        'text': fields.String(required=True),
        'choices': fields.List(fields.Nested(choice_fields), required=True)
    })
