from datetime import datetime

from mongoengine import connect

from app.settings import DATABASE_SERVER, DATABASE_USER, DATABASE_PASSWORD, DATABASE_AUTH

mongo_connection = connect(
    host=f'mongodb://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_SERVER}/{DATABASE_AUTH}?retryWrites=true&w=majority')


def update(document):
    return document.save()


def insert(document):
    if not document.creation_date:
        document.creation_date = datetime.now()
    return document.save()


def to_json(document):
    task_json = document.to_mongo()
    task_json['id'] = str(document.id)
    if document.creation_date:
        task_json['creation_date'] = str(document.creation_date)
    del task_json['_id']
    return task_json
