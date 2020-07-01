from mongoengine import Document, StringField, DateTimeField, ListField, FloatField


class AssetModel(Document):
    owner_id = StringField(required=True)
    address = StringField(required=True)
    room_num = FloatField(required=True)
    rent_fee = FloatField(required=True)
    tenant_list = ListField(default=None)
    documents = ListField(default=None)
    group_payments = ListField(default=None)
    service_calls = ListField(default=None)
    comments = StringField()
    creation_date = DateTimeField()
    meta = {'collection': 'Assets'}
