import json
from json.decoder import JSONDecodeError

from bson import ObjectId
from bson.errors import InvalidId
from flask import request, jsonify, make_response
from flask_restful_swagger_3 import Resource, swagger
from mongoengine import DoesNotExist, ValidationError

from app.adapters.db_adapter import update, delete
from app.decorators.auth_decorators import requires_auth
from app.models.assetmodel import Asset
from app.resources.assets.asset_docs import asset_put_doc, asset_delete_doc


class AssetPathId(Resource):
    # @requires_auth
    # @swagger.doc(asset_get_by_assetId_doc)
    # def get(self, asset_id):
    #     try:
    #         asset = Asset.objects.get(id=ObjectId(asset_id))
    #         return to_json(asset)
    #     except InvalidId:
    #         return make_response("Invalid asset ID", 400)
    #     except DoesNotExist:
    #         return make_response("Asset not found", 404)
    #     except Exception as e:
    #         return make_response("Internal Server Error: {}".format(e.__str__()), 500)

    @requires_auth
    @swagger.doc(asset_put_doc)
    def put(self, asset_id):
        try:
            asset = Asset.objects.get(id=ObjectId(asset_id))
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

    @requires_auth
    @swagger.doc(asset_delete_doc)
    def delete(self, asset_id):
        try:
            asset = Asset.objects.get(id=ObjectId(asset_id))
            delete(asset)
            return jsonify({"deleted asset_id": str(asset_id)})
        except InvalidId:
            return make_response("Invalid asset ID", 400)
        except DoesNotExist:
            return make_response("Asset not found", 404)
        except Exception as e:
            return make_response("Internal Server Error: {}".format(e.__str__()), 500)
