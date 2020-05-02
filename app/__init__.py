from flask import Flask
from flask_restful_swagger_3 import Api
from flask_swagger_ui import get_swaggerui_blueprint
from flask_migrate import Migrate

from app.models import db
from app.resources.auth.login import Login
from app.resources.auth.logout import Logout
from app.resources.auth.register import Register
from app.resources.auth.users import Users
from app.settings import DB_USERNAME, DB_SERVER, DB_NAME, DB_PASSWORD

migrate = Migrate()


def create_app():
    app = Flask('Properit')
    blueprint = get_swaggerui_blueprint('/docs', '/api/swagger.json')
    app.register_blueprint(blueprint, url_prefix='/docs', )
    api = Api(app, description="Properit API", api_spec_url='/api/swagger')

    api.add_resource(Login, "/login")
    api.add_resource(Register, "/register")
    api.add_resource(Users, "/users")
    api.add_resource(Logout, "/logout")

    app.config[
        'SQLALCHEMY_DATABASE_URI'] = f'mssql+pyodbc://{DB_USERNAME}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}?driver=SQL+Server?trusted_connection=yes'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    return app
