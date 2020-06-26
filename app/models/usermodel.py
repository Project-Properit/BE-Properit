from mongoengine import Document, StringField, DateTimeField, EmailField, BooleanField, DictField


class UserModel(Document):
    last_name = StringField(required=True)
    first_name = StringField(required=True)
    phone = StringField(required=True)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)
    payment_details = DictField(required=False)
    is_tenant = BooleanField()
    is_owner = BooleanField(default=False)
    creation_date = DateTimeField()
    meta = {'collection': 'Users'}
