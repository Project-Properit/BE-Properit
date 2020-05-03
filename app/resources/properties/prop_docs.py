from app.resources.models import PropertyParameters

prop_get_doc = {
    'tags': ['Property'],
    'description': 'Get property',
    'parameters': [
        {
            'name': 'property_address',
            'description': "Property's address to fetch",
            'in': 'query',
            'type': 'string',
            'required': True
        },
    ],
    'responses': {
        '200': {
            'description': 'Property fetch successfully'
        },
        '400': {
            'description': 'Missing or invalid parameters in request'
        },
        '404': {
            'description': 'Property not found'
        },
        '500': {
            'description': 'Internal server error'
        }
    }
}

prop_post_doc = {
    'tags': ['Property'],
    'description': 'New property',
    'parameters': [
        {
            'name': 'property_parameters',
            'description': 'Property parameters',
            'in': 'query',
            'required': True,
            'schema': PropertyParameters
        }
    ],
    'responses': {
        '200': {
            'description': 'Property added successfully'
        },
        '400': {
            'description': 'Missing or invalid parameters in request'
        },
        '500': {
            'description': 'Internal server error'
        }
    }
}

prop_put_doc = {
    'tags': ['Property'],
    'description': 'Update property',
    'parameters': [
        {
            'name': 'property_parameters',
            'description': 'Property parameters',
            'in': 'query',
            'required': True,
            'schema': PropertyParameters
        }
    ],
    'responses': {
        '200': {
            'description': 'Property fetch successfully'
        },
        '400': {
            'description': 'Missing or invalid parameters in request'
        },
        '404': {
            'description': 'Property not found'
        },
        '500': {
            'description': 'Internal server error'
        }
    }
}

prop_delete_doc = {
    'tags': ['Property'],
    'description': 'Delete property',
    'parameters': [
        {
            'name': 'property_address',
            'description': "Property's address to fetch",
            'in': 'query',
            'type': 'string',
            'required': True
        },
    ],
    'responses': {
        '200': {
            'description': 'Property fetch successfully'
        },
        '400': {
            'description': 'Missing or invalid parameters in request'
        },
        '404': {
            'description': 'Property not found'
        },
        '500': {
            'description': 'Internal server error'
        }
    }
}
