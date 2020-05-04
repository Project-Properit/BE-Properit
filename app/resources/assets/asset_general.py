import json

from bson import ObjectId
from flask import request, jsonify
from flask_restful_swagger_3 import Resource, swagger

from app.adapters.db_adapter import update, delete, to_json
from app.decorators.auth_decorators import requires_auth
from app.models.assetmodel import Asset
from app.resources.assets.asset_docs import asset_get_by_assetId_doc, asset_put_doc, asset_delete_doc


class AssetGeneral(Resource):
    @requires_auth
    @swagger.doc(asset_get_by_assetId_doc)
    def get(self, asset_id):
        asset = Asset.objects.get(id=ObjectId(asset_id))
        return to_json(asset)

    @requires_auth
    @swagger.doc(asset_put_doc)
    def put(self, asset_id):
        asset = Asset.objects.get(id=ObjectId(asset_id))
        data = json.loads(request.data)
        # Todo: Think of better way to update each property
        asset.address = data['address']
        asset.owner = data['owner']
        asset.asset_type = data['asset_type']
        asset.room_num = data['room_num']
        asset.rent_fee = data['rent_fee']
        asset.comments = data['comments']
        update(asset)
        return jsonify({"updated asset_id": str(asset_id)})

    @requires_auth
    @swagger.doc(asset_delete_doc)
    def delete(self, asset_id):
        asset = Asset.objects.get(id=ObjectId(asset_id))
        delete(asset)
        return jsonify({"deleted asset_id": str(asset_id)})
