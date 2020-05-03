from bson import ObjectId
from flask import jsonify
from flask_restful_swagger_3 import Resource, swagger

from app.decorators.auth_decorators import token_required
from app.models.usermodel import UserModel
from app.resources.users.user_docs import user_get_doc


class User(Resource):
    @swagger.doc(user_get_doc)
    @token_required
    def get(self, user_id):
        user = UserModel.objects.get(id=ObjectId(user_id))
        return jsonify({'first_name': user.first_name, 'last_name': user.last_name, 'phone': user.phone, 'email': user.email})
