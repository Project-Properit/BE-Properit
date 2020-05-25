from mongoengine import Document, StringField, DateTimeField, ListField, FloatField, DictField


class AssetModel(Document):
    owner_id = StringField(required=True)
    address = StringField(required=True)
    asset_type = StringField(required=True)
    room_num = FloatField(required=True)
    rent_fee = FloatField(required=True)
    tenant_list = ListField()
    documents = DictField()
    group_payments = ListField()
    comments = StringField()
    creation_date = DateTimeField()
    meta = {'collection': 'Assets'}
