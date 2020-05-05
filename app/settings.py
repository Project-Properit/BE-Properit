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


import os
ACCESS_KEY = 'ASIAQK5OE254EBTIPQ4D'
SECRET_KEY = 'x/kiO9BkwkE1W7qq39/oJi8g3AVuhpuBOhAnP1tJ'
AWS_TOKEN = 'FwoGZXIvYXdzEGYaDIIOiCobyRvlT/cPGiLGAXFKroT9XZo6SdhZrB2a5ROsR3DJNATEsVhKxkKCxaNcXX53PGhxOF5au++GR5Ndox0YNjn3J/wovRV2tKP5caiG7peV3oL53LxjHVvbzubZCpPYXIZRH3t8wWjfAL0wi3wyeH6fHg41uu98ydrMo+Vzr3iSHSFmbHL00CIH5BQl/mcKoaZxDt3auc586QWuzFuKq5iQCDd8FCtmV0+H1xUhTCZLMJiud9E+C5nuZCkEhtXPzm0nlHetl7s2SLrvST0ASUXhJyiUwMX1BTIt6wGCFMlXVaTeUE23N/GmrMSyCVmmnT1X+hTRcJfDm/Xog0ir6mbN/+gO2Bna'
S3_LOCATION = 'http://{}.s3.amazonaws.com/'.format('properit-s3')
BUCKET_NAME = 'properit-s3'