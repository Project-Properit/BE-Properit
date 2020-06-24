from typing import List

from app.models.usermodel import UserModel


def get_user_by_id(user_id):
    user = UserModel.objects.get(id=user_id)
    return {'id': str(user.id),
            'first_name': user.first_name,
            'last_name': user.last_name}


def build_participants(payment_obj):
    participant = get_user_by_id(payment_obj.pay_from)
    participant['amount'] = payment_obj.amount
    participant['is_open'] = payment_obj.is_open
    return participant


def sort_list_of_dicts(list_of_dicts: List, user_id, is_open=True):
    new_list_of_dicts = []
    for d in list_of_dicts:
        if d['id'] == user_id and d['is_open'] == is_open:
            i = list_of_dicts.index(d)
            new_list_of_dicts.append(d)
            list_of_dicts.pop(i)
    for d in list_of_dicts:
        if d['is_open'] == is_open:
            i = list_of_dicts.index(d)
            new_list_of_dicts.append(d)
            list_of_dicts.pop(i)
    for d in list_of_dicts:
        if d['id'] == user_id and not d['is_open']:
            i = list_of_dicts.index(d)
            new_list_of_dicts.append(d)
            list_of_dicts.pop(i)
    for d in list_of_dicts:
        new_list_of_dicts.append(d)
    return new_list_of_dicts
