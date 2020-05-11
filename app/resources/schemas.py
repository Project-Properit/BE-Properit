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


class UserUpdatableParameters(ValidatedSchema):
    type = 'object'
    properties = {
        'phone': {'type': 'string'},
        'first_name': {'type': 'string'},
        'last_name': {'type': 'string'}
    }


class AssetParameters(ValidatedSchema):
    type = 'object'
    properties = {
        'owner_id': {'type': 'string'},
        'address': {'type': 'string'},
        'asset_type': {'type': 'string'},
        'room_num': {'type': 'number'},
        'rent_fee': {'type': 'number'},
        'tenant_list': {'type': 'array',
                        'items': {'type': 'string'}},
        'comments': {'type': 'string'}
    }


class PatchAssetPromissory(ValidatedSchema):
    type = 'object'
    properties = {
        'promissory': {'type': 'string',
                       'format': 'binary'}
    }


class GroupPaymentsParameters(ValidatedSchema):
    type = 'object'
    properties = {
        'title': {'type': 'string'},
        'description': {'type': 'string'},
        'amount': {'type': 'number'}
    }
