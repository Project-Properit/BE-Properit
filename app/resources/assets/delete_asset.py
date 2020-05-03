import json

from bson import ObjectId
from flask import request, jsonify
from flask_restful_swagger_3 import Resource, swagger

from app.adapters.db_adapter import delete
from app.decorators.auth_decorators import requires_auth
from app.models.assetmodel import Asset
from app.resources.assets.asset_docs import asset_delete_doc


class DeleteAssetResource(Resource):
    @requires_auth
    @swagger.doc(asset_delete_doc)
    def delete(self, asset_id):
        asset = Asset.objects.get(id=ObjectId(asset_id))
        delete(asset)
        return jsonify({"deleted asset_id": str(asset_id)})
