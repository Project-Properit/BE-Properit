login_get_doc = {
    'tags': ['Auth'],
    'description': 'Login',
    'responses': {
        '200': {
            'description': 'Login successfully'
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
