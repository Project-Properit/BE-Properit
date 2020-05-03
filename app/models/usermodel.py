from mongoengine import Document, StringField, DateTimeField, EmailField, ObjectIdField, ListField


class UserModel(Document):
    last_name = StringField()
    first_name = StringField()
    phone = StringField()
    email = EmailField()
    password = StringField()
    owned_assets = ListField()
    rent_asset = StringField()
    creation_date = DateTimeField()
    meta = {'collection': 'Users'}
