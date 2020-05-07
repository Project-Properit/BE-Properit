from mongoengine import Document, StringField, DateTimeField


class TokenModel(Document):
    token = StringField(required=True)
    creation_date = DateTimeField()
    meta = {'collection': 'Tokens'}
