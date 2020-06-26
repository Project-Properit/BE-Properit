from app.consts import PAYMENTS_SECTION
from app.resources.schemas import PaymentParameters, PaymentUpdateableParameters

# region asset_general


payment_post_doc = {
    'tags': [PAYMENTS_SECTION],
    'description': 'Add new payment',
    'requestBody': {
        'description': 'Payment parameters',
        'required': True,
        'content': {
            'application/json': {'schema': PaymentParameters}
        }
    },
    'responses': {
        '201': {'description': 'Payment added successfully'},
        '400': {'description': 'Missing or invalid parameters in request'},
        '500': {'description': 'Internal server error'}
    }
}
payment_get_filters_doc = {
    'tags': [PAYMENTS_SECTION],
    'description': 'Get payments by filters',
    'parameters': [
        {
            'name': 'id',
            'description': 'filter payments by their ID',
            'in': 'query',
            'schema': {'type': 'string'},
            'required': False,
            'allowReserved': True
        },
        {
            'name': 'pay_from',
            'description': 'filter payments by their pay_from field',
            'in': 'query',
            'schema': {'type': 'string'},
            'required': False,
            'allowReserved': True
        },
        {
            'name': 'pay_to',
            'description': 'filter payments by their pay_to field',
            'in': 'query',
            'schema': {'type': 'string'},
            'required': False,
            'allowReserved': True
        },
        {
            'name': 'amount',
            'description': 'filter payments by their amount',
            'in': 'query',
            'schema': {'type': 'number'},
            'required': False,
            'allowReserved': True
        },
        {
            'name': 'method',
            'description': 'filter payments by their pay method',
            'in': 'query',
            'schema': {'type': 'string'},
            'required': False,
            'allowReserved': True
        },
        {
            'name': 'is_open',
            'description': 'filter payments by their status',
            'in': 'query',
            'schema': {'type': 'boolean'},
            'required': False,
            'allowReserved': True
        }
    ],
    'responses': {
        '200': {'description': 'Payment fetched successfully'},
        '400': {'description': 'Missing or invalid parameters in request'},
        '404': {'description': 'Payment not found'},
        '500': {'description': 'Internal server error'}
    }
}

# endregion

# region asset_path_id

payment_put_doc = {
    'tags': [PAYMENTS_SECTION],
    'description': 'Update payment parameters',
    'parameters': [
        {
            'name': 'payment_id',
            'description': "Payment ID to update",
            'in': 'path',
            'required': True,
            'schema': {'type': 'string'}
        }
    ],
    'requestBody': {
        'description': 'Payment parameters',
        'required': True,
        'content': {
            'application/json': {'schema': PaymentUpdateableParameters}
        }
    },
    'responses': {
        '200': {'description': 'Payment updated successfully'},
        '400': {'description': 'Missing or invalid parameters in request'},
        '404': {'description': 'Payment not found'},
        '500': {'description': 'Internal server error'}
    }
}

payment_delete_doc = {
    'tags': [PAYMENTS_SECTION],
    'description': 'Delete payment',
    'parameters': [
        {
            'name': 'payment_id',
            'description': "Payment ID to delete",
            'in': 'path',
            'required': True,
            'schema': {'type': 'string'}
        },
    ],
    'responses': {
        '200': {'description': 'Payment deleted successfully'},
        '400': {'description': 'Missing or invalid parameters in request'},
        '404': {'description': 'Payment not found'},
        '500': {'description': 'Internal server error'}
    }
}

# endregion
