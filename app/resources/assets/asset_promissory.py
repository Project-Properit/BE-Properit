from bson import ObjectId
from flask import request, jsonify
from flask_restful_swagger_3 import Resource, swagger

from app.adapters.db_adapter import update
from app.adapters.dropbox_adapter import DropboxAdapter
from app.models.assetmodel import Asset
from app.resources.assets.asset_docs import asset_patch_promissory_doc
from app.settings import DBX_ACCESS_TOKEN


class AssetPromissory(Resource):
    # @requires_auth
    @swagger.doc(asset_patch_promissory_doc)
    def patch(self, asset_id):
        asset = Asset.objects.get(id=ObjectId(asset_id))
        promissory_file = request.files['promissory']
        # modified_filename = secure_filename(promissory_file.filename)  # Todo: use it .rsplit(".", 1)[1]
        dbx_adapter = DropboxAdapter(DBX_ACCESS_TOKEN)
        # dbx_filepath = '/{}/promissory_note.pdf'.format(asset_id)
        dbx_filepath = '/{}/asd'.format(asset_id)  # Todo: get file suffix by the filename split by "."
        if dbx_adapter.check_file_existence(dbx_filepath):
            asset.promissory_note_url = dbx_adapter.update_file(promissory_file.read(), dbx_filepath)
        else:
            asset.promissory_note_url = dbx_adapter.upload_file(promissory_file.read(), dbx_filepath)
        update(asset)
        return jsonify({"promissory note url:": asset.promissory_note_url})
