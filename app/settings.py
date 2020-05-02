import configparser

config = configparser.ConfigParser()
config.read('/configs/config.ini')

db_section = config['db_section']
DB_USERNAME = db_section['db_username']
DB_PASSWORD = db_section['db_password']
DB_SERVER = db_section['db_server']
DB_NAME = db_section['db_name']

api_section = config['api_section']
APP_SECRET_KEY = api_section['app_secret_key'].encode('UTF-8')
