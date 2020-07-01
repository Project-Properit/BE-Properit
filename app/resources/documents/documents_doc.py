from app.consts import DOCUMENTS_SECTION
from app.resources.schemas import PatchAssetDocument

document_post_doc = {
    'tags': [DOCUMENTS_SECTION],
    'description': "Add document",
    'parameters': [
        {
            'name': 'asset_id',
            'in': 'path',
            'required': True,
            'schema': {'type': 'string'},
        },
    ],
    'requestBody': {
        'required': True,
        'content': {
            'multipart/form-data:': {'schema': PatchAssetDocument}
        }
    },
    'responses': {
        '200': {'description': 'Object added successfully'},
        '400': {'description': 'Missing or invalid parameters in request'},
        '404': {'description': 'Object not found'},
        '500': {'description': 'Internal server error'}
    }
}

document_delete_doc = {
    'tags': [DOCUMENTS_SECTION],
    'description': 'Delete document',
    'parameters': [
        {
            'name': 'asset_id',
            'in': 'path',
            'required': True,
            'schema': {'type': 'string'}
        },
        {
            'name': 'doc_id',
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
