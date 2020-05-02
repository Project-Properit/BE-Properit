from flask import request, make_response, jsonify
from flask_restful_swagger_3 import Resource
from jwt import jwt

from app.decorators.tokens_tools import token_required
from app.models.user import LogoutToken, save

token_manager = jwt.JWT()


class Logout(Resource):
    # @swagger.doc()
    @token_required
    def post(self, current_user):
        token = request.headers['x-access-tokens']
        expired_token = LogoutToken(token=token)
        save(expired_token)
        return jsonify({'message': 'logout successfully'})
