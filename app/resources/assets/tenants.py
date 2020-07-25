import json
from json.decoder import JSONDecodeError

from bson import ObjectId
from bson.errors import InvalidId
from flask import request, jsonify, make_response
from flask_restful_swagger_3 import Resource, swagger
from mongoengine import DoesNotExist, ValidationError

from app.adapters.db_adapter import update
from app.models.assetmodel import AssetModel
from app.resources.assets.asset_docs import asset_patch_tenants_doc
from app.utils.auth_decorators import token_required


class Tenants(Resource):
    @token_required(return_user=True)
    @swagger.doc(asset_patch_tenants_doc)
    def patch(self, token_user_id, asset_id):
        try:
            asset = AssetModel.objects.get(id=ObjectId(asset_id))
            if token_user_id != asset.owner_id:
                return make_response("Insufficient Permissions", 403)
            data = json.loads(request.data)
            for user_id in data['user_invite']:
                if user_id in asset.pending_tenants:
                    continue
                asset.pending_tenants += user_id
            update(asset)
            return jsonify(users=data['user_invite'],
                           asset=asset_id)
        except InvalidId:
            return make_response("Invalid payment ID", 400)
        except JSONDecodeError as e:
            return make_response("Invalid JSON: {}".format(e.__str__()), 400)
        except KeyError as e:
            return make_response("Missing / Invalid json key: {}".format(e.__str__()), 400)
        except ValidationError as e:
            return make_response("Invalid json parameters: {}".format(e.__str__()), 400)
        except DoesNotExist:
            return make_response("Payment not found", 404)
        except Exception as e:
            return make_response("Internal Server Error: {}".format(e.__str__()), 500)