from typing import List

from app.adapters.db_adapter import to_json
from app.models.assetmodel import AssetModel
from app.models.usermodel import UserModel


def get_user_by_filters(filter_dict):
    user = UserModel.objects.get(**filter_dict)
    return {'id': str(user.id),
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'phone': user.phone}


def build_participants_obj(payment_obj):
    participant = get_user_by_filters(dict(id=payment_obj.pay_from))
    participant['amount'] = payment_obj.amount
    participant['is_open'] = payment_obj.is_open
    participant['payment_id'] = str(payment_obj.id)
    if not payment_obj.is_open:
        participant['when_payed'] = str(payment_obj.when_payed)
    return participant


def build_gp_object(gp_obj, participants, my_payment):
    gp = to_json(gp_obj)
    gp['participants'] = participants.copy()
    if my_payment:
        gp['my_payment'] = my_payment
    gp['owner'] = get_user_by_filters(dict(id=gp_obj.owner))
    return gp


def sort_participants(participants: List, user_id):
    participants.sort(key=lambda k: (not k['is_open'], k['id'] != user_id))


def get_user_payment(participants, user_id):
    for index, par in enumerate(participants):
        if par['id'] == user_id:
            return participants.pop(index)


def check_user_in_participants(participants, user_id):
    for par in participants:
        if par['id'] == user_id:
            return True
    return False


def sort_group_payments(gp_list: List, filter_by, filter_value):
    if filter_by == 'pay_from':
        for gp in list(gp_list):
            if 'my_payment' not in gp:
                gp_list.remove(gp)
        gp_list.sort(key=lambda k: (k['my_payment']['is_open'], k['creation_date']), reverse=True)

    elif filter_by == 'pay_to':
        gp_copy = gp_list.copy()
        gp_list.clear()
        gp_list += [item for item in gp_copy if item['owner']['id'] == filter_value]
        gp_list.sort(
            key=lambda k: (k['participants'][0]['is_open'] if k['participants'] else bool(k), k['creation_date']),
            reverse=True)
        # gp_list.sort(key=lambda k: (not k['status']))  # Todo: Group payment status ?


def get_user_asset_as_tenant(user):
    for asset in AssetModel.objects():
        if str(user.id) in asset.tenant_list:
            return str(asset.id)


def get_asset_doc(asset, doc_id):
    for doc in asset.documents:
        if doc['doc_id'] == doc_id:
            return doc
