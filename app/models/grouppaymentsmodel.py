from mongoengine import Document, StringField, DateTimeField, FloatField, ListField


class GroupPaymentsModel(Document):
    title = StringField(required=True)
    description = StringField(required=True)
    amount = FloatField(required=True)
    payments = ListField()
    creation_date = DateTimeField()
    meta = {'collection': 'GroupPayments'}
