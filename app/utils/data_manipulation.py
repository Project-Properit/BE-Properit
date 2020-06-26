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
    participant['payment_id'] = str(payment_obj.id)
    if not payment_obj.is_open:
        participant['when_payed'] = str(payment_obj.when_payed)
    return participant


def sort_list_of_dicts(list_of_dicts: List, user_id, is_open=True, get_my_payment=False):
    new_list_of_dicts = []
    user_id_payment = None
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

    # pop out user_id payment #
    if get_my_payment:
        for d in new_list_of_dicts:
            if d['id'] == user_id:
                i = new_list_of_dicts.index(d)
                user_id_payment = new_list_of_dicts.pop(i)
                break
        return user_id_payment, new_list_of_dicts
    return new_list_of_dicts


def reorder_group_payment(gp_list: List, user_id):
    new_gp_list = []
    for gp in gp_list:
        for par in gp['participants']:
            if par['id'] == user_id and par['is_open']:
                i = gp_list.index(gp)
                new_gp_list.append(gp)
                gp_list.pop(i)
    gp_list.sort(key=lambda x: x['creation_time'])
    for gp in gp_list:
        new_gp_list.append(gp)
    return new_gp_list
