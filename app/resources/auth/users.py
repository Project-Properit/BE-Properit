from flask import jsonify
from flask_restful_swagger_3 import Resource

from app.decorators.tokens_tools import token_required
from app.models.user import User


class Users(Resource):
    @token_required
    def get(self, current_user):
        users = User.query.all()
        result = []
        for user in users:
            user_data = {'name': user.name, 'password': user.password, 'admin': user.admin}
            result.append(user_data)
        return jsonify({'auth': result})
