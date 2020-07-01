from app.consts import PAYMENTS_SECTION
from app.resources.schemas import PaymentParameters

payment_post_doc = {
    'tags': [PAYMENTS_SECTION],
    'description': 'Add new payment',
    'requestBody': {
        'required': True,
        'content': {
            'application/json': {'schema': PaymentParameters}
        }
    },
    'responses': {
        '200': {'description': 'Object added successfully'},
        '400': {'description': 'Missing or invalid parameters in request'},
        '500': {'description': 'Internal server error'}
    }
}
payment_get_filters_doc = {
    'tags': [PAYMENTS_SECTION],
    'description': 'get with filters',
    'parameters': [
        {
            'name': 'id',
            'in': 'query',
            'schema': {'type': 'string'},
            'required': False,
            'allowReserved': True
        },
        {
            'name': 'pay_from',
            'description': 'who need to pay',
            'in': 'query',
            'schema': {'type': 'string'},
            'required': False,
            'allowReserved': True
        },
        {
            'name': 'pay_to',
            'description': 'who asked the payment',
            'in': 'query',
            'schema': {'type': 'string'},
            'required': False,
            'allowReserved': True
        },
        {
            'name': 'amount',
            'in': 'query',
            'schema': {'type': 'number'},
            'required': False,
            'allowReserved': True
        },
        {
            'name': 'method',
            'in': 'query',
            'schema': {'type': 'string'},
            'required': False,
            'allowReserved': True
        },
        {
            'name': 'is_open',
            'in': 'query',
            'schema': {'type': 'boolean'},
            'required': False,
            'allowReserved': True,
            'allowEmptyValue': True
        }
    ],
    'responses': {
        '200': {'description': 'Object fetched successfully'},
        '400': {'description': 'Missing or invalid parameters in request'},
        '404': {'description': 'Object not found'},
        '500': {'description': 'Internal server error'}
    }
}

payment_put_doc = {
    'tags': [PAYMENTS_SECTION],
    'description': 'pay method',
    'parameters': [
        {
            'name': 'payment_id',
            'in': 'path',
            'required': True,
            'schema': {'type': 'string'}
        }
    ],
    'responses': {
        '200': {'description': 'Payment payed successfully'},
        '400': {'description': 'Missing or invalid parameters in request'},
        '404': {'description': 'Object not found'},
        '500': {'description': 'Internal server error'}
    }
}

payment_delete_doc = {
    'tags': [PAYMENTS_SECTION],
    'description': 'Delete payment',
    'parameters': [
        {
            'name': 'payment_id',
            'in': 'path',
            'required': True,
            'schema': {'type': 'string'}
        },
    ],
    'responses': {
        '200': {'description': 'Object deleted successfully'},
        '400': {'description': 'Missing or invalid parameters in request'},
        '404': {'description': 'Object not found'},
        '500': {'description': 'Internal server error'}
    }
}
