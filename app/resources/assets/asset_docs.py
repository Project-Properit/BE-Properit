from app.resources.schemas import AssetParameters, PatchAssetTenants, PatchAssetPromissory
from consts import ASSETS_SECTION

# region asset_general

asset_get_filters_doc = {
    'tags': [ASSETS_SECTION],
    'description': 'Get asset by filters',
    'parameters': [
        {
            'name': 'owner_id',
            'in': 'query',
            'schema': {'type': 'string'},
            'required': False,
            'description': 'filter assets by their owner',
            'allowReserved': True
        },
    ],
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

# endregion

# region asset_path_id

asset_get_by_assetId_doc = {
    'tags': [ASSETS_SECTION],
    'description': 'Get asset by asset ID',
    'parameters': [
        {
            'name': 'asset_id',
            'description': "Asset's ID to fetch",
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

asset_put_doc = {
    'tags': [ASSETS_SECTION],
    'description': 'Update asset general parameters',
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

# endregion

# region asset_tenants

asset_patch_tenants_doc = {
    'tags': [ASSETS_SECTION],
    'description': "Patch asset",
    'parameters': [
        {
            'name': 'asset_id',
            'description': "Asset's ID to patch",
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

# endregion

# region asset_promissory

asset_patch_promissory_doc = {
    'tags': [ASSETS_SECTION],
    'description': "Patch asset",
    'parameters': [
        {
            'name': 'asset_id',
            'description': "Asset's ID to patch",
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
            'multipart/form-data:': {
                'schema': PatchAssetPromissory
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

# endregion
