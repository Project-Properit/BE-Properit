from app.consts import SERVICE_CALL_SECTION
from app.resources.schemas import ServiceCallParameters, ServiceCallUpdateableParameters

sc_post_docs = {
    'tags': [SERVICE_CALL_SECTION],
    'description': 'Create service call',
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
            'application/json': {'schema': ServiceCallParameters}
        }
    },
    'responses': {
        '200': {'description': 'Object created successfully'},
        '400': {'description': 'Missing or invalid parameters in request'},
        '500': {'description': 'Internal server error'}
    }
}

sc_get_filters_doc = {
    'tags': [SERVICE_CALL_SECTION],
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
            'name': 'company',
            'in': 'query',
            'schema': {'type': 'string'},
            'required': False,
            'allowReserved': True
        },
        {
            'name': 'phone',
            'in': 'query',
            'schema': {'type': 'string'},
            'required': False,
            'allowReserved': True
        },
        {
            'name': 'price',
            'in': 'query',
            'schema': {'type': 'string'},
            'required': False,
            'allowReserved': True
        },
        {
            'name': 'arrival_date',
            'in': 'query',
            'schema': {'type': 'number'},
            'required': False,
            'allowReserved': True
        },
        {
            'name': 'is_closed',
            'in': 'query',
            'schema': {'type': 'number'},
            'required': False,
            'allowReserved': True
        },
        {
            'name': 'group_payment_id',
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

sc_put_doc = {
    'tags': [SERVICE_CALL_SECTION],
    'description': 'Update service-call parameters',
    'parameters': [
        {
            'name': 'asset_id',
            'in': 'path',
            'required': True,
            'schema': {'type': 'string'}
        },
        {
            'name': 'service_call_id',
            'in': 'path',
            'required': True,
            'schema': {'type': 'string'}
        }
    ],
    'requestBody': {
        'required': True,
        'content': {
            'application/json': {'schema': ServiceCallUpdateableParameters}
        }
    },
    'responses': {
        '200': {'description': 'Object updated successfully'},
        '400': {'description': 'Missing or invalid parameters in request'},
        '404': {'description': 'Object not found'},
        '500': {'description': 'Internal server error'}
    }
}

sc_delete_docs = {
    'tags': [SERVICE_CALL_SECTION],
    'description': 'Delete service call',
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
        '200': {'description': 'Object deleted successfully'},
        '400': {'description': 'Missing or invalid parameters in request'},
        '404': {'description': 'Object not found'},
        '500': {'description': 'Internal server error'}
    }
}
