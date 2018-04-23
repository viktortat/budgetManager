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
    invited_email = serializers.EmailField(allow_blank=False,  write_only=True)

    class Meta:
        model = Invitation
        fields = ["id", "date", "creator", "invited", "invited_id", "invited_email", "wallet", "resolved"]
        read_only_fields = ["date", "creator"]
