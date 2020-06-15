from mongoengine import Document, StringField, DateTimeField, EmailField, BooleanField, FloatField


class ServiceCallModel(Document):
    name = StringField(required=True)
    company = StringField(required=True)
    phone = StringField(required=True)
    price = FloatField(required=True, unique=True)
    arrival_date = DateTimeField(required=True)
    is_closed = BooleanField(default=False)
    group_payment_id = StringField(default=None)
    creation_date = DateTimeField()
    meta = {'collection': 'ServiceCalls'}
