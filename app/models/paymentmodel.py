from mongoengine import Document, StringField, DateTimeField, ListField, FloatField, URLField


class PaymentModel(Document):  # from the payer side
    pay_from = StringField(required=True)
    pay_to = StringField(required=True)
    amount = FloatField(required=True)
    method = StringField(required=True)
    status = StringField(required=True, default='Pending')
    creation_date = DateTimeField()
    meta = {'collection': 'Payments'}
