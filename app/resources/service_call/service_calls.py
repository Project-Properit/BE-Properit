# import json
#
# from bson import ObjectId
# from bson.errors import InvalidId
# from flask import request, make_response, jsonify
# from flask_restful_swagger_3 import Resource, swagger
# from mongoengine import DoesNotExist
#
# from app.adapters.db_adapter import insert, update, to_json
# from app.models.assetmodel import AssetModel
# from app.models.servicecallmodel import ServiceCallModel
# from app.resources.service_call.service_call_docs import sc_post_docs, sc_get_filters_doc
# from app.utils.auth_decorators import token_required
#
#
# class ServiceCalls(Resource):
#     @swagger.doc(sc_post_docs)
#     @token_required(return_user=True)
#     def post(self, token_user_id, asset_id):
#         try:
#             asset = AssetModel.objects.get(id=ObjectId(asset_id))
#         except InvalidId:
#             return make_response("Invalid asset ID", 400)
#         except DoesNotExist as e:
#             return make_response('Asset not found', 404)
#         try:
#             if token_user_id not in asset.tenant_list and token_user_id != asset.owner_id:
#                 return make_response("Insufficient Permissions", 403)
#             data = json.loads(request.data)
#             new_service_call = ServiceCallModel(name=data['name'],
#                                                 company=data['company'],
#                                                 phone=data['phone'],
#                                                 price=data['price'],
#                                                 arrival_date=data['arrival_date'],
#                                                 is_closed=False,
#                                                 group_payment_id=data['group_payment_id'])
#             service_call = insert(new_service_call)
#             asset.service_calls.append(str(service_call.id))
#             update(asset)
#             return jsonify({'service_call_id': str(service_call.id)})
#         except Exception as e:
#             return make_response("Internal Server Error: {}".format(e.__str__()), 500)
#
#     # @swagger.doc(sc_get_filters_doc)
#     # def get(self, asset_id):
#     #     try:
#     #         json_service_call_list = list()
#     #         filters = request.args
#     #         if filters:
#     #             filter_dict = {k: v for k, v in filters.items()}
#     #             service_call_list = ServiceCallModel.objects(**filter_dict)
#     #             for sc in service_call_list:
#     #                 json_service_call_list.append(to_json(sc))
#     #         else:
#     #             for sc in ServiceCallModel.objects():
#     #                 json_service_call_list.append(to_json(sc))

#     #         return json_service_call_list
#     #     except DoesNotExist:
#     #         return make_response("No assets available", 404)
#     #     except Exception as e:
#     #         return make_response("Internal Server Error: {}".format(e.__str__()), 500)
