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
        '400': {
            'description': 'Missing or invalid parameters in request'
        },
        '404': {
            'description': 'User not found'
        },
        '500': {
            'description': 'Internal server error'
        }
    }
}
