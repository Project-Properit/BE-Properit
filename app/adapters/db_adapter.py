from datetime import datetime
from urllib.parse import quote_plus

from mongoengine import connect

from app.settings import DATABASE_SERVER, DATABASE_USER, DATABASE_PASSWORD, DATABASE_AUTH, DATABASE_PORT

mongo_connection = connect(
    host=f'mongodb://{DATABASE_USER}:{quote_plus(DATABASE_PASSWORD)}@{DATABASE_SERVER}:{DATABASE_PORT}/{DATABASE_AUTH}?retryWrites=true&w=majority')


def update(document):
    return document.save()


def insert(document):
    if not document.creation_date:
        document.creation_date = datetime.now().replace(microsecond=0)
    return document.save()


def delete(document):
    document.delete()


def to_json(document):
    task_json = document.to_mongo()
    task_json['id'] = str(document.id)
    if document.creation_date:
        task_json['creation_date'] = str(document.creation_date)
    if document.when_payed:
        task_json['when_payed'] = str(document.when_payed)
    del task_json['_id']
    return task_json
