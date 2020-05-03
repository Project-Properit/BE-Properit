from mongoengine import Document, StringField, DateTimeField, ListField, FloatField, FileField, IntField


class Asset(Document):
    address = StringField()
    owner = StringField()
    asset_type = StringField()
    room_num = IntField()
    rent_fee = FloatField()
    tenant_list = ListField()
    promissory = FileField()
    comments = StringField()
    creation_date = DateTimeField()
    meta = {'collection': 'Assets'}
