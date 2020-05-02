import configparser

config = configparser.ConfigParser()
config.read('/configs/config.ini')

db_section = config['db_section']
DATABASE_SERVER = db_section['database_server']
DATABASE_PORT = int(db_section['database_port'])
DATABASE_NAME = db_section['database_name']
DATABASE_USER = db_section['database_user']
DATABASE_PASSWORD = db_section['database_password']
DATABASE_AUTH = db_section['database_auth']

api_section = config['api_section']
APP_SECRET_KEY = api_section['app_secret_key'].encode('UTF-8')
