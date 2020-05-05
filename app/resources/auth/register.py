import json

from flask import request, make_response
from flask_restful_swagger_3 import Resource, swagger
from jwt import jwt
from mongoengine import NotUniqueError
from werkzeug.security import generate_password_hash

from app.adapters.db_adapter import insert
from app.models.usermodel import UserModel
from app.resources.auth.auth_docs import register_post_doc

token_manager = jwt.JWT()


class Register(Resource):
    @swagger.doc(register_post_doc)
    def post(self):
        data = json.loads(request.data)
        hashed_password = generate_password_hash(data['password'], method='sha256')
        new_user = UserModel(email=data['email'], password=hashed_password, phone=data['phone'],
                             first_name=data['first_name'], last_name=data['last_name'])
        try:
            insert(new_user)
        except NotUniqueError as e:
            return make_response('User already exist.', 409)
