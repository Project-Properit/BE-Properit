from mongoengine import Document, StringField, DateTimeField, ListField, FloatField, URLField, BooleanField


class PaymentModel(Document):  # from the payer side
    pay_from = StringField(required=True)
    pay_to = StringField(required=True)
    amount = FloatField(required=True)
    method = StringField(required=True)
    is_open = BooleanField(default=True)
    when_payed = DateTimeField(default=None)
    creation_date = DateTimeField()
    meta = {'collection': 'Payments'}
