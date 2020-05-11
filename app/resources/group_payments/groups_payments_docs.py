from app.consts import GROUP_PAYMENTS_SECTION
from app.resources.schemas import GroupPaymentsParameters

groups_payments_post_docs = {
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
        'description': 'Group payment parameters',
        'required': True,
        'content': {
            'application/json': {'schema': GroupPaymentsParameters}
        }
    },
    'responses': {
        '201': {
            'description': 'Group payments created successfully',
        },
        '400': {
            'description': 'Missing or invalid parameters in request'
        },
        '404': {
            'description': 'Object not found'
        },
        '500': {
            'description': 'Internal server error'
        }
    }
}
groups_payments_get_docs = {
    'tags': [GROUP_PAYMENTS_SECTION],
    'description': 'Get Asset groups payments',
    'parameters': [
        {
            'in': 'path',
            'name': 'asset_id',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': 'Get groups payments successfully',
        },
        '400': {
            'description': 'Missing or invalid parameters in request'
        },
        '404': {
            'description': 'Object not found'
        },
        '500': {
            'description': 'Internal server error'
        }
    }
}
