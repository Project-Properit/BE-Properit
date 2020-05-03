import json

from bson import ObjectId
from flask import request, jsonify
from flask_restful_swagger_3 import Resource, swagger

from app.adapters.db_adapter import update
from app.decorators.auth_decorators import requires_auth
from app.models.assetmodel import Asset
from app.resources.assets.asset_docs import asset_put_doc


class UpdateAssetResource(Resource):
    @requires_auth
    @swagger.doc(asset_put_doc)
    def put(self, asset_id):
        asset = Asset.objects.get(id=ObjectId(asset_id))
        new_data = json.loads(request.data)
        asset.address = new_data['address']
        asset.owner = new_data['owner']
        asset.asset_type = new_data['asset_type']
        asset.room_num = new_data['room_num']
        asset.rent_fee = new_data['rent_fee']
        asset.comments = new_data['comments']
        update(asset)
        return jsonify({"updated asset_id": str(asset_id)})
