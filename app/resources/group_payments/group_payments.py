import json

from bson import ObjectId
from bson.errors import InvalidId
from flask import request, make_response, jsonify
from flask_restful_swagger_3 import Resource, swagger
from mongoengine import DoesNotExist

from app.adapters.db_adapter import insert, update, to_json
from app.models.assetmodel import AssetModel
from app.models.grouppaymentmodel import GroupPaymentModel
from app.models.paymentmodel import PaymentModel
from app.resources.group_payments.group_payment_docs import group_payments_post_docs, group_payments_filter_get_docs
from app.utils.auth_decorators import token_required
from app.utils.data_manipulation import build_participants_obj, sort_group_payments, \
    sort_participants, get_user_payment, build_gp_object, check_user_in_participants


class GroupPayments(Resource):
    @swagger.doc(group_payments_post_docs)
    @token_required(return_user=True)
    def post(self, token_user_id, asset_id):
        try:
            asset = AssetModel.objects.get(id=ObjectId(asset_id))
        except InvalidId:
            return make_response("Invalid asset ID", 400)
        except DoesNotExist as e:
            return make_response('Asset not found', 404)
        try:
            if token_user_id not in asset.tenant_list and token_user_id != asset.owner_id:
                return make_response("Insufficient Permissions", 403)
            data = json.loads(request.data)
            new_group_payment = GroupPaymentModel(owner=token_user_id,
                                                  title=data['title'],
                                                  description=data['description'],
                                                  is_public=data['is_public'],
                                                  amount=data['amount'],
                                                  payments=data['payments'])
            group_payment = insert(new_group_payment)
            asset.group_payments.append(str(group_payment.id))
            update(asset)
            return jsonify(group_payment_id=str(group_payment.id))
        except Exception as e:
            return make_response("Internal Server Error: {}".format(e.__str__()), 500)

    @swagger.doc(group_payments_filter_get_docs)
    @token_required(return_user=True)
    def get(self, token_user_id, asset_id):
        try:
            asset_obj = AssetModel.objects.get(id=asset_id)
            if token_user_id not in asset_obj.tenant_list and token_user_id != asset_obj.owner_id:
                return make_response("Insufficient Permissions", 403)
            gp_list = list()
            filters = request.args
            if filters:
                if filters.__len__() > 1:
                    return make_response("Only one filter", 400)
                filter_key, filter_value = next(iter(filters.items()))
                asset_gp_list = asset_obj['group_payments']

                for gp_id in asset_gp_list:
                    my_payment = None
                    participants = list()
                    gp_obj = GroupPaymentModel.objects.get(id=ObjectId(gp_id))
                    gp_payment_list = gp_obj.payments
                    for payment_id in gp_payment_list:
                        payment_obj = PaymentModel.objects.get(id=ObjectId(payment_id))
                        participants.append(build_participants_obj(payment_obj))

                    if check_user_in_participants(participants, filter_value):  # == pay_from filter used
                        my_payment = get_user_payment(participants, filter_value)
                        if not gp_obj.is_public:
                            participants.clear()
                    sort_participants(participants, filter_value)

                    new_gp_obj = build_gp_object(gp_obj, participants, my_payment)
                    gp_list.append(new_gp_obj)
                sort_group_payments(gp_list, filter_key, filter_value)

            else:
                for gp in GroupPaymentModel.objects():
                    gp_list.append(to_json(gp))
            if not gp_list:
                return make_response("No group payment found by filters", 404)

            return jsonify(gp_list)

        except DoesNotExist:
            return make_response("No payments available", 404)
        except Exception as e:
            return make_response("Internal Server Error: {}".format(e.__str__()), 500)
