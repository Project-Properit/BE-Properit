from bson import ObjectId
from bson.errors import InvalidId
from flask import request, jsonify, make_response
from flask_restful_swagger_3 import Resource, swagger
from mongoengine import DoesNotExist
from werkzeug.utils import secure_filename

from app.adapters.db_adapter import update
from app.adapters.dropbox_adapter import DropBoxAdapter
from app.utils.auth_decorators import token_required
from app.models.assetmodel import AssetModel
from app.resources.documents.documents_doc import document_patch_doc, document_delete_doc
from app.settings import DBX_ACCESS_TOKEN


class Doc(Resource):
    @token_required(return_user=True)
    @swagger.doc(document_patch_doc)
    def patch(self, token_user_id, asset_id, document_id):
        try:
            dbx_adapter = DropBoxAdapter(DBX_ACCESS_TOKEN)
            asset = AssetModel.objects.get(id=ObjectId(asset_id))
            if token_user_id != asset.owner_id:
                return make_response("Insufficient Permissions", 403)
            if not request.files:
                return make_response("Upload at least 1 file", 200)
            for key, doc in request.files.items():
                # dbx_filename = secure_filename(doc.filename)  # .rsplit(".", 1)[#]
                dbx_filepath = '/{}/{}'.format(asset_id, key)  # dbx_filename can be changed to 'key'
                asset.documents[document_id] = {'doc_name': key,
                                                'dbx_url': dbx_adapter.upload_file(doc, dbx_filepath),
                                                'dbx_path': dbx_filepath}
            update(asset)
            return jsonify(asset.documents[document_id])
        except InvalidId:
            return make_response("Invalid asset ID", 400)
        except DoesNotExist:
            return make_response("Asset not found", 404)
        except Exception as e:
            return make_response("Internal Server Error: {}".format(e.__str__()), 500)

    @token_required(return_user=True)
    @swagger.doc(document_delete_doc)
    def delete(self, token_user_id, asset_id, document_id):
        try:
            dbx_adapter = DropBoxAdapter(DBX_ACCESS_TOKEN)
            asset = AssetModel.objects.get(id=ObjectId(asset_id))
            if token_user_id != asset.owner_id:
                return make_response("Insufficient Permissions", 403)
            dbx_adapter.delete_file(asset.documents[document_id]['dbx_path'])
            del asset.documents[document_id]
            update(asset)
            return jsonify({"deleted document_id": document_id})
        except InvalidId:
            return make_response("Invalid asset ID", 400)
        except DoesNotExist:
            return make_response("Asset not found", 404)
        except Exception as e:
            return make_response("Internal Server Error: {}".format(e.__str__()), 500)
