from mongoengine import Document, StringField, DateTimeField, FloatField, ListField, BooleanField


class GroupPaymentsModel(Document):
    owner = StringField(required=True)
    title = StringField(required=True)
    description = StringField(required=True)
    amount = FloatField(required=True)
    payments = ListField()
    is_public = BooleanField()
    creation_date = DateTimeField()
    meta = {'collection': 'GroupPayments'}
