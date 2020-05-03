from mongoengine import Document, StringField, DateTimeField, ListField, FloatField, FileField, IntField

from app.models.user import User


class Property(Document):
    address = StringField()
    owner = IntField()
    prop_type = StringField()
    room_num = IntField()
    tenants_list = ListField()
    rent_fee = FloatField()
    promissory = FileField()
    comments = StringField()
    creation_date = DateTimeField()
    meta = {'collection': 'Properties'}
