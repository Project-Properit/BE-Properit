from mongoengine import Document, StringField, DateTimeField, ListField, FloatField, IntField


class Asset(Document):
    address = StringField(required=True)
    owner = StringField(required=True)
    asset_type = StringField(required=True)
    room_num = IntField(required=True)
    rent_fee = FloatField(required=True)
    tenant_list = ListField()
    promissory_note_url = StringField()
    comments = StringField()
    creation_date = DateTimeField()
    meta = {'collection': 'Assets'}
