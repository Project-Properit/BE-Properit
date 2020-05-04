from mongoengine import Document, StringField, DateTimeField, EmailField, ListField


class UserModel(Document):
    last_name = StringField(required=True)
    first_name = StringField(required=True)
    phone = StringField(required=True)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)
    owned_assets = ListField(required=False)
    rent_asset = StringField(required=False, null=True)
    creation_date = DateTimeField()
    meta = {'collection': 'Users'}
