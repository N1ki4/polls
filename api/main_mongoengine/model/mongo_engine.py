from datetime import datetime

from mongoengine import *


class Choice(EmbeddedDocument):
    _id = IntField(required=True)
    text = StringField(required=True)
    vote_link = URLField('vote')
    votes = IntField(default=0)
    rate = FloatField(default=0)
    rate_count = IntField(default=0)


class Question(Document):
    _id = StringField(required=True)
    text = StringField(required=True)
    date_time = DateTimeField(default=datetime.utcnow)
    choices = ListField(EmbeddedDocumentField(Choice))

    meta = {'collection': 'questions'}
