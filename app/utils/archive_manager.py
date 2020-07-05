from bson import ObjectId

from app.adapters.db_adapter import archive, ArchiveCollections
from app.models.assetmodel import AssetModel
from app.models.grouppaymentmodel import GroupPaymentModel
from app.models.paymentmodel import PaymentModel
from app.models.servicecallmodel import ServiceCallModel


def archive_asset(asset):
    for gp_id in asset.group_payments:
        gp_obj = GroupPaymentModel.objects.get(id=ObjectId(gp_id))
        for p_id in gp_obj.payments:
            p_obj = PaymentModel.objects.get(id=ObjectId(p_id))
            archive(p_obj, ArchiveCollections.payments)
        archive(gp_obj, ArchiveCollections.group_payments)
    for sc_id in asset.service_calls:
        sc_obj = ServiceCallModel.objects.get(id=ObjectId(sc_id))
        archive(sc_obj, ArchiveCollections.service_calls)
    archive(asset, ArchiveCollections.assets)


def archive_group_payment(group_payment):
    for payment_id in group_payment.payments:
        payment = PaymentModel.objects.get(id=ObjectId(payment_id))
        archive(payment, ArchiveCollections.payments)
    archive(group_payment, ArchiveCollections.group_payments)


def archive_user(user):
    user_id = str(user.id)
    all_assets = AssetModel.objects()
    all_group_payments = GroupPaymentModel.objects()
    all_payments = PaymentModel.objects()
    for asset_obj in all_assets:
        if user_id in asset_obj.tenant_list:
            asset_obj.tenant_list.remove(user_id)
        elif user_id in asset_obj.pending_tenants:
            asset_obj.pending_tenants.remove(user_id)
        elif user_id == asset_obj.owner_id:
            archive_asset(asset_obj)
    for gp_obj in all_group_payments:
        if user_id == gp_obj.owner:
            archive(gp_obj, ArchiveCollections.group_payments)
    for p_obj in all_payments:
        if user_id in (p_obj.pay_to, p_obj.pay_from):
            archive(p_obj, ArchiveCollections.payments)
    archive(user, ArchiveCollections.users)
