import json

from bson import ObjectId
from flask import jsonify, make_response, request
from flask_restful_swagger_3 import Resource, swagger
from mongoengine import DoesNotExist

from app.adapters.db_adapter import update
from app.decorators.auth_decorators import token_required
from app.models.usermodel import UserModel
from app.resources.users.user_docs import user_get_doc, user_put_doc


class User(Resource):
    @swagger.doc(user_get_doc)
    @token_required()
    def get(self, user_id):
        try:
            user = UserModel.objects.get(id=ObjectId(user_id))
            return jsonify(
                {'first_name': user.first_name, 'last_name': user.last_name, 'phone': user.phone, 'email': user.email})
        except DoesNotExist as e:
            return make_response('User not found', 404)

    @swagger.doc(user_put_doc)
    @token_required(return_user=True)
    def put(self, token_user_id, user_id):
        if user_id == token_user_id:
            data = json.loads(request.data)
            user = UserModel.objects.get(id=ObjectId(user_id))
            for value, key in data.items():
                user[value] = key
            update(user)
            return jsonify({'message': 'User update successfully'})
        else:
            return make_response('Wrong UserId', 400)
