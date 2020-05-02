from mongoengine import Document, StringField, DateTimeField


class Token(Document):
    token = StringField()
    creation_date = DateTimeField()
    meta = {'collection': 'Tokens'}
