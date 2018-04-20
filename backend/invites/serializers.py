from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Invitation
from transactions.serializers import UsersEmailSerializer

User = get_user_model()


class InvitationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    creator = UsersEmailSerializer(read_only=True)
    invited = UsersEmailSerializer(read_only=True)
    invited_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='invited', write_only=True, required=True)

    class Meta:
        model = Invitation
        fields = ["date", "creator", "id", "invited", "invited_id", "wallet", "status"]
        read_only_fields = ["date", "creator"]
