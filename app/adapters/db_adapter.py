from datetime import datetime
from enum import Enum
from urllib.parse import quote_plus

import bson
from mongoengine import connect

from app.settings import DATABASE_SERVER, DATABASE_USER, DATABASE_PASSWORD, DATABASE_AUTH, DATABASE_PORT

mongo_connection = connect(
    host=f'mongodb://{DATABASE_USER}:{quote_plus(DATABASE_PASSWORD)}@{DATABASE_SERVER}:{DATABASE_PORT}/{DATABASE_AUTH}?retryWrites=true&w=majority')


class ArchiveCollections(Enum):
    assets = '_AssetsArchive'
    group_payments = '_GroupPaymentsArchive'
    payments = '_PaymentsArchive'
    service_calls = '_ServiceCallsArchive'
    users = '_UsersArchive'


def update(document):
    return document.save()


def insert(document):
    if not document.creation_date:
        document.creation_date = datetime.now().replace(microsecond=0)
    return document.save()


def archive(document, collection):
    source_collection = document._meta['collection']
    document.switch_collection(collection.value, keep_created=False)
    document.save()
    document.switch_collection(source_collection, keep_created=False)
    document.delete()


def delete(document):
    document.delete()


def to_json(document):
    task_json = document.to_mongo()
    for k, v in task_json.items():
        if isinstance(v, (datetime, bson.objectid.ObjectId)):
            task_json[k] = str(v)
        if k == 'password':
            del task_json[k]
    task_json['id'] = task_json.pop('_id')
    return task_json
