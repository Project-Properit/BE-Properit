from mongoengine import Document, StringField, DateTimeField, FloatField, BooleanField, IntField


class PaymentModel(Document):
    pay_from = StringField(required=True)
    pay_to = StringField(required=True)
    amount = FloatField(required=True)
    is_open = BooleanField(default=True)
    method = StringField(default=None)
    when_payed = DateTimeField(default=None)
    deadline = IntField(default=0)
    creation_date = DateTimeField()
    meta = {'collection': 'Payments'}
