from datetime import datetime

from mongoengine import Document, StringField, BooleanField, UUIDField, DateTimeField


class User(Document):
    last_name = StringField()
    first_name = StringField()
    phone = StringField()
    email = StringField()
    admin = BooleanField()
    password = StringField()
    user_id = UUIDField()
    creation_date = DateTimeField()
    meta = {'collection': 'Users'}
