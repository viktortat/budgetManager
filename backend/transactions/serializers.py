from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Transaction, Category, Wallet, Budget

User = get_user_model()


class UsersEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email")


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ("id", "transaction_type", "notes", "category", "amount", "date", "user", "wallet")
        read_only_fields = ["user", "wallet"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "transactions", "color", "balance", "wallet")
        read_only_fields = ["balance", "transactions"]
        extra_kwargs = {'wallet': {'required': True}}


class WalletSerializer(serializers.ModelSerializer):
    users = UsersEmailSerializer(read_only=True, many=True)
    users_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='users', write_only=True, many=True, required=False)

    class Meta:
        model = Wallet
        fields = ("id", "name", "categories", "balance", "owner", "users", "users_id")
        read_only_fields = ["balance", "owner", "categories"]


class BudgetSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(many=True, queryset=Category.objects.all())

    class Meta:
        model = Budget
        fields = ("id", "name", "categories", "wallet", "amount", "period")
        read_only_fields = ["wallet"]
