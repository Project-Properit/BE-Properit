from app.consts import DOCUMENTS_SECTION
from app.resources.schemas import PatchAssetDocument

# region asset_general

# endregion

# region asset_path_id

document_post_doc = {
    'tags': [DOCUMENTS_SECTION],
    'description': "Patch asset documents",
    'parameters': [
        {
            'name': 'asset_id',
            'description': "Asset ID to patch its documents",
            'in': 'path',
            'required': True,
            'schema': {'type': 'string'},
        },
    ],
    'requestBody': {
        'description': 'Asset parameters',
        'required': True,
        'content': {
            'multipart/form-data:': {'schema': PatchAssetDocument}
        }
    },
    'responses': {
        '200': {'description': 'Asset documents patched successfully'},
        '400': {'description': 'Missing or invalid parameters in request'},
        '404': {'description': 'Asset not found'},
        '500': {'description': 'Internal server error'}
    }
}

document_delete_doc = {
    'tags': [DOCUMENTS_SECTION],
    'description': 'Delete asset',
    'parameters': [
        {
            'name': 'asset_id',
            'description': "Asset ID to delete",
            'in': 'path',
            'required': True,
            'schema': {'type': 'string'}
        },
        {
            'name': 'document_id',
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

document_patch_doc = {
    'tags': [DOCUMENTS_SECTION],
    'description': "Patch asset documents",
    'parameters': [
        {
            'name': 'asset_id',
            'description': "Asset ID to patch its documents",
            'in': 'path',
            'required': True,
            'schema': {'type': 'string'},
        },
        {
            'name': 'document_id',
            'description': "Document ID to patch",
            'in': 'path',
            'required': True,
            'schema': {'type': 'string'},
        },
    ],
    'requestBody': {
        'description': 'Asset parameters',
        'required': True,
        'content': {
            'multipart/form-data:': {'schema': PatchAssetDocument}
        }
    },
    'responses': {
        '200': {'description': 'Asset documents patched successfully'},
        '400': {'description': 'Missing or invalid parameters in request'},
        '404': {'description': 'Asset not found'},
        '500': {'description': 'Internal server error'}
    }
}

# endregion
