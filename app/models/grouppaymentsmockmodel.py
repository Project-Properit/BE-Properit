from mongoengine import Document, StringField, DateTimeField, FloatField, ListField, DictField


class GroupPaymentsMockModel(Document):
    participants = DictField(required=True)
    name = StringField(required=True)
    description = StringField(required=True)
    total_amount = FloatField()
    owner = DictField()
    creation_date = DateTimeField()
    meta = {'collection': 'GroupPaymentsMock'}
