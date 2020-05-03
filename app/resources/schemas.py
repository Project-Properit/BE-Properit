import jsonschema
from flask_restful_swagger_3 import Schema


class ValidatedSchema(Schema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        jsonschema.validate(kwargs, self)


class UserParameters(ValidatedSchema):
    type = 'object'
    properties = {
        'email': {'type': 'string'},
        'password': {'type': 'string'},
        'phone': {'type': 'string'},
        'first_name': {'type': 'string'},
        'last_name': {'type': 'string'}
    }


class AssetParameters(ValidatedSchema):
    type = 'object'
    properties = {
        'address': {'type': 'string'},
        'owner': {'type': 'string'},
        'asset_type': {'type': 'string'},
        'room_num': {'type': 'number'},
        'rent_fee': {'type': 'number'},
        'comments': {'type': 'string'}
    }
