from flask import request, jsonify
from flask_restful_swagger_3 import Resource, swagger
from jwt import jwt

from app.adapters.db_adapter import insert
from app.decorators.auth_decorators import token_required
from app.models.tokenmodel import TokenModel
from app.resources.auth.auth_docs import logout_post_doc

token_manager = jwt.JWT()


class Logout(Resource):
    @swagger.doc(logout_post_doc)
    @token_required()
    def post(self):
        token = request.headers['x-access-tokens']
        expired_token = TokenModel(token=token)
        insert(expired_token)
        return jsonify({'message': 'logout successfully'})
