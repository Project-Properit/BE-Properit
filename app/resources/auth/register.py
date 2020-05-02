import json
import uuid

from flask import request, jsonify
from flask_restful_swagger_3 import Resource
from jwt import jwt
from werkzeug.security import generate_password_hash

from app.models.user import save, User

token_manager = jwt.JWT()


class Register(Resource):
    # @swagger.doc()
    def post(self):
        data = json.loads(request.data)
        hashed_password = generate_password_hash(data['password'], method='sha256')
        new_user = User(name=data['name'], password=hashed_password,
                        admin=False, email=data['email'], phone=data['phone'], first_name=data['first_name'],
                        last_name=data['last_name'])
        save(new_user)
        return jsonify({'message': 'registered successfully'})
