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
        'is_tenant': {'type': 'boolean'},
        'is_owner': {'type': 'boolean'}
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
        'address': {'type': 'string'},
        'room_num': {'type': 'number'},
        'rent_fee': {'type': 'number'},
        'comments': {'type': 'string'}
    }


class PatchAssetDocument(ValidatedSchema):
    type = 'object'
    properties = {
        'doc_name': {'type': 'string',
                     'format': 'binary'},
    }


class GroupPaymentsParameters(ValidatedSchema):
    type = 'object'
    properties = {
        'owner': {'type': 'string'},
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


class PaymentUpdateableParameters(ValidatedSchema):
    type = 'object'
    properties = {
        'is_open': {'type': 'boolean'}
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
