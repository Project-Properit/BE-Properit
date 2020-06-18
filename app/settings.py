import configparser
import os

config = configparser.ConfigParser()
config.read(os.getenv('CONFIG_FILE', '/configs/config.ini'))
db_section = config['db_section']
api_section = config['api_section']
dbx_section = config['dbx_section']

DATABASE_SERVER = os.getenv('DATABASE_SERVER', db_section['database_server'])
DATABASE_PORT = os.getenv('DATABASE_PORT', int(db_section['database_port']))
DATABASE_NAME = os.getenv('DATABASE_NAME', db_section['database_name'])
DATABASE_USER = os.getenv('DATABASE_USER', db_section['database_user'])
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', db_section['database_password'])
DATABASE_AUTH = os.getenv('DATABASE_AUTH', db_section['database_auth'])

APP_SECRET_KEY = os.getenv('APP_SECRET_KEY', api_section['app_secret_key']).encode('UTF-8')

DBX_ACCESS_TOKEN = os.getenv('DBX_ACCESS_TOKEN', dbx_section['dbx_access_token'])
