import json
from json.decoder import JSONDecodeError

from bson import ObjectId
from bson.errors import InvalidId
from flask import request, jsonify, make_response
from flask_restful_swagger_3 import Resource, swagger
from mongoengine import DoesNotExist, ValidationError
from werkzeug.utils import secure_filename

from app.adapters.db_adapter import delete
from app.adapters.db_adapter import update
from app.adapters.dropbox_adapter import DropBoxAdapter
from app.decorators.auth_decorators import token_required
from app.models.assetmodel import AssetModel
from app.resources.assets.asset_docs import asset_patch_documents_doc
from app.resources.assets.asset_docs import asset_put_doc, asset_delete_doc
from app.settings import DBX_ACCESS_TOKEN


class Asset(Resource):
    @token_required()
    @swagger.doc(asset_put_doc)
    def put(self, asset_id):
        try:
            asset = AssetModel.objects.get(id=ObjectId(asset_id))
            data = json.loads(request.data)
            for value, key in data.items():
                asset[value] = key
            update(asset)
            return jsonify({"updated asset_id": str(asset_id)})
        except InvalidId:
            return make_response("Invalid asset ID", 400)
        except JSONDecodeError as e:
            return make_response("Invalid JSON: {}".format(e.__str__()), 400)
        except KeyError as e:
            return make_response("Missing / Invalid json key: {}".format(e.__str__()), 400)
        except ValidationError as e:
            return make_response("Invalid json parameters: {}".format(e.__str__()), 400)
        except DoesNotExist:
            return make_response("Asset not found", 404)
        except Exception as e:
            return make_response("Internal Server Error: {}".format(e.__str__()), 500)

    @token_required(return_user=True)
    @swagger.doc(asset_patch_documents_doc)
    def patch(self, token_user_id, asset_id):
        try:
            dbx_adapter = DropBoxAdapter(DBX_ACCESS_TOKEN)
            asset = AssetModel.objects.get(id=ObjectId(asset_id))
            if token_user_id != asset.owner_id:
                return make_response("Insufficient Permissions", 403)
            if not request.files:
                return make_response("Upload at least 1 file", 400)
            for key, doc in request.files.items():
                dbx_filename = secure_filename(doc.filename)  # .rsplit(".", 1)[#]
                dbx_filepath = '/{}/{}'.format(asset_id, dbx_filename)  # file name can be changed to 'key'
                asset.documents[key] = dbx_adapter.upload_file(doc, dbx_filepath)
            update(asset)
            return jsonify(asset.documents)
        except InvalidId:
            return make_response("Invalid asset ID", 400)
        except DoesNotExist:
            return make_response("Asset not found", 404)
        except Exception as e:
            return make_response("Internal Server Error: {}".format(e.__str__()), 500)

    @token_required(return_user=True)
    @swagger.doc(asset_delete_doc)
    def delete(self, token_user_id, asset_id):
        try:
            asset = AssetModel.objects.get(id=ObjectId(asset_id))
            if token_user_id != asset.owner_id:
                return make_response("Insufficient Permissions", 403)
            delete(asset)
            return jsonify({"deleted asset_id": str(asset_id)})
        except InvalidId:
            return make_response("Invalid asset ID", 400)
        except DoesNotExist:
            return make_response("Asset not found", 404)
        except Exception as e:
            return make_response("Internal Server Error: {}".format(e.__str__()), 500)
