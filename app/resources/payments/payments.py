import json
from json.decoder import JSONDecodeError

from flask import request, jsonify, make_response
from flask_restful_swagger_3 import Resource, swagger
from mongoengine import DoesNotExist

from app.adapters.db_adapter import insert, to_json
from app.models.paymentmodel import PaymentModel
from app.resources.payments.payment_docs import payment_get_filters_doc, payment_post_doc
from app.utils.auth_decorators import token_required


class Payments(Resource):
    @token_required(return_user=True)
    @swagger.doc(payment_get_filters_doc)
    def get(self, token_user_id):
        try:
            payments_list = list()
            filters = request.args  # Todo: bool filter get as str
            if filters:
                filter_dict = {k: v for k, v in filters.items()}
                payment_obj_list = PaymentModel.objects(**filter_dict)
            else:
                payment_obj_list = PaymentModel.objects()
            for payment in payment_obj_list:
                if token_user_id not in [payment.pay_to, payment.pay_from]:
                    continue
                payments_list.append(to_json(payment))

            return jsonify(payments_list)
        except DoesNotExist:
            return make_response("No payments available", 404)
        except Exception as e:
            return make_response("Internal Server Error: {}".format(e.__str__()), 500)

    @token_required()
    @swagger.doc(payment_post_doc)
    def post(self):
        try:
            data = json.loads(request.data)
            new_payment = PaymentModel(pay_from=data['pay_from'],
                                       pay_to=data['pay_to'],
                                       amount=data['amount'],
                                       method=data['method'])
            payment_obj = insert(new_payment)
            return jsonify({"payment_id": str(payment_obj.id)})
        except JSONDecodeError as e:
            return make_response("Invalid JSON: {}".format(e.__str__()), 400)
        except KeyError as e:
            return make_response("Missing / Invalid json key: {}".format(e.__str__()), 400)
        except Exception as e:
            return make_response("Internal Server Error: {}".format(e.__str__()), 500)
