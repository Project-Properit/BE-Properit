import json

from bson import ObjectId
from flask import request, jsonify
from flask_restful_swagger_3 import Resource, swagger

from app.adapters.db_adapter import update
from app.decorators.auth_decorators import requires_auth
from app.models.assetmodel import Asset
from app.resources.assets.asset_docs import asset_patch_tenants_doc


class AssetTenants(Resource):
    @requires_auth
    @swagger.doc(asset_patch_tenants_doc)
    def patch(self, asset_id):
        asset = Asset.objects.get(id=ObjectId(asset_id))
        data = json.loads(request.data)
        if data['tenant_list']:
            asset.tenant_list = data['tenant_list']
        update(asset)
        return jsonify({"patched asset_id": str(asset_id)})
