from app.consts import USERS_SECTION
from app.resources.schemas import UserParameters

user_get_filters_doc = {
    'tags': [USERS_SECTION],
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
            'name': 'email',
            'in': 'query',
            'schema': {'type': 'string'},
            'required': False,
            'allowReserved': True
        },
        {
            'name': 'is_tenant',
            'in': 'query',
            'schema': {'type': 'boolean'},
            'required': False,
            'allowReserved': True
        },
        {
            'name': 'is_owner',
            'in': 'query',
            'schema': {'type': 'boolean'},
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

user_put_doc = {
    'tags': [USERS_SECTION],
    'parameters': [
        {
            'in': 'path',
            'name': 'user_id',
            'required': True
        }
    ],
    'requestBody': {
        'required': True,
        'content': {
            'application/json': {
                'schema': UserParameters
            }

        }
    },
    'responses': {
        '200': {'description': 'Object updated successfully'},
        '400': {'description': 'Missing or invalid parameters in request'},
        '500': {'description': 'Internal server error'}
    }
}
