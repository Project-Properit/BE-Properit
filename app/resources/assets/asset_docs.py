from app.consts import ASSETS_SECTION
from app.resources.schemas import AssetParameters, PatchAssetPromissory

# region asset_general

asset_get_filters_doc = {
    'tags': [ASSETS_SECTION],
    'description': 'Get asset by filters',
    'parameters': [
        {
            'name': 'id',
            'description': 'filter assets by their owner',
            'in': 'query',
            'schema': {'type': 'string'},
            'required': False,
            'allowReserved': True
        },
        {
            'name': 'owner_id',
            'description': 'filter assets by their owner',
            'in': 'query',
            'schema': {'type': 'string'},
            'required': False,
            'allowReserved': True
        },
        {
            'name': 'address',
            'description': 'filter assets by their ID',
            'in': 'query',
            'schema': {'type': 'string'},
            'required': False,
            'allowReserved': True
        },
        {
            'name': 'asset_type',
            'description': 'filter assets by their ID',
            'in': 'query',
            'schema': {'type': 'string'},
            'required': False,
            'allowReserved': True
        },
        {
            'name': 'room_num',
            'description': 'filter assets by their ID',
            'in': 'query',
            'schema': {'type': 'number'},
            'required': False,
            'allowReserved': True
        },
        {
            'name': 'rent_fee',
            'description': 'filter assets by their ID',
            'in': 'query',
            'schema': {'type': 'number'},
            'required': False,
            'allowReserved': True
        },
        {
            'name': 'comments',
            'description': 'filter assets by their ID',
            'in': 'query',
            'schema': {'type': 'string'},
            'required': False,
            'allowReserved': True
        },
    ],
    'responses': {
        '200': {'description': 'Asset fetched successfully'},
        '400': {'description': 'Missing or invalid parameters in request'},
        '404': {'description': 'Asset not found'},
        '500': {'description': 'Internal server error'}
    }
}

asset_post_doc = {
    'tags': [ASSETS_SECTION],
    'description': 'Add new asset',
    'requestBody': {
        'description': 'Asset parameters',
        'required': True,
        'content': {
            'application/json': {'schema': AssetParameters}
        }
    },
    'responses': {
        '201': {'description': 'Asset added successfully'},
        '400': {'description': 'Missing or invalid parameters in request'},
        '500': {'description': 'Internal server error'}
    }
}

# endregion

# region asset_path_id

# asset_get_by_assetId_doc = {
#     'tags': [ASSETS_SECTION],
#     'description': 'Get asset by asset ID',
#     'parameters': [
#         {
#             'name': 'asset_id',
#             'description': "Asset's ID to fetch",
#             'in': 'path',
#             'required': True,
#             'schema': {'type': 'string'},
#         },
#     ],
#     'responses': {
#         '200': {'description': 'Asset fetched successfully'},
#         '400': {'description': 'Missing or invalid parameters in request'},
#         '404': {'description': 'Asset not found'},
#         '500': {'description': 'Internal server error'}
#     }
# }

asset_put_doc = {
    'tags': [ASSETS_SECTION],
    'description': 'Update asset general parameters',
    'parameters': [
        {
            'name': 'asset_id',
            'description': "Asset ID to update",
            'in': 'path',
            'required': True,
            'schema': {'type': 'string'}
        }
    ],
    'requestBody': {
        'description': 'Asset parameters',
        'required': True,
        'content': {
            'application/json': {'schema': AssetParameters}
        }
    },
    'responses': {
        '200': {'description': 'Asset updated successfully'},
        '400': {'description': 'Missing or invalid parameters in request'},
        '404': {'description': 'Asset not found'},
        '500': {'description': 'Internal server error'}
    }
}

asset_delete_doc = {
    'tags': [ASSETS_SECTION],
    'description': 'Delete asset',
    'parameters': [
        {
            'name': 'asset_id',
            'description': "Asset ID to delete",
            'in': 'path',
            'required': True,
            'schema': {'type': 'string'}
        },
    ],
    'responses': {
        '200': {'description': 'Asset deleted successfully'},
        '400': {'description': 'Missing or invalid parameters in request'},
        '404': {'description': 'Asset not found'},
        '500': {'description': 'Internal server error'}
    }
}

# endregion

# region asset_tenants

# asset_patch_tenants_doc = {
#     'tags': [ASSETS_SECTION],
#     'description': "Patch asset tenants",
#     'parameters': [
#         {
#             'name': 'asset_id',
#             'description': "Asset ID to patch its tenants",
#             'in': 'path',
#             'required': True,
#             'schema': {'type': 'string'},
#         },
#     ],
#     'requestBody': {
#         'description': 'Asset parameters',
#         'required': True,
#         'content': {
#             'application/json': {'schema': PatchAssetTenants}
#         }
#     },
#     'responses': {
#         '200': {'description': 'Asset tenants patched successfully'},
#         '400': {'description': 'Missing or invalid parameters in request'},
#         '404': {'description': 'Asset not found'},
#         '500': {'description': 'Internal server error'}
#     }
# }

# endregion

# region asset_promissory

asset_patch_promissory_doc = {
    'tags': [ASSETS_SECTION],
    'description': "Patch asset promissory note url",
    'parameters': [
        {
            'name': 'asset_id',
            'description': "Asset ID to patch its promissory note",
            'in': 'path',
            'required': True,
            'schema': {'type': 'string'},
        },
    ],
    'requestBody': {
        'description': 'Asset parameters',
        'required': True,
        'content': {
            'multipart/form-data:': {'schema': PatchAssetPromissory}
        }
    },
    'responses': {
        '200': {'description': 'Asset promissory note patched successfully'},
        '400': {'description': 'Missing or invalid parameters in request'},
        '404': {'description': 'Asset not found'},
        '500': {'description': 'Internal server error'}
    }
}

# endregion
