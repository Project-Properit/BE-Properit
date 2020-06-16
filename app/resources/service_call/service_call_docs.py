from app.consts import SERVICE_CALL_SECTION
from app.resources.schemas import ServiceCallParameters, ServiceCallUpdateableParameters

sc_post_docs = {
    'tags': [SERVICE_CALL_SECTION],
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
            'application/json': {'schema': ServiceCallParameters}
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

sc_get_filters_doc = {
    'tags': [SERVICE_CALL_SECTION],
    'description': 'Get asset by filters',
    'parameters': [
        {
            'name': 'id',
            'description': 'filter assets by their id',
            'in': 'query',
            'schema': {'type': 'string'},
            'required': False,
            'allowReserved': True
        },
        {
            'name': 'company',
            'description': 'filter assets by their owner',
            'in': 'query',
            'schema': {'type': 'string'},
            'required': False,
            'allowReserved': True
        },
        {
            'name': 'phone',
            'description': 'filter assets by their address',
            'in': 'query',
            'schema': {'type': 'string'},
            'required': False,
            'allowReserved': True
        },
        {
            'name': 'price',
            'description': 'filter assets by their type',
            'in': 'query',
            'schema': {'type': 'string'},
            'required': False,
            'allowReserved': True
        },
        {
            'name': 'arrival_date',
            'description': 'filter assets by their room number',
            'in': 'query',
            'schema': {'type': 'number'},
            'required': False,
            'allowReserved': True
        },
        {
            'name': 'is_closed',
            'description': 'filter assets by their rent fee',
            'in': 'query',
            'schema': {'type': 'number'},
            'required': False,
            'allowReserved': True
        },
        {
            'name': 'group_payment_id',
            'description': 'filter assets by their comments',
            'in': 'query',
            'schema': {'type': 'string'},
            'required': False,
            'allowReserved': True
        },
    ],
    'responses': {
        '200': {'description': 'Asset fetched successfully'},
        '400': {'description': 'Missing or invalid parameters in request'},
        '404': {'description': 'Asset not found'},
        '500': {'description': 'Internal server error'}
    }
}

sc_put_doc = {
    'tags': [SERVICE_CALL_SECTION],
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
            'name': 'service_call_id',
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
            'application/json': {'schema': ServiceCallUpdateableParameters}
        }
    },
    'responses': {
        '200': {'description': 'Asset updated successfully'},
        '400': {'description': 'Missing or invalid parameters in request'},
        '404': {'description': 'Asset not found'},
        '500': {'description': 'Internal server error'}
    }
}

sc_delete_docs = {
    'tags': [SERVICE_CALL_SECTION],
    'description': 'Delete Asset group payments',
    'parameters': [
        {
            'in': 'path',
            'name': 'asset_id',
            'required': True
        },
        {
            'in': 'path',
            'name': 'service_call_id',
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
