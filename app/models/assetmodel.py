from mongoengine import Document, StringField, DateTimeField, ListField, FloatField, IntField


class Asset(Document):
    address = StringField()
    owner = StringField()
    asset_type = StringField()
    room_num = IntField()
    rent_fee = FloatField()
    tenant_list = ListField()
    promissory_note_url = StringField()
    comments = StringField()
    creation_date = DateTimeField()
    meta = {'collection': 'Assets'}
