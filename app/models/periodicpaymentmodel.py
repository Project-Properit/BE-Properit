from mongoengine import Document, StringField, DateTimeField, FloatField, ListField, BooleanField


class PeriodicPaymentModel(Document):
    owner = StringField(required=True)
    title = StringField(required=True)
    description = StringField(required=True)
    amount = FloatField(required=True)
    payments = ListField()
    is_approved = BooleanField()
    creation_date = DateTimeField()
    meta = {'collection': 'GroupPayments'}
