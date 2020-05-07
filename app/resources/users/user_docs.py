from app.resources.schemas import UserUpdatableParameters

user_get_doc = {
    'tags': ['Users'],
    'description': 'Get user',
    'parameters': [
        {
            'in': 'path',
            'name': 'user_id',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': 'Get user successfully',
        },
        '404': {
            'description': 'User not found'
        },
        '500': {
            'description': 'Internal server error'
        }
    }
}
user_put_doc = {
    'tags': ['Users'],
    'description': 'Put user',
    'parameters': [
        {
            'in': 'path',
            'name': 'user_id',
            'required': True
        }
    ],
    'requestBody': {
        'description': 'User updatble parameters',
        'required': True,
        'content': {
            'application/json': {
                'schema': UserUpdatableParameters
            }

        }
    },
    'responses': {
        '200': {
            'description': 'Update user successfully',
        },
        '400': {
            'description': 'Missing or invalid parameters in request'
        },
        '500': {
            'description': 'Internal server error'
        }
    }
}
