from app.resources.models import UserParameters

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
logout_post_doc = {
    'tags': ['Auth'],
    'description': 'Logout',
    'responses': {
        '200': {
            'description': 'Logout successfully'
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
register_post_doc = {
    'tags': ['Auth'],
    'description': 'Register',
    'parameters': [
        {
            'name': 'user_parameters',
            'description': 'User parameters',
            'in': 'query',
            'required': True,
            'schema': UserParameters
        }
    ],
    'responses': {
        '200': {
            'description': 'Register successfully'
        },
        '400': {
            'description': 'Missing or invalid parameters in request'
        },
        '500': {
            'description': 'Internal server error'
        }
    }
}
