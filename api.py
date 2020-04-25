from flask import Flask
from flask_restful_swagger_3 import Api
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask('Properit')
blueprint = get_swaggerui_blueprint(api_url='', base_url='/docs')
app.register_blueprint(blueprint, url_prefix='/docs')

api = Api(app, description="Properit API")
# api.add_resource(Users, "/users")

if __name__ == '__main__':  # For Debugging
    app.run(host='0.0.0.0', port=8080, threaded=True)
