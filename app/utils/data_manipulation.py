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
    participant['status'] = payment_obj.status
    return participant


def sort_list_of_dicts(list_of_dicts: List, user_id, status="pending"):
    new_list_of_dicts = []
    for d in list_of_dicts:
        if d['id'] == user_id and d['status'] == status:
            i = list_of_dicts.index(d)
            new_list_of_dicts.append(d)
            list_of_dicts.pop(i)
    for d in list_of_dicts:
        if d['status'] == status:
            i = list_of_dicts.index(d)
            new_list_of_dicts.append(d)
            list_of_dicts.pop(i)
    for d in list_of_dicts:
        if d['id'] == user_id and d['status'] == 'payed':
            i = list_of_dicts.index(d)
            new_list_of_dicts.append(d)
            list_of_dicts.pop(i)
    for d in list_of_dicts:
        new_list_of_dicts.append(d)
    return new_list_of_dicts
