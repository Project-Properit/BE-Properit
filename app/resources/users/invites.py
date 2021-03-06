import json
from json.decoder import JSONDecodeError

from bson import ObjectId
from bson.errors import InvalidId
from flask import jsonify, make_response, request
from flask_restful_swagger_3 import Resource, swagger
from mongoengine import DoesNotExist

from app.adapters.db_adapter import update
from app.models.assetmodel import AssetModel
from app.resources.users.user_docs import user_in_path_doc, user_handle_invites_doc
from app.utils.auth_decorators import token_required
from app.utils.manipulator import get_user_by_filters


class UserInvites(Resource):
    @swagger.doc(user_in_path_doc)
    @token_required(return_user=True)
    def get(self, token_user_id, user_id):  # get all user's invites to assets
        try:
            if token_user_id != user_id:
                return make_response("Insufficient Permissions", 403)
            user_pending_invites = list()
            assets_obj = AssetModel.objects()
            for asset in assets_obj:
                if user_id in asset.pending_tenants:
                    user_pending_invites.append(dict(asset_id=str(asset.id),
                                                     asset_address=asset.address,
                                                     invite_date=asset.pending_tenants[user_id],
                                                     asset_owner=get_user_by_filters(dict(id=asset.owner_id))))
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

    @swagger.doc(user_handle_invites_doc)
    @token_required(return_user=True)
    def patch(self, token_user_id, user_id):  # accept invite to specific asset
        try:
            data = json.loads(request.data)
            asset_id = data['asset_id']
            asset_obj = AssetModel.objects.get(id=ObjectId(asset_id))
            if token_user_id != user_id:
                return make_response("Insufficient Permissions", 403)

            # check if user already tenant in other asset
            all_assets = AssetModel.objects()
            for asset in all_assets:
                if user_id in asset.tenant_list:
                    return make_response("You are already tenant in other asset", 404)

            if user_id in asset_obj.pending_tenants:
                del asset_obj.pending_tenants[user_id]
                asset_obj.tenant_list.append(user_id)
            else:
                return make_response("user not in pending invitations", 404)
            update(asset_obj)

            # remove user invites from other assets
            assets_obj = AssetModel.objects()
            for asset in assets_obj:
                if user_id in asset.pending_tenants:
                    del asset.pending_tenants[user_id]
                    update(asset_obj)

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

    @swagger.doc(user_handle_invites_doc)
    @token_required(return_user=True)
    def delete(self, token_user_id, user_id):  # decline asset invite
        try:
            data = json.loads(request.data)
            asset_id = data['asset_id']
            asset_obj = AssetModel.objects.get(id=ObjectId(asset_id))
            if token_user_id != user_id:
                return make_response("Insufficient Permissions", 403)
            if user_id in asset_obj.pending_tenants:
                del asset_obj.pending_tenants[user_id]
            else:
                return make_response("user not in pending invitations", 404)
            update(asset_obj)
            return jsonify(declined_asset=asset_id,
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
