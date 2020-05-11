from mongoengine import Document, StringField, DateTimeField, ListField, FloatField, URLField


class Asset(Document):
    owner_id = StringField(required=True)
    address = StringField(required=True)
    asset_type = StringField(required=True)
    room_num = FloatField(required=True)
    rent_fee = FloatField(required=True)
    tenant_list = ListField()
    group_payments = ListField()
    promissory_note_url = URLField()
    comments = StringField()
    creation_date = DateTimeField()
    meta = {'collection': 'Assets'}
