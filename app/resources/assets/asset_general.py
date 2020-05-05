import json

from flask import request, jsonify
from flask_restful_swagger_3 import Resource, swagger

from app.adapters.db_adapter import insert, to_json
from app.decorators.auth_decorators import requires_auth
from app.models.assetmodel import Asset
from app.resources.assets.asset_docs import asset_post_doc, asset_get_filters_doc


class AssetGeneral(Resource):
    @swagger.doc(asset_get_filters_doc)
    def get(self):
        json_asset_list = []
        filters = request.args
        if filters:
            owner_id = filters['owner_id']
            user_asset_list = Asset.objects(owner=owner_id)
            for asset in user_asset_list:
                json_asset_list.append(to_json(asset))
        else:
            for asset in Asset.objects():
                json_asset_list.append(to_json(asset))
        return json_asset_list

    @requires_auth
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
