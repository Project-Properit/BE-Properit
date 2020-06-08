import json
from json.decoder import JSONDecodeError

from flask import request, jsonify, make_response
from flask_restful_swagger_3 import Resource, swagger
from mongoengine import DoesNotExist

from app.adapters.db_adapter import insert, to_json
from app.decorators.auth_decorators import token_required
from app.models.assetmodel import AssetModel
from app.resources.assets.asset_docs import asset_post_doc, asset_get_filters_doc


class Assets(Resource):
    @token_required()
    @swagger.doc(asset_get_filters_doc)
    def get(self):
        try:
            json_asset_list = []
            filters = request.args
            if filters:
                filter_dict = {k: v for k, v in filters.items()}
                asset_list = AssetModel.objects(**filter_dict)
                for asset in asset_list:
                    json_asset_list.append(to_json(asset))
            else:
                for asset in AssetModel.objects():
                    json_asset_list.append(to_json(asset))
            # if not json_asset_list:
            #     return make_response("No assets found by filters", 200)
            return json_asset_list
        except DoesNotExist:
            return make_response("No assets available", 404)
        except Exception as e:
            return make_response("Internal Server Error: {}".format(e.__str__()), 500)

    @token_required()
    @swagger.doc(asset_post_doc)
    def post(self):
        try:
            data = json.loads(request.data)
            new_asset = AssetModel(owner_id=data['owner_id'],
                                   address=data['address'],
                                   asset_type=data['asset_type'],
                                   room_num=data['room_num'],
                                   rent_fee=data['rent_fee'],
                                   tenant_list=data['tenant_list'],
                                   documents={},
                                   group_payments=[],
                                   comments=data['comments'])
            insert(new_asset)
            return jsonify({"new asset_id": str(new_asset.id)})
        except JSONDecodeError as e:
            return make_response("Invalid JSON: {}".format(e.__str__()), 400)
        except KeyError as e:
            return make_response("Missing / Invalid json key: {}".format(e.__str__()), 400)
        except Exception as e:
            return make_response("Internal Server Error: {}".format(e.__str__()), 500)
