import json
import uuid
from datetime import datetime

from bson import ObjectId
from bson.errors import InvalidId
from flask import request, jsonify, make_response
from flask_restful_swagger_3 import Resource, swagger
from mongoengine import DoesNotExist
from werkzeug.utils import secure_filename

from app.adapters.db_adapter import update
from app.adapters.dropbox_adapter import DropBoxAdapter
from app.models.assetmodel import AssetModel
from app.resources.documents.documents_doc import document_post_doc
from app.settings import DBX_ACCESS_TOKEN
from app.utils.auth_decorators import token_required


class Docs(Resource):
    @token_required(return_user=True)
    @swagger.doc(document_post_doc)
    def patch(self, token_user_id, asset_id):
        try:
            uploaded_docs = list()
            asset = AssetModel.objects.get(id=ObjectId(asset_id))
            if token_user_id != asset.owner_id:
                return make_response("Insufficient Permissions", 403)
            if not request.files:
                return make_response("Upload at least 1 file", 200)

            permission = request.form['permission'].lower()
            dbx_adapter = DropBoxAdapter(DBX_ACCESS_TOKEN)
            for key, doc in request.files.items():  # Todo: Multi-select file upload (FE)
                new_uuid = uuid.uuid1().hex
                dbx_filename = secure_filename(doc.filename)  # .rsplit(".", 1)[#]
                dbx_filepath = '/{}/{}'.format(asset_id, dbx_filename)  # dbx_filename can be changed to 'key'
                url, preview_url = dbx_adapter.upload_file(doc, dbx_filepath)
                asset.documents.append({'doc_id': new_uuid,
                                        'doc_name': key,
                                        'url': url,
                                        'preview_url': preview_url,
                                        'dbx_path': dbx_filepath,
                                        'creation_date': datetime.now().replace(microsecond=0),
                                        'permission': permission})  # Todo: user permissions
                uploaded_docs.append(dict(url=url,
                                          preview_url=preview_url,
                                          doc_name=key,
                                          doc_id=new_uuid,
                                          permission=permission))
            update(asset)
            return jsonify(uploaded_docs)
        except InvalidId:
            return make_response("Invalid asset ID", 400)
        except DoesNotExist:
            return make_response("Asset not found", 404)
        except Exception as e:
            return make_response("Internal Server Error: {}".format(e.__str__()), 500)
