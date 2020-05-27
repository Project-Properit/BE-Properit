import json
from json.decoder import JSONDecodeError

from flask import request, jsonify, make_response
from flask_restful_swagger_3 import Resource, swagger
from mongoengine import DoesNotExist

from app.adapters.db_adapter import insert, to_json
from app.decorators.auth_decorators import token_required
from app.models.paymentmodel import PaymentModel
from app.resources.payments.payment_docs import payment_get_filters_doc, payment_post_doc


class Payments(Resource):
    @token_required()
    @swagger.doc(payment_get_filters_doc)
    def get(self):
        try:
            json_payment_list = []
            filters = request.args
            if filters:
                filter_dict = {k: v for k, v in filters.items()}
                payments_list = PaymentModel.objects(**filter_dict)
                for payment in payments_list:
                    json_payment_list.append(to_json(payment))
            else:
                for payment in PaymentModel.objects():
                    json_payment_list.append(to_json(payment))
            if not json_payment_list:
                return make_response("No payment found by filters", 404)
            return json_payment_list
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
            insert(new_payment)
            return jsonify({"new payment_id": str(new_payment.id)})
        except JSONDecodeError as e:
            return make_response("Invalid JSON: {}".format(e.__str__()), 400)
        except KeyError as e:
            return make_response("Missing / Invalid json key: {}".format(e.__str__()), 400)
        except Exception as e:
            return make_response("Internal Server Error: {}".format(e.__str__()), 500)
