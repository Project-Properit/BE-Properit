from mongoengine import Document, StringField, DateTimeField, ListField, FloatField, DictField


class AssetModel(Document):
    owner_id = StringField(required=True)
    address = StringField(required=True)
    asset_type = StringField(required=True)
    room_num = FloatField(required=True)
    rent_fee = FloatField(required=True)
    tenant_list = ListField(default=None)
    documents = DictField(default=None)
    group_payments = ListField(default=None)
    service_calls = ListField(default=None)
    comments = StringField()
    creation_date = DateTimeField()
    meta = {'collection': 'Assets'}
