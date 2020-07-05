import json
from json.decoder import JSONDecodeError

from bson import ObjectId
from bson.errors import InvalidId
from flask import request, jsonify, make_response
from flask_restful_swagger_3 import Resource, swagger
from mongoengine import DoesNotExist, ValidationError

from app.adapters.db_adapter import update
from app.models.assetmodel import AssetModel
from app.resources.assets.asset_docs import asset_put_doc, asset_delete_doc
from app.utils.archive_manager import archive_asset
from app.utils.auth_decorators import token_required


class Asset(Resource):
    @token_required(return_user=True)
    @swagger.doc(asset_put_doc)
    def put(self, token_user_id, asset_id):
        try:
            asset = AssetModel.objects.get(id=ObjectId(asset_id))
            if token_user_id != asset.owner_id:
                return make_response("Insufficient Permissions", 403)
            data = json.loads(request.data)
            for value, key in data.items():
                asset[value] = key
            update(asset)
            return jsonify(asset_id=str(asset_id))
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
    @swagger.doc(asset_delete_doc)
    def delete(self, token_user_id, asset_id):
        try:
            asset_obj = AssetModel.objects.get(id=ObjectId(asset_id))
            if token_user_id != asset_obj.owner_id:
                return make_response("Insufficient Permissions", 403)
            archive_asset(asset_obj)

            return jsonify(archived_asset_id=str(asset_id))
        except InvalidId:
            return make_response("Invalid asset ID", 400)
        except DoesNotExist:
            return make_response("Asset not found", 404)
        except Exception as e:
            return make_response("Internal Server Error: {}".format(e.__str__()), 500)
