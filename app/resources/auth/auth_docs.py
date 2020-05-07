from app.consts import AUTH_SECTION
from app.resources.schemas import UserParameters

login_get_doc = {
    'tags': [AUTH_SECTION],
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
    'tags': [AUTH_SECTION],
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
    'tags': [AUTH_SECTION],
    'description': 'Register',
    'requestBody': {
        'description': 'User parameters',
        'required': True,
        'content': {
            'application/json': {
                'schema': UserParameters
            }

        }
    },
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
