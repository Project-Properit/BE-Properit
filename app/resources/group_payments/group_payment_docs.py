from app.consts import GROUP_PAYMENTS_SECTION
from app.resources.schemas import GroupPaymentsParameters

group_payments_post_docs = {
    'tags': [GROUP_PAYMENTS_SECTION],
    'description': 'Create group payments',
    'parameters': [
        {
            'in': 'path',
            'name': 'asset_id',
            'required': True
        }
    ],
    'requestBody': {
        'required': True,
        'content': {
            'application/json': {'schema': GroupPaymentsParameters}
        }
    },
    'responses': {
        '200': {'description': 'Object added successfully'},
        '400': {'description': 'Missing or invalid parameters in request'},
        '404': {'description': 'Object not found'},
        '500': {'description': 'Internal server error'}
    }
}
group_payments_filter_get_docs = {
    'tags': [GROUP_PAYMENTS_SECTION],
    'description': 'Get with filters',
    'parameters': [
        {
            'in': 'path',
            'name': 'asset_id',
            'required': True
        },
        {
            'name': 'pay_to',
            'in': 'query',
            'schema': {'type': 'string'},
            'required': False,
            'allowReserved': True
        },
        {
            'name': 'pay_from',
            'in': 'query',
            'schema': {'type': 'string'},
            'required': False,
            'allowReserved': True
        },
    ],
    'responses': {
        '200': {'description': 'Object fetched successfully'},
        '400': {'description': 'Missing or invalid parameters in request'},
        '404': {'description': 'Object not found'},
        '500': {'description': 'Internal server error'}
    }
}

group_payments_put_doc = {
    'tags': [GROUP_PAYMENTS_SECTION],
    'description': 'Update group payment',
    'parameters': [
        {
            'name': 'asset_id',
            'in': 'path',
            'required': True,
            'schema': {'type': 'string'}
        },
        {
            'name': 'group_payments_id',
            'in': 'path',
            'required': True,
            'schema': {'type': 'string'}
        }
    ],
    'requestBody': {
        'required': True,
        'content': {
            'application/json': {'schema': GroupPaymentsParameters}
        }
    },
    'responses': {
        '200': {'description': 'Object updated successfully'},
        '400': {'description': 'Missing or invalid parameters in request'},
        '404': {'description': 'Object not found'},
        '500': {'description': 'Internal server error'}
    }
}

group_payments_delete_docs = {
    'tags': [GROUP_PAYMENTS_SECTION],
    'description': 'Delete group payment',
    'parameters': [
        {
            'in': 'path',
            'name': 'asset_id',
            'required': True
        },
        {
            'in': 'path',
            'name': 'group_payments_id',
            'required': True
        }
    ],
    'responses': {
        '200': {'description': 'Object deleted successfully'},
        '400': {'description': 'Missing or invalid parameters in request'},
        '404': {'description': 'Object not found'},
        '500': {'description': 'Internal server error'}
    }
}
