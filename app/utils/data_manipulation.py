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
