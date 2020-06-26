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
groups_payments_filter_get_docs = {
    'tags': [GROUP_PAYMENTS_SECTION],
    'description': 'Get Asset groups payments',
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

group_payments_put_doc = {
    'tags': [GROUP_PAYMENTS_SECTION],
    'description': 'Update asset general parameters',
    'parameters': [
        {
            'name': 'asset_id',
            'description': "Asset ID to update",
            'in': 'path',
            'required': True,
            'schema': {'type': 'string'}
        },
        {
            'name': 'group_payments_id',
            'description': "Group payment ID to update",
            'in': 'path',
            'required': True,
            'schema': {'type': 'string'}
        }
    ],
    'requestBody': {
        'description': 'Asset parameters',
        'required': True,
        'content': {
            'application/json': {'schema': GroupPaymentsParameters}
        }
    },
    'responses': {
        '200': {'description': 'Asset updated successfully'},
        '400': {'description': 'Missing or invalid parameters in request'},
        '404': {'description': 'Asset not found'},
        '500': {'description': 'Internal server error'}
    }
}

group_payments_delete_docs = {
    'tags': [GROUP_PAYMENTS_SECTION],
    'description': 'Delete Asset group payments',
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
        '200': {
            'description': 'Deleted group payments successfully',

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
