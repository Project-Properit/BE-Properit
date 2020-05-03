from consts import ASSETS_SECTION, AUTH_SECTION
from app.resources.schemas import AssetParameters, PatchAssetTenants

asset_get_doc = {
    'tags': [ASSETS_SECTION],
    'description': 'Get asset',
    'parameters': [
        {
            'name': 'asset_id',
            'description': "Asset's ID to fetch",
            # Todo: path or query?
            # Todo: multiple query filters?
            'in': 'path',
            'required': True,
            'schema': {
                'type': 'string'
            },
        },
    ],
    'responses': {
        '200': {
            'description': 'Asset fetch successfully'
        },
        '400': {
            'description': 'Missing or invalid parameters in request'
        },
        '404': {
            'description': 'Asset not found'
        },
        '500': {
            'description': 'Internal server error'
        }
    }
}

asset_post_doc = {
    'tags': [ASSETS_SECTION],
    'description': 'Add new asset',
    'requestBody': {
        'description': 'Asset parameters',
        'required': True,
        'content': {
            'application/json': {
                'schema': AssetParameters
            }

        }
    },
    'responses': {
        '200': {
            'description': 'Asset added successfully'
        },
        '400': {
            'description': 'Missing or invalid parameters in request'
        },
        '500': {
            'description': 'Internal server error'
        }
    }
}

asset_put_doc = {
    'tags': [ASSETS_SECTION],
    'description': 'Update asset',
    'parameters': [
        {
            'name': 'asset_id',
            'description': "asset's ID to update",
            'in': 'path',
            'required': True,
            'schema': {
                'type': 'string'
            }
        }
    ],
    'requestBody': {
        'description': 'Asset parameters',
        'required': True,
        'content': {
            'application/json': {
                'schema': AssetParameters
            }

        }
    },
    'responses': {
        '200': {
            'description': 'Asset updated successfully'
        },
        '400': {
            'description': 'Missing or invalid parameters in request'
        },
        '404': {
            'description': 'Asset not found'
        },
        '500': {
            'description': 'Internal server error'
        }
    }
}

asset_patch_tenants_doc = {
    'tags': [ASSETS_SECTION],
    'description': "Patch asset's tenant list",
    'parameters': [
        {
            'name': 'asset_id',
            'description': "Asset's ID to patch its tenant list",
            'in': 'path',
            'required': True,
            'schema': {
                'type': 'string'
            },
        },
    ],
    'requestBody': {
        'description': 'Asset parameters',
        'required': True,
        'content': {
            'application/json': {
                'schema': PatchAssetTenants
            }

        }
    },
    'responses': {
        '200': {
            'description': 'Asset fetch successfully'
        },
        '400': {
            'description': 'Missing or invalid parameters in request'
        },
        '404': {
            'description': 'Asset not found'
        },
        '500': {
            'description': 'Internal server error'
        }
    }
}

asset_delete_doc = {
    'tags': [ASSETS_SECTION],
    'description': 'Delete asset',
    'parameters': [
        {
            'name': 'asset_id',
            'description': "Asset's ID to delete",
            'in': 'path',
            'required': True,
            'schema': {
                'type': 'string'
            }
        },
    ],
    'responses': {
        '200': {
            'description': 'Asset deleted successfully'
        },
        '400': {
            'description': 'Missing or invalid parameters in request'
        },
        '404': {
            'description': 'Asset not found'
        },
        '500': {
            'description': 'Internal server error'
        }
    }
}
