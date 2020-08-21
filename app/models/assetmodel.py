from mongoengine import Document, StringField, DateTimeField, ListField, FloatField


class AssetModel(Document):
    owner_id = StringField(required=True)
    address = StringField(required=True)
    room_num = FloatField(required=True)
    rent_fee = FloatField(required=True)
    tenant_list = ListField(default=[])
    pending_tenants = ListField(default=[])
    documents = ListField(default=[])
    group_payments = ListField(default=[])
    periodic_payments = ListField(default=[])
    service_calls = ListField(default=[])
    comments = StringField()
    creation_date = DateTimeField()
    meta = {'collection': 'Assets'}
