from mongoengine import Document, StringField, DateTimeField


class TokenModel(Document):
    token = StringField()
    creation_date = DateTimeField()
    meta = {'collection': 'Tokens'}
