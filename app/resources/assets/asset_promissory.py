import boto3
from bson import ObjectId
from flask import request, jsonify
from flask_restful_swagger_3 import Resource, swagger

from app.adapters.db_adapter import update
from app.models.assetmodel import Asset
from app.resources.assets.asset_docs import asset_patch_promissory_doc
from app.settings import BUCKET_NAME


class AssetPromissory(Resource):
    # @requires_auth
    @swagger.doc(asset_patch_promissory_doc)
    def patch(self, asset_id):
        asset = Asset.objects.get(id=ObjectId(asset_id))
        promissory_file = request.files['promissory']
        # modified_filename = secure_filename(promissory_file.filename)
        aws_key = '{}/promissory_note'.format(asset_id)
        s3 = boto3.resource('s3')

        s3.Bucket(BUCKET_NAME).put_object(Key=aws_key,
                                          Body=promissory_file,
                                          ContentDisposition="inline",
                                          ContentType="application/pdf",
                                          ACL='public-read')
        asset.promissory_note_url = 'https://{}.s3.amazonaws.com/{}'.format(BUCKET_NAME, aws_key)
        update(asset)
        return jsonify({"promissory note url:": asset.promissory_note_url})
