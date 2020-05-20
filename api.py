from flask import Flask
from flask_cors import CORS
from flask_restful_swagger_3 import Api
from flask_swagger_ui import get_swaggerui_blueprint

from app.adapters.db_adapter import mongo_connection
from app.resources.assets.assets import Assets
from app.resources.assets.asset import Asset
from app.resources.auth.login import Login
from app.resources.auth.logout import Logout
from app.resources.auth.register import Register
from app.resources.group_payments.group_payments import GroupPayments
from app.resources.group_payments.groups_payments import GroupsPayments
from app.resources.payments.payments import Payments
from app.resources.payments.payment import Payment
from app.resources.users.user import User

app = Flask('Properit')
blueprint = get_swaggerui_blueprint('/docs', '/api/swagger.json')
app.register_blueprint(blueprint, url_prefix='/docs')
CORS(app)
components = \
    {
        'securitySchemes': {
            'BasicAuth': {
                'type': 'http',
                'scheme': 'basic'
            },
            'ApiKeyAuth': {
                'type': 'apiKey',
                'in': 'header',
                'name': 'x-access-tokens'}
        }
    }
api = Api(app, description="Properit API", api_spec_url='/api/swagger', components=components,
          security=[{'ApiKeyAuth': []}, {'BasicAuth': []}])

db_connection = mongo_connection

api.add_resource(Login, "/login")
api.add_resource(Register, "/register")
api.add_resource(Logout, "/logout")

api.add_resource(User, "/users/<string:user_id>")

api.add_resource(Assets, "/api/assets")
api.add_resource(Asset, "/api/assets/<string:asset_id>")

api.add_resource(GroupsPayments, "/api/assets/<string:asset_id>/group-payments")
api.add_resource(GroupPayments, "/api/assets/<string:asset_id>/group-payments/<string:group_payments_id>")

api.add_resource(Payments, "/api/payments")
api.add_resource(Payment, "/api/payments/<string:payment_id>")

if __name__ == '__main__':  # For Debugging
    app.run(host='0.0.0.0', port=8080, threaded=True)
