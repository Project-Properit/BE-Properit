from bson import ObjectId
from bson.errors import InvalidId
from flask import make_response, jsonify
from flask_restful_swagger_3 import Resource, swagger
from mongoengine import DoesNotExist

from app.adapters.db_adapter import delete, update
from app.decorators.auth_decorators import token_required
from app.models.assetmodel import AssetModel
from app.models.grouppaymentsmodel import GroupPaymentsModel
from app.resources.group_payments.group_payments_docs import group_payments_get_docs


class GroupPayments(Resource):
    @swagger.doc(group_payments_get_docs)
    @token_required(return_user=True)
    def get(self, token_user_id, asset_id, group_payments_id):
        try:
            asset = AssetModel.objects.get(id=ObjectId(asset_id))
        except InvalidId:
            return make_response("Invalid asset ID", 400)
        except DoesNotExist as e:
            return make_response('Asset not found', 404)
        try:
            if token_user_id not in asset.tenant_list and token_user_id != asset.owner_id:
                return make_response("Insufficient Permissions", 403)
            group_payments = GroupPaymentsModel.objects.get(id=ObjectId(group_payments_id))
            return jsonify(
                dict(title=group_payments.title, description=group_payments.description, amount=group_payments.amount))
        except InvalidId:
            return make_response("Invalid group payments ID", 400)
        except DoesNotExist as e:
            return make_response('Group payments not found', 404)
        except Exception as e:
            return make_response("Internal Server Error: {}".format(e.__str__()), 500)

    @swagger.doc(group_payments_get_docs)
    @token_required(return_user=True)
    def delete(self, token_user_id, asset_id, group_payments_id):
        try:
            asset = AssetModel.objects.get(id=ObjectId(asset_id))
        except InvalidId:
            return make_response("Invalid asset ID", 400)
        except DoesNotExist as e:
            return make_response('Asset not found', 404)
        try:
            if token_user_id not in asset.tenant_list and token_user_id != asset.owner_id:
                return make_response("Insufficient Permissions", 403)
            group_payments = GroupPaymentsModel.objects.get(id=ObjectId(group_payments_id))
            delete(group_payments)
            asset.group_payments.remove(group_payments_id)
            update(asset)
            return jsonify({"deleted group_payments_id": str(group_payments_id)})
        except InvalidId:
            return make_response("Invalid group payments ID", 400)
        except DoesNotExist as e:
            return make_response('Group payments not found', 404)
        except Exception as e:
            return make_response("Internal Server Error: {}".format(e.__str__()), 500)
