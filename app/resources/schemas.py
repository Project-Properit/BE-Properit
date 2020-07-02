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
        'last_name': {'type': 'string'},
        'payment_details': {'type': 'object',
                            'additionalProperties': {'type': 'string'}},
        'is_tenant': {'type': 'boolean',
                      'default': False},
        'is_owner': {'type': 'boolean',
                     'default': False}
    }


class AssetParameters(ValidatedSchema):
    type = 'object'
    properties = {
        'address': {'type': 'string'},
        'room_num': {'type': 'number'},
        'rent_fee': {'type': 'number'},
        'comments': {'type': 'string'}
    }


class AssetPatchTenantsParams(ValidatedSchema):
    type = 'object'
    properties = {
        'address': {'type': 'string'},
        'room_num': {'type': 'number'},
        'rent_fee': {'type': 'number'},
        'comments': {'type': 'string'}
    }


class PatchAssetDocument(ValidatedSchema):
    type = 'object'
    properties = {
        'email_list': {'type': 'array',
                       'items': {'type': 'string'}}
    }


class GroupPaymentsParameters(ValidatedSchema):
    type = 'object'
    properties = {
        'title': {'type': 'string'},
        'description': {'type': 'string'},
        'is_public': {'type': 'boolean'},
        'amount': {'type': 'number'},
        'payments': {'type': 'array',
                     'items': {'type': 'string'}}
    }


class PaymentParameters(ValidatedSchema):
    type = 'object'
    properties = {
        'pay_from': {'type': 'string'},
        'pay_to': {'type': 'string'},
        'amount': {'type': 'number'},
        'method': {'type': 'string'}
    }


class ServiceCallParameters(ValidatedSchema):
    type = 'object'
    properties = {
        'name': {'type': 'string'},
        'company': {'type': 'string'},
        'phone': {'type': 'string'},
        'price': {'type': 'number'},
        'arrival_date': {'type': 'string'},
        'group_payment_id': {'type': 'string'}
    }


class ServiceCallUpdateableParameters(ValidatedSchema):
    type = 'object'
    properties = {
        'arrival_date': {'type': 'string'},
        'is_closed': {'type': 'boolean'}
    }
