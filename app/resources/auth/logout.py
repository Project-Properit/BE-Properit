from flask import request, jsonify, make_response
from flask_restful_swagger_3 import Resource, swagger
from jwt import jwt

from app.adapters.db_adapter import insert
from app.models.tokenmodel import TokenModel
from app.resources.auth.auth_docs import logout_post_doc
from app.utils.auth_decorators import token_required

token_manager = jwt.JWT()


class Logout(Resource):
    @swagger.doc(logout_post_doc)
    @token_required()
    def post(self):
        try:
            token = request.headers['x-access-tokens']
            expired_token = TokenModel(token=token)
            insert(expired_token)
            return jsonify(message='user logged out successfully')
        except Exception as e:
            return make_response("Internal Server Error: {}".format(e.__str__()), 500)
