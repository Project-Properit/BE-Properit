from mongoengine import Document, StringField, DateTimeField, FloatField, ListField, BooleanField


class GroupPaymentModel(Document):
    owner = StringField(required=True)
    title = StringField(required=True)
    description = StringField(required=True)
    amount = FloatField(required=True)
    payments = ListField()
    is_public = BooleanField(default=False)
    is_periodic = BooleanField(default=False)
    is_approved = BooleanField(default=False)
    when_approved = DateTimeField(default=None)
    creation_date = DateTimeField()
    meta = {'collection': 'GroupPayments'}
