from django.db.models import Q
from dry_rest_permissions.generics import DRYPermissionFiltersBase


class InvitationFilterBackend(DRYPermissionFiltersBase):
    def filter_list_queryset(self, request, queryset, view):
        if request.user.is_staff:
            return queryset
        else:
            return queryset.filter(Q(creator=request.user) | Q(invited=request.user) | Q(wallet__owner=request.user)).distinct()
