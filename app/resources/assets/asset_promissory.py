import json

from bson import ObjectId
from flask import request, jsonify
from flask_restful_swagger_3 import Resource, swagger

from app.adapters.db_adapter import update, to_json
from app.models.assetmodel import Asset
from app.resources.assets.asset_docs import asset_patch_promissory_doc


class AssetPromissory(Resource):
    # @requires_auth
    @swagger.doc(asset_patch_promissory_doc)
    def patch(self, asset_id):
        # Todo: upload file S3 and save its usage url to mongo
        # Todo: check if url contains uniq substring
        # asset = Asset.objects.get(id=ObjectId(asset_id))
        #
        # update(asset)
        return jsonify({"patched asset_id": str(asset_id)})
