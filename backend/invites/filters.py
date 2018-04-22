from django_filters import rest_framework as filters

from .models import Invitation


class InvitationFilter(filters.FilterSet):
    class Meta:
        model = Invitation
        fields = '__all__'
