import json

from bson import ObjectId
from bson.errors import InvalidId
from flask import request, make_response, jsonify
from flask_restful_swagger_3 import Resource, swagger
from mongoengine import DoesNotExist

from app.adapters.db_adapter import insert, update, to_json
from app.models.assetmodel import AssetModel
from app.models.grouppaymentsmodel import GroupPaymentsModel
from app.models.paymentmodel import PaymentModel
from app.resources.group_payments.group_payments_docs import groups_payments_post_docs, groups_payments_filter_get_docs
from app.utils.auth_decorators import token_required
from app.utils.data_manipulation import get_user_by_id, build_participants, sort_list_of_dicts


class GroupsPayments(Resource):
    @swagger.doc(groups_payments_post_docs)
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
            new_group_payments = GroupPaymentsModel(owner=data['owner'],
                                                    title=data['title'],
                                                    description=data['description'],
                                                    is_public=data['is_public'],
                                                    amount=data['amount'],
                                                    payments=data['payments'])
            group_payments = insert(new_group_payments)
            asset.group_payments.append(str(group_payments.id))
            update(asset)
            return jsonify({'group_payments_id': str(group_payments.id)})
        except Exception as e:
            return make_response("Internal Server Error: {}".format(e.__str__()), 500)

    @swagger.doc(groups_payments_filter_get_docs)
    @token_required(return_user=True)
    def get(self, token_user_id, asset_id):
        try:
            json_gp_list = []
            filters = request.args
            if filters:
                filter_dict = {k: v for k, v in filters.items()}
                gp_list = []

                if 'pay_from' in filter_dict:
                    pay_from_filter = filter_dict['pay_from']
                    payment_list = PaymentModel.objects(pay_from=pay_from_filter)

                    asset_group_payments_list = AssetModel.objects.get(id=asset_id)['group_payments']
                    for gp in asset_group_payments_list:
                        group_payment = GroupPaymentsModel.objects.get(id=ObjectId(gp))
                        for p in payment_list:
                            if str(p.id) in group_payment.payments:
                                gp_list.append(group_payment)

                    for gp in gp_list:
                        participants = []
                        filter_participants = []
                        final_obj = {}
                        for p in gp.payments:
                            payment = PaymentModel.objects.get(id=p)
                            participants.append(build_participants(payment))
                        if not gp.is_public:
                            for par in participants:
                                if pay_from_filter in str(par['id']):
                                    filter_participants.append(par)
                        if filter_participants:
                            sorted_participants = sort_list_of_dicts(filter_participants, pay_from_filter)
                        else:
                            sorted_participants = sort_list_of_dicts(participants, pay_from_filter)
                        final_obj['participants'] = sorted_participants
                        final_obj['title'] = gp.title
                        final_obj['description'] = gp.description
                        final_obj['owner'] = get_user_by_id(gp.owner)
                        final_obj['creation_time'] = str(gp.creation_date)
                        final_obj['id'] = str(gp.id)
                        json_gp_list.append(final_obj)
                    return json_gp_list

                if 'pay_to' in filter_dict:
                    pay_to_filter = filter_dict['pay_to']
                    asset_group_payments_list = AssetModel.objects.get(id=asset_id)['group_payments']
                    group_payment_list = []
                    for gp in asset_group_payments_list:
                        group_payment_list.append(GroupPaymentsModel.objects.get(id=ObjectId(gp)))
                    for gp in group_payment_list:
                        participants = []
                        final_obj = {}
                        if gp.owner in pay_to_filter:
                            for p in gp.payments:
                                payment = PaymentModel.objects.get(id=p)
                                participants.append(build_participants(payment))
                            sorted_participants = sort_list_of_dicts(participants, pay_to_filter)
                            final_obj['participants'] = sorted_participants
                            final_obj['title'] = gp.title
                            final_obj['description'] = gp.description
                            final_obj['owner'] = get_user_by_id(gp.owner)
                            final_obj['creation_time'] = str(gp.creation_date)
                            final_obj['id'] = str(gp.id)
                            json_gp_list.append(final_obj)
                    return json_gp_list
            else:
                for gp in GroupPaymentsModel.objects():
                    json_gp_list.append(to_json(gp))
            if not json_gp_list:
                return make_response("No group payment found by filters", 404)
            return json_gp_list
        except DoesNotExist:
            return make_response("No payments available", 404)
        except Exception as e:
            return make_response("Internal Server Error: {}".format(e.__str__()), 500)

    # @swagger.doc(groups_payments_get_docs)
    # @token_required(return_user=True)
    # def get(self, token_user_id, asset_id):
    #     try:
    #         asset = AssetModel.objects.get(id=ObjectId(asset_id))
    #     except InvalidId:
    #         return make_response("Invalid asset ID", 400)
    #     except DoesNotExist as e:
    #         return make_response('Asset not found', 404)
    #     try:
    #         if token_user_id not in asset.tenant_list and token_user_id != asset.owner_id:
    #             return make_response("Insufficient Permissions", 403)
    #         return jsonify(asset.group_payments)
    #     except Exception as e:
    #         return make_response("Internal Server Error: {}".format(e.__str__()), 500)
