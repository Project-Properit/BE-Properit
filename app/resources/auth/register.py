import json
from json.decoder import JSONDecodeError

from flask import request, make_response, jsonify
from flask_restful_swagger_3 import Resource, swagger
from jwt import jwt
from mongoengine import NotUniqueError, ValidationError
from werkzeug.security import generate_password_hash

from app.adapters.db_adapter import insert
from app.models.usermodel import UserModel
from app.resources.auth.auth_docs import register_post_doc

token_manager = jwt.JWT()


class Register(Resource):
    @swagger.doc(register_post_doc)
    def post(self):
        try:
            data = json.loads(request.data)
            hashed_password = generate_password_hash(data['password'], method='sha256')
            new_user = UserModel(email=data['email'],
                                 password=hashed_password,
                                 phone=data['phone'],
                                 first_name=data['first_name'],
                                 last_name=data['last_name'],
                                 payment_details=data['payment_details'],
                                 is_tenant=data['is_tenant'],
                                 is_owner=data['is_owner'])
            new_user_id = insert(new_user)
            return jsonify(user_id=new_user_id)
        except NotUniqueError:
            return make_response('User already exist.', 409)
        except JSONDecodeError as e:
            return make_response("Invalid JSON: {}".format(e.__str__()), 400)
        except KeyError as e:
            return make_response("Missing / Invalid json key: {}".format(e.__str__()), 400)
        except ValidationError as e:
            return make_response("Invalid json parameters: {}".format(e.__str__()), 400)
        except Exception as e:
            return make_response("Internal Server Error: {}".format(e.__str__()), 500)
