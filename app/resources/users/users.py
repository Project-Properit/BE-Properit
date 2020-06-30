from bson.errors import InvalidId
from flask import jsonify, make_response, request
from flask_restful_swagger_3 import Resource, swagger
from mongoengine import DoesNotExist

from app.adapters.db_adapter import to_json
from app.models.usermodel import UserModel
from app.resources.users.user_docs import user_get_filters_doc
from app.utils.auth_decorators import token_required


class Users(Resource):
    @swagger.doc(user_get_filters_doc)
    @token_required()  # Todo: admin token ?
    def get(self):
        try:
            users_list = list()
            filters = request.args
            if filters:
                filter_dict = {k: v for k, v in filters.items()}
                user_obj_list = UserModel.objects(**filter_dict)
            else:
                user_obj_list = UserModel.objects()
            for user in user_obj_list:
                users_list.append(to_json(user))
            if not users_list:
                return make_response("No users found by filters", 200)
            return jsonify(users_list)
        except InvalidId:
            return make_response("Invalid user ID", 400)
        except DoesNotExist as e:
            return make_response('User not found', 404)
        except Exception as e:
            return make_response("Internal Server Error: {}".format(e.__str__()), 500)
