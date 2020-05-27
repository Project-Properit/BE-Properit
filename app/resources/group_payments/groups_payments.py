import json

from bson import ObjectId
from bson.errors import InvalidId
from flask import request, make_response, jsonify
from flask_restful_swagger_3 import Resource, swagger
from mongoengine import DoesNotExist

from app.adapters.db_adapter import insert, update, to_json
from app.decorators.auth_decorators import token_required
from app.models.assetmodel import Asset
from app.models.grouppaymentsmodel import GroupPaymentsModel
from app.resources.group_payments.groups_payments_docs import groups_payments_post_docs, groups_payments_get_docs


class GroupsPayments(Resource):
    @swagger.doc(groups_payments_post_docs)
    @token_required(return_user=True)
    def post(self, token_user_id, asset_id):
        try:
            asset = Asset.objects.get(id=ObjectId(asset_id))
        except InvalidId:
            return make_response("Invalid asset ID", 400)
        except DoesNotExist as e:
            return make_response('Asset not found', 404)
        try:
            if token_user_id not in asset.tenant_list and token_user_id != asset.owner_id:
                return make_response("Insufficient Permissions", 403)
            data = json.loads(request.data)
            new_group_payments = GroupPaymentsModel(title=data['title'], description=data['description'],
                                                    amount=data['amount'], payments=[])
            group_payments = insert(new_group_payments)
            asset.group_payments.append(str(group_payments.id))
            update(asset)
            return jsonify({'group_payments_id': str(group_payments.id)})
        except Exception as e:
            return make_response("Internal Server Error: {}".format(e.__str__()), 500)

    @swagger.doc(groups_payments_get_docs)
    @token_required(return_user=True)
    def get(self, token_user_id, asset_id):
        try:
            asset = Asset.objects.get(id=ObjectId(asset_id))
        except InvalidId:
            return make_response("Invalid asset ID", 400)
        except DoesNotExist as e:
            return make_response('Asset not found', 404)
        try:
            if token_user_id not in asset.tenant_list and token_user_id != asset.owner_id:
                return make_response("Insufficient Permissions", 403)
            return jsonify([to_json(GroupPaymentsModel.objects.get(id=ObjectId(group_payments))) for group_payments in
                            asset.group_payments])
        except Exception as e:
            return make_response("Internal Server Error: {}".format(e.__str__()), 500)