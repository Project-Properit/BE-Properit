import json

from bson import ObjectId
from flask import request, jsonify
from flask_restful_swagger_3 import Resource, swagger

from app.adapters.db_adapter import insert, update, delete, to_json
from app.models.assetmodel import Asset
from app.resources.assets.asset_docs import asset_get_doc, asset_post_doc, asset_put_doc, asset_delete_doc, \
    asset_patch_tenants_doc


class NewAssetResource(Resource):
    # @requires_auth
    @swagger.doc(asset_post_doc)
    def post(self):
        data = json.loads(request.data)
        new_asset = Asset(address=data['address'],
                          owner=data['owner'],
                          asset_type=data['asset_type'],
                          room_num=data['room_num'],
                          rent_fee=data['rent_fee'],
                          tenant_list=None,
                          promissory=None,
                          comments=data['comments'])
        insert(new_asset)
        return jsonify({"new asset_id": str(new_asset.id)})


class ManageAssetResource(Resource):
    # @requires_auth
    @swagger.doc(asset_get_doc)
    def get(self, asset_id):
        asset = Asset.objects.get(id=ObjectId(asset_id))
        return to_json(asset)

    # @requires_auth
    @swagger.doc(asset_put_doc)
    def put(self, asset_id):
        asset = Asset.objects.get(id=ObjectId(asset_id))
        new_data = json.loads(request.data)
        # Todo: Think of better way to update each property
        asset.address = new_data['address']
        asset.owner = new_data['owner']
        asset.asset_type = new_data['asset_type']
        asset.room_num = new_data['room_num']
        asset.rent_fee = new_data['rent_fee']
        asset.comments = new_data['comments']
        update(asset)
        return jsonify({"updated asset_id": str(asset_id)})

    # @requires_auth
    @swagger.doc(asset_patch_tenants_doc)
    def patch_tenants(self, asset_id):
        asset = Asset.objects.get(id=ObjectId(asset_id))

        # Todo: Ask Daniel about patch tenants list & promissory note
        data = json.loads(request.data)
        asset.tenant_list = data['tenant_list']

        update(asset)

    # @requires_auth
    @swagger.doc(asset_delete_doc)
    def delete(self, asset_id):
        asset = Asset.objects.get(id=ObjectId(asset_id))
        delete(asset)
        return jsonify({"deleted asset_id": str(asset_id)})
