import time
from datetime import datetime
from json.decoder import JSONDecodeError

from bson import ObjectId
from bson.errors import InvalidId
from flask import jsonify, make_response
from flask_restful_swagger_3 import Resource, swagger
from mongoengine import DoesNotExist, ValidationError

from app.adapters.db_adapter import update, delete
from app.models.paymentmodel import PaymentModel
from app.resources.payments.payment_docs import payment_put_doc, payment_delete_doc
from app.utils.auth_decorators import token_required


class Payment(Resource):
    @token_required()
    @swagger.doc(payment_put_doc)
    def put(self, payment_id):  # Todo: who can edit payment?
        try:
            payment = PaymentModel.objects.get(id=ObjectId(payment_id))
            time.sleep(5)  # pay #
            payment.is_open = False
            payment.when_payed = datetime.now().replace(microsecond=0)
            update(payment)
            return jsonify({"payment_id": str(payment_id)})
        except InvalidId:
            return make_response("Invalid payment ID", 400)
        except JSONDecodeError as e:
            return make_response("Invalid JSON: {}".format(e.__str__()), 400)
        except KeyError as e:
            return make_response("Missing / Invalid json key: {}".format(e.__str__()), 400)
        except ValidationError as e:
            return make_response("Invalid json parameters: {}".format(e.__str__()), 400)
        except DoesNotExist:
            return make_response("Payment not found", 404)
        except Exception as e:
            return make_response("Internal Server Error: {}".format(e.__str__()), 500)

    @token_required(return_user=True)
    @swagger.doc(payment_delete_doc)
    def delete(self, token_user_id, payment_id):
        try:
            payment = PaymentModel.objects.get(id=ObjectId(payment_id))
            if token_user_id != payment.pay_to:
                return make_response("Insufficient Permissions", 403)
            delete(payment)
            return jsonify({"deleted payment_id": str(payment_id)})
        except InvalidId:
            return make_response("Invalid payment ID", 400)
        except DoesNotExist:
            return make_response("Payment not found", 404)
        except Exception as e:
            return make_response("Internal Server Error: {}".format(e.__str__()), 500)
