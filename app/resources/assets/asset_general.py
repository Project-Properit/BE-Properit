import json
from json.decoder import JSONDecodeError

from flask import request, jsonify, make_response
from flask_restful_swagger_3 import Resource, swagger
from mongoengine import DoesNotExist

from app.adapters.db_adapter import insert, to_json
from app.decorators.auth_decorators import requires_auth
from app.models.assetmodel import Asset
from app.resources.assets.asset_docs import asset_post_doc, asset_get_filters_doc


class AssetGeneral(Resource):
    @swagger.doc(asset_get_filters_doc)
    def get(self):
        try:
            json_asset_list = []
            filters = request.args
            if filters:
                owner_id = filters['owner_id']
                user_asset_list = Asset.objects(owner=owner_id)
                for asset in user_asset_list:
                    json_asset_list.append(to_json(asset))
            else:
                for asset in Asset.objects():
                    json_asset_list.append(to_json(asset))
            if not json_asset_list:
                return make_response("Assets not found by input filters", 404)
            return json_asset_list
        except DoesNotExist:
            return make_response("Assets not found", 404)
        except Exception as e:
            return make_response("Internal Server Error: {}".format(e.__str__()), 500)

    @requires_auth
    @swagger.doc(asset_post_doc)
    def post(self):
        try:
            data = json.loads(request.data)
            new_asset = Asset(address=data['address'],
                              owner=data['owner'],
                              asset_type=data['asset_type'],
                              room_num=data['room_num'],
                              rent_fee=data['rent_fee'],
                              tenant_list=None,
                              promissory_note_url='',
                              comments=data['comments'])
            insert(new_asset)
            return jsonify({"new asset_id": str(new_asset.id)})
        except JSONDecodeError as e:
            return make_response("Invalid JSON: {}".format(e.__str__()), 400)
        except KeyError as e:
            return make_response("Missing / Invalid json key: {}".format(e.__str__()), 400)
        except Exception as e:
            return make_response("Internal Server Error: {}".format(e.__str__()), 500)
