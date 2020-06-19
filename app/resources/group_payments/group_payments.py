import json
from json import JSONDecodeError

from bson import ObjectId
from bson.errors import InvalidId
from flask import make_response, jsonify, request
from flask_restful_swagger_3 import Resource, swagger
from mongoengine import DoesNotExist, ValidationError

from app.adapters.db_adapter import delete, update
from app.decorators.auth_decorators import token_required
from app.models.assetmodel import AssetModel
from app.models.grouppaymentsmodel import GroupPaymentsModel
from app.models.paymentmodel import PaymentModel
from app.models.usermodel import UserModel
from app.resources.group_payments.group_payments_docs import group_payments_get_docs, group_payments_put_doc


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

            # ##
            payments_list = []
            if group_payments.payments:
                for payment_id in group_payments.payments:
                    payment = PaymentModel.objects.get(id=ObjectId(payment_id))
                    user_from = UserModel.objects.get(id=ObjectId(payment.pay_from))
                    user_to = UserModel.objects.get(id=ObjectId(payment.pay_to))
                    payments_list.append({'id': str(payment.id),
                                          'pay_from': {'first_name': user_from.first_name,
                                                       'last_name': user_from.last_name},
                                          'pay_to': {'first_name': user_to.first_name,
                                                     'last_name': user_to.last_name},
                                          'amount': payment.amount,
                                          'method': payment.method,
                                          'status': payment.status})
            # ##

            return jsonify(
                dict(title=group_payments.title, description=group_payments.description, amount=group_payments.amount,
                     payments=payments_list))
        except InvalidId:
            return make_response("Invalid group payments ID", 400)
        except DoesNotExist as e:
            return make_response('Group payments not found', 404)
        except Exception as e:
            return make_response("Internal Server Error: {}".format(e.__str__()), 500)

    @token_required(return_user=True)
    @swagger.doc(group_payments_put_doc)
    def put(self, token_user_id, asset_id, group_payments_id):
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
            data = json.loads(request.data)
            for value, key in data.items():
                group_payments[value] = key
            update(group_payments)
            return jsonify({"updated group_payments_id": str(group_payments_id)})
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
