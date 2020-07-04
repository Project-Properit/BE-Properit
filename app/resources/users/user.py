import json
from json.decoder import JSONDecodeError

from bson import ObjectId
from bson.errors import InvalidId
from flask import jsonify, make_response, request
from flask_restful_swagger_3 import Resource, swagger
from mongoengine import DoesNotExist
from werkzeug.security import generate_password_hash

from app.adapters.db_adapter import update
from app.models.assetmodel import AssetModel
from app.models.usermodel import UserModel
from app.resources.users.user_docs import user_put_doc, user_get_invites_doc
from app.utils.auth_decorators import token_required
from app.utils.manipulator import get_user_by_filters


class User(Resource):
    @swagger.doc(user_get_invites_doc)
    @token_required(return_user=True)
    def put(self, token_user_id, user_id):
        try:
            if token_user_id != user_id:
                return make_response("Insufficient Permissions", 403)
            data = json.loads(request.data)
            user = UserModel.objects.get(id=ObjectId(user_id))
            for key, value in data.items():
                if key == 'password':
                    user[key] = generate_password_hash(value, method='sha256')
                    continue
                user[key] = value
            update(user)
            return jsonify(message='User update successfully')
        except InvalidId:
            return make_response("Invalid user ID", 400)
        except JSONDecodeError as e:
            return make_response("Invalid JSON: {}".format(e.__str__()), 400)
        except KeyError as e:
            return make_response("Missing / Invalid json key: {}".format(e.__str__()), 400)
        except DoesNotExist:
            return make_response("User not found", 404)
        except Exception as e:
            return make_response("Internal Server Error: {}".format(e.__str__()), 500)

    @swagger.doc(user_get_invites_doc)
    @token_required(return_user=True)
    def get(self, token_user_id, user_id):  # Todo: A.R.A.B
        try:
            if token_user_id != user_id:
                return make_response("Insufficient Permissions", 403)
            user_pending_invites = list()
            assets_obj = AssetModel.objects()
            for asset in assets_obj:
                if user_id in asset.pending_tenants:
                    user_pending_invites.append(dict(asset_id=str(asset.id),
                                                     asset_address=asset.address,
                                                     asset_owner=get_user_by_filters(dict(id=asset.owner))))
            return jsonify(user_pending_invites)
        except InvalidId:
            return make_response("Invalid user ID", 400)
        except JSONDecodeError as e:
            return make_response("Invalid JSON: {}".format(e.__str__()), 400)
        except KeyError as e:
            return make_response("Missing / Invalid json key: {}".format(e.__str__()), 400)
        except DoesNotExist:
            return make_response("User not found", 404)
        except Exception as e:
            return make_response("Internal Server Error: {}".format(e.__str__()), 500)

    @swagger.doc(user_get_invites_doc)
    @token_required(return_user=True)
    def patch(self, token_user_id, user_id):
        try:
            if token_user_id != user_id:
                return make_response("Insufficient Permissions", 403)
            data = json.loads(request.data)
            asset_id = data['asset_id']
            approved_asset = AssetModel.objects.get(id=ObjectId(asset_id))
            approved_asset.pending_tenants.remove(user_id)
            approved_asset.tenant_list.append(user_id)

            assets_obj = AssetModel.objects()
            for asset in assets_obj:
                if user_id in asset.pending_tenants:
                    asset.pending_tenants.remove(user_id)

            return jsonify(approved_asset=asset_id,
                           user_id=user_id)
        except InvalidId:
            return make_response("Invalid user ID", 400)
        except JSONDecodeError as e:
            return make_response("Invalid JSON: {}".format(e.__str__()), 400)
        except KeyError as e:
            return make_response("Missing / Invalid json key: {}".format(e.__str__()), 400)
        except DoesNotExist:
            return make_response("User not found", 404)
        except Exception as e:
            return make_response("Internal Server Error: {}".format(e.__str__()), 500)
