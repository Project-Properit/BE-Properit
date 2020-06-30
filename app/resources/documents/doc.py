from bson import ObjectId
from bson.errors import InvalidId
from flask import jsonify, make_response
from flask_restful_swagger_3 import Resource, swagger
from mongoengine import DoesNotExist

from app.adapters.db_adapter import update
from app.adapters.dropbox_adapter import DropBoxAdapter
from app.models.assetmodel import AssetModel
from app.resources.documents.documents_doc import document_delete_doc
from app.settings import DBX_ACCESS_TOKEN
from app.utils.auth_decorators import token_required
from app.utils.data_manipulation import get_asset_doc


# from werkzeug.utils import secure_filename


class Doc(Resource):
    @token_required(return_user=True)
    @swagger.doc(document_delete_doc)
    def delete(self, token_user_id, asset_id, doc_id):
        try:
            asset = AssetModel.objects.get(id=ObjectId(asset_id))
            if token_user_id != asset.owner_id:
                return make_response("Insufficient Permissions", 403)
            dbx_adapter = DropBoxAdapter(DBX_ACCESS_TOKEN)
            doc = get_asset_doc(asset, doc_id)
            if not doc:
                return make_response("Document not found", 404)
            dbx_adapter.delete_file(doc['dbx_path'])
            asset.documents.remove(doc)
            update(asset)
            return jsonify(document_id=doc_id)
        except InvalidId:
            return make_response("Invalid asset ID", 400)
        except DoesNotExist:
            return make_response("Asset not found", 404)
        except Exception as e:
            return make_response("Internal Server Error: {}".format(e.__str__()), 500)
