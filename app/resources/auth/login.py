from datetime import datetime, timedelta, timezone

from flask import request, jsonify, make_response
from flask_restful_swagger_3 import Resource, swagger
from jwt import jwt
from jwt.jwk import OctetJWK
from mongoengine import DoesNotExist
from werkzeug.security import check_password_hash

from app.models.usermodel import UserModel
from app.resources.auth.auth_docs import login_get_doc
from app.settings import APP_SECRET_KEY
from app.utils.auth_decorators import requires_auth
from app.utils.manipulator import get_user_asset_as_tenant

token_manager = jwt.JWT()
THREE_HOURS = 60 * 3


class Login(Resource):
    @requires_auth
    @swagger.doc(login_get_doc)
    def get(self):
        try:
            auth = request.authorization
            user = UserModel.objects.get(email=auth.username.lower())
            tenant_asset_id = get_user_asset_as_tenant(user)
            if check_password_hash(user.password, auth.password):
                expiration_time = datetime.now(timezone.utc) + timedelta(minutes=THREE_HOURS)
                token = token_manager.encode(
                    {'id': str(user.id), 'exp': int(expiration_time.timestamp())},
                    OctetJWK(APP_SECRET_KEY))
                return jsonify(token=token,
                               user_id=str(user.id),
                               first_name=user.first_name,
                               last_name=user.last_name,
                               is_tenant=user.is_tenant,
                               is_owner=user.is_owner,
                               tenant_asset_id=tenant_asset_id)
            return make_response('Wrong credentials', 401)
        except DoesNotExist:
            return make_response('User not registered', 404)
        except Exception as e:
            return make_response("Internal Server Error: {}".format(e.__str__()), 500)
