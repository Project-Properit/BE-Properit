from bson import ObjectId
from bson.errors import InvalidId
from flask import make_response, jsonify
from flask_restful_swagger_3 import Resource, swagger
from mongoengine import DoesNotExist

from app.adapters.db_adapter import update
from app.models.assetmodel import AssetModel
from app.models.grouppaymentmodel import GroupPaymentModel
from app.resources.group_payments.group_payment_docs import group_payments_delete_docs
from app.utils.archive_manager import archive_group_payment
from app.utils.auth_decorators import token_required


class GroupPayment(Resource):
    @swagger.doc(group_payments_delete_docs)
    @token_required(return_user=True)
    def delete(self, token_user_id, asset_id, group_payments_id):
        try:
            asset = AssetModel.objects.get(id=ObjectId(asset_id))
        except InvalidId:
            return make_response("Invalid asset ID", 400)
        except DoesNotExist as e:
            return make_response('Asset not found', 404)
        try:
            group_payment_obj = GroupPaymentModel.objects.get(id=ObjectId(group_payments_id))
            if token_user_id != group_payment_obj.owner:
                return make_response("Insufficient Permissions", 403)
            archive_group_payment(group_payment_obj)
            asset.group_payments.remove(group_payments_id)
            update(asset)
            return jsonify(archived_group_payment_id=str(group_payments_id))
        except InvalidId:
            return make_response("Invalid group payment ID", 400)
        except DoesNotExist as e:
            return make_response('Group payment not found', 404)
        except Exception as e:
            return make_response("Internal Server Error: {}".format(e.__str__()), 500)
