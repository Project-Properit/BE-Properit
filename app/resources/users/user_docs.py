from app.resources.schemas import UserUpdatableParameters

user_get_doc = {
    'tags': ['Users'],
    'parameters': [
        {
            'in': 'path',
            'name': 'user_id',
            'required': True
        }
    ],
    'responses': {
        '200': {'description': 'Object fetched successfully'},
        '404': {'description': 'Object not found'},
        '500': {'description': 'Internal server error'}
    }
}
user_put_doc = {
    'tags': ['Users'],
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
                'schema': UserUpdatableParameters
            }

        }
    },
    'responses': {
        '200': {'description': 'Object updated successfully'},
        '400': {'description': 'Missing or invalid parameters in request'},
        '500': {'description': 'Internal server error'}
    }
}
