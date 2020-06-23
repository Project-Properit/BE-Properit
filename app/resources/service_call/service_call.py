import json
from json import JSONDecodeError

from bson import ObjectId
from bson.errors import InvalidId
from flask import make_response, jsonify, request
from flask_restful_swagger_3 import Resource, swagger
from mongoengine import DoesNotExist, ValidationError

from app.adapters.db_adapter import delete, update
from app.utils.auth_decorators import token_required
from app.models.assetmodel import AssetModel
from app.models.servicecallmodel import ServiceCallModel
from app.resources.service_call.service_call_docs import sc_put_doc, sc_delete_docs


class ServiceCall(Resource):
    @token_required(return_user=True)
    @swagger.doc(sc_put_doc)
    def put(self, token_user_id, asset_id, service_call_id):
        try:
            asset = AssetModel.objects.get(id=ObjectId(asset_id))
        except InvalidId:
            return make_response("Invalid asset ID", 400)
        except DoesNotExist as e:
            return make_response('Asset not found', 404)
        try:
            if token_user_id not in asset.tenant_list and token_user_id != asset.owner_id:
                return make_response("Insufficient Permissions", 403)
            service_call = ServiceCallModel.objects.get(id=ObjectId(service_call_id))
            data = json.loads(request.data)
            for value, key in data.items():
                service_call[value] = key
            update(service_call)
            return jsonify({"updated group_payments_id": str(service_call_id)})
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

    @swagger.doc(sc_delete_docs)
    @token_required(return_user=True)
    def delete(self, token_user_id, asset_id, service_call):
        try:
            asset = AssetModel.objects.get(id=ObjectId(asset_id))
        except InvalidId:
            return make_response("Invalid asset ID", 400)
        except DoesNotExist as e:
            return make_response('Asset not found', 404)
        try:
            if token_user_id not in asset.tenant_list and token_user_id != asset.owner_id:
                return make_response("Insufficient Permissions", 403)
            service_call = ServiceCallModel.objects.get(id=ObjectId(service_call))
            delete(service_call)
            asset.group_payments.remove(service_call)
            update(asset)
            return jsonify({"deleted group_payments_id": str(service_call)})
        except InvalidId:
            return make_response("Invalid group payments ID", 400)
        except DoesNotExist as e:
            return make_response('Group payments not found', 404)
        except Exception as e:
            return make_response("Internal Server Error: {}".format(e.__str__()), 500)
