from app.consts import ASSETS_SECTION
from app.resources.schemas import AssetParameters, PatchAssetPendingTenants

asset_get_filters_doc = {
    'tags': [ASSETS_SECTION],
    'description': 'get with filters',
    'parameters': [
        {
            'name': 'id',
            'in': 'query',
            'schema': {'type': 'string'},
            'required': False,
            'allowReserved': True
        },
        {
            'name': 'owner_id',
            'in': 'query',
            'schema': {'type': 'string'},
            'required': False,
            'allowReserved': True
        },
        {
            'name': 'address',
            'in': 'query',
            'schema': {'type': 'string'},
            'required': False,
            'allowReserved': True
        },
        {
            'name': 'asset_type',
            'in': 'query',
            'schema': {'type': 'string'},
            'required': False,
            'allowReserved': True
        },
        {
            'name': 'room_num',
            'in': 'query',
            'schema': {'type': 'number'},
            'required': False,
            'allowReserved': True
        },
        {
            'name': 'rent_fee',
            'in': 'query',
            'schema': {'type': 'number'},
            'required': False,
            'allowReserved': True
        },
        {
            'name': 'comments',
            'in': 'query',
            'schema': {'type': 'string'},
            'required': False,
            'allowReserved': True
        },
    ],
    'responses': {
        '200': {'description': 'Object fetched successfully'},
        '400': {'description': 'Missing or invalid parameters in request'},
        '404': {'description': 'Object not found'},
        '500': {'description': 'Internal server error'}
    }
}

asset_post_doc = {
    'tags': [ASSETS_SECTION],
    'description': 'Add new asset',
    'requestBody': {
        'required': True,
        'content': {
            'application/json': {'schema': AssetParameters}
        }
    },
    'responses': {
        '200': {'description': 'Object added successfully'},
        '400': {'description': 'Missing or invalid parameters in request'},
        '500': {'description': 'Internal server error'}
    }
}

asset_put_doc = {
    'tags': [ASSETS_SECTION],
    'description': 'Update asset parameters',
    'parameters': [
        {
            'name': 'asset_id',
            'in': 'path',
            'required': True,
            'schema': {'type': 'string'}
        }
    ],
    'requestBody': {
        'required': True,
        'content': {
            'application/json': {'schema': AssetParameters}
        }
    },
    'responses': {
        '200': {'description': 'Object updated successfully'},
        '400': {'description': 'Missing or invalid parameters in request'},
        '404': {'description': 'Object not found'},
        '500': {'description': 'Internal server error'}
    }
}

asset_patch_tenants_doc = {
    'tags': [ASSETS_SECTION],
    'description': 'Update asset tenants',
    'parameters': [
        {
            'name': 'asset_id',
            'in': 'path',
            'required': True,
            'schema': {'type': 'string'}
        }
    ],
    'requestBody': {
        'required': True,
        'content': {
            'application/json': {'schema': PatchAssetPendingTenants}
        }
    },
    'responses': {
        '200': {'description': 'Object updated successfully'},
        '400': {'description': 'Missing or invalid parameters in request'},
        '404': {'description': 'Object not found'},
        '500': {'description': 'Internal server error'}
    }
}

asset_delete_doc = {
    'tags': [ASSETS_SECTION],
    'description': 'Delete asset',
    'parameters': [
        {
            'name': 'asset_id',
            'in': 'path',
            'required': True,
            'schema': {'type': 'string'}
        },
    ],
    'responses': {
        '200': {'description': 'Object deleted successfully'},
        '400': {'description': 'Missing or invalid parameters in request'},
        '404': {'description': 'Object not found'},
        '500': {'description': 'Internal server error'}
    }
}
