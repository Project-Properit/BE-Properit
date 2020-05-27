from app.consts import GROUP_PAYMENTS_SECTION
from app.resources.schemas import GroupPaymentsParameters, GroupPaymentsUpdateableParameters

group_payments_get_docs = {
    'tags': [GROUP_PAYMENTS_SECTION],
    'description': 'Get Asset group payments',
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
            'description': 'Get group payments successfully',

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
            'application/json': {'schema': GroupPaymentsUpdateableParameters}
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
