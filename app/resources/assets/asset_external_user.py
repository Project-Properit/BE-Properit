from flask_restful_swagger_3 import Resource, swagger

from app.adapters.db_adapter import to_json
from app.models.assetmodel import Asset
from app.resources.assets.asset_docs import asset_get_by_userId_doc


class AssetExternalUser(Resource):
    @swagger.doc(asset_get_by_userId_doc)
    def get(self, user_id):
        json_asset_list = []
        user_asset_list = Asset.objects(owner=user_id)
        for asset in user_asset_list:
            json_asset_list.append(to_json(asset))
        return json_asset_list
