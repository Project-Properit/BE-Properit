from flask import jsonify
from flask_restful_swagger_3 import Resource

from app.decorators.auth_decorators import token_required
from app.models.user import User


class Users(Resource):
    @token_required
    def get(self, current_user):
        users = User.objects
        result = []
        for user in users:
            user_data = {'name': user.email, 'password': user.password, 'admin': user.admin}
            result.append(user_data)
        return jsonify({'auth': result})
