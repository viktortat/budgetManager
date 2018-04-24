from django.db.models import Q
from dry_rest_permissions.generics import DRYPermissionFiltersBase

from .models import Wallet


class WalletFilterBackend(DRYPermissionFiltersBase):
    def filter_list_queryset(self, request, queryset, view):
        if request.user.is_staff:
            return queryset
        else:
            return queryset.filter(Q(owner=request.user) | Q(users=request.user)).distinct()


class WalletFilterBackendFK(DRYPermissionFiltersBase):
    def filter_list_queryset(self, request, queryset, view):
        if request.user.is_staff:
            return queryset
        else:
            return queryset.filter(Q(wallet__owner=request.user) | Q(wallet__users=request.user)).distinct()


def check_wallet_ownership(wallet_id, user):
    wallet = Wallet.objects.filter(id=wallet_id).first()
    if wallet:
        return user == wallet.owner or user in wallet.users.all() or user.is_staff
    else:
        return True
