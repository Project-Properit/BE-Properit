from datetime import datetime
from urllib.parse import quote_plus

import bson
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
    for k, v in task_json.items():
        if isinstance(v, (datetime, bson.objectid.ObjectId)):
            task_json[k] = str(v)
    task_json['id'] = task_json.pop('_id')
    return task_json
