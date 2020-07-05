from bson import ObjectId
from bson.errors import InvalidId
from flask import jsonify, make_response
from flask_restful_swagger_3 import Resource, swagger
from mongoengine import DoesNotExist

from app.adapters.db_adapter import archive, ArchiveCollections
from app.models.paymentmodel import PaymentModel
from app.resources.payments.payment_docs import payment_delete_doc
from app.utils.auth_decorators import token_required


class Payment(Resource):
    @token_required(return_user=True)
    @swagger.doc(payment_delete_doc)
    def delete(self, token_user_id, payment_id):
        try:
            payment = PaymentModel.objects.get(id=ObjectId(payment_id))
            if token_user_id != payment.pay_to:
                return make_response("Insufficient Permissions", 403)
            archive(payment, ArchiveCollections.payments)
            return jsonify(archived_payment_id=str(payment_id))
        except InvalidId:
            return make_response("Invalid payment ID", 400)
        except DoesNotExist:
            return make_response("Payment not found", 404)
        except Exception as e:
            return make_response("Internal Server Error: {}".format(e.__str__()), 500)
