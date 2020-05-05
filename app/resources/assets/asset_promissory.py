import boto3
from botocore.config import Config
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
        aws_key = 'assets/{}/promissory_note'.format(asset_id)
        s3 = boto3.resource('s3',
                            aws_access_key_id='ASIAQK5OE254CXRP7N6J',
                            aws_secret_access_key='iOWIQM1bsLkLM2p+ZGBgHdW0ArE8kg5OtN/F7WAO',
                            aws_session_token='FwoGZXIvYXdzEG0aDM1eXHogmJ7Sp0oGXSLGAbeekaOHSY3Mw+8NP7Ewa3+P5a9A3C65jOFq/rIL0SWXtLtAPwHsFLw3qRHl/EmV9e8B7JY0Z1WHZ5APjXgY0VjSAOj7qSNKsvuUuPM0bUtKYy4sLjvIHf0OohzZv+wn/AsGx1WPPd9PUKenPl50t4JNgi9SLeSSou5qFRfjQaPqgVFeMm4Ff96oX/ZcVhBUHsDu/ix8AW/clzOUG6WgLypaIK24zNS9CsSIFIoJxX10spbeSinibC7AJIft9jLse2jTnaJJWCi6+8b1BTItPiyklrQnHxzLv8i2dyfoqWUqOI0rE/S3e6DYjnML9ICGQZhzg6gIyzrjBSwg',
                            config=Config(signature_version='s3v4'))

        s3.Bucket(BUCKET_NAME).put_object(Key=aws_key,
                                          Body=promissory_file,
                                          ContentDisposition="inline",
                                          ContentType="application/pdf",
                                          ACL='public-read')
        
        asset.promissory_note_url = 'https://{}.s3.amazonaws.com/{}'.format(BUCKET_NAME, aws_key)
        update(asset)
        return jsonify({"promissory note url:": asset.promissory_note_url})
