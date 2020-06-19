import json
import uuid
from datetime import date

from bson import ObjectId
from bson.errors import InvalidId
from flask import request, jsonify, make_response
from flask_restful_swagger_3 import Resource, swagger
from mongoengine import DoesNotExist
from werkzeug.utils import secure_filename

from app.adapters.db_adapter import update
from app.adapters.dropbox_adapter import DropBoxAdapter
from app.decorators.auth_decorators import token_required
from app.models.assetmodel import AssetModel
from app.resources.documents.documents_doc import document_post_doc
from app.settings import DBX_ACCESS_TOKEN


class Docs(Resource):
    @token_required(return_user=True)
    @swagger.doc(document_post_doc)
    def post(self, token_user_id, asset_id):
        try:
            data = json.loads(request.data)
            dbx_adapter = DropBoxAdapter(DBX_ACCESS_TOKEN)
            asset = AssetModel.objects.get(id=ObjectId(asset_id))
            if token_user_id != asset.owner_id:
                return make_response("Insufficient Permissions", 403)
            if not request.files:
                return make_response("Upload at least 1 file", 200)
            new_uuid = uuid.uuid4().hex
            for key, doc in request.files.items():
                dbx_filename = secure_filename(doc.filename)  # .rsplit(".", 1)[#]
                dbx_filepath = '/{}/{}'.format(asset_id, dbx_filename)  # dbx_filename can be changed to 'key'
                asset.documents.append({'doc_id': new_uuid,
                                        'doc_name': key,
                                        'url': dbx_adapter.upload_file(doc, dbx_filepath),
                                        'dbx_path': dbx_filepath,
                                        'creation_date': date.today().strftime('%d/%m/%Y'),
                                        'users': data['users']})
            update(asset)
            return jsonify({'document_url': asset.documents[new_uuid]['dbx_url'], 'document_uuid': new_uuid})
        except InvalidId:
            return make_response("Invalid asset ID", 400)
        except DoesNotExist:
            return make_response("Asset not found", 404)
        except Exception as e:
            return make_response("Internal Server Error: {}".format(e.__str__()), 500)
