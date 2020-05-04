import json

from flask import request, jsonify
from flask_restful_swagger_3 import Resource, swagger

from app.adapters.db_adapter import insert
from app.models.assetmodel import Asset
from app.resources.assets.asset_docs import asset_post_doc


class NewAsset(Resource):
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
                          promissory_note_url='',
                          comments=data['comments'])
        insert(new_asset)
        return jsonify({"new asset_id": str(new_asset.id)})
